#!/usr/bin/env python3
"""
merge_shot_list.py — 合并 7 个批次的 shot_list_batch{N}.md 为全片 shot_list.md

每个批次文件结构：
    # 镜头表 — 批次N（SCXXX-SCXXX）
    > ...
    ## 批次统计
    ...
    ## 场次：SCXXX
    **场次摘要**: ...
    | 镜号 | ... |

合并逻辑：
1. 跳过每个批次文件的头（批次标题 + 批次统计）
2. 按 "## 场次：SCxxx" 切分场次段落
3. 按 SC 号排序，合并后加一个全局头部（统计 + 章节索引）

输出：production/step5-storyboard/shot_list.md
"""
import os
import re
from pathlib import Path

BASE = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent.parent.parent / 'production'
STEP5 = BASE / 'step5-storyboard'

BATCHES = [f'shot_list_batch{i}.md' for i in range(1, 8)]


def parse_duration(s: str) -> int:
    s = s.strip().lower().rstrip('s秒')
    m = re.match(r'(\d+(?:\.\d+)?)', s)
    if m:
        return int(float(m.group(1)))
    return 0


def format_time(sec: int) -> str:
    return f"{sec // 60:02d}:{sec % 60:02d}"


def extract_scene_blocks(content: str) -> list:
    """提取 '## 场次：SCxxx' 起到下一个 '## 场次' 或文件尾的段落"""
    pattern = re.compile(r'^## 场次：(SC\d+)\s*$', re.MULTILINE)
    matches = list(pattern.finditer(content))
    blocks = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        blocks.append((m.group(1), content[start:end].rstrip()))
    return blocks


def count_shots_in_block(block: str) -> int:
    """场次块中以 SCxxx-yyy 开头的表格行数"""
    return len(re.findall(r'\|\s*SC\d+-\d+\s*\|', block))


def sum_duration_in_block(block: str) -> int:
    """场次块中所有镜头时长（秒）累加"""
    # 匹配表格行的第 5 列时长，格式如 "| 10s |" 或 "| 8s |"
    # 更宽松：匹配 "| Xs |" 或 "| X 秒 |" 或 "| Xs 秒 |"
    total = 0
    for line in block.splitlines():
        if not line.startswith('|'):
            continue
        if line.startswith('| 镜号'):
            continue
        if re.match(r'^\|\s*[-:]+\s*\|', line):
            continue
        # 找匹配的 "Xs" 或 "X s"
        cells = [c.strip() for c in line.split('|')]
        for cell in cells:
            m = re.match(r'^(\d+(?:\.\d+)?)\s*s$', cell)
            if m:
                total += int(float(m.group(1)))
                break
    return total


def main():
    all_scenes = {}  # sc -> block
    batch_stats = []

    for batch_fname in BATCHES:
        path = STEP5 / batch_fname
        if not path.exists():
            print(f"⚠️ 缺失: {path}")
            continue
        content = path.read_text(encoding='utf-8')
        blocks = extract_scene_blocks(content)
        total_shots = sum(count_shots_in_block(b) for _, b in blocks)
        total_dur = sum(sum_duration_in_block(b) for _, b in blocks)
        batch_stats.append({
            'file': batch_fname,
            'scenes': len(blocks),
            'shots': total_shots,
            'duration': total_dur,
            'sc_range': f"{blocks[0][0]}-{blocks[-1][0]}" if blocks else '—',
        })
        for sc, block in blocks:
            if sc in all_scenes:
                print(f"⚠️ 重复场次: {sc}（后者覆盖前者）")
            all_scenes[sc] = block

    # 排序
    def sc_num(sc):
        m = re.match(r'SC(\d+)', sc)
        return int(m.group(1)) if m else 0
    sorted_scenes = sorted(all_scenes.items(), key=lambda x: sc_num(x[0]))

    total_scenes = len(sorted_scenes)
    total_shots = sum(count_shots_in_block(b) for _, b in sorted_scenes)
    total_dur = sum(sum_duration_in_block(b) for _, b in sorted_scenes)

    # 生成头部
    lines = [
        "# 镜头表（全片）",
        "",
        "> 本文件由阶段5（场次分解与分镜）产出，是全片的镜头序列设计。",
        "> 每个镜头对应一次 Seedance 2.0 生成调用。",
        "> 镜头中的角色/场景阶段标注（stage_id）用于阶段6通过 asset_index.md 查找参考图。",
        "",
        "## 全片统计",
        "",
        "| 指标 | 值 |",
        "|------|-----|",
        f"| 总场次数 | {total_scenes} |",
        f"| 总镜头数 | {total_shots} |",
        f"| 平均每场次镜头数 | {total_shots / total_scenes:.2f} |",
        f"| 预估总片长 | {format_time(total_dur)} |",
        f"| 单镜头时长铁律 | ≤ 15 秒（Seedance 2.0 物理上限） |",
        "",
        "## 批次生成统计",
        "",
        "| 批次 | SC 范围 | 场次数 | 镜头数 | 累计时长 |",
        "|------|---------|--------|--------|---------|",
    ]
    for bs in batch_stats:
        lines.append(
            f"| {bs['file'].replace('shot_list_', '').replace('.md', '')} | "
            f"{bs['sc_range']} | {bs['scenes']} | {bs['shots']} | {format_time(bs['duration'])} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 镜头明细",
        "",
    ])

    for sc, block in sorted_scenes:
        lines.append(block)
        lines.append("")

    output_path = STEP5 / 'shot_list.md'
    output_path.write_text('\n'.join(lines), encoding='utf-8')

    print(f"✅ shot_list.md 已生成: {output_path}")
    print(f"   总场次数: {total_scenes}")
    print(f"   总镜头数: {total_shots}")
    print(f"   平均每场次镜头数: {total_shots / total_scenes:.2f}")
    print(f"   预估总片长: {format_time(total_dur)}")
    print(f"\n   批次分布:")
    for bs in batch_stats:
        print(f"     {bs['file']}: {bs['scenes']} 场 / {bs['shots']} 镜 [{bs['sc_range']}]")


if __name__ == '__main__':
    main()
