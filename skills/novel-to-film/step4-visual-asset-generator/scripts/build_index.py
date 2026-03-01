#!/usr/bin/env python3
"""
build_index.py — 扫描 step4-assets/ 实际文件，生成 asset_index.md

功能：
1. 遍历 production/step4-assets/ 下所有图片文件
2. 交叉引用圣经阶段注册表，获取 stage_id 对应的章节范围
3. 生成 asset_index.md（下游 Step 5/6 的核心映射表）

用法：
    python3 build_index.py [--base-dir /path/to/production]

注意：
    - 目录为空时也会生成骨架索引（图片数=0），方便预览结构
    - 图片文件识别：.png, .jpg, .jpeg, .webp
"""

import os
import re
import argparse
from pathlib import Path
from datetime import datetime

# 导入共享工具函数
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bible_utils import count_stars, extract_stage_chapters, count_images, BIBLE_DIRS, IMAGE_EXTS


DEFAULT_BASE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "production")



def build_bible_map(base_dir: str) -> dict:
    """构建 {元素类型: {名称: {stars, stages: {stage_id: chapter_range}}}} """
    bible_map = {}
    for elem_type, rel_path in BIBLE_DIRS.items():
        bible_dir = os.path.join(base_dir, rel_path)
        if not os.path.isdir(bible_dir):
            continue
        bible_map[elem_type] = {}
        for root, dirs, files in os.walk(bible_dir):
            for fname in sorted(files):
                if not fname.endswith('.md'):
                    continue
                fpath = os.path.join(root, fname)
                with open(fpath, 'r', encoding='utf-8') as f:
                    text = f.read()
                name = fname.replace('.md', '')
                bible_map[elem_type][name] = {
                    'stars': count_stars(text),
                    'stages': extract_stage_chapters(text),
                }
    return bible_map


def generate_index(base_dir: str, output_path: str):
    """生成 asset_index.md"""
    assets_root = os.path.join(base_dir, "step4-assets")
    bible_map = build_bible_map(base_dir)

    lines = [
        "# 视觉资产索引",
        "",
        "> 本文件由阶段4（视觉资产生成）产出，是阶段5（分镜脚本）和阶段6（首帧合成）查找参考图的核心映射表。",
        '> 分镜脚本中标注"角色名(阶段: {stage_id})"后, 直接在本表中查找对应的参考图路径。',
        f"",
        f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]

    total_assets = 0
    total_images = 0

    # ---- 角色资产 ----
    lines.append("## 角色资产\n")
    lines.append("| 角色名 | 类型 | stage_id | 章节范围 | 参考图路径 | 图片数 |")
    lines.append("|--------|------|----------|---------|-----------|--------|")

    char_dir = os.path.join(assets_root, "characters")
    if os.path.isdir(char_dir):
        char_bibles = bible_map.get("characters", {})
        for name in sorted(os.listdir(char_dir)):
            name_dir = os.path.join(char_dir, name)
            if not os.path.isdir(name_dir):
                continue
            info = char_bibles.get(name, {'stars': 0, 'stages': {}})
            stars = info['stars']

            # 肖像行
            portrait_dir = os.path.join(name_dir, "_portrait")
            img_count = count_images(portrait_dir)
            rel_path = f"characters/{name}/_portrait/"
            lines.append(f"| {name} | 肖像 | — | — | {rel_path} | {img_count} |")
            total_images += img_count
            total_assets += 1

            # 阶段行
            for sub in sorted(os.listdir(name_dir)):
                if sub == '_portrait':
                    continue
                sub_dir = os.path.join(name_dir, sub)
                if not os.path.isdir(sub_dir):
                    continue
                chapter = info['stages'].get(sub, '—')
                img_count = count_images(sub_dir)
                rel_path = f"characters/{name}/{sub}/"
                lines.append(f"| {name} | 阶段 | {sub} | {chapter} | {rel_path} | {img_count} |")
                total_images += img_count
                total_assets += 1

    # ---- 场景资产 ----
    lines.append("\n## 场景资产\n")
    lines.append("| 场景名 | stage_id | 章节范围 | 参考图路径 | 图片数 |")
    lines.append("|--------|----------|---------|-----------|--------|")

    loc_dir = os.path.join(assets_root, "locations")
    if os.path.isdir(loc_dir):
        loc_bibles = bible_map.get("locations", {})
        for name in sorted(os.listdir(loc_dir)):
            name_dir = os.path.join(loc_dir, name)
            if not os.path.isdir(name_dir):
                continue
            info = loc_bibles.get(name, {'stars': 0, 'stages': {}})

            for sub in sorted(os.listdir(name_dir)):
                sub_dir = os.path.join(name_dir, sub)
                if not os.path.isdir(sub_dir):
                    continue
                chapter = info['stages'].get(sub, '—')
                img_count = count_images(sub_dir)
                rel_path = f"locations/{name}/{sub}/"
                lines.append(f"| {name} | {sub} | {chapter} | {rel_path} | {img_count} |")
                total_images += img_count
                total_assets += 1

    # ---- 道具资产 ----
    lines.append("\n## 道具资产\n")
    lines.append("| 道具名 | stage_id | 章节范围 | 参考图路径 | 图片数 |")
    lines.append("|--------|----------|---------|-----------|--------|")

    prop_dir = os.path.join(assets_root, "props")
    if os.path.isdir(prop_dir):
        prop_bibles = bible_map.get("props", {})
        for name in sorted(os.listdir(prop_dir)):
            name_dir = os.path.join(prop_dir, name)
            if not os.path.isdir(name_dir):
                continue
            info = prop_bibles.get(name, {'stars': 0, 'stages': {}})

            # 检查是否有子目录（有阶段的道具）
            subs = [s for s in os.listdir(name_dir) if os.path.isdir(os.path.join(name_dir, s))]
            if subs:
                for sub in sorted(subs):
                    sub_dir = os.path.join(name_dir, sub)
                    chapter = info['stages'].get(sub, '—')
                    img_count = count_images(sub_dir)
                    rel_path = f"props/{name}/{sub}/"
                    lines.append(f"| {name} | {sub} | {chapter} | {rel_path} | {img_count} |")
                    total_images += img_count
                    total_assets += 1
            else:
                # 无阶段，图片直接在道具名目录下
                img_count = count_images(name_dir)
                rel_path = f"props/{name}/"
                lines.append(f"| {name} | — | — | {rel_path} | {img_count} |")
                total_images += img_count
                total_assets += 1

    # 尾部统计
    lines.append(f"\n---\n")
    lines.append(f"**总资产条目**: {total_assets} | **总图片数**: {total_images}")

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
    print(f"   资产条目: {assets}, 图片: {images}")


if __name__ == '__main__':
    main()
