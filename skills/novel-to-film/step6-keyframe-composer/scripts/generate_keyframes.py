#!/usr/bin/env python3
"""
generate_keyframes.py — 调用 Seedream API 批量生成锚点首帧图

核心功能：
1. 读取 prompt_assembly.json（含已翻译的 Layer 3）
2. 组装最终 prompt（Layer 1 + Layer 2 + Layer 3 + Negative）
3. 收集参考图路径
4. 调用 Seedream API 生成图片（每个镜头 3-5 张候选）
5. 保存到 step6-keyframes/{场次}/{镜号}_first.png
6. 生成 {镜号}_prompt.md 记录文件

用法：
    export ARK_API_KEY="your-api-key"
    python3 generate_keyframes.py [--base-dir /path/to/production]
    python3 generate_keyframes.py --dry-run          # 只看计划
    python3 generate_keyframes.py --limit 5          # 只生成 5 个
    python3 generate_keyframes.py --shot SC001-001   # 只生成指定镜头
    python3 generate_keyframes.py --candidates 3     # 每镜头 3 张候选
"""

import os
import sys
import json
import time
import base64
import argparse
import logging
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("请先安装 requests: pip install requests --break-system-packages")
    sys.exit(1)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from storyboard_utils import DEFAULT_BASE

# ---------------------------------------------------------------------------
# 日志 & 常量
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("generate")

# 火山引擎方舟 Seedream API
DEFAULT_ARK_API_URL = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
DEFAULT_MODEL = "doubao-seedream-5-0-260128"
DEFAULT_SIZE = "1920x804"   # 2.39:1 宽银幕
DEFAULT_SEED_BASE = 100
DEFAULT_QPS_DELAY = 1.5
MAX_RETRIES = 3
RETRY_BACKOFF = 2.0
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp'}


# ---------------------------------------------------------------------------
# 参考图工具
# ---------------------------------------------------------------------------
def load_ref_image_as_data_uri(image_path: str) -> str:
    """读取本地图片文件，返回 data:image/...;base64,... URI"""
    ext = os.path.splitext(image_path)[1].lower()
    mime_map = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}
    mime = mime_map.get(ext, "image/png")
    with open(image_path, "rb") as f:
        b64_str = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{b64_str}"


def find_first_image(ref_dir: str, assets_root: str) -> str:
    """在参考图目录中找到第一张图片"""
    full_dir = os.path.join(assets_root, ref_dir)
    if not os.path.isdir(full_dir):
        return ""
    for f in sorted(os.listdir(full_dir)):
        if os.path.splitext(f)[1].lower() in IMAGE_EXTS:
            return os.path.join(full_dir, f)
    return ""


# ---------------------------------------------------------------------------
# Prompt 组装
# ---------------------------------------------------------------------------
def assemble_final_prompt(assembly: dict) -> str:
    """将 4 层 prompt 组装为最终字符串"""
    parts = []

    # Layer 1: 全局风格前缀
    if assembly.get("layer1_global_prefix"):
        parts.append(assembly["layer1_global_prefix"])

    # Layer 2: 景别 + 机位
    if assembly.get("layer2_shot_spec"):
        parts.append(assembly["layer2_shot_spec"])

    # Layer 3: 翻译后的画面内容
    if assembly.get("layer3_visual_content"):
        parts.append(assembly["layer3_visual_content"])

    return ", ".join(parts)


def assemble_negative_prompt(assembly: dict) -> str:
    """组装负面提示词"""
    parts = []
    if assembly.get("negative_global"):
        parts.append(assembly["negative_global"])
    if assembly.get("negative_scene"):
        parts.append(assembly["negative_scene"])
    return ", ".join(parts)


# ---------------------------------------------------------------------------
# API 调用
# ---------------------------------------------------------------------------
def generate_one_image(
    api_url: str,
    api_key: str,
    prompt: str,
    negative: str,
    model: str,
    size: str,
    seed: int,
    output_path: str,
    ref_image_paths: list = None,
) -> bool:
    """调用 Seedream REST API 生成单张图片"""
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

    if negative:
        payload["negative_prompt"] = negative

    # 参考图
    if ref_image_paths:
        ref_uris = []
        for rpath in ref_image_paths:
            if os.path.exists(rpath):
                try:
                    ref_uris.append(load_ref_image_as_data_uri(rpath))
                except Exception as e:
                    log.warning(f"  ⚠️ 读取参考图失败: {rpath}: {e}")
        if ref_uris:
            payload["image"] = ref_uris
            log.info(f"  📎 使用 {len(ref_uris)} 个参考图")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.post(api_url, headers=headers, json=payload, timeout=120)

            if resp.status_code != 200:
                raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:200]}")

            data = resp.json()
            img_data_list = data.get("data", [])
            if not img_data_list:
                raise RuntimeError(f"返回数据中无 data 字段")

            b64_data = img_data_list[0].get("b64_json", "")
            if not b64_data:
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
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF ** attempt
                log.warning(f"  ⚠️ 第{attempt}次失败: {str(e)[:80]}... {wait:.1f}s 后重试")
                time.sleep(wait)
            else:
                log.error(f"  ❌ 生成失败: {str(e)[:120]}")
                return False

    return False


# ---------------------------------------------------------------------------
# Prompt 记录文件
# ---------------------------------------------------------------------------
def write_prompt_record(assembly: dict, final_prompt: str, negative: str,
                        ref_images_used: list, seed: int, output_dir: str,
                        model: str, size: str, success: bool):
    """生成 {镜号}_prompt.md 记录文件"""
    sid = assembly["shot_id"]
    scene_id = assembly["scene_id"]
    md_path = os.path.join(output_dir, scene_id, f"{sid}_prompt.md")

    lines = [
        f"# Prompt Record: {sid}",
        "",
        "## 来源",
        "",
        f"- 分镜脚本：storyboard/{scene_id}.md → 镜头 {sid}",
        f"- 章节：{assembly['metadata'].get('chapter', '')}",
        "",
        "## 完整 Prompt",
        "",
        "### Positive (English)",
        "```",
        final_prompt,
        "```",
        "",
        "### Positive (中文)",
        "```",
        assembly.get("layer3_source_cn", "")[:500],
        "```",
        "",
        "### Negative (English)",
        "```",
        negative,
        "```",
        "",
        "## 参考图",
        "",
        "| 用途 | 文件路径 | 权重 | 说明 |",
        "|------|---------|------|------|",
    ]

    for ref in assembly.get("ref_images", []):
        lines.append(f"| {ref['purpose']} | {ref['ref_path']} | {ref['weight']} | {ref['note']} |")

    lines.extend([
        "",
        "## 生成参数",
        "",
        "| 参数 | 值 |",
        "|------|-----|",
        f"| 图片类型 | 锚点帧 |",
        f"| 分辨率 | {size} |",
        f"| Seed | {seed} |",
        f"| 模型 | {model} |",
        f"| 生成时间 | {datetime.now().isoformat()} |",
        f"| 成功 | {'✅' if success else '❌'} |",
    ])

    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="调用 Seedream API 批量生成锚点首帧图")
    parser.add_argument("--base-dir", default=DEFAULT_BASE, help="production 目录")
    parser.add_argument("--input", default=None, help="prompt_assembly.json 路径")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Seedream 模型 (默认: {DEFAULT_MODEL})")
    parser.add_argument("--size", default=DEFAULT_SIZE, help=f"图片尺寸 (默认: {DEFAULT_SIZE})")
    parser.add_argument("--candidates", type=int, default=1, help="每镜头生成候选数 (默认: 1)")
    parser.add_argument("--dry-run", action="store_true", help="只看计划")
    parser.add_argument("--limit", type=int, default=0, help="最多生成 N 个")
    parser.add_argument("--shot", default=None, help="只生成指定镜头")
    parser.add_argument("--no-skip", action="store_true", help="不跳过已有图片")
    parser.add_argument("--delay", type=float, default=DEFAULT_QPS_DELAY, help=f"API 间隔 (默认: {DEFAULT_QPS_DELAY}s)")
    parser.add_argument("--ark-api-url", default=DEFAULT_ARK_API_URL, help="方舟 API URL")
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    input_path = args.input or os.path.join(base, "step6-keyframes", "prompt_assembly.json")
    translations_path = os.path.join(base, "step6-keyframes", "layer3_translations.json")
    output_dir = os.path.join(base, "step6-keyframes")
    assets_root = os.path.join(base, "step4-assets")

    # 1. 加载 prompt 骨架
    if not os.path.exists(input_path):
        log.error(f"输入文件不存在: {input_path}")
        log.error("请先运行: python3 assemble_prompts.py")
        sys.exit(1)

    with open(input_path, 'r', encoding='utf-8') as f:
        assemblies = json.load(f)
    log.info(f"加载 {len(assemblies)} 个 prompt 骨架")

    # 2. 加载 Layer 3 翻译并合并
    if not os.path.exists(translations_path):
        log.error(f"翻译文件不存在: {translations_path}")
        log.error("请先在 Claude Desktop 对话中生成 layer3_translations.json")
        sys.exit(1)

    with open(translations_path, 'r', encoding='utf-8') as f:
        translations = json.load(f)
    log.info(f"加载 {len(translations)} 条 Layer 3 翻译")

    # 合并：将翻译写入 assembly 的 layer3_visual_content
    merged = 0
    for a in assemblies:
        l3 = translations.get(a["shot_id"], "")
        if l3:
            a["layer3_visual_content"] = l3
            merged += 1

    ready = [a for a in assemblies if a.get("layer3_visual_content")]
    log.info(f"合并完成: {merged} 条翻译已注入, {len(ready)} 个 prompt 就绪")

    # 2. 过滤
    tasks = ready
    if args.shot:
        tasks = [a for a in tasks if a["shot_id"] == args.shot]
    if not args.no_skip:
        before = len(tasks)
        tasks = [a for a in tasks if not os.path.exists(
            os.path.join(output_dir, a["scene_id"], f"{a['shot_id']}_first.png")
        )]
        skipped = before - len(tasks)
        if skipped:
            log.info(f"跳过已有图片: {skipped} 个")
    if args.limit > 0:
        tasks = tasks[:args.limit]

    log.info(f"待生成: {len(tasks)} 个锚点帧")

    if not tasks:
        log.info("无待生成任务")
        return

    # 3. Dry-run
    if args.dry_run:
        print(f"\nDRY RUN — 共 {len(tasks)} 个待生成\n")
        for a in tasks[:5]:
            final = assemble_final_prompt(a)
            negative = assemble_negative_prompt(a)
            print(f"--- {a['shot_id']} ---")
            print(f"  Prompt: {final[:120]}...")
            print(f"  Negative: {negative[:80]}...")
            print(f"  参考图: {len(a.get('ref_images', []))} 个")
            print(f"  输出: {output_dir}/{a['scene_id']}/{a['shot_id']}_first.png\n")
        return

    # 4. API Key
    api_key = os.environ.get("ARK_API_KEY", "")
    if not api_key:
        log.error("未设置 ARK_API_KEY 环境变量！")
        sys.exit(1)

    # 5. 批量生成
    total = len(tasks)
    success = 0
    failed = 0
    start_time = time.time()

    log_path = os.path.join(output_dir, "generation_log.jsonl")

    log.info(f"\n开始生成 {total} 个锚点帧 (模型: {args.model}, 尺寸: {args.size})\n")

    for i, assembly in enumerate(tasks, 1):
        sid = assembly["shot_id"]
        scene_id = assembly["scene_id"]
        log.info(f"[{i}/{total}] 生成 {sid}")

        final_prompt = assemble_final_prompt(assembly)
        negative = assemble_negative_prompt(assembly)
        output_path = os.path.join(output_dir, scene_id, f"{sid}_first.png")
        seed = (DEFAULT_SEED_BASE + hash(sid)) % (2**31)

        # 收集参考图实际路径
        ref_paths = []
        for ref in assembly.get("ref_images", []):
            img_path = find_first_image(ref["ref_path"], assets_root)
            if img_path:
                ref_paths.append(img_path)

        ok = generate_one_image(
            api_url=args.ark_api_url,
            api_key=api_key,
            prompt=final_prompt,
            negative=negative,
            model=args.model,
            size=args.size,
            seed=seed,
            output_path=output_path,
            ref_image_paths=ref_paths,
        )

        if ok:
            success += 1
        else:
            failed += 1

        # 写 prompt 记录
        write_prompt_record(assembly, final_prompt, negative, ref_paths, seed,
                            output_dir, args.model, args.size, ok)

        # 生成日志
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "shot_id": sid,
            "scene_id": scene_id,
            "output_path": output_path,
            "seed": seed,
            "model": args.model,
            "size": args.size,
            "ref_count": len(ref_paths),
            "success": ok,
            "prompt_preview": final_prompt[:200],
        }
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

        if i < total:
            time.sleep(args.delay)

    elapsed = time.time() - start_time
    log.info(f"\n{'='*50}")
    log.info(f"生成完成！用时 {elapsed:.1f}s")
    log.info(f"  成功: {success}/{total}")
    log.info(f"  失败: {failed}/{total}")
    log.info(f"{'='*50}")


if __name__ == "__main__":
    main()
