#!/usr/bin/env python3
"""
renumber_scenes.py — 拆分类型 A 场次后，把所有 SCxxx / SCxxx.N 编号重新映射为连续整数

工作：
1. 按文件中出现顺序读取所有 "### SCxxx" 和 "### SCxxx.N" 标题
2. 建立 老编号 → 新编号 映射（新编号从 SC001 起连续）
3. 全文替换：
   - "### SCxxx" 或 "### SCxxx.N" → "### {new_sc}"
   - 表格行 "| 场次编号 | SCxxx/SCxxx.N |" → "| 场次编号 | {new_sc} |"
4. 重新计算概览（总场次、总时长）
5. 重建章节→场次索引

输出：覆盖原文件 scene_breakdown.md
"""
import os
import re
from pathlib import Path

BASE = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent.parent.parent / 'production'
STEP5 = BASE / 'step5-storyboard'
PATH = STEP5 / 'scene_breakdown.md'


def parse_duration(s: str) -> int:
    s = s.strip()
    m = re.match(r'(\d+):(\d+)', s)
    if m:
        return int(m.group(1)) * 60 + int(m.group(2))
    m = re.match(r'(\d+)\s*分', s)
    if m:
        return int(m.group(1)) * 60
    return 0


def format_duration(sec: int) -> str:
    return f"{sec // 60:02d}:{sec % 60:02d}"


def main():
    content = PATH.read_text(encoding='utf-8')

    # 按文件顺序找所有 "### SCxxx" 或 "### SCxxx.N"
    pattern = re.compile(r'^### (SC\d+(?:\.\d+)?)\s*$', re.MULTILINE)
    matches = list(pattern.finditer(content))

    if not matches:
        print("❌ 未找到场次标题")
        return

    # 映射：老编号 → 新编号
    mapping = {}
    for idx, m in enumerate(matches, 1):
        old = m.group(1)
        new = f'SC{idx:03d}'
        if old not in mapping:
            mapping[old] = new

    # 替换 "### SCxxx.N" → "### {new}"
    def repl_header(m):
        return f'### {mapping[m.group(1)]}'
    content = pattern.sub(repl_header, content)

    # 替换表格行 "| 场次编号 | SCxxx/SCxxx.N |"
    cell_pattern = re.compile(r'(\|\s*场次编号\s*\|\s*)(SC\d+(?:\.\d+)?)(\s*\|)')

    def repl_cell(m):
        old = m.group(2)
        new = mapping.get(old, old)
        return f'{m.group(1)}{new}{m.group(3)}'
    content = cell_pattern.sub(repl_cell, content)

    # 重新切分场次，准备重建概览和索引
    scenes = []
    pattern_new = re.compile(r'^### (SC\d+)\s*$', re.MULTILINE)
    matches_new = list(pattern_new.finditer(content))
    for i, m in enumerate(matches_new):
        start = m.start()
        end = matches_new[i + 1].start() if i + 1 < len(matches_new) else len(content)
        block = content[start:end]

        # 提取章节号
        ch_match = re.search(r'\|\s*对应章节\s*\|([^|]+)\|', block)
        chapter = 0
        if ch_match:
            ch_text = ch_match.group(1)
            cm = re.search(r'ch(\d+)', ch_text)
            if cm:
                chapter = int(cm.group(1))

        # 提取时长
        dur_match = re.search(r'\|\s*预估时长\s*\|([^|]+)\|', block)
        duration_sec = parse_duration(dur_match.group(1)) if dur_match else 0

        scenes.append({
            'sc': m.group(1),
            'chapter': chapter,
            'duration': duration_sec,
        })

    total = len(scenes)
    total_sec = sum(s['duration'] for s in scenes)

    # 重建概览与索引
    # 找到 "## 全片概览" 到 "## 场次明细" 之间的内容，替换
    header_end = content.find('## 场次明细')
    if header_end == -1:
        print("❌ 未找到 '## 场次明细' 锚点")
        return

    # 重建 header
    by_chapter = {}
    for s in scenes:
        by_chapter.setdefault(s['chapter'], []).append(s['sc'])

    header = [
        "# 场次分解表（全片）",
        "",
        "> 本文件由阶段5（场次分解与分镜）产出，是全片的结构骨架。",
        "> 每个场次对应一个连续的时空单元。场次编号 SC{NNN} 是后续镜头编号的前缀。",
        "> 已完成类型 A 转场场次的拆分与全局重新编号。",
        "",
        "## 全片概览",
        "",
        "| 指标 | 值 |",
        "|------|-----|",
        f"| 总场次数 | {total} |",
        f"| 覆盖章节 | ch1-ch71 |",
        f"| 场次编号范围 | SC001-SC{total:03d} |",
        f"| 预估总片长 | {format_duration(total_sec)} |",
        "",
        "## 叙事结构分幕（三幕式参考）",
        "",
        "| 幕 | 章节范围 | 叙事功能 |",
        "|-----|---------|---------|",
        "| 第一幕：开端 | ch1-ch20 | 建立世界（泉水/灵魂体系）、引入朱围庸与宋小仙对立、泊岗镇势力崛起 |",
        "| 第二幕：激化 | ch21-ch55 | 兄弟决裂、泊岗沦陷、清平镇战、天德城陷落、荣康城攻防 |",
        "| 第三幕：终局 | ch56-ch71 | 小顶之死、数字人崛起、神界交涉、威刚显神、美女榕斩根、集体轮回 |",
        "",
        "> 幕与幕之间的具体场次分割点由导演确定。",
        "",
        "## 章节 → 场次索引",
        "",
        "| 章节 | 场次 |",
        "|------|------|",
    ]
    for ch in range(1, 72):
        scs = by_chapter.get(ch, [])
        if scs:
            if len(scs) <= 4:
                sc_str = ', '.join(scs)
            else:
                sc_str = f"{scs[0]}-{scs[-1]}（{len(scs)} 个）"
            header.append(f"| ch{ch} | {sc_str} |")
        else:
            header.append(f"| ch{ch} | — |")
    header.append("")
    header.append("---")
    header.append("")

    new_content = '\n'.join(header) + content[header_end:]
    PATH.write_text(new_content, encoding='utf-8')

    print(f"✅ 全局重编号完成: {PATH}")
    print(f"   总场次数: {total}")
    print(f"   预估总片长: {format_duration(total_sec)}")
    print(f"   SC 编号范围: SC001-SC{total:03d}")

    # 打印小数编号到新编号的部分示例（前 10 个有拆分的）
    decimal_mappings = [(k, v) for k, v in mapping.items() if '.' in k]
    if decimal_mappings:
        print(f"\n   拆分场次映射（共 {len(decimal_mappings)} 个小数编号）前 15 例：")
        for old, new in decimal_mappings[:15]:
            print(f"     {old} → {new}")


if __name__ == '__main__':
    main()
