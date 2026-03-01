#!/usr/bin/env python3
"""
scaffold_assets.py — 根据 Step 3 圣经的 stage_id 预建 Step 4 资产目录树

功能：
1. 读取所有角色/场景/道具圣经的阶段注册表
2. 创建 production/step4-assets/ 下的完整目录结构
3. 角色: {角色名}/_portrait/ + {角色名}/{stage_id}/
4. 场景: {场景名}/{stage_id}/
5. 道具: {道具名}/{stage_id}/ (有阶段) 或 {道具名}/ (无阶段)

用法：
    python3 scaffold_assets.py [--base-dir /path/to/production] [--dry-run]
"""

import os
import re
import argparse
from pathlib import Path

# 导入共享工具函数
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bible_utils import count_stars, extract_stages, has_stage_registry, BIBLE_DIRS


DEFAULT_BASE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "production")

PORTRAIT_VIEWS = {
    5: ["正面半身像", "四分之三侧面半身像", "正侧面半身像", "全身正面像", "背面全身像", "眼部特写"],
    4: ["正面半身像", "四分之三侧面半身像", "正侧面半身像", "全身正面像"],
    3: ["正面半身像", "全身正面像"],
}


def scaffold(base_dir: str, dry_run: bool = False):
    """构建目录树"""
    assets_root = os.path.join(base_dir, "step4-assets")
    created = []

    for elem_type, rel_path in BIBLE_DIRS.items():
        bible_dir = os.path.join(base_dir, rel_path)
        if not os.path.isdir(bible_dir):
            print(f"⚠️ 圣经目录不存在: {bible_dir}")
            continue

        for root, dirs, files in os.walk(bible_dir):
            for fname in sorted(files):
                if not fname.endswith('.md'):
                    continue
                fpath = os.path.join(root, fname)
                with open(fpath, 'r', encoding='utf-8') as f:
                    text = f.read()

                name = fname.replace('.md', '')
                stars = count_stars(text)
                stages = extract_stages(text)
                has_reg = has_stage_registry(text)

                if elem_type == "characters":
                    # 角色: _portrait/ + stage_id 目录
                    portrait_dir = os.path.join(assets_root, "characters", name, "_portrait")
                    created.append(portrait_dir)

                    if stages:
                        for sid in stages:
                            d = os.path.join(assets_root, "characters", name, sid)
                            created.append(d)
                    else:
                        # 无阶段的角色也建一个默认目录
                        d = os.path.join(assets_root, "characters", name, "默认")
                        created.append(d)

                elif elem_type == "locations":
                    if stages:
                        for sid in stages:
                            d = os.path.join(assets_root, "locations", name, sid)
                            created.append(d)
                    else:
                        d = os.path.join(assets_root, "locations", name, "默认")
                        created.append(d)

                elif elem_type == "props":
                    if has_reg and stages:
                        for sid in stages:
                            d = os.path.join(assets_root, "props", name, sid)
                            created.append(d)
                    else:
                        # 无阶段的道具直接放道具名目录下
                        d = os.path.join(assets_root, "props", name)
                        created.append(d)

    # 创建目录
    for d in created:
        if dry_run:
            print(f"  [DRY-RUN] mkdir -p {d}")
        else:
            os.makedirs(d, exist_ok=True)

    return created


def print_tree(assets_root: str, max_depth: int = 3):
    """打印目录树概览"""
    if not os.path.isdir(assets_root):
        return
    for elem_type in ["characters", "locations", "props"]:
        type_dir = os.path.join(assets_root, elem_type)
        if not os.path.isdir(type_dir):
            continue
        print(f"\n{elem_type}/")
        items = sorted(os.listdir(type_dir))
        for item in items:
            item_path = os.path.join(type_dir, item)
            if os.path.isdir(item_path):
                subs = sorted(os.listdir(item_path))
                sub_str = ', '.join(subs) if subs else '(empty)'
                print(f"  ├── {item}/ → [{sub_str}]")


def main():
    parser = argparse.ArgumentParser(description="预建 Step 4 资产目录结构")
    parser.add_argument('--base-dir', default=DEFAULT_BASE, help='production 目录路径')
    parser.add_argument('--dry-run', action='store_true', help='仅显示将创建的目录，不实际创建')
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    print(f"基于圣经构建资产目录: {base}")

    dirs = scaffold(base, dry_run=args.dry_run)

    print(f"\n✅ {'将创建' if args.dry_run else '已创建'} {len(dirs)} 个目录")

    if not args.dry_run:
        print("\n目录树概览:")
        print_tree(os.path.join(base, "step4-assets"))


if __name__ == '__main__':
    main()
