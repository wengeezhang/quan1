#!/usr/bin/env python3
"""
validate_prompt_titles.py — 校验所有圣经 AI 提示词标题是否符合统一标准

标准格式（三类元素统一）：
  ### 提示词N：{stage_id}
  ### 提示词N：{stage_id}-描述

角色肖像使用 "肖像" 作为 stage_id：
  ### 提示词1：肖像-正面半身像

不允许的格式：
  ### 阶段：xxx / ### 肖像：xxx / ### 场景N：xxx / ### Prompt Set N
  ### 繁华期 / ### S01_xxx / ### Ch9A xxx / ### A. xxx / 其他裸标题

额外校验：
  - 提示词中的 stage_id 必须与阶段注册表匹配（"肖像" 除外）
  - 编号必须从 1 开始连续递增
  - 每个 stage_id 至少出现一次

用法：
    python3 validate_prompt_titles.py [--base-dir /path/to/production]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bible_utils import extract_stages, BIBLE_DIRS

DEFAULT_BASE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "production")

# 标准格式正则：### 提示词N：{stage_id} 或 ### 提示词N：{stage_id}-描述
# N 可以是数字，stage_id 不能为空
TITLE_RE = re.compile(r'^###\s*提示词\s*(\d+)\s*[：:]\s*(.+)$')

# 用于识别 AI 提示词章节的二级标题
PROMPT_SECTION_RE = re.compile(r'^##\s.*AI绘图提示词')

# 用于识别 A/B 板块子标题（角色圣经），这些不是提示词标题，允许存在
PANEL_RE = re.compile(r'^####?\s*[A-Z][.．、]\s')


def extract_prompt_titles(text: str) -> list:
    """
    从圣经文本中提取 AI 提示词章节内的所有 ### 标题。
    返回 [(line_number, line_text), ...]
    """
    lines = text.splitlines()
    in_section = False
    titles = []

    for i, line in enumerate(lines, 1):
        if PROMPT_SECTION_RE.match(line):
            in_section = True
            continue
        # 遇到下一个 ## 标题且不是 AI 提示词 → 离开
        if in_section and re.match(r'^##\s[^#]', line) and not PROMPT_SECTION_RE.match(line):
            in_section = False
            continue
        if in_section and re.match(r'^###\s', line):
            titles.append((i, line))

    return titles


def validate_file(fpath: str, elem_type: str) -> list:
    """
    校验单个圣经文件的提示词标题。
    返回错误列表 [(severity, message), ...]
      severity: "ERROR" | "WARN"
    """
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    name = os.path.basename(fpath).replace('.md', '')
    errors = []

    # 提取阶段注册表
    stages = extract_stages(text)

    # 提取提示词标题
    titles = extract_prompt_titles(text)

    if not titles:
        # 有些圣经可能确实没有提示词章节（罕见）
        errors.append(("WARN", f"{name}: 未找到任何 ### 提示词标题"))
        return errors

    # 校验每个标题
    seen_numbers = []
    seen_stage_ids = set()

    for lineno, line in titles:
        m = TITLE_RE.match(line.strip())
        if not m:
            # 检查是否是允许的非提示词标题（如 #### A. 角色肖像提示词）
            if PANEL_RE.match(line.strip()):
                continue
            # 不合规标题
            errors.append(("ERROR", f"{name} L{lineno}: 非标准标题 → {line.strip()}"))
            continue

        num = int(m.group(1))
        stage_part = m.group(2).strip()

        # 提取 stage_id（取 - 之前的部分）
        stage_id = stage_part.split('-')[0].strip() if '-' in stage_part else stage_part.strip()

        seen_numbers.append(num)
        seen_stage_ids.add(stage_id)

        # 校验 stage_id 与注册表匹配
        if stage_id == '肖像':
            # 角色肖像，合法
            if elem_type != 'characters':
                errors.append(("WARN", f"{name} L{lineno}: 非角色元素使用了 '肖像' stage_id"))
        elif stages and stage_id not in stages:
            errors.append(("ERROR", f"{name} L{lineno}: stage_id '{stage_id}' 不在注册表中 {stages}"))

    # 校验编号连续性
    if seen_numbers:
        expected = list(range(1, len(seen_numbers) + 1))
        if seen_numbers != expected:
            errors.append(("WARN", f"{name}: 编号不连续 — 实际 {seen_numbers}，期望 {expected}"))

    # 校验注册表覆盖率（每个 stage_id 至少出现一次）
    if stages:
        for sid in stages:
            if sid not in seen_stage_ids:
                errors.append(("WARN", f"{name}: 注册表 stage_id '{sid}' 在提示词标题中未出现（内容缺失）"))

    return errors


def main():
    import argparse
    parser = argparse.ArgumentParser(description="校验所有圣经 AI 提示词标题是否符合统一标准")
    parser.add_argument('--base-dir', default=DEFAULT_BASE, help='production 目录路径')
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    total_files = 0
    total_errors = 0
    total_warns = 0
    all_issues = []

    for elem_type, rel_path in BIBLE_DIRS.items():
        bible_dir = os.path.join(base, rel_path)
        if not os.path.isdir(bible_dir):
            continue

        for root, dirs, files in os.walk(bible_dir):
            for fname in sorted(files):
                if not fname.endswith('.md'):
                    continue
                fpath = os.path.join(root, fname)
                total_files += 1
                issues = validate_file(fpath, elem_type)
                if issues:
                    all_issues.extend(issues)
                    for sev, msg in issues:
                        if sev == "ERROR":
                            total_errors += 1
                        else:
                            total_warns += 1

    # 输出报告
    print(f"\n{'='*70}")
    print(f"提示词标题校验报告")
    print(f"{'='*70}")
    print(f"扫描文件: {total_files}")
    print(f"错误 (ERROR): {total_errors}")
    print(f"警告 (WARN):  {total_warns}")
    print(f"{'='*70}\n")

    if all_issues:
        current_sev = None
        error_items = [x for x in all_issues if x[0] == "ERROR"]
        warn_items = [x for x in all_issues if x[0] == "WARN"]

        if error_items:
            print("--- ERROR ---\n")
            for _, msg in error_items:
                print(f"  ❌ {msg}")
            print()

        if warn_items:
            print("--- WARN ---\n")
            for _, msg in warn_items:
                print(f"  ⚠️  {msg}")
            print()
    else:
        print("✅ 所有文件的提示词标题均符合标准！\n")

    # 返回 exit code
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == '__main__':
    main()
