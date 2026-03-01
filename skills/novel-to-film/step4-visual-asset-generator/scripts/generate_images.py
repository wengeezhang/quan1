#!/usr/bin/env python3
"""
generate_images.py — 调用 Seedream API 批量生成视觉资产图片

核心流程：
  1. 复用 extract_prompts.scan_bibles() 从圣经源文件提取结构化提示词
  2. 为 has_inline_prefix=False 的提示词动态拼接全局 style prefix
  3. 按优先级排序，逐条调用 Seedream API 生成图片
  4. 将生成的图片保存到 step4-assets/{type}/{name}/{stage_id}/ 目录
  5. 支持断点续跑（已有图片的目录自动跳过）

用法：
    # 安装依赖（首次）
    pip install volcenginesdkarkruntime --break-system-packages

    # 设置 API Key（环境变量）
    export ARK_API_KEY="your-api-key-here"

    # 全量生成
    python3 generate_images.py

    # 只看计划，不调 API
    python3 generate_images.py --dry-run

    # 只跑高优先级角色肖像
    python3 generate_images.py --priority P0/P1

    # 只跑指定元素
    python3 generate_images.py --element 吴文顶

    # 指定模型和分辨率
    python3 generate_images.py --model doubao-seedream-4-5-251128 --size 2K
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

# 火山引擎方舟 API (中国区)
DEFAULT_ARK_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"
DEFAULT_MODEL = "doubao-seedream-4-0-250828"
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
# API 客户端（延迟初始化，dry-run 时不需要）
# ---------------------------------------------------------------------------
_client = None


def get_client(base_url: str, api_key: str):
    """延迟初始化 Ark SDK 客户端"""
    global _client
    if _client is None:
        try:
            from volcenginesdkarkruntime import Ark
        except ImportError:
            log.error("未安装 volcenginesdkarkruntime，请运行: pip install volcenginesdkarkruntime --break-system-packages")
            sys.exit(1)
        _client = Ark(base_url=base_url, api_key=api_key)
    return _client


def generate_one_image(
    client,
    prompt: str,
    model: str,
    size: str,
    seed: int,
    output_path: str,
) -> bool:
    """
    调用 Seedream API 生成单张图片并保存到磁盘。

    返回 True=成功, False=失败
    """
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.images.generate(
                model=model,
                prompt=prompt,
                size=size,
                seed=seed,
                response_format="b64_json",
                watermark=False,
            )

            # 解码 base64 并保存
            b64_data = response.data[0].b64_json
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

    每个任务 = {
        "element": 元素名,
        "type": characters/locations/props,
        "priority": P0/P1 等,
        "stars": 星级,
        "stage_id": 阶段ID或None,
        "prompt_en": 英文提示词（已拼接前缀）,
        "prompt_cn": 中文提示词,
        "output_path": 输出文件绝对路径,
        "seed": 种子值,
        "is_portrait": 是否为肖像,
    }
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

            # 确定输出路径
            if elem_type == "characters":
                # 第一个提示词通常是肖像
                if idx == 0:
                    # 肖像 → _portrait/ 目录
                    out_path = os.path.join(type_dir, "_portrait", "正面半身像.png")
                    is_portrait = True
                elif stage_id:
                    out_path = os.path.join(type_dir, stage_id, f"{idx:02d}.png")
                    is_portrait = False
                else:
                    out_path = os.path.join(type_dir, "_portrait", f"{idx:02d}.png")
                    is_portrait = True
            elif elem_type == "locations":
                if stage_id:
                    out_path = os.path.join(type_dir, stage_id, f"{idx:02d}.png")
                else:
                    out_path = os.path.join(type_dir, "默认", f"{idx:02d}.png")
                is_portrait = False
            else:  # props
                if stage_id:
                    out_path = os.path.join(type_dir, stage_id, f"{idx:02d}.png")
                else:
                    out_path = os.path.join(type_dir, f"{idx:02d}.png")
                is_portrait = False

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
    parser = argparse.ArgumentParser(description="调用 Seedream API 批量生成视觉资产")
    parser.add_argument("--base-dir", default=DEFAULT_BASE, help="production 目录")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Seedream 模型 ID (默认: {DEFAULT_MODEL})")
    parser.add_argument("--size", default=DEFAULT_SIZE, help=f"图片尺寸 (默认: {DEFAULT_SIZE})")
    parser.add_argument("--priority", default=None, help="只生成指定优先级 (如: P0/P1, P2)")
    parser.add_argument("--element", default=None, help="只生成指定元素 (如: 吴文顶)")
    parser.add_argument("--type", default=None, dest="elem_type", help="只生成指定类型 (characters/locations/props)")
    parser.add_argument("--dry-run", action="store_true", help="只输出计划，不调 API")
    parser.add_argument("--no-skip", action="store_true", help="不跳过已有图片的目录")
    parser.add_argument("--delay", type=float, default=DEFAULT_QPS_DELAY, help=f"API 调用间隔秒数 (默认: {DEFAULT_QPS_DELAY})")
    parser.add_argument("--ark-base-url", default=DEFAULT_ARK_BASE_URL, help="Ark API base URL")
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
            print(f"  [{t['type']}] {t['element']}/{t['stage_id']}{portrait_tag}")
            print(f"    → {t['output_path']}")
            print(f"    prompt: {t['prompt_en'][:80]}...")
            print()

        # 统计摘要
        by_type = {}
        for t in tasks:
            by_type[t["type"]] = by_type.get(t["type"], 0) + 1
        print(f"\n摘要: ", end="")
        print(", ".join(f"{k}: {v}" for k, v in by_type.items()))
        print(f"总计: {len(tasks)} 张图片待生成")
        return

    # ---- 实际调用 API ----
    api_key = os.environ.get("ARK_API_KEY", "")
    if not api_key:
        log.error("未设置 ARK_API_KEY 环境变量！请运行: export ARK_API_KEY=your-key")
        sys.exit(1)

    client = get_client(args.ark_base_url, api_key)

    total = len(tasks)
    success = 0
    failed = 0
    start_time = time.time()

    # 生成日志（用于断点恢复和事后审计）
    log_path = os.path.join(assets_root, "generation_log.jsonl")

    log.info(f"\n开始生成 {total} 张图片 (模型: {args.model}, 尺寸: {args.size})\n")

    for i, t in enumerate(tasks, 1):
        portrait_tag = " [肖像]" if t["is_portrait"] else ""
        log.info(f"[{i}/{total}] {t['element']}/{t['stage_id']}{portrait_tag}")

        ok = generate_one_image(
            client=client,
            prompt=t["prompt_en"],
            model=args.model,
            size=args.size,
            seed=t["seed"],
            output_path=t["output_path"],
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
