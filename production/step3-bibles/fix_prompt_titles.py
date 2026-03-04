#!/usr/bin/env python3
"""
fix_prompt_titles.py — 自动修复所有圣经文件中的 AI 提示词标题
统一为：### 提示词N：{stage_id} 或 ### 提示词N：{stage_id}-描述
角色肖像：### 提示词N：肖像-{视角}
"""

import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                                'skills', 'novel-to-film', 'step4-visual-asset-generator', 'scripts'))
from bible_utils import extract_stages, BIBLE_DIRS

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')  # production/

PROMPT_SECTION_RE = re.compile(r'^##\s.*AI绘图提示词')

# 已标准的格式
STANDARD_RE = re.compile(r'^###\s*提示词\s*(\d+)\s*[：:]\s*(.+)$')

# 非提示词辅助标题关键词
NON_PROMPT_KEYWORDS = [
    '使用指南', '全局设置', '全局前缀', '全局风格', '通用注意事项', '注意事项',
    '绘图注意事项', '技术说明', '核心美术指向', '标准参数调整参考表', '负面提示词',
    '提示词关键要素', '提示词组合说明', '提示词模板', '快速参考', '镜头场景组合',
    '场景特殊效果提示词', '场景演变关键时刻', '关键事件补充', '7.1', '7.2', '7.3',
]


def is_non_prompt_header(text):
    stripped = text.lstrip('#').strip().rstrip('：:')
    for kw in NON_PROMPT_KEYWORDS:
        if stripped.startswith(kw):
            return True
    return False


def strip_english(text):
    """移除 ' | English...' 双语后缀"""
    if ' | ' in text:
        return text.split(' | ')[0].strip()
    return text


def strip_chapter_ref(text):
    """移除 （chN-chM） 或 （第N章xxx） 后缀"""
    return re.sub(r'\s*[（(](?:ch|第)\d+[^)）]*[)）]\s*$', '', text).strip()


def match_stage_id(text, stages):
    """将文本匹配到注册表中的 stage_id"""
    if not stages:
        return text
    if text in stages:
        return text
    # "默认期" vs "默认"
    for sid in stages:
        if text == sid + '期' or text + '期' == sid:
            return sid
    # 包含匹配
    for sid in stages:
        if sid in text:
            return sid
    for sid in stages:
        if text in sid:
            return sid
    return text


def get_default_stage(stages):
    if not stages:
        return '默认'
    if '默认' in stages:
        return '默认'
    return stages[0]


def normalize_prop_desc(stage_desc, stages):
    """
    规范道具/场景提示词的 stage_id-desc 部分。
    "默认期-概念设计" → "默认-概念设计"（如果注册表是"默认"）
    """
    stage_desc = strip_english(stage_desc)
    if '-' in stage_desc:
        stage_id, desc = stage_desc.split('-', 1)
        stage_id = stage_id.strip()
        desc = strip_english(desc.strip())
        if stages:
            stage_id = match_stage_id(stage_id, stages)
        return f'{stage_id}-{desc}'
    else:
        if stages:
            return match_stage_id(stage_desc.strip(), stages)
        return stage_desc.strip()


def has_sub_headings(lines, start, end):
    """检查 start 之后、下一个 ### 之前是否有 #### 子标题"""
    for i in range(start + 1, end):
        line = lines[i].rstrip('\n')
        if re.match(r'^###\s', line):
            break
        if re.match(r'^####\s', line):
            return True
    return False


def convert_sub_heading(line, stages, elem_type, is_portrait_section):
    """
    将 #### 子标题转换为标准提示词描述部分。
    返回 (type, content)：
      type: 'portrait' → 肖像-{视角}
      type: 'stage' → {stage_id}
      type: 'scene' → {stage_id}-{desc}
    """
    stripped = line.lstrip('#').strip()

    # #### 视图N：{视角} 或 #### 视角 N：{视角}
    m = re.match(r'视[图角]\s*\d*[：:]\s*(.+)$', stripped)
    if m:
        return 'portrait', f'肖像-{m.group(1).strip()}'

    # #### 肖像：{视角}
    m = re.match(r'肖像[：:]\s*(.+)$', stripped)
    if m:
        return 'portrait', f'肖像-{m.group(1).strip()}'

    # #### 场景：{desc}
    m = re.match(r'场景[：:]\s*(.+)$', stripped)
    if m:
        desc = strip_chapter_ref(m.group(1).strip())
        desc = strip_english(desc)
        stage_id = get_default_stage(stages)
        return 'scene', f'{stage_id}-{desc}'

    # #### {stage_id}（chN-chM）- Ch9B 格式
    m = re.match(r'(.+?)(?:\s*[（(]ch[^)）]*[)）])?\s*$', stripped)
    if m:
        stage_text = m.group(1).strip()
        stage_text = strip_chapter_ref(stage_text)
        if is_portrait_section:
            return 'portrait', f'肖像-{stage_text}'
        matched = match_stage_id(stage_text, stages)
        if matched in (stages or []):
            return 'stage', matched
        # 可能是描述性标题
        stage_id = get_default_stage(stages)
        return 'scene', f'{stage_id}-{stage_text}'

    return 'unknown', stripped


def fix_file(fpath, elem_type, dry_run=False):
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    name = os.path.basename(fpath).replace('.md', '')
    text = ''.join(lines)
    stages = extract_stages(text)

    changes = []

    # 找 AI 提示词章节范围
    section_start = None
    section_end = len(lines)
    for i, line in enumerate(lines):
        if PROMPT_SECTION_RE.match(line):
            section_start = i
        elif section_start is not None and re.match(r'^##\s[^#]', line) and not PROMPT_SECTION_RE.match(line):
            section_end = i
            break

    if section_start is None:
        return 0, []

    new_lines = list(lines)
    prompt_counter = 0
    i = section_start + 1

    while i < section_end:
        line = new_lines[i]
        stripped = line.rstrip('\n')

        # === 非提示词辅助标题 ===
        if re.match(r'^#{3,4}\s', stripped) and is_non_prompt_header(stripped):
            # 检查是否有 #### 子标题（如美女榕的 7.1/7.2/7.3 或恶灵区的关键事件）
            if has_sub_headings(new_lines, i, section_end):
                # 有子标题 → 删除标题，转换子标题
                old = stripped
                changes.append((i + 1, old, '[删除]'))
                new_lines[i] = '\n'
                j = i + 1
                while j < section_end:
                    sub = new_lines[j].rstrip('\n')
                    if re.match(r'^###\s', sub):
                        break
                    if re.match(r'^####\s', sub):
                        prompt_counter += 1
                        sub_content = sub.lstrip('#').strip()
                        # #### 提示词N：xxx → 直接规范化
                        sub_std = re.match(r'提示词\s*\d+[：:]\s*(.+)$', sub_content)
                        if sub_std:
                            desc = normalize_prop_desc(sub_std.group(1).strip(), stages)
                            new_sub = f'### 提示词{prompt_counter}：{desc}\n'
                        else:
                            sub_desc = strip_chapter_ref(strip_english(sub_content))
                            stage_id = get_default_stage(stages)
                            new_sub = f'### 提示词{prompt_counter}：{stage_id}-{sub_desc}\n'
                        changes.append((j + 1, sub, new_sub.rstrip('\n')))
                        new_lines[j] = new_sub
                    j += 1
                i = j
                continue
            else:
                old = stripped
                content = stripped.lstrip('#').strip().rstrip('：:')
                new_lines[i] = f'**{content}**\n'
                changes.append((i + 1, old, f'**{content}**'))
                i += 1
                continue

        # === Ch9A/Ch9B 角色格式 ===
        if re.match(r'^###\s+Ch9[AB]\s', stripped):
            is_ch9a = 'Ch9A' in stripped or '定妆照' in stripped
            changes.append((i + 1, stripped, '[删除]'))
            new_lines[i] = '\n'
            j = i + 1
            while j < section_end:
                sub = new_lines[j].rstrip('\n')
                if re.match(r'^###\s', sub):
                    break
                if re.match(r'^####\s', sub):
                    prompt_counter += 1
                    _, content = convert_sub_heading(sub, stages, elem_type, is_ch9a)
                    new_title = f'### 提示词{prompt_counter}：{content}\n'
                    changes.append((j + 1, sub, new_title.rstrip('\n')))
                    new_lines[j] = new_title
                j += 1
            i = j
            continue

        # === A./B./C./D. 面板标题 ===
        panel_m = re.match(r'^###\s+([A-Z])[.．、]\s*(.*)$', stripped)
        if panel_m:
            panel_desc = panel_m.group(2).strip()
            has_children = has_sub_headings(new_lines, i, section_end)

            if has_children:
                # 面板标题有 #### 子标题 → 删除面板标题，转换子标题
                is_portrait = any(kw in panel_desc for kw in ['肖像', '视角', '视图', '定妆', '半身像'])
                changes.append((i + 1, stripped, '[删除]'))
                new_lines[i] = '\n'
                j = i + 1
                while j < section_end:
                    sub = new_lines[j].rstrip('\n')
                    if re.match(r'^###\s', sub):
                        break
                    if re.match(r'^####\s', sub):
                        prompt_counter += 1
                        _, content = convert_sub_heading(sub, stages, elem_type, is_portrait)
                        new_title = f'### 提示词{prompt_counter}：{content}\n'
                        changes.append((j + 1, sub, new_title.rstrip('\n')))
                        new_lines[j] = new_title
                    j += 1
                i = j
                continue
            else:
                # 面板标题本身就是提示词 → 转换
                prompt_counter += 1
                desc = panel_desc
                desc = strip_english(desc)
                # 判断是肖像还是场景
                if any(kw in desc for kw in ['半身像', '全身', '正面像', '肖像', '定妆', '视图']):
                    # 提取纯视角部分
                    desc = re.sub(r'[（(].*[)）]', '', desc).strip()
                    new_title = f'### 提示词{prompt_counter}：肖像-{desc}\n'
                else:
                    stage_id = get_default_stage(stages)
                    # 清理 "场景：" 前缀
                    desc = re.sub(r'^场景[：:]\s*', '', desc)
                    desc = re.sub(r'^场景插画.*?：\s*', '', desc)
                    desc = strip_chapter_ref(desc)
                    if desc:
                        new_title = f'### 提示词{prompt_counter}：{stage_id}-{desc}\n'
                    else:
                        new_title = f'### 提示词{prompt_counter}：{stage_id}\n'
                changes.append((i + 1, stripped, new_title.rstrip('\n')))
                new_lines[i] = new_title
                i += 1
                continue

        # === ### A - xxx 格式（无点号） ===
        panel_dash_m = re.match(r'^###\s+[A-Z]\s*[-–—]\s*(.+)$', stripped)
        if panel_dash_m:
            prompt_counter += 1
            desc = panel_dash_m.group(1).strip()
            desc = strip_english(desc)
            if any(kw in desc for kw in ['半身像', '全身', '正面像', '肖像']):
                new_title = f'### 提示词{prompt_counter}：肖像-{desc}\n'
            else:
                stage_id = get_default_stage(stages)
                desc = re.sub(r'^场景[：:]\s*', '', desc)
                desc = strip_chapter_ref(desc)
                new_title = f'### 提示词{prompt_counter}：{stage_id}-{desc}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === ### B1. 场景：xxx 格式 ===
        b1_m = re.match(r'^###\s+[A-Z]\d+[.．]\s*(.+)$', stripped)
        if b1_m:
            prompt_counter += 1
            desc = b1_m.group(1).strip()
            desc = strip_english(desc)
            stage_id = get_default_stage(stages)
            # 清理 "场景：" 前缀
            desc = re.sub(r'^场景[：:]\s*', '', desc)
            desc = strip_chapter_ref(desc)
            new_title = f'### 提示词{prompt_counter}：{stage_id}-{desc}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === 已标准的提示词 ===
        std_m = STANDARD_RE.match(stripped)
        if std_m:
            prompt_counter += 1
            old_num = int(std_m.group(1))
            stage_part = std_m.group(2).strip()
            stage_part = strip_english(stage_part)

            # 从带括号的描述中提取正确的 stage_id
            # 例如："泉水源头（宁静期）" → stage_id=宁静期, desc=泉水源头
            paren_m = re.match(r'^(.+?)\s*[（(](.+?)[)）]\s*$', stage_part)
            if paren_m and stages:
                desc_part = paren_m.group(1).strip()
                paren_content = paren_m.group(2).strip()
                # 检查括号内容是否为 stage_id
                matched_paren = match_stage_id(paren_content, stages)
                if matched_paren in stages:
                    stage_part = f'{matched_paren}-{desc_part}'

            # 检查和修正 stage_id
            if '-' in stage_part:
                sid = stage_part.split('-', 1)[0].strip()
                desc = stage_part.split('-', 1)[1].strip()
                if sid != '肖像' and stages:
                    matched = match_stage_id(sid, stages)
                    if matched != sid:
                        stage_part = f'{matched}-{desc}'
            else:
                if stage_part != '肖像' and stages:
                    matched = match_stage_id(stage_part, stages)
                    if matched != stage_part and matched in stages:
                        # 保留原始文本作为描述（如 "阶段一：默认状态（平静）" → "默认-阶段一：默认状态（平静）"）
                        # 但如果原文本就是 stage_id 的简单变体（如 "默认期" vs "默认"），直接替换
                        if stage_part == matched + '期' or stage_part + '期' == matched:
                            stage_part = matched
                        elif stage_part not in stages:
                            stage_part = f'{matched}-{stage_part}'
                        else:
                            stage_part = matched

            new_title = f'### 提示词{prompt_counter}：{stage_part}\n'
            if new_title != line:
                changes.append((i + 1, stripped, new_title.rstrip('\n')))
                new_lines[i] = new_title
            i += 1
            continue

        # === ### 肖像：xxx ===
        pm = re.match(r'^###\s*肖像[：:]\s*(.+)$', stripped)
        if pm:
            prompt_counter += 1
            view = pm.group(1).strip()
            # "阶段名 - 视角" → "视角（阶段名）"
            if ' - ' in view:
                parts = view.split(' - ', 1)
                view = f'{parts[1].strip()}（{parts[0].strip()}）'
            new_title = f'### 提示词{prompt_counter}：肖像-{view}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === ### 肖像 A1：xxx ===
        pm2 = re.match(r'^###\s*肖像\s*[A-Z]\d*[：:]\s*(.+)$', stripped)
        if pm2:
            prompt_counter += 1
            desc = pm2.group(1).strip()
            if ' - ' in desc:
                parts = desc.rsplit(' - ', 1)
                view = f'{parts[1].strip()}（{parts[0].strip()}）'
            else:
                view = desc
            new_title = f'### 提示词{prompt_counter}：肖像-{view}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === ### 阶段：{stage_id} ===
        sm = re.match(r'^###\s*阶段[：:]\s*(.+?)(?:\s*[（(].*[)）])?\s*$', stripped)
        if sm:
            prompt_counter += 1
            stage_text = sm.group(1).strip()
            matched = match_stage_id(stage_text, stages)
            new_title = f'### 提示词{prompt_counter}：{matched}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === ### 阶段N：xxx场景（chN—chM） ===
        sm = re.match(r'^###\s*阶段[一二三四五六七八九十\d]+[：:]\s*(.+?)(?:场景)?\s*(?:[（(].*[)）])?\s*$', stripped)
        if sm:
            prompt_counter += 1
            stage_text = sm.group(1).strip()
            matched = match_stage_id(stage_text, stages)
            new_title = f'### 提示词{prompt_counter}：{matched}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === ### 场景 B：xxx（角色格式） ===
        sm = re.match(r'^###\s*场景\s*[A-Z][：:]\s*(.+)$', stripped)
        if sm:
            prompt_counter += 1
            desc = strip_english(strip_chapter_ref(sm.group(1).strip()))
            # 从描述猜 stage_id
            stage_id = get_default_stage(stages)
            if stages:
                for sid in stages:
                    if sid in desc:
                        stage_id = sid
                        break
            new_title = f'### 提示词{prompt_counter}：{stage_id}-{desc}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === ### 场景：xxx（杨伯礼格式） ===
        sm = re.match(r'^###\s*场景[：:]\s*(.+)$', stripped)
        if sm:
            prompt_counter += 1
            desc = strip_chapter_ref(sm.group(1).strip())
            desc = strip_english(desc)
            stage_id = get_default_stage(stages)
            if stages:
                for sid in stages:
                    if sid in desc:
                        stage_id = sid
                        break
            new_title = f'### 提示词{prompt_counter}：{stage_id}-{desc}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === ### Prompt Set N - xxx ===
        sm = re.match(r'^###\s*Prompt\s+Set\s+\d+\s*[-–—]\s*(.+)$', stripped)
        if sm:
            prompt_counter += 1
            desc = strip_english(sm.group(1).strip())
            stage_id = get_default_stage(stages)
            new_title = f'### 提示词{prompt_counter}：{stage_id}-{desc}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === ### 提示词 N - xxx（空格+横线） ===
        sm = re.match(r'^###\s*提示词\s+\d+\s*[-–—]\s*(.+)$', stripped)
        if sm:
            prompt_counter += 1
            desc = strip_english(sm.group(1).strip())
            stage_id = get_default_stage(stages)
            new_title = f'### 提示词{prompt_counter}：{stage_id}-{desc}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === ### S0N_{stage_id}提示词 ===
        sm = re.match(r'^###\s*S\d+_(.+?)提示词\s*$', stripped)
        if sm:
            stage_text = sm.group(1).strip()
            matched = match_stage_id(stage_text, stages)
            # 不为 S0N 标题本身创建提示词编号，只转换其 #### 子标题
            # 将 S0N 标题改为加粗的阶段说明
            changes.append((i + 1, stripped, f'**{matched}阶段**'))
            new_lines[i] = f'**{matched}阶段**\n'
            j = i + 1
            while j < section_end:
                sub = new_lines[j].rstrip('\n')
                if re.match(r'^###\s', sub):
                    break
                if re.match(r'^####\s', sub):
                    prompt_counter += 1
                    sub_desc = sub.lstrip('#').strip()
                    sub_desc = strip_chapter_ref(sub_desc)
                    sub_desc = strip_english(sub_desc)
                    new_sub = f'### 提示词{prompt_counter}：{matched}-{sub_desc}\n'
                    changes.append((j + 1, sub, new_sub.rstrip('\n')))
                    new_lines[j] = new_sub
                j += 1
            i = j
            continue

        # === ### 场景N：xxx（场景/道具） ===
        sm = re.match(r'^###\s*场景[一二三四五六七八九十\d]+[：:]\s*(.+)$', stripped)
        if sm:
            prompt_counter += 1
            desc = sm.group(1).strip()
            desc = strip_english(desc)
            # 检查是否已包含 stage_id-desc 格式
            if '-' in desc:
                desc = normalize_prop_desc(desc, stages)
                new_title = f'### 提示词{prompt_counter}：{desc}\n'
            else:
                stage_id = get_default_stage(stages)
                desc = strip_chapter_ref(desc)
                new_title = f'### 提示词{prompt_counter}：{stage_id}-{desc}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === 道具：### 提示词组N/A：xxx ===
        sm = re.match(r'^###\s*提示词组[A-Z0-9]+[：:]\s*(.+)$', stripped)
        if sm:
            prompt_counter += 1
            desc = normalize_prop_desc(sm.group(1).strip(), stages)
            new_title = f'### 提示词{prompt_counter}：{desc}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === 道具：### 提示N：xxx（缺"词"字） ===
        sm = re.match(r'^###\s*提示[一二三四五六七八九十]+[：:]\s*(.+)$', stripped)
        if sm:
            prompt_counter += 1
            desc = normalize_prop_desc(sm.group(1).strip(), stages)
            new_title = f'### 提示词{prompt_counter}：{desc}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === 道具：### **默认期-xxx ===
        sm = re.match(r'^###\s*\*\*(.+?)(?:\*\*)?\s*$', stripped)
        if sm:
            prompt_counter += 1
            desc = normalize_prop_desc(sm.group(1).strip(), stages)
            new_title = f'### 提示词{prompt_counter}：{desc}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        # === 裸标题匹配（### {stage_id} 或 ### {stage_id}场景组） ===
        if re.match(r'^###\s', stripped):
            bare = stripped.lstrip('#').strip()
            # 跳过 #### 级别（不应在此处理）
            if stripped.startswith('####'):
                i += 1
                continue

            # 尝试匹配注册表
            clean = re.sub(r'(场景组|场景)\s*$', '', bare).strip()
            if stages and clean:
                matched = match_stage_id(clean, stages)
                if matched in stages:
                    prompt_counter += 1
                    new_title = f'### 提示词{prompt_counter}：{matched}\n'
                    changes.append((i + 1, stripped, new_title.rstrip('\n')))
                    new_lines[i] = new_title
                    i += 1
                    continue

            # 其他裸标题 → 作为描述
            prompt_counter += 1
            stage_id = get_default_stage(stages)
            desc = strip_chapter_ref(strip_english(bare))
            new_title = f'### 提示词{prompt_counter}：{stage_id}-{desc}\n'
            changes.append((i + 1, stripped, new_title.rstrip('\n')))
            new_lines[i] = new_title
            i += 1
            continue

        i += 1

    if changes and not dry_run:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

    return len(changes), changes


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--file', help='只处理指定文件名（部分匹配）')
    args = parser.parse_args()

    total_changes = 0
    total_files = 0

    for elem_type, rel_path in BIBLE_DIRS.items():
        bible_dir = os.path.join(BASE, rel_path)
        if not os.path.isdir(bible_dir):
            continue
        for root, dirs, files in os.walk(bible_dir):
            for fname in sorted(files):
                if not fname.endswith('.md'):
                    continue
                if args.file and args.file not in fname:
                    continue
                fpath = os.path.join(root, fname)
                count, details = fix_file(fpath, elem_type, dry_run=args.dry_run)
                if count > 0:
                    total_files += 1
                    total_changes += count
                    print(f"\n{'='*60}")
                    print(f"📝 {fname} ({count} changes)")
                    print(f"{'='*60}")
                    for lineno, old, new in details:
                        print(f"  L{lineno}: {old}")
                        print(f"      → {new}")

    print(f"\n{'='*60}")
    print(f"总计: {total_files} 文件, {total_changes} 处变更")
    if args.dry_run:
        print("（dry-run 模式，未实际修改文件）")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
