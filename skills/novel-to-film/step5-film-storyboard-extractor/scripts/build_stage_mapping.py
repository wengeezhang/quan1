#!/usr/bin/env python3
"""
build_stage_mapping.py — 扫描 step3-bibles/，构建章节→阶段映射表

产出 production/step5-storyboard/stage_mapping_reference.md，供 5b/5c/5d 查询：
    "章节 ch{N} 时，角色 X 处于哪个 stage_id？"

算法：
1. 遍历所有圣经，提取 stage_id → 章节范围 映射
2. 展开章节范围（如 "ch3-ch5" → [3,4,5]；"ch1-71,跳过ch40" 等复杂表达需要人工审视）
3. 反转为 章节 → {元素名: stage_id}
4. 与 asset_index.md 交叉验证（可选）

用法：
    python3 build_stage_mapping.py
"""
import os
import re
import sys
from collections import defaultdict

# 复用 Step 4 的圣经解析逻辑
STEP4_SCRIPTS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'step4-visual-asset-generator', 'scripts'
)
sys.path.insert(0, STEP4_SCRIPTS)
from bible_utils import extract_stage_chapters, BIBLE_DIRS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'production'))
OUT_PATH = os.path.join(BASE, 'step5-storyboard', 'stage_mapping_reference.md')

TOTAL_CHAPTERS = 71


def parse_chapter_range(s: str) -> list:
    """解析章节范围字符串，返回 [int, ...] 章节列表。

    支持格式：
        ch1            → [1]
        ch1-5          → [1,2,3,4,5]
        ch1-ch5        → [1,2,3,4,5]
        ch3-71         → [3,4,...,71]
        ch1-5,ch10-12  → [1,2,3,4,5,10,11,12]
        ch1-71         → [1..71]

    无法解析的复杂表达返回空列表（需人工处理）。
    """
    if not s or s == '—':
        return []
    chapters = set()
    # 匹配所有 chN 或 N 形式的数字
    # 先按逗号/顿号/空格切分
    parts = re.split(r'[,，、;；\s]+', s)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # 匹配 ch3-71 / 3-71 / ch3-ch71 等
        m = re.match(r'^(?:ch|第)?(\d+)\s*[-~到至]\s*(?:ch|第)?(\d+)', part)
        if m:
            start, end = int(m.group(1)), int(m.group(2))
            if start <= end:
                for i in range(start, end + 1):
                    chapters.add(i)
                continue
        # 单章 ch3 / 3
        m = re.match(r'^(?:ch|第)?(\d+)$', part)
        if m:
            chapters.add(int(m.group(1)))
            continue
    return sorted(chapters)


def build_mapping(base_dir: str) -> dict:
    """构建映射：{元素类型: {名称: {stage_id: [章节列表], ...}}}"""
    mapping = {}
    for elem_type, rel_path in BIBLE_DIRS.items():
        bible_dir = os.path.join(base_dir, rel_path)
        if not os.path.isdir(bible_dir):
            continue
        mapping[elem_type] = {}
        for root, _dirs, files in os.walk(bible_dir):
            for fname in sorted(files):
                if not fname.endswith('.md'):
                    continue
                fpath = os.path.join(root, fname)
                with open(fpath, 'r', encoding='utf-8') as f:
                    text = f.read()
                name = fname.replace('.md', '')
                stage_map = extract_stage_chapters(text)
                if not stage_map:
                    continue
                mapping[elem_type][name] = {
                    stage_id: {
                        'raw': chapter_range,
                        'chapters': parse_chapter_range(chapter_range),
                    }
                    for stage_id, chapter_range in stage_map.items()
                }
    return mapping


def invert_to_chapter(mapping: dict) -> dict:
    """反转为 {章节: {元素类型: {名称: stage_id}}}"""
    by_chapter = defaultdict(lambda: defaultdict(dict))
    for elem_type, elems in mapping.items():
        for name, stages in elems.items():
            for stage_id, info in stages.items():
                for ch in info['chapters']:
                    # 若同名元素在某章节有多个 stage_id，按字典序优先保留最后一个
                    # 实际上 step3 圣经中不应出现重叠
                    by_chapter[ch][elem_type][name] = stage_id
    return by_chapter


def generate_md(mapping: dict, by_chapter: dict, output_path: str):
    """生成 stage_mapping_reference.md"""
    lines = [
        "# 章节 → 阶段映射表",
        "",
        "> 本文件由 Step 5 脚本 `build_stage_mapping.py` 自动生成。",
        "> 供场次分解 / 镜头设计 / 分镜脚本查询：章节 ch{N} 时各元素的 stage_id。",
        "",
        "## 概览",
        "",
        f"| 项目 | 数量 |",
        f"|------|------|",
        f"| 角色总数 | {len(mapping.get('characters', {}))} |",
        f"| 场景总数 | {len(mapping.get('locations', {}))} |",
        f"| 道具总数 | {len(mapping.get('props', {}))} |",
        f"| 章节总数 | {TOTAL_CHAPTERS} |",
        "",
        "---",
        "",
        "## 元素 → 阶段注册表（源自圣经）",
        "",
    ]

    # 角色
    lines.append("### 角色阶段注册表\n")
    lines.append("| 角色 | stage_id | 章节范围（原文） | 展开章节数 |")
    lines.append("|------|---------|-----------------|-----------|")
    for name in sorted(mapping.get('characters', {})):
        stages = mapping['characters'][name]
        for stage_id, info in stages.items():
            raw = info['raw'] or '—'
            n_ch = len(info['chapters'])
            lines.append(f"| {name} | {stage_id} | {raw} | {n_ch} |")

    # 场景
    lines.append("\n### 场景阶段注册表\n")
    lines.append("| 场景 | stage_id | 章节范围（原文） | 展开章节数 |")
    lines.append("|------|---------|-----------------|-----------|")
    for name in sorted(mapping.get('locations', {})):
        stages = mapping['locations'][name]
        for stage_id, info in stages.items():
            raw = info['raw'] or '—'
            n_ch = len(info['chapters'])
            lines.append(f"| {name} | {stage_id} | {raw} | {n_ch} |")

    # 道具
    lines.append("\n### 道具阶段注册表\n")
    lines.append("| 道具 | stage_id | 章节范围（原文） | 展开章节数 |")
    lines.append("|------|---------|-----------------|-----------|")
    for name in sorted(mapping.get('props', {})):
        stages = mapping['props'][name]
        for stage_id, info in stages.items():
            raw = info['raw'] or '—'
            n_ch = len(info['chapters'])
            lines.append(f"| {name} | {stage_id} | {raw} | {n_ch} |")

    # 逐章映射
    lines.append("\n---\n")
    lines.append("## 逐章元素阶段速查\n")
    lines.append("> 给定章节，快速查询当前所有出场元素的 stage_id。")
    lines.append('> ⚠️ 只包含"覆盖章节"范围内的元素；未在本章出场的元素不列出。\n')

    for ch in range(1, TOTAL_CHAPTERS + 1):
        lines.append(f"### Ch{ch}\n")
        ch_data = by_chapter.get(ch, {})

        chars = ch_data.get('characters', {})
        if chars:
            lines.append("**角色：**")
            for name in sorted(chars):
                lines.append(f"- {name} → `{chars[name]}`")
            lines.append("")

        locs = ch_data.get('locations', {})
        if locs:
            lines.append("**场景：**")
            for name in sorted(locs):
                lines.append(f"- {name} → `{locs[name]}`")
            lines.append("")

        props = ch_data.get('props', {})
        if props:
            lines.append("**道具：**")
            for name in sorted(props):
                lines.append(f"- {name} → `{props[name]}`")
            lines.append("")

        lines.append("---\n")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def main():
    mapping = build_mapping(BASE)
    by_chapter = invert_to_chapter(mapping)

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    generate_md(mapping, by_chapter, OUT_PATH)

    n_chars = len(mapping.get('characters', {}))
    n_locs = len(mapping.get('locations', {}))
    n_props = len(mapping.get('props', {}))
    total_stages = sum(
        len(stages) for elems in mapping.values() for stages in elems.values()
    )
    print(f"✅ stage_mapping_reference.md 已生成: {OUT_PATH}")
    print(f"   角色 {n_chars} / 场景 {n_locs} / 道具 {n_props}")
    print(f"   总 stage 条目: {total_stages}")

    # 异常检测：章节范围解析为空的项目
    unparseable = []
    for elem_type, elems in mapping.items():
        for name, stages in elems.items():
            for stage_id, info in stages.items():
                if info['raw'] and info['raw'] != '—' and not info['chapters']:
                    unparseable.append((elem_type, name, stage_id, info['raw']))
    if unparseable:
        print(f"\n⚠️ 发现 {len(unparseable)} 条无法解析的章节范围:")
        for t, n, s, r in unparseable:
            print(f"   {t}/{n} [{s}]: {r!r}")


if __name__ == '__main__':
    main()
