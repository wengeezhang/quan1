#!/usr/bin/env python3
"""
build_index.py — 扫描 step4-assets/ 实际文件，生成 asset_index.md

功能：
1. 遍历 production/step4-assets/ 下所有图片文件（扁平化结构）
2. 交叉引用圣经阶段注册表，获取 stage_id 对应的章节范围
3. 生成 asset_index.md（下游 Step 5/6 的核心映射表）

扁平化目录结构（v2）：
    characters/{角色名}/{角色名}_肖像.png    — 正面半身像
    characters/{角色名}/{角色名}_三视图.png   — Character Sheet
    characters/{角色名}/{角色名}_{stage_id}.png — 阶段图
    locations/{场景名}/{场景名}_{stage_id}.png
    props/{道具名}/{道具名}_{stage_id}.png

用法：
    python3 build_index.py [--base-dir /path/to/production]

注意：
    - 文件存在时图片数=1，缺失时=0
    - 图片文件识别：.png, .jpg, .jpeg, .webp
"""

import os
import argparse
from pathlib import Path
from datetime import datetime

# 导入共享工具函数
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bible_utils import extract_stage_chapters, BIBLE_DIRS, IMAGE_EXTS


DEFAULT_BASE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "production")

# 肖像类固定后缀（非阶段）
PORTRAIT_SUFFIX = "肖像"
CHARACTER_SHEET_SUFFIX = "三视图"


def build_bible_map(base_dir: str) -> dict:
    """构建 {元素类型: {名称: {stage_id: 章节范围}}}"""
    bible_map = {}
    for elem_type, rel_path in BIBLE_DIRS.items():
        bible_dir = os.path.join(base_dir, rel_path)
        if not os.path.isdir(bible_dir):
            continue
        bible_map[elem_type] = {}
        for root, _dirs, files in os.walk(bible_dir):
            for fname in sorted(files):
                if not fname.endswith('.md'):
                    continue
                fpath = os.path.join(root, fname)
                with open(fpath, 'r', encoding='utf-8') as f:
                    text = f.read()
                name = fname.replace('.md', '')
                bible_map[elem_type][name] = extract_stage_chapters(text)
    return bible_map


def parse_filename(fname: str, element_name: str) -> tuple:
    """
    解析文件名，返回 (类别, 后缀) 或 None（不符合规则）。

    类别：'肖像' | '三视图' | '阶段'
    后缀：对于阶段图，后缀即 stage_id；对于肖像/三视图，后缀为固定值
    """
    base, ext = os.path.splitext(fname)
    if ext.lower() not in IMAGE_EXTS:
        return None

    prefix = f"{element_name}_"
    if not base.startswith(prefix):
        return None

    suffix = base[len(prefix):]
    if not suffix:
        return None

    if suffix == PORTRAIT_SUFFIX:
        return ('肖像', suffix)
    if suffix == CHARACTER_SHEET_SUFFIX:
        return ('三视图', suffix)
    return ('阶段', suffix)


def scan_element_dir(elem_dir: str, element_name: str) -> dict:
    """
    扫描单个元素目录，返回：
    {
        'portrait': 文件名 or None,
        'character_sheet': 文件名 or None,
        'stages': {stage_id: 文件名},
    }
    """
    result = {'portrait': None, 'character_sheet': None, 'stages': {}}
    if not os.path.isdir(elem_dir):
        return result

    for fname in sorted(os.listdir(elem_dir)):
        parsed = parse_filename(fname, element_name)
        if not parsed:
            continue
        category, suffix = parsed
        if category == '肖像':
            result['portrait'] = fname
        elif category == '三视图':
            result['character_sheet'] = fname
        else:  # 阶段
            result['stages'][suffix] = fname

    return result


def generate_index(base_dir: str, output_path: str):
    """生成 asset_index.md"""
    assets_root = os.path.join(base_dir, "step4-assets")
    bible_map = build_bible_map(base_dir)

    lines = [
        "# 视觉资产索引",
        "",
        "> 本文件由阶段4（视觉资产生成）产出，是阶段5（分镜脚本）和阶段6（首帧合成）查找参考图的核心映射表。",
        '> 分镜脚本中标注"角色名(阶段: {stage_id})"后, 直接在本表中查找对应的参考图路径。',
        "",
        f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "**目录结构**（扁平化）：",
        "- `characters/{name}/{name}_肖像.png` — 正面半身像",
        "- `characters/{name}/{name}_三视图.png` — Character Sheet",
        "- `characters/{name}/{name}_{stage_id}.png` — 阶段图",
        "- `locations/{name}/{name}_{stage_id}.png`",
        "- `props/{name}/{name}_{stage_id}.png`",
        "",
    ]

    total_assets = 0
    total_images = 0

    # ---- 角色资产 ----
    lines.append("## 角色资产\n")
    lines.append("| 角色名 | 类型 | stage_id | 章节范围 | 参考图路径 | 存在 |")
    lines.append("|--------|------|----------|---------|-----------|------|")

    char_dir = os.path.join(assets_root, "characters")
    if os.path.isdir(char_dir):
        char_bibles = bible_map.get("characters", {})
        for name in sorted(os.listdir(char_dir)):
            name_dir = os.path.join(char_dir, name)
            if not os.path.isdir(name_dir):
                continue

            assets = scan_element_dir(name_dir, name)
            stage_chapters = char_bibles.get(name, {})

            # 肖像行
            fname = assets['portrait'] or f"{name}_肖像.png"
            exists = 1 if assets['portrait'] else 0
            rel_path = f"characters/{name}/{fname}"
            lines.append(f"| {name} | 肖像 | — | — | {rel_path} | {exists} |")
            total_images += exists
            total_assets += 1

            # 三视图行
            fname = assets['character_sheet'] or f"{name}_三视图.png"
            exists = 1 if assets['character_sheet'] else 0
            rel_path = f"characters/{name}/{fname}"
            lines.append(f"| {name} | 三视图 | — | — | {rel_path} | {exists} |")
            total_images += exists
            total_assets += 1

            # 阶段行（基于圣经的阶段注册表，不是文件系统）
            for stage_id, chapter in stage_chapters.items():
                fname = assets['stages'].get(stage_id) or f"{name}_{stage_id}.png"
                exists = 1 if stage_id in assets['stages'] else 0
                rel_path = f"characters/{name}/{fname}"
                lines.append(f"| {name} | 阶段 | {stage_id} | {chapter} | {rel_path} | {exists} |")
                total_images += exists
                total_assets += 1

    # ---- 场景资产 ----
    lines.append("\n## 场景资产\n")
    lines.append("| 场景名 | stage_id | 章节范围 | 参考图路径 | 存在 |")
    lines.append("|--------|----------|---------|-----------|------|")

    loc_dir = os.path.join(assets_root, "locations")
    if os.path.isdir(loc_dir):
        loc_bibles = bible_map.get("locations", {})
        for name in sorted(os.listdir(loc_dir)):
            name_dir = os.path.join(loc_dir, name)
            if not os.path.isdir(name_dir):
                continue

            assets = scan_element_dir(name_dir, name)
            stage_chapters = loc_bibles.get(name, {})

            for stage_id, chapter in stage_chapters.items():
                fname = assets['stages'].get(stage_id) or f"{name}_{stage_id}.png"
                exists = 1 if stage_id in assets['stages'] else 0
                rel_path = f"locations/{name}/{fname}"
                lines.append(f"| {name} | {stage_id} | {chapter} | {rel_path} | {exists} |")
                total_images += exists
                total_assets += 1

    # ---- 道具资产 ----
    lines.append("\n## 道具资产\n")
    lines.append("| 道具名 | stage_id | 章节范围 | 参考图路径 | 存在 |")
    lines.append("|--------|----------|---------|-----------|------|")

    prop_dir = os.path.join(assets_root, "props")
    if os.path.isdir(prop_dir):
        prop_bibles = bible_map.get("props", {})
        for name in sorted(os.listdir(prop_dir)):
            name_dir = os.path.join(prop_dir, name)
            if not os.path.isdir(name_dir):
                continue

            assets = scan_element_dir(name_dir, name)
            stage_chapters = prop_bibles.get(name, {})

            for stage_id, chapter in stage_chapters.items():
                fname = assets['stages'].get(stage_id) or f"{name}_{stage_id}.png"
                exists = 1 if stage_id in assets['stages'] else 0
                rel_path = f"props/{name}/{fname}"
                lines.append(f"| {name} | {stage_id} | {chapter} | {rel_path} | {exists} |")
                total_images += exists
                total_assets += 1

    # 尾部统计
    lines.append(f"\n---\n")
    lines.append(f"**总资产条目**: {total_assets} | **已生成图片**: {total_images} | **缺失**: {total_assets - total_images}")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return total_assets, total_images


def main():
    parser = argparse.ArgumentParser(description="生成 asset_index.md")
    parser.add_argument('--base-dir', default=DEFAULT_BASE, help='production 目录路径')
    parser.add_argument('--output', default=None, help='输出路径 (默认: step4-assets/asset_index.md)')
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    output = args.output or os.path.join(base, "step4-assets", "asset_index.md")
    os.makedirs(os.path.dirname(output), exist_ok=True)

    assets, images = generate_index(base, output)
    print(f"✅ asset_index.md 已生成: {output}")
    print(f"   资产条目: {assets}, 已生成图片: {images}, 缺失: {assets - images}")


if __name__ == '__main__':
    main()
