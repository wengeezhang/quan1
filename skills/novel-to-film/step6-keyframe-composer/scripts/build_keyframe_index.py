#!/usr/bin/env python3
"""
build_keyframe_index.py — 扫描已生成的锚点帧，输出 keyframe_index.md

核心功能：
1. 读取 shot_classification.json（镜头分类）
2. 扫描 step6-keyframes/ 下的实际文件
3. 生成 keyframe_index.md（step7 的核心输入）

用法：
    python3 build_keyframe_index.py [--base-dir /path/to/production]
"""

import os
import sys
import json
import argparse
import logging
from datetime import datetime
from collections import defaultdict

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
log = logging.getLogger("build_index")

# 帧类型映射
FRAME_TYPE_LABELS = {
    "independent": "独立锚点",
    "chain_head": "链头锚点",
    "chain_internal": "step7提供",
    "shot_reverse_shot": "正反打锚点",
}


def main():
    parser = argparse.ArgumentParser(description="生成 keyframe_index.md")
    parser.add_argument("--base-dir", default=DEFAULT_BASE, help="production 目录")
    parser.add_argument("--output", default=None, help="输出路径")
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    kf_dir = os.path.join(base, "step6-keyframes")
    class_path = os.path.join(kf_dir, "shot_classification.json")
    output = args.output or os.path.join(kf_dir, "keyframe_index.md")

    # 1. 加载分类
    if not os.path.exists(class_path):
        log.error(f"分类文件不存在: {class_path}")
        sys.exit(1)

    with open(class_path, 'r', encoding='utf-8') as f:
        classification = json.load(f)

    shots = classification["shots"]
    chains = classification.get("chains", [])
    srs_groups = classification.get("srs_groups", [])
    stats = classification.get("stats", {})

    # 2. 扫描实际文件
    existing_frames = set()
    for root, dirs, files in os.walk(kf_dir):
        for f in files:
            if f.endswith("_first.png"):
                shot_id = f.replace("_first.png", "")
                existing_frames.add(shot_id)

    # 3. 统计
    step6_expected = sum(1 for s in shots if s.get("step6_generates"))
    step6_actual = len(existing_frames)
    step7_count = sum(1 for s in shots if not s.get("step6_generates"))

    log.info(f"总镜头: {len(shots)}")
    log.info(f"step6 期望锚点帧: {step6_expected}")
    log.info(f"step6 实际锚点帧: {step6_actual}")
    log.info(f"step7 提供首帧: {step7_count}")

    # 4. 生成 keyframe_index.md
    lines = [
        "# 锚点帧索引",
        "",
        "> 本文件由阶段6（首帧合成）产出。",
        "> 阶段7（视频生成）通过本索引确定：哪些镜头有 step6 提供的锚点帧，哪些镜头需要从前一视频提取首帧。",
        f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## 统计",
        "",
        "| 指标 | 值 |",
        "|------|-----|",
        f"| 总镜头数 | {len(shots)} |",
        f"| step6 锚点帧数（期望） | {step6_expected} |",
        f"| step6 锚点帧数（实际） | {step6_actual} |",
        f"| 连续性链内镜头数（step7 提供首帧） | {step7_count} |",
        f"| 连续性链数量 | {len(chains)} |",
        f"| 正反打序列组数 | {len(srs_groups)} |",
        "",
    ]

    # 连续性链清单
    if chains:
        lines.extend([
            "## 连续性链清单",
            "",
            "| 链 ID | 链头镜号 | 链内镜号 | 长度 |",
            "|-------|---------|---------|------|",
        ])
        for chain in chains:
            head = chain["head"]
            internals = ", ".join(chain["shots"][1:]) if len(chain["shots"]) > 1 else "—"
            lines.append(f"| {chain['chain_id']} | {head} | {internals} | {chain['length']} |")
        lines.append("")

    # 正反打序列清单
    if srs_groups:
        lines.extend([
            "## 正反打序列清单",
            "",
            "| 组 ID | 镜头 | 数量 |",
            "|-------|------|------|",
        ])
        for g in srs_groups:
            shots_str = ", ".join(g["shots"])
            lines.append(f"| {g['group_id']} | {shots_str} | {len(g['shots'])} |")
        lines.append("")

    # 镜头索引
    lines.extend([
        "## 镜头索引",
        "",
        "| 镜号 | 帧类型 | 锚点帧路径 | 连续性链 | 链内位置 | 正反打组 | 备注 |",
        "|------|--------|-----------|---------|---------|---------|------|",
    ])

    for s in shots:
        sid = s["shot_id"]
        scene_id = s["scene_id"]
        frame_type = FRAME_TYPE_LABELS.get(s["frame_type"], s["frame_type"])
        chain_id = s.get("chain_id") or "—"
        chain_pos = s.get("chain_position") or "—"
        srs_group = s.get("srs_group") or "—"

        if s.get("step6_generates"):
            rel_path = f"{scene_id}/{sid}_first.png"
            if sid in existing_frames:
                note = "✅"
            else:
                note = "⚠️ 未生成"
        else:
            rel_path = "—"
            # 找前驱镜头
            prev_sid = None
            for shot_full in classification["shots"]:
                if shot_full["shot_id"] == sid and shot_full.get("chain_id"):
                    # 在链中找前驱
                    chain_obj = next((c for c in chains if c["chain_id"] == shot_full["chain_id"]), None)
                    if chain_obj:
                        idx = chain_obj["shots"].index(sid) if sid in chain_obj["shots"] else -1
                        if idx > 0:
                            prev_sid = chain_obj["shots"][idx - 1]
                    break
            if prev_sid:
                note = f"首帧来自 {prev_sid} 视频尾帧"
            else:
                note = "step7 提供"

        lines.append(f"| {sid} | {frame_type} | {rel_path} | {chain_id} | {chain_pos} | {srs_group} | {note} |")

    # 缺失警告
    missing = []
    for s in shots:
        if s.get("step6_generates") and s["shot_id"] not in existing_frames:
            missing.append(s["shot_id"])

    if missing:
        lines.extend([
            "",
            "## ⚠️ 缺失锚点帧",
            "",
            f"以下 {len(missing)} 个镜头应由 step6 生成但尚无文件：",
            "",
        ])
        for sid in missing[:50]:
            lines.append(f"- {sid}")
        if len(missing) > 50:
            lines.append(f"- ... 还有 {len(missing) - 50} 个")

    # 写入
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    log.info(f"✅ keyframe_index.md 已生成: {output}")
    if missing:
        log.warning(f"  ⚠️ {len(missing)} 个锚点帧尚未生成")


if __name__ == "__main__":
    main()
