#!/usr/bin/env python3
"""
generate_images.py — 调用火山引擎方舟 Seedream API 批量生成视觉资产图片

使用纯 requests 调用 REST API，无需安装火山引擎 SDK。

支持两阶段角色生成：
  Phase 1: 生成角色基准肖像（正面半身像）+ 场景/道具（纯文生图）
  Phase 2: 以基准肖像为参考图，生成角色的其余图片（图生图，保证外观一致性）

用法：
    export ARK_API_KEY="your-api-key-here"

    # Phase 1: 生成基准肖像 + 场景 + 道具
    python3 generate_images.py --phase 1

    # 人工检查基准肖像，不满意的删掉重跑
    python3 generate_images.py --phase 1 --element 某角色 --no-skip

    # Phase 2: 以基准肖像为参考图，生成角色剩余图片
    python3 generate_images.py --phase 2

    # 不分阶段，全量生成（phase 2 任务自动检测基准肖像是否存在）
    python3 generate_images.py

    # 其他常用参数
    python3 generate_images.py --dry-run          # 只看计划
    python3 generate_images.py --limit 1           # 只跑1张
    python3 generate_images.py --element 吴文顶    # 只跑指定角色
    python3 generate_images.py --priority P0/P1    # 只跑高优先级
"""

import os
import sys
import re
import time
import json
import base64
import argparse
import logging
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("请先安装 requests: pip install requests")
    sys.exit(1)

# ---------------------------------------------------------------------------
# 导入本地模块
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_prompts import scan_bibles, get_global_prefix
from bible_utils import count_images, IMAGE_EXTS

# ---------------------------------------------------------------------------
# 常量 & 默认值
# ---------------------------------------------------------------------------
DEFAULT_BASE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "production")

# 火山引擎方舟 REST API (中国区)
DEFAULT_ARK_API_URL = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
DEFAULT_MODEL = "doubao-seedream-5-0-260128"
DEFAULT_SIZE = "2K"          # "2K" | "4K" | "1024x1024" 等
DEFAULT_SEED_BASE = 42       # 基础种子，每个元素+阶段偏移确保差异化但可复现
DEFAULT_QPS_DELAY = 1.5      # 每次 API 调用间隔（秒），防限流
MAX_RETRIES = 3              # 失败重试次数
RETRY_BACKOFF = 2.0          # 重试指数退避基数

# 优先级排序
PRIORITY_ORDER = {"P0/P1": 0, "P2": 1, "P3": 2, "P4": 3, "P5": 4}

# 肖像视角名称（按星级）
PORTRAIT_VIEWS = {
    6: ["正面半身像", "四分之三侧面半身像", "正侧面半身像", "全身正面像", "背面全身像", "眼部特写"],
    5: ["正面半身像", "四分之三侧面半身像", "正侧面半身像", "全身正面像"],
    4: ["正面半身像", "四分之三侧面半身像", "正侧面半身像", "全身正面像"],
    3: ["正面半身像", "全身正面像"],
}

# ---------------------------------------------------------------------------
# 日志
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("generate")


# ---------------------------------------------------------------------------
# 参考图工具
# ---------------------------------------------------------------------------
def load_ref_image_as_data_uri(image_path: str) -> str:
    """读取本地图片文件，返回 data:image/... ;base64,... 格式的 URI"""
    ext = os.path.splitext(image_path)[1].lower()
    mime_map = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}
    mime = mime_map.get(ext, "image/png")

    with open(image_path, "rb") as f:
        b64_str = base64.b64encode(f.read()).decode("ascii")

    return f"data:{mime};base64,{b64_str}"


# ---------------------------------------------------------------------------
# API 调用（纯 requests，无需 SDK）
# ---------------------------------------------------------------------------
def generate_one_image(
    api_url: str,
    api_key: str,
    prompt: str,
    model: str,
    size: str,
    seed: int,
    output_path: str,
    ref_image_path: str = None,
) -> bool:
    """
    调用 Seedream REST API 生成单张图片并保存到磁盘。

    ref_image_path: 可选，本地参考图路径。传入后使用图生图模式（角色一致性）。

    返回 True=成功, False=失败
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "seed": seed,
        "response_format": "b64_json",
        "watermark": False,
    }

    # 如果提供了参考图，加入 image_urls 字段（图生图模式）
    if ref_image_path and os.path.exists(ref_image_path):
        try:
            data_uri = load_ref_image_as_data_uri(ref_image_path)
            payload["image_urls"] = [data_uri]
            log.info(f"  📎 使用参考图: {os.path.basename(ref_image_path)}")
        except Exception as e:
            log.warning(f"  ⚠️ 读取参考图失败: {e}，退回文生图模式")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.post(
                api_url,
                headers=headers,
                json=payload,
                timeout=120,
            )

            # HTTP 层错误
            if resp.status_code != 200:
                raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:200]}")

            data = resp.json()

            # 提取 base64 图片数据
            img_data_list = data.get("data", [])
            if not img_data_list:
                raise RuntimeError(f"返回数据中无 data 字段: {json.dumps(data, ensure_ascii=False)[:200]}")

            b64_data = img_data_list[0].get("b64_json", "")
            if not b64_data:
                # 尝试 url 格式
                img_url = img_data_list[0].get("url", "")
                if img_url:
                    img_resp = requests.get(img_url, timeout=60)
                    img_resp.raise_for_status()
                    img_bytes = img_resp.content
                else:
                    raise RuntimeError("返回数据中无 b64_json 也无 url")
            else:
                img_bytes = base64.b64decode(b64_data)

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(img_bytes)

            file_kb = len(img_bytes) / 1024
            log.info(f"  ✅ 已保存 {output_path} ({file_kb:.0f} KB)")
            return True

        except Exception as e:
            err_msg = str(e)
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF ** attempt
                log.warning(f"  ⚠️ 第{attempt}次失败: {err_msg[:80]}... {wait:.1f}s 后重试")
                time.sleep(wait)
            else:
                log.error(f"  ❌ 彻底失败: {err_msg[:120]}")
                return False

    return False


# ---------------------------------------------------------------------------
# 生成任务构建
# ---------------------------------------------------------------------------
def build_tasks(results: list, global_prefix: str, assets_root: str) -> list:
    """
    从 scan_bibles() 的结果构建生成任务列表。

    每个任务包含 phase 和 ref_portrait_path 字段：
      - phase=1: 角色基准肖像(idx==0) + 所有场景/道具（纯文生图）
      - phase=2: 角色其余图片（以基准肖像为参考图）
      - ref_portrait_path: phase=2 任务的参考图路径
    """
    tasks = []

    for r in results:
        if not r["prompts"]:
            continue

        elem_name = r["name"]
        elem_type = r["type"]
        priority = r["priority"]
        stars = r["stars"]
        has_prefix = r.get("has_inline_prefix", True)
        sub_dir = r.get("sub_dir", "")

        # 基础输出目录
        type_dir = os.path.join(assets_root, elem_type, elem_name)

        # 角色基准肖像路径（供 phase 2 任务引用）
        base_portrait_path = os.path.join(type_dir, "_portrait", "正面半身像.png")

        for idx, p in enumerate(r["prompts"]):
            eng = p.get("english", "").strip()
            chn = p.get("chinese", "").strip()
            stage_id = p.get("stage_id")

            if not eng:
                continue

            # 动态拼接全局前缀
            final_prompt = eng
            if not has_prefix and global_prefix:
                if global_prefix.lower()[:20] not in eng.lower()[:80]:
                    final_prompt = f"{global_prefix}\n{eng}"

            # 确定输出路径 & phase & 参考图
            if elem_type == "characters":
                if idx == 0:
                    # 基准肖像 → phase 1
                    out_path = base_portrait_path
                    is_portrait = True
                    phase = 1
                    ref_path = None
                elif stage_id:
                    out_path = os.path.join(type_dir, stage_id, f"{idx:02d}.png")
                    is_portrait = False
                    phase = 2
                    ref_path = base_portrait_path
                else:
                    out_path = os.path.join(type_dir, "_portrait", f"{idx:02d}.png")
                    is_portrait = True
                    phase = 2
                    ref_path = base_portrait_path
            elif elem_type == "locations":
                if stage_id:
                    out_path = os.path.join(type_dir, stage_id, f"{idx:02d}.png")
                else:
                    out_path = os.path.join(type_dir, "默认", f"{idx:02d}.png")
                is_portrait = False
                phase = 1
                ref_path = None
            else:  # props
                if stage_id:
                    out_path = os.path.join(type_dir, stage_id, f"{idx:02d}.png")
                else:
                    out_path = os.path.join(type_dir, f"{idx:02d}.png")
                is_portrait = False
                phase = 1
                ref_path = None

            # 种子值：基于元素名+序号的确定性哈希，保证可复现
            seed = (DEFAULT_SEED_BASE + hash(elem_name) + idx * 7) % (2**31)

            tasks.append({
                "element": elem_name,
                "type": elem_type,
                "priority": priority,
                "stars": stars,
                "stage_id": stage_id or "默认",
                "prompt_en": final_prompt,
                "prompt_cn": chn,
                "output_path": out_path,
                "seed": seed,
                "is_portrait": is_portrait,
                "prompt_idx": idx,
                "phase": phase,
                "ref_portrait_path": ref_path,
            })

    # 按优先级 → 星级（降序）→ 元素名排序
    tasks.sort(key=lambda t: (
        PRIORITY_ORDER.get(t["priority"], 9),
        -t["stars"],
        t["element"],
        t["prompt_idx"],
    ))

    return tasks


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="调用 Seedream API 批量生成视觉资产（支持两阶段角色生成）")
    parser.add_argument("--base-dir", default=DEFAULT_BASE, help="production 目录")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Seedream 模型 ID (默认: {DEFAULT_MODEL})")
    parser.add_argument("--size", default=DEFAULT_SIZE, help=f"图片尺寸 (默认: {DEFAULT_SIZE})")
    parser.add_argument("--phase", type=int, default=0, choices=[0, 1, 2],
                        help="生成阶段: 1=基准肖像+场景道具, 2=角色参考图生图, 0=全部 (默认: 0)")
    parser.add_argument("--priority", default=None, help="只生成指定优先级 (如: P0/P1, P2)")
    parser.add_argument("--element", default=None, help="只生成指定元素 (如: 吴文顶)")
    parser.add_argument("--type", default=None, dest="elem_type", help="只生成指定类型 (characters/locations/props)")
    parser.add_argument("--dry-run", action="store_true", help="只输出计划，不调 API")
    parser.add_argument("--no-skip", action="store_true", help="不跳过已有图片的目录")
    parser.add_argument("--limit", type=int, default=0, help="最多生成N张图片 (默认: 0=不限)")
    parser.add_argument("--delay", type=float, default=DEFAULT_QPS_DELAY, help=f"API 调用间隔秒数 (默认: {DEFAULT_QPS_DELAY})")
    parser.add_argument("--ark-api-url", default=DEFAULT_ARK_API_URL, help="方舟图片生成 API URL")
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    assets_root = os.path.join(base, "step4-assets")

    # ---- Step 1: 扫描圣经，提取提示词 ----
    log.info(f"扫描圣经目录: {base}")
    results, global_prefix = scan_bibles(base)
    log.info(f"找到 {len(results)} 个圣经文件, 全局前缀: {global_prefix[:40]}...")

    # ---- Step 2: 构建任务列表 ----
    all_tasks = build_tasks(results, global_prefix, assets_root)
    log.info(f"构建了 {len(all_tasks)} 个生成任务")

    # ---- Step 3: 过滤 ----
    tasks = all_tasks

    # Phase 过滤
    if args.phase == 1:
        tasks = [t for t in tasks if t["phase"] == 1]
        log.info(f"Phase 1 模式: {len(tasks)} 个任务（基准肖像 + 场景 + 道具）")
    elif args.phase == 2:
        tasks = [t for t in tasks if t["phase"] == 2]
        log.info(f"Phase 2 模式: {len(tasks)} 个任务（角色参考图生图）")

    if args.priority:
        tasks = [t for t in tasks if t["priority"] == args.priority]
        log.info(f"过滤优先级 {args.priority}: {len(tasks)} 个任务")
    if args.element:
        tasks = [t for t in tasks if t["element"] == args.element]
        log.info(f"过滤元素 {args.element}: {len(tasks)} 个任务")
    if args.elem_type:
        tasks = [t for t in tasks if t["type"] == args.elem_type]
        log.info(f"过滤类型 {args.elem_type}: {len(tasks)} 个任务")

    # ---- Step 4: 断点续跑——跳过已有图片 ----
    if not args.no_skip:
        before = len(tasks)
        tasks = [t for t in tasks if not os.path.exists(t["output_path"])]
        skipped = before - len(tasks)
        if skipped:
            log.info(f"跳过已有图片: {skipped} 个, 剩余: {len(tasks)} 个")

    # ---- Step 4b: Phase 2 检查参考图是否就绪 ----
    if args.phase != 1:  # phase=0 或 phase=2 时需要检查
        ready_tasks = []
        skipped_no_ref = 0
        for t in tasks:
            if t["phase"] == 2 and t["ref_portrait_path"]:
                if not os.path.exists(t["ref_portrait_path"]):
                    skipped_no_ref += 1
                    continue
            ready_tasks.append(t)
        if skipped_no_ref:
            log.warning(f"跳过 {skipped_no_ref} 个 Phase 2 任务（基准肖像未生成，请先跑 --phase 1）")
        tasks = ready_tasks

    # ---- Step 4c: 限制数量 ----
    if args.limit > 0 and len(tasks) > args.limit:
        log.info(f"限制生成数量: {len(tasks)} → {args.limit}")
        tasks = tasks[:args.limit]

    if not tasks:
        log.info("没有待生成的任务，全部完成！")
        return

    # ---- Step 5: Dry-run 或实际生成 ----
    if args.dry_run:
        print(f"\n{'='*70}")
        print(f"DRY RUN — 共 {len(tasks)} 个待生成任务")
        print(f"{'='*70}\n")
        current_p = None
        for t in tasks:
            if t["priority"] != current_p:
                current_p = t["priority"]
                print(f"\n--- {current_p} ---\n")
            portrait_tag = " [肖像]" if t["is_portrait"] else ""
            phase_tag = f" [P{t['phase']}]"
            ref_tag = ""
            if t["ref_portrait_path"]:
                ref_exists = "✅" if os.path.exists(t["ref_portrait_path"]) else "❌"
                ref_tag = f" [参考图:{ref_exists}]"
            print(f"  [{t['type']}] {t['element']}/{t['stage_id']}{portrait_tag}{phase_tag}{ref_tag}")
            print(f"    → {t['output_path']}")
            print(f"    prompt: {t['prompt_en'][:80]}...")
            if t["ref_portrait_path"]:
                print(f"    ref: {t['ref_portrait_path']}")
            print()

        # 统计摘要
        by_type = {}
        by_phase = {1: 0, 2: 0}
        for t in tasks:
            by_type[t["type"]] = by_type.get(t["type"], 0) + 1
            by_phase[t["phase"]] = by_phase.get(t["phase"], 0) + 1
        print(f"\n摘要: ", end="")
        print(", ".join(f"{k}: {v}" for k, v in by_type.items()))
        print(f"Phase 1 (文生图): {by_phase[1]}, Phase 2 (参考图生图): {by_phase[2]}")
        print(f"总计: {len(tasks)} 张图片待生成")
        return

    # ---- 实际调用 API ----
    api_key = os.environ.get("ARK_API_KEY", "")
    if not api_key:
        log.error("未设置 ARK_API_KEY 环境变量！请运行: export ARK_API_KEY=your-key")
        sys.exit(1)

    total = len(tasks)
    success = 0
    failed = 0
    start_time = time.time()

    # 生成日志（用于断点恢复和事后审计）
    log_path = os.path.join(assets_root, "generation_log.jsonl")

    log.info(f"\n开始生成 {total} 张图片 (模型: {args.model}, 尺寸: {args.size})\n")

    for i, t in enumerate(tasks, 1):
        portrait_tag = " [肖像]" if t["is_portrait"] else ""
        phase_tag = " [参考图生图]" if t["phase"] == 2 else ""
        log.info(f"[{i}/{total}] {t['element']}/{t['stage_id']}{portrait_tag}{phase_tag}")

        ok = generate_one_image(
            api_url=args.ark_api_url,
            api_key=api_key,
            prompt=t["prompt_en"],
            model=args.model,
            size=args.size,
            seed=t["seed"],
            output_path=t["output_path"],
            ref_image_path=t.get("ref_portrait_path"),
        )

        if ok:
            success += 1
        else:
            failed += 1

        # 写入生成日志
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "element": t["element"],
            "type": t["type"],
            "stage_id": t["stage_id"],
            "output_path": t["output_path"],
            "seed": t["seed"],
            "model": args.model,
            "size": args.size,
            "phase": t["phase"],
            "ref_image": t.get("ref_portrait_path", ""),
            "success": ok,
            "prompt_preview": t["prompt_en"][:200],
        }
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

        # 速率控制
        if i < total:
            time.sleep(args.delay)

    # ---- 完成统计 ----
    elapsed = time.time() - start_time
    log.info(f"\n{'='*50}")
    log.info(f"生成完成！用时 {elapsed:.1f}s")
    log.info(f"  成功: {success}/{total}")
    log.info(f"  失败: {failed}/{total}")
    log.info(f"  日志: {log_path}")
    log.info(f"{'='*50}")

    if failed:
        log.warning(f"有 {failed} 张图片生成失败，可重新运行脚本自动跳过已完成的任务。")


if __name__ == "__main__":
    main()
