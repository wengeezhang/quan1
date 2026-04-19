#!/usr/bin/env python3
"""
merge_scene_breakdown.py — 合并 7 个批次的 scene_breakdown_batch{N}.md 为单一 scene_breakdown.md

处理逻辑：
1. 读取 7 个批次文件
2. 提取每个批次的场次明细（"### SCxxx" 起，到下一个 "### SCxxx" 或文件尾）
3. 全局重新编号 SC001-SCxxx（跨批次连续）
4. 生成全片概览、分幕结构、章节映射、场次明细

输出：production/step5-storyboard/scene_breakdown.md
"""
import os
import re
from pathlib import Path

BASE = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent.parent.parent / 'production'
STEP5 = BASE / 'step5-storyboard'

BATCHES = [
    ('batch1', 'ch1-ch10'),
    ('batch2', 'ch11-ch20'),
    ('batch3', 'ch21-ch30'),
    ('batch4', 'ch31-ch40'),
    ('batch5', 'ch41-ch50'),
    ('batch6', 'ch51-ch60'),
    ('batch7', 'ch61-ch71'),
]

# 时长解析
def parse_duration(s: str) -> int:
    """解析 'MM:SS' 返回总秒数"""
    s = s.strip()
    m = re.match(r'(\d+):(\d+)', s)
    if m:
        return int(m.group(1)) * 60 + int(m.group(2))
    m = re.match(r'(\d+)\s*[分min]', s)
    if m:
        return int(m.group(1)) * 60
    return 0


def format_duration(sec: int) -> str:
    return f"{sec // 60:02d}:{sec % 60:02d}"


def extract_scenes(content: str) -> list:
    """从批次文件提取所有场次块。

    返回 [(scene_num_local, scene_block_text)]
    scene_num_local: 批次内编号（如 SC001）
    scene_block_text: 从 "### SCxxx" 起到下一个 "### SCxxx" 或 "---\n" 分隔符前
    """
    # 匹配 ### SCxxx 开头
    pattern = re.compile(r'^### (SC\d+)\s*$', re.MULTILINE)
    matches = list(pattern.finditer(content))
    scenes = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        block = content[start:end]
        scenes.append((m.group(1), block))
    return scenes


def renumber_scene_block(block: str, new_sc: str) -> str:
    """将场次块中的 SC 编号替换为新编号。

    替换项：
    - ### SCxxx  → ### {new_sc}
    - | 场次编号 | SCxxx |  → | 场次编号 | {new_sc} |
    """
    block = re.sub(r'^### SC\d+', f'### {new_sc}', block, flags=re.MULTILINE)
    block = re.sub(r'(\| 场次编号 \|)\s*SC\d+\s*(\|)', rf'\1 {new_sc} \2', block)
    return block


def extract_scene_field(block: str, field: str) -> str:
    """从场次块中提取字段值（表格行的右侧单元格）"""
    pattern = rf'\|\s*{re.escape(field)}\s*\|(.+?)\|'
    m = re.search(pattern, block)
    if m:
        return m.group(1).strip()
    return ''


def extract_chapter_from_field(s: str) -> int:
    """从 '对应章节' 字段解析章节号（取第一个数字）"""
    m = re.search(r'ch(\d+)', s)
    return int(m.group(1)) if m else 0


def main():
    # 收集所有场次
    all_scenes = []  # [(old_batch, old_sc, block, chapter_num)]
    batch_stats = []

    for batch_name, ch_range in BATCHES:
        path = STEP5 / f'scene_breakdown_{batch_name}.md'
        if not path.exists():
            print(f"⚠️ 缺失: {path}")
            continue
        content = path.read_text(encoding='utf-8')
        scenes = extract_scenes(content)
        batch_stats.append({
            'batch': batch_name,
            'ch_range': ch_range,
            'count': len(scenes),
            'old_range': f"{scenes[0][0]}-{scenes[-1][0]}" if scenes else '—',
        })
        for old_sc, block in scenes:
            chapter = extract_chapter_from_field(extract_scene_field(block, '对应章节'))
            all_scenes.append((batch_name, old_sc, block, chapter))

    # 重新编号
    total = len(all_scenes)
    renumbered_scenes = []
    for idx, (batch, old_sc, block, chapter) in enumerate(all_scenes, 1):
        new_sc = f'SC{idx:03d}'
        new_block = renumber_scene_block(block, new_sc)
        renumbered_scenes.append({
            'new_sc': new_sc,
            'old_sc': old_sc,
            'old_batch': batch,
            'block': new_block,
            'chapter': chapter,
            'duration': extract_scene_field(new_block, '预估时长'),
            'location': extract_scene_field(new_block, '地点'),
            'time': extract_scene_field(new_block, '时间'),
            'characters': extract_scene_field(new_block, '出场角色'),
            'emotion': extract_scene_field(new_block, '情绪基调'),
            'event': extract_scene_field(new_block, '关联事件'),
            'narrative': extract_scene_field(new_block, '叙事功能'),
        })

    # 统计
    total_seconds = sum(parse_duration(s['duration']) for s in renumbered_scenes)

    # 更新批次对照表：记录旧→新范围
    cumulative = 0
    for i, bs in enumerate(batch_stats):
        bs['new_start'] = cumulative + 1
        cumulative += bs['count']
        bs['new_end'] = cumulative
        bs['new_range'] = f"SC{bs['new_start']:03d}-SC{bs['new_end']:03d}"

    # 生成输出
    lines = [
        "# 场次分解表（全片）",
        "",
        "> 本文件由阶段5（场次分解与分镜）产出，是全片的结构骨架。",
        "> 每个场次对应一个连续的时空单元。场次编号 SC{NNN} 是后续镜头编号的前缀。",
        "> 由 7 个批次合并，场次编号已全局重新编排。",
        "",
        "## 全片概览",
        "",
        "| 指标 | 值 |",
        "|------|-----|",
        f"| 总场次数 | {total} |",
        f"| 覆盖章节 | ch1-ch71 |",
        f"| 场次编号范围 | SC001-SC{total:03d} |",
        f"| 预估总片长 | {format_duration(total_seconds)} |",
        "",
        "## 批次对照表（旧编号 → 新编号）",
        "",
        "| 批次 | 章节范围 | 批次内编号 | 全片编号 | 场次数 |",
        "|------|---------|-----------|---------|--------|",
    ]
    for bs in batch_stats:
        lines.append(
            f"| {bs['batch']} | {bs['ch_range']} | {bs['old_range']} | {bs['new_range']} | {bs['count']} |"
        )

    # 分幕结构（基于叙事节点）
    lines.extend([
        "",
        "## 叙事结构分幕（三幕式参考）",
        "",
        "| 幕 | 场次范围 | 章节范围 | 叙事功能 |",
        "|-----|---------|---------|---------|",
        "| 第一幕：开端 | SC001-?  | ch1-ch20 | 建立世界（泉水/灵魂体系）、引入朱围庸与宋小仙对立、泊岗镇势力崛起 |",
        "| 第二幕：激化 | ?-?      | ch21-ch55 | 兄弟决裂、泊岗沦陷、清平镇战、天德城陷落、荣康城攻防 |",
        "| 第三幕：终局 | ?-SC"+f"{total:03d}" + " | ch56-ch71 | 小顶之死、数字人崛起、神界交涉、威刚显神、美女榕斩根、集体轮回 |",
        "",
        "> 幕与幕之间的具体场次分割点由导演确定。这里按章节范围粗分。",
        "",
    ])

    # 章节 → 场次索引
    lines.extend([
        "## 章节 → 场次索引",
        "",
        "| 章节 | 场次 |",
        "|------|------|",
    ])
    by_chapter = {}
    for s in renumbered_scenes:
        by_chapter.setdefault(s['chapter'], []).append(s['new_sc'])
    for ch in range(1, 72):
        scs = by_chapter.get(ch, [])
        if scs:
            if len(scs) <= 4:
                sc_str = ', '.join(scs)
            else:
                sc_str = f"{scs[0]}-{scs[-1]}（{len(scs)} 个）"
            lines.append(f"| ch{ch} | {sc_str} |")
        else:
            lines.append(f"| ch{ch} | — |")

    lines.extend(["", "---", "", "## 场次明细", ""])

    # 注入所有场次（去掉块内尾部 "---" 避免重复）
    for s in renumbered_scenes:
        block = s['block'].rstrip()
        # 移除末尾的 "---" 行（批次原文带的分隔符）
        block = re.sub(r'\n+---\s*$', '', block)
        lines.append(block)
        lines.append("")
        lines.append("---")
        lines.append("")

    output_path = STEP5 / 'scene_breakdown.md'
    output_path.write_text('\n'.join(lines), encoding='utf-8')

    print(f"✅ scene_breakdown.md 已生成: {output_path}")
    print(f"   总场次数: {total}")
    print(f"   预估总片长: {format_duration(total_seconds)}")
    print(f"   批次分布:")
    for bs in batch_stats:
        print(f"     {bs['batch']} ({bs['ch_range']}): {bs['count']} 场 [{bs['new_range']}]")


if __name__ == '__main__':
    main()
