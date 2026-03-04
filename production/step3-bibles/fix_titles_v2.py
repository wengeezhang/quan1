#!/usr/bin/env python3
"""
fix_titles_v2.py — 将所有 ### 提示词N：... 标题严格规范为两种形式：

  1. ### 提示词N：肖像-{视角}
  2. ### 提示词N：{stage_id}

不允许任何 {stage_id}-描述 或 肖像-{复杂描述} 形式。
"""

import os
import re
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, os.path.join(BASE, '..', 'skills', 'novel-to-film',
                                'step4-visual-asset-generator', 'scripts'))
from bible_utils import extract_stages, BIBLE_DIRS

# ---------------------------------------------------------------------------
# 标准肖像视角名（用于模糊匹配）
# ---------------------------------------------------------------------------
STANDARD_VIEWS = [
    "正面半身像",
    "四分之三侧面半身像",
    "正侧面半身像",
    "全身正面像",
    "背面全身像",
    "眼部特写",
    "角色肖像提示词",
    "群体肖像标准构图",
]

# 视角关键词 → 标准名映射
VIEW_KEYWORDS = [
    (r"群体肖像|群体场景", "群体肖像标准构图"),
    (r"角色肖像", "角色肖像提示词"),
    (r"背面.*全身|全身.*背面", "背面全身像"),
    (r"眼部特写|眼部.*特写", "眼部特写"),
    (r"全身正面|正面.*全身|全身像", "全身正面像"),
    (r"3/4.*侧面|四分之三.*侧面|3/4.*半身|四分之三.*半身", "四分之三侧面半身像"),
    (r"正侧面", "正侧面半身像"),
    (r"正面.*半身|半身.*正面|正面特写|正面.*像|View\s*1|视角一", "正面半身像"),
    (r"侧面.*半身|半身.*侧面|侧面|View\s*2|视角二", "四分之三侧面半身像"),
]


def normalize_portrait_view(raw: str) -> str:
    """将复杂的肖像视角描述归一化为标准视角名。"""
    # 先检查是否已经是标准名
    stripped = raw.strip()
    if stripped in STANDARD_VIEWS:
        return stripped

    # 用关键词匹配
    for pattern, standard_name in VIEW_KEYWORDS:
        if re.search(pattern, stripped):
            return standard_name

    # 如果完全无法匹配，返回 None 表示需要人工处理
    return None


def find_matching_stage(content: str, stages: list) -> str:
    """
    从标题 content 中识别匹配的 stage_id。
    content 可能是 '{stage_id}' 或 '{stage_id}-描述' 或 '{stage_id} - 描述'。
    """
    content = content.strip()

    # 完全匹配
    if content in stages:
        return content

    # 按长度降序匹配前缀（避免 "默认" 误匹配 "默认期"）
    sorted_stages = sorted(stages, key=len, reverse=True)
    for sid in sorted_stages:
        # 精确前缀: "{stage_id}-" 或 "{stage_id} -" 或 "{stage_id} "
        if content.startswith(sid + '-') or content.startswith(sid + ' -') or content.startswith(sid + ' '):
            return sid
        # 直接前缀（无分隔符，适用于如 "默认期场景全景"）
        if content.startswith(sid) and len(content) > len(sid):
            return sid

    # 如果 content 包含 - 或 空格-空格，取第一段尝试
    for sep in [' - ', '-']:
        if sep in content:
            first = content.split(sep, 1)[0].strip()
            if first in stages:
                return first

    return None


def fix_file(fpath: str, elem_type: str) -> list:
    """修复单个文件，返回修改记录列表。"""
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    stages = extract_stages(text)
    lines = text.split('\n')
    changes = []
    new_lines = []

    TITLE_RE = re.compile(r'^(###\s*提示词\s*\d+\s*[：:])\s*(.+)$')

    for i, line in enumerate(lines):
        m = TITLE_RE.match(line)
        if not m:
            new_lines.append(line)
            continue

        prefix = m.group(1)  # e.g. "### 提示词3："
        content = m.group(2).strip()

        # --- 肖像类 ---
        if content.startswith('肖像'):
            # 提取 "肖像-" 后面的部分
            view_raw = content[len('肖像'):].lstrip('-').strip()
            if not view_raw:
                # 纯 "肖像" 无视角 → 保留（罕见）
                new_lines.append(line)
                continue

            # 检查是否已经是标准视角
            if view_raw in STANDARD_VIEWS:
                new_lines.append(line)
                continue

            # 归一化
            std_view = normalize_portrait_view(view_raw)
            if std_view:
                new_title = f"{prefix}肖像-{std_view}"
                if new_title != line:
                    changes.append((i + 1, line.strip(), new_title.strip()))
                    new_lines.append(new_title)
                else:
                    new_lines.append(line)
            else:
                # 无法自动映射 → 标记为需人工处理
                changes.append((i + 1, line.strip(), f"[MANUAL] 无法归一化肖像视角: {view_raw}"))
                new_lines.append(line)
            continue

        # --- 阶段类 ---
        # 检查是否已经是纯 stage_id（无描述后缀）
        if content in stages:
            new_lines.append(line)
            continue

        # 含有描述后缀，需要剥离
        matched_stage = find_matching_stage(content, stages)
        if matched_stage:
            new_title = f"{prefix}{matched_stage}"
            changes.append((i + 1, line.strip(), new_title.strip()))
            new_lines.append(new_title)
        else:
            # 无法匹配任何 stage_id → 标记
            changes.append((i + 1, line.strip(), f"[MANUAL] 无法匹配stage_id: {content}"))
            new_lines.append(line)

    if changes:
        # 只有真正修改了的才写入
        real_changes = [c for c in changes if not c[2].startswith('[MANUAL]')]
        if real_changes:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))

    return changes


def main():
    total_changes = 0
    manual_needed = []

    for elem_type, rel_path in BIBLE_DIRS.items():
        bible_dir = os.path.join(BASE, rel_path)
        if not os.path.isdir(bible_dir):
            continue

        for root, dirs, files in os.walk(bible_dir):
            for fname in sorted(files):
                if not fname.endswith('.md'):
                    continue
                fpath = os.path.join(root, fname)
                changes = fix_file(fpath, elem_type)

                if changes:
                    real = [c for c in changes if not c[2].startswith('[MANUAL]')]
                    manual = [c for c in changes if c[2].startswith('[MANUAL]')]

                    if real:
                        print(f"\n📝 {fname} ({len(real)} 处修改)")
                        for ln, old, new in real:
                            print(f"  L{ln}: {old}")
                            print(f"    → {new}")
                        total_changes += len(real)

                    if manual:
                        for ln, old, msg in manual:
                            manual_needed.append((fname, ln, old, msg))

    print(f"\n{'='*60}")
    print(f"总计修改: {total_changes} 处")

    if manual_needed:
        print(f"\n⚠️ 需要人工处理 ({len(manual_needed)} 处):")
        for fname, ln, old, msg in manual_needed:
            print(f"  {fname} L{ln}: {old}")
            print(f"    → {msg}")


if __name__ == '__main__':
    main()
