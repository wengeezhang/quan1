#!/usr/bin/env python3
"""
fix_stage_id_fields.py — 修复 scene_breakdown.md 中类型 B/C 的 stage_id 字段

问题模式：
    | 地点 | 永安镇小顶家（stage_id：永安镇） |  ← 场景名被写成了 stage_id 值

正确形式：
    | 地点 | 永安镇小顶家（stage_id：默认） |   ← stage_id 应为映射表里的阶段值

处理逻辑：
1. 从 step3-bibles 构建 {场景名: {stage_id: [章节列表]}} 映射
2. 逐场次扫描"地点"字段，定位 stage_id 被写成场景名的条目
3. 根据场次章节号选择正确的 stage_id：
   - 单阶段场景（如永安镇=默认）：直接替换为唯一 stage_id
   - 多阶段场景（如天德城=繁华期/沦陷期）：根据章节号选择对应阶段
4. 原地更新 scene_breakdown.md
"""
import os
import re
import sys
from pathlib import Path

HERE = Path(os.path.dirname(os.path.abspath(__file__)))
STEP4_SCRIPTS = HERE.parent.parent / 'step4-visual-asset-generator' / 'scripts'
sys.path.insert(0, str(STEP4_SCRIPTS))
from bible_utils import extract_stage_chapters, BIBLE_DIRS

BASE = HERE.parent.parent.parent.parent / 'production'
STEP5 = BASE / 'step5-storyboard'
PATH = STEP5 / 'scene_breakdown.md'


def parse_chapter_range(s: str) -> set:
    """解析章节范围，返回 int 集合"""
    chapters = set()
    if not s or s == '—':
        return chapters
    parts = re.split(r'[,，、;；\s]+', s)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        m = re.match(r'^(?:ch|第)?(\d+)\s*[-~到至]\s*(?:ch|第)?(\d+)', part)
        if m:
            start, end = int(m.group(1)), int(m.group(2))
            if start <= end:
                for i in range(start, end + 1):
                    chapters.add(i)
                continue
        m = re.match(r'^(?:ch|第)?(\d+)$', part)
        if m:
            chapters.add(int(m.group(1)))
    return chapters


def build_location_map(base_dir: Path) -> dict:
    """构建 {场景名: {stage_id: {chapter_set}}}"""
    result = {}
    loc_dir = base_dir / 'step3-bibles' / 'locations'
    if not loc_dir.exists():
        return result
    for fname in os.listdir(loc_dir):
        if not fname.endswith('.md'):
            continue
        fpath = loc_dir / fname
        text = fpath.read_text(encoding='utf-8')
        name = fname.replace('.md', '')
        stage_map = extract_stage_chapters(text)
        if not stage_map:
            continue
        result[name] = {
            stage_id: parse_chapter_range(chapter_range)
            for stage_id, chapter_range in stage_map.items()
        }
    return result


def resolve_stage_id(loc_name: str, chapter: int, location_map: dict) -> str:
    """给定场景名+章节，返回正确的 stage_id；无法确定返回空字符串"""
    if loc_name not in location_map:
        return ''
    stages = location_map[loc_name]
    if len(stages) == 1:
        # 单阶段：直接返回
        return list(stages.keys())[0]
    # 多阶段：按章节号选
    for stage_id, chapter_set in stages.items():
        if chapter in chapter_set:
            return stage_id
    # 章节超出注册表范围：fallback 到最早/最晚的阶段
    # 取最接近的：先找小于等于当前章节的最大章节所属阶段
    best = None
    best_ch = -1
    for stage_id, chapter_set in stages.items():
        if not chapter_set:
            continue
        max_ch = max(chapter_set)
        if max_ch <= chapter and max_ch > best_ch:
            best_ch = max_ch
            best = stage_id
    if best:
        return best
    # 否则取最早阶段
    for stage_id, chapter_set in stages.items():
        if chapter_set:
            return stage_id
    return ''


def main():
    location_map = build_location_map(BASE)
    print(f"场景注册表已载入：{len(location_map)} 个场景")

    content = PATH.read_text(encoding='utf-8')

    # 按场次切分
    scene_pattern = re.compile(r'^### (SC\d+)\s*$', re.MULTILINE)
    matches = list(scene_pattern.finditer(content))

    # stage_id 字段模式：（stage_id：{某个值}）其中值不是已知 stage_id
    # 已知的有效 stage_id（非场景名类）
    VALID_STAGE_IDS = {
        '默认', '默认期', '繁华期', '沦陷期', '陷落期', '围城期',
        '灵魂期', '乞丐前期', '乞丐后期', '老农期', '乞丐期',
        '未激活', '激活后', '—',
    }

    fixes = []
    replacements = []  # (old_text, new_text)

    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        block = content[start:end]
        sc = m.group(1)

        # 提取章节号
        ch_match = re.search(r'\|\s*对应章节\s*\|([^|]+)\|', block)
        chapter = 0
        if ch_match:
            cm = re.search(r'ch(\d+)', ch_match.group(1))
            if cm:
                chapter = int(cm.group(1))

        # 在"地点"字段中找 stage_id 被写成场景名的情况
        # 匹配 stage_id：{value} 其中 value 是一个场景名
        # 两种格式：（stage_id：xxx）  和  `xxx`  形式
        def repl_paren(mm):
            value = mm.group(1).strip()
            original_value = value
            if value in VALID_STAGE_IDS:
                return mm.group(0)
            if value in location_map:
                correct = resolve_stage_id(value, chapter, location_map)
                if correct:
                    fixes.append((sc, original_value, correct, chapter))
                    return f'（stage_id：{correct}）'
            # 模式 1: "场景名 `阶段值`[——/；后备注]" → 阶段值
            # 如：'皇宫 `默认`——国都街巷'、'AA大学 `默认`'、'天德城 `沦陷期`'
            m = re.match(r'^([^\s`]+)\s+`([^`]+)`', value)
            if m:
                scene_name, stage_val = m.group(1), m.group(2)
                # 验证场景名在映射表且阶段值合理
                if scene_name in location_map:
                    if stage_val in location_map[scene_name] or stage_val in VALID_STAGE_IDS:
                        fixes.append((sc, original_value, stage_val, chapter))
                        return f'（stage_id：{stage_val}）'
            # 模式 2: "—，任何备注" → —
            if value.startswith('—'):
                fixes.append((sc, original_value, '—', chapter))
                return f'（stage_id：—）'
            # 模式 3: "恶灵区 `默认` 相邻通道；按同一超自然场景" 已被模式 1 覆盖
            return mm.group(0)

        new_block = re.sub(r'（stage_id：([^）]+)）', repl_paren, block)

        # 也处理 ` ` 反引号格式里的场景名：`场景名` (stage_id 值位置)
        # 典型格式：{场景名}（stage_id：`场景名`） 或 {场景名}（stage_id：场景名 `默认期`）
        # 较少见，先不处理

        if new_block != block:
            replacements.append((block, new_block))

    # 应用替换
    for old, new in replacements:
        content = content.replace(old, new, 1)

    PATH.write_text(content, encoding='utf-8')

    print(f"\n✅ 修复完成：{len(fixes)} 处 stage_id 字段")
    # 分组统计：按修复前值
    by_value = {}
    for sc, old, new, ch in fixes:
        key = f"{old} → {new}"
        by_value.setdefault(key, []).append((sc, ch))
    for key in sorted(by_value):
        print(f"  {key}: {len(by_value[key])} 处")

    # 检查还有哪些 stage_id 字段未知
    print("\n—— 剩余未知 stage_id 值（需人工审视）：")
    unknown = set()
    for m in re.finditer(r'（stage_id：([^）]+)）', content):
        value = m.group(1).strip()
        if value in VALID_STAGE_IDS:
            continue
        if value in location_map:
            continue
        unknown.add(value)
    for v in sorted(unknown):
        print(f"  {v!r}")


if __name__ == '__main__':
    main()
