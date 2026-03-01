#!/usr/bin/env python3
"""
validate_assets.py — 校验 Step 4 资产库的完整性和一致性

功能：
1. 目录 vs 圣经：每个圣经的 stage_id 是否都有对应资产目录
2. 资产 vs 索引：asset_index.md 中的路径是否都真实存在
3. 图片覆盖率：每个 stage_id 目录是否至少有 1 张图片
4. 角色肖像完整性：★★★★★/★★★★☆ 角色是否有完整肖像集

用法：
    python3 validate_assets.py [--base-dir /path/to/production]
"""

import os
import re
import argparse
from pathlib import Path

# 导入共享工具函数
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bible_utils import count_stars, extract_stages, has_stage_registry, count_images, BIBLE_DIRS, IMAGE_EXTS


DEFAULT_BASE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "production")

PORTRAIT_EXPECTED = {
    5: 6,  # 正面半身 + 3/4侧面 + 正侧面 + 全身正面 + 背面全身 + 眼部特写
    4: 4,  # 正面半身 + 3/4侧面 + 正侧面 + 全身正面
}


class ValidationReport:
    def __init__(self):
        self.errors = []    # 必须修复
        self.warnings = []  # 建议修复
        self.info = []      # 信息

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def ok(self, msg):
        self.info.append(msg)

    def print_report(self):
        print("\n" + "=" * 60)
        print("  Step 4 资产校验报告")
        print("=" * 60)

        if self.errors:
            print(f"\n❌ 错误 ({len(self.errors)})")
            for e in self.errors:
                print(f"  ✗ {e}")

        if self.warnings:
            print(f"\n⚠️  警告 ({len(self.warnings)})")
            for w in self.warnings:
                print(f"  △ {w}")

        print(f"\nℹ️  信息 ({len(self.info)})")
        for i in self.info:
            print(f"  · {i}")

        print("\n" + "-" * 60)
        if not self.errors and not self.warnings:
            print("✅ 全部通过！资产库状态良好。")
        elif not self.errors:
            print(f"⚠️ 无错误，{len(self.warnings)} 个警告。")
        else:
            print(f"❌ {len(self.errors)} 个错误，{len(self.warnings)} 个警告需要处理。")

        return len(self.errors) == 0


def validate(base_dir: str) -> bool:
    report = ValidationReport()
    assets_root = os.path.join(base_dir, "step4-assets")

    # ---- 检查 1: 资产根目录是否存在 ----
    if not os.path.isdir(assets_root):
        report.error("step4-assets/ 目录不存在 → 先运行 scaffold_assets.py")
        report.print_report()
        return False

    # ---- 检查 2: 圣经 stage_id vs 资产目录 ----
    total_expected = 0
    total_found = 0
    empty_dirs = 0

    for elem_type, rel_path in BIBLE_DIRS.items():
        bible_dir = os.path.join(base_dir, rel_path)
        if not os.path.isdir(bible_dir):
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
                    # 检查 _portrait/
                    portrait_dir = os.path.join(assets_root, "characters", name, "_portrait")
                    total_expected += 1
                    if os.path.isdir(portrait_dir):
                        total_found += 1
                        img_n = count_images(portrait_dir)
                        if img_n == 0:
                            empty_dirs += 1
                        # 肖像完整性
                        expected = PORTRAIT_EXPECTED.get(stars, 0)
                        if expected > 0 and img_n < expected:
                            report.warn(f"角色 {name} (★{'★'*stars}) 肖像不完整: {img_n}/{expected}")
                        elif img_n >= expected and expected > 0:
                            report.ok(f"角色 {name} 肖像完整 ({img_n}/{expected})")
                    else:
                        report.error(f"缺少目录: characters/{name}/_portrait/")

                    # 检查 stage_id 目录
                    for sid in (stages or ['默认']):
                        total_expected += 1
                        sid_dir = os.path.join(assets_root, "characters", name, sid)
                        if os.path.isdir(sid_dir):
                            total_found += 1
                            if count_images(sid_dir) == 0:
                                empty_dirs += 1
                        else:
                            report.error(f"缺少目录: characters/{name}/{sid}/")

                elif elem_type == "locations":
                    for sid in (stages or ['默认']):
                        total_expected += 1
                        sid_dir = os.path.join(assets_root, "locations", name, sid)
                        if os.path.isdir(sid_dir):
                            total_found += 1
                            if count_images(sid_dir) == 0:
                                empty_dirs += 1
                        else:
                            report.error(f"缺少目录: locations/{name}/{sid}/")

                elif elem_type == "props":
                    if has_reg and stages:
                        for sid in stages:
                            total_expected += 1
                            sid_dir = os.path.join(assets_root, "props", name, sid)
                            if os.path.isdir(sid_dir):
                                total_found += 1
                                if count_images(sid_dir) == 0:
                                    empty_dirs += 1
                            else:
                                report.error(f"缺少目录: props/{name}/{sid}/")
                    else:
                        total_expected += 1
                        prop_dir = os.path.join(assets_root, "props", name)
                        if os.path.isdir(prop_dir):
                            total_found += 1
                            if count_images(prop_dir) == 0:
                                empty_dirs += 1
                        else:
                            report.error(f"缺少目录: props/{name}/")

    report.ok(f"目录覆盖率: {total_found}/{total_expected}")
    if empty_dirs > 0:
        report.warn(f"{empty_dirs} 个目录为空（尚无图片）")

    # ---- 检查 3: asset_index.md 存在性和路径验证 ----
    index_path = os.path.join(assets_root, "asset_index.md")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_text = f.read()

        # 提取所有路径
        paths_in_index = re.findall(r'(?:characters|locations|props)/[^\s|]+/', index_text)
        valid_paths = 0
        invalid_paths = 0
        for p in paths_in_index:
            full = os.path.join(assets_root, p)
            if os.path.isdir(full):
                valid_paths += 1
            else:
                invalid_paths += 1
                report.error(f"asset_index.md 引用了不存在的路径: {p}")

        report.ok(f"asset_index.md 路径检查: {valid_paths} 有效, {invalid_paths} 无效")
    else:
        report.warn("asset_index.md 不存在 → 运行 build_index.py 生成")

    # ---- 检查 4: 资产目录中有无"野"目录（不在圣经中） ----
    for elem_type in ["characters", "locations", "props"]:
        type_dir = os.path.join(assets_root, elem_type)
        if not os.path.isdir(type_dir):
            continue
        bible_dir = os.path.join(base_dir, BIBLE_DIRS[elem_type])
        bible_names = set()
        if os.path.isdir(bible_dir):
            for r, d, fs in os.walk(bible_dir):
                for fn in fs:
                    if fn.endswith('.md'):
                        bible_names.add(fn.replace('.md', ''))

        for item in os.listdir(type_dir):
            if os.path.isdir(os.path.join(type_dir, item)) and item not in bible_names:
                report.warn(f"资产目录 {elem_type}/{item}/ 无对应圣经文件")

    return report.print_report()


def main():
    parser = argparse.ArgumentParser(description="校验 Step 4 资产库完整性")
    parser.add_argument('--base-dir', default=DEFAULT_BASE, help='production 目录路径')
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    success = validate(base)
    exit(0 if success else 1)


if __name__ == '__main__':
    main()
