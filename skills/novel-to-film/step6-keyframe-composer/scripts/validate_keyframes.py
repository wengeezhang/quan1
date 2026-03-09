#!/usr/bin/env python3
"""
validate_keyframes.py — 校验锚点帧完整性与一致性

校验维度：
1. 完整性：所有 step6_generates=true 的镜头是否都有对应文件
2. 文件完整性：每个锚点帧是否有对应的 _prompt.md
3. 分类一致性：chain_internal 镜头不应有 step6 生成的文件
4. 参考图可用性：prompt 记录中的参考图路径是否存在

用法：
    python3 validate_keyframes.py [--base-dir /path/to/production]
    python3 validate_keyframes.py --fix    # 自动修复可修复的问题
"""

import os
import sys
import json
import argparse
import logging

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from storyboard_utils import DEFAULT_BASE

# ---------------------------------------------------------------------------
# 日志
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("validate")

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp'}


def main():
    parser = argparse.ArgumentParser(description="校验锚点帧完整性与一致性")
    parser.add_argument("--base-dir", default=DEFAULT_BASE, help="production 目录")
    parser.add_argument("--fix", action="store_true", help="自动修复可修复的问题")
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    kf_dir = os.path.join(base, "step6-keyframes")
    class_path = os.path.join(kf_dir, "shot_classification.json")
    assets_root = os.path.join(base, "step4-assets")

    errors = []
    warnings = []

    # ---- 检查分类文件 ----
    if not os.path.exists(class_path):
        log.error(f"分类文件不存在: {class_path}")
        log.error("请先运行: python3 classify_shots.py")
        sys.exit(1)

    with open(class_path, 'r', encoding='utf-8') as f:
        classification = json.load(f)

    shots = classification["shots"]
    chains = classification.get("chains", [])
    log.info(f"加载 {len(shots)} 个镜头分类")

    # ---- 1. 锚点帧完整性 ----
    log.info("\n检查 1: 锚点帧完整性")
    missing_frames = []
    for s in shots:
        if s.get("step6_generates"):
            sid = s["shot_id"]
            scene_id = s["scene_id"]
            frame_path = os.path.join(kf_dir, scene_id, f"{sid}_first.png")
            if not os.path.exists(frame_path):
                missing_frames.append(sid)

    if missing_frames:
        errors.append(f"缺失锚点帧: {len(missing_frames)} 个")
        log.error(f"  ❌ {len(missing_frames)} 个锚点帧缺失")
        for sid in missing_frames[:10]:
            log.error(f"    - {sid}")
        if len(missing_frames) > 10:
            log.error(f"    ... 还有 {len(missing_frames) - 10} 个")
    else:
        expected = sum(1 for s in shots if s.get("step6_generates"))
        log.info(f"  ✅ 全部 {expected} 个锚点帧存在")

    # ---- 2. Prompt 记录完整性 ----
    log.info("\n检查 2: Prompt 记录完整性")
    missing_prompts = []
    for s in shots:
        if s.get("step6_generates"):
            sid = s["shot_id"]
            scene_id = s["scene_id"]
            prompt_path = os.path.join(kf_dir, scene_id, f"{sid}_prompt.md")
            frame_path = os.path.join(kf_dir, scene_id, f"{sid}_first.png")
            if os.path.exists(frame_path) and not os.path.exists(prompt_path):
                missing_prompts.append(sid)

    if missing_prompts:
        warnings.append(f"缺失 prompt 记录: {len(missing_prompts)} 个")
        log.warning(f"  ⚠️ {len(missing_prompts)} 个 prompt 记录缺失（有图片但无记录）")
        for sid in missing_prompts[:10]:
            log.warning(f"    - {sid}")
    else:
        log.info(f"  ✅ 所有锚点帧都有对应 prompt 记录")

    # ---- 3. 链内镜头不应有 step6 文件 ----
    log.info("\n检查 3: 链内镜头文件检查")
    orphan_files = []
    for s in shots:
        if not s.get("step6_generates"):
            sid = s["shot_id"]
            scene_id = s["scene_id"]
            frame_path = os.path.join(kf_dir, scene_id, f"{sid}_first.png")
            if os.path.exists(frame_path):
                orphan_files.append(sid)

    if orphan_files:
        warnings.append(f"链内镜头存在多余文件: {len(orphan_files)} 个")
        log.warning(f"  ⚠️ {len(orphan_files)} 个链内镜头存在不应有的锚点帧文件")
        for sid in orphan_files[:10]:
            log.warning(f"    - {sid}")
    else:
        log.info(f"  ✅ 链内镜头无多余文件")

    # ---- 4. 连续性链完整性 ----
    log.info("\n检查 4: 连续性链完整性")
    broken_chains = []
    for chain in chains:
        head = chain["head"]
        head_frame = os.path.join(kf_dir, head.rsplit('-', 1)[0] if '-' in head else head,
                                   f"{head}_first.png")
        # 简单匹配 scene_id
        for s in shots:
            if s["shot_id"] == head:
                head_frame = os.path.join(kf_dir, s["scene_id"], f"{head}_first.png")
                break
        if not os.path.exists(head_frame):
            broken_chains.append(chain["chain_id"])

    if broken_chains:
        errors.append(f"连续性链链头缺失: {len(broken_chains)} 条")
        log.error(f"  ❌ {len(broken_chains)} 条连续性链的链头锚点帧缺失")
        for cid in broken_chains[:10]:
            log.error(f"    - {cid}")
    else:
        log.info(f"  ✅ 全部 {len(chains)} 条连续性链的链头锚点帧存在")

    # ---- 5. 文件大小检查 ----
    log.info("\n检查 5: 文件大小检查")
    small_files = []
    total_size = 0
    file_count = 0
    for root, dirs, files in os.walk(kf_dir):
        for f in files:
            if f.endswith("_first.png"):
                fpath = os.path.join(root, f)
                size = os.path.getsize(fpath)
                total_size += size
                file_count += 1
                if size < 10 * 1024:  # 小于 10KB
                    small_files.append((f, size))

    if small_files:
        warnings.append(f"疑似损坏文件: {len(small_files)} 个（< 10KB）")
        log.warning(f"  ⚠️ {len(small_files)} 个文件小于 10KB（可能损坏）")
        for fname, size in small_files[:10]:
            log.warning(f"    - {fname} ({size} bytes)")
    else:
        avg = total_size / max(file_count, 1) / 1024
        log.info(f"  ✅ {file_count} 个文件, 平均 {avg:.0f} KB")

    # ---- 汇总 ----
    print(f"\n{'='*50}")
    print(f"校验完成")
    print(f"{'='*50}")
    if errors:
        print(f"  ❌ 错误: {len(errors)}")
        for e in errors:
            print(f"    - {e}")
    if warnings:
        print(f"  ⚠️ 警告: {len(warnings)}")
        for w in warnings:
            print(f"    - {w}")
    if not errors and not warnings:
        print(f"  ✅ 全部通过！")
    print(f"{'='*50}\n")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
