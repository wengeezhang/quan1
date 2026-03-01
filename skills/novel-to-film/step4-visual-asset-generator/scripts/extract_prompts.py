#!/usr/bin/env python3
"""
extract_prompts.py — 从 Step 3 圣经中批量提取 AI 绘图提示词

功能：
1. 扫描全部角色/场景/道具圣经的 AI 绘图提示词章节
2. 提取中英双语提示词对
3. 校验全局 style prompt 前缀是否存在
4. 按优先级输出结构化提示词清单 (prompts_plan.md)

用法：
    python3 extract_prompts.py [--base-dir /path/to/project]
"""

import os
import re
import argparse
from pathlib import Path

# 导入共享工具函数
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bible_utils import count_stars, extract_stages, BIBLE_DIRS


# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------
DEFAULT_BASE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "production")

ART_DIRECTION = "step2-art-direction/art_direction.md"

# 优先级映射（SKILL.md 定义）
PRIORITY_MAP = {
    "characters": {5: "P0/P1", 4: "P3", 3: "P5", 2: "P5", 1: "P5"},
    "locations":  {5: "P2",    4: "P4", 3: "P5", 2: "P5", 1: "P5"},
    "props":      {5: "P4",    4: "P4", 3: "P5", 2: "P5", 1: "P5"},
}


def _collect_block(lines: list, i: int, stop_patterns: list) -> tuple:
    """
    从第 i 行开始收集内容块（支持 code block 和纯文本），
    遇到 stop_patterns 中的行或 code block 结束时停止。
    返回 (collected_text, new_i)
    """
    collected = []
    in_code = False
    while i < len(lines):
        l = lines[i]
        if l.strip().startswith('```') and not in_code:
            in_code = True
            i += 1
            continue
        if l.strip().startswith('```') and in_code:
            break
        if in_code:
            collected.append(l)
        else:
            # 检查是否遇到终止标记
            should_stop = False
            for pat in stop_patterns:
                if re.match(pat, l):
                    should_stop = True
                    break
            if should_stop:
                i -= 1
                break
            if l.strip():
                collected.append(l)
            elif collected and not l.strip():
                # 空行且已有内容 → 段落结束
                break
        i += 1
    return '\n'.join(collected).strip(), i


def extract_prompt_blocks(text: str) -> list:
    """
    提取所有中英双语提示词对。
    支持多种格式：
      A: **English：** 后换行 + ``` 代码块 ```
      B: **English：** 后换行 + 纯文本
      C: **English：** 同行内联内容
      D: ### English Prompts 章节 + **阶段标题** + code blocks（美女榕格式）
    返回 [{ "title": str, "english": str, "chinese": str, "stage_id": str|None }, ...]
    """
    prompts = []
    lines = text.splitlines()
    i = 0
    current_title = ""
    current_stage = None

    # 终止模式列表
    stop_pats = [
        r'\*\*(中文|English)[：:]',
        r'^###\s',
        r'^##\s',
    ]

    while i < len(lines):
        line = lines[i]

        # ---- 捕获提示词标题行 (### 提示词N：xxx) ----
        if re.match(r'^###\s*提示词', line):
            current_title = line.strip('#').strip()
            for part in re.split(r'[：:—\-]', current_title):
                part = part.strip()
                if part and not re.match(r'^提示词\d*', part):
                    current_stage = part
                    break

        # ---- 格式D: ### English Prompts 章节（美女榕等特殊格式）----
        elif re.match(r'^###\s*English\s+Prompts?', line, re.I):
            i += 1
            while i < len(lines):
                l = lines[i]
                # 遇到中文 Prompts 章节或下一个 ## 标题 → 停止
                if re.match(r'^###\s*(中文|Chinese)\s+Prompts?', l, re.I) or re.match(r'^##\s', l):
                    i -= 1
                    break
                # **阶段标题** 后跟 code block = 一个提示词
                stage_title = re.match(r'^\*\*(.+?)\*\*', l)
                if stage_title:
                    stage_name = stage_title.group(1).strip()
                    # 提取 stage_id：从标题中尝试获取阶段信息
                    sid = None
                    for part in re.split(r'[：:（()）]', stage_name):
                        part = part.strip()
                        if part and not re.match(r'^(基础|通用|阶段)', part):
                            sid = part
                            break
                    i += 1
                    eng_text, i = _collect_block(lines, i, stop_pats + [r'^\*\*'])
                    if eng_text:
                        prompts.append({
                            "title": stage_name,
                            "english": eng_text,
                            "chinese": "",
                            "stage_id": sid or stage_name,
                        })
                i += 1
            # 然后尝试找 ### 中文 Prompts 章节
            i += 1
            if i < len(lines) and re.match(r'^###\s*(中文|Chinese)\s+Prompts?', lines[i], re.I):
                i += 1
                prompt_idx = 0
                while i < len(lines):
                    l = lines[i]
                    if re.match(r'^##\s', l):
                        i -= 1
                        break
                    stage_title = re.match(r'^\*\*(.+?)\*\*', l)
                    if stage_title:
                        i += 1
                        chn_text, i = _collect_block(lines, i, stop_pats + [r'^\*\*'])
                        if chn_text and prompt_idx < len(prompts):
                            prompts[prompt_idx]["chinese"] = chn_text
                        prompt_idx += 1
                    i += 1
            else:
                i -= 1  # 回退

        # ---- 格式A/B/C: **English：** 标签 ----
        else:
            eng_label = re.match(r'\*\*English[：:]\*\*\s*(.*)', line)
            if eng_label:
                eng_lines = []
                inline_content = eng_label.group(1).strip()

                if inline_content:
                    eng_lines.append(inline_content)
                    english = '\n'.join(eng_lines).strip()
                else:
                    i += 1
                    english, i = _collect_block(lines, i, stop_pats)

                # 紧接着找中文块
                chinese = ""
                i += 1
                while i < len(lines):
                    l = lines[i]
                    chn_label = re.match(r'\*\*中文[：:]\*\*\s*(.*)', l)
                    if chn_label:
                        chn_inline = chn_label.group(1).strip()
                        if chn_inline:
                            chinese = chn_inline
                        else:
                            i += 1
                            chinese, i = _collect_block(lines, i, stop_pats)
                        break
                    elif re.match(r'^###\s', l) or re.match(r'^##\s', l) or re.match(r'\*\*English[：:]', l):
                        i -= 1
                        break
                    i += 1

                if english or chinese:
                    prompts.append({
                        "title": current_title,
                        "english": english,
                        "chinese": chinese,
                        "stage_id": current_stage,
                    })

        i += 1

    return prompts


def get_global_prefix(base_dir: str) -> str:
    """读取 art_direction.md 第七章的全局 style prompt 前缀"""
    path = os.path.join(base_dir, ART_DIRECTION)
    if not os.path.exists(path):
        return ""
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    # 找第七章
    m = re.search(r'##\s*七[、.．]\s*(.*?)(?=\n##\s|\Z)', text, re.S)
    if m:
        section = m.group(1)
        # 找代码块中的前缀
        code = re.findall(r'```[^\n]*\n(.*?)```', section, re.S)
        if code:
            return code[0].strip().split('\n')[0].strip()
    # fallback: 找 "Cinematic still" 开头的行
    for line in text.splitlines():
        if 'Cinematic still' in line:
            return line.strip().strip('`').strip('"').strip("'")
    return ""


# ---------------------------------------------------------------------------
# 主逻辑
# ---------------------------------------------------------------------------
def scan_bibles(base_dir: str):
    """扫描所有圣经，提取提示词和元数据"""
    global_prefix = get_global_prefix(base_dir)
    results = []

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
                prompts = extract_prompt_blocks(text)
                priority = PRIORITY_MAP.get(elem_type, {}).get(stars, "P5")

                # 子目录（配角/群像等）
                sub = os.path.relpath(root, bible_dir)
                if sub == '.':
                    sub = ''

                # 校验全局前缀 — 记录提示词是否已内含前缀
                # 注意：前缀可以在 API 调用时动态拼接，不强制要求写在圣经中
                prefix_ok = True
                has_inline_prefix = True
                if global_prefix:
                    for p in prompts:
                        if p['english'] and global_prefix[:20].lower() not in p['english'][:80].lower():
                            has_inline_prefix = False
                            break

                results.append({
                    "type": elem_type,
                    "name": name,
                    "sub_dir": sub,
                    "stars": stars,
                    "priority": priority,
                    "stages": stages,
                    "prompts": prompts,
                    "prompt_count": len(prompts),
                    "has_english": all(p['english'] for p in prompts),
                    "has_chinese": all(p['chinese'] for p in prompts),
                    "prefix_ok": prefix_ok,
                    "has_inline_prefix": has_inline_prefix,
                    "source": fpath,
                })

    return results, global_prefix


def write_plan(results: list, global_prefix: str, output_path: str):
    """输出结构化提示词计划"""
    # 按优先级排序
    priority_order = {"P0/P1": 0, "P2": 1, "P3": 2, "P4": 3, "P5": 4}
    results.sort(key=lambda r: (priority_order.get(r['priority'], 9), -r['stars'], r['name']))

    total_prompts = sum(r['prompt_count'] for r in results)
    missing_eng = [r for r in results if not r['has_english'] and r['prompt_count'] > 0]
    missing_chn = [r for r in results if not r['has_chinese'] and r['prompt_count'] > 0]
    no_prefix = [r for r in results if not r['prefix_ok']]
    no_inline_prefix = [r for r in results if not r.get('has_inline_prefix', True) and r['prompt_count'] > 0]
    no_prompts = [r for r in results if r['prompt_count'] == 0]

    lines = [
        "# 视觉资产生成计划 (Prompt Extraction Report)",
        "",
        f"> 自动生成 by extract_prompts.py",
        f"> 全局 Style Prefix: `{global_prefix[:60]}...`" if global_prefix else "> ⚠️ 未找到全局 Style Prefix",
        f"> 注意：全局前缀可在 Seedream API 调用时动态拼接，不强制要求写在圣经提示词中",
        "",
        "## 统计总览",
        "",
        f"| 指标 | 数值 |",
        f"|------|------|",
        f"| 圣经文件总数 | {len(results)} |",
        f"| 提示词总数 | {total_prompts} |",
        f"| 缺少英文提示词 | {len(missing_eng)} |",
        f"| 缺少中文提示词 | {len(missing_chn)} |",
        f"| 未内含全局前缀（可动态拼接） | {len(no_inline_prefix)} |",
        f"| 无提示词的圣经 | {len(no_prompts)} |",
        "",
    ]

    # 按优先级分组输出
    current_p = None
    for r in results:
        if r['priority'] != current_p:
            current_p = r['priority']
            lines.append(f"---\n")
            lines.append(f"## {current_p} — {'角色肖像+主角阶段图' if current_p == 'P0/P1' else '主要场景' if current_p == 'P2' else '配角阶段图' if current_p == 'P3' else '道具+次要场景' if current_p == 'P4' else '低优先级'}\n")
            lines.append(f"| 元素 | 类型 | ★ | 阶段数 | 提示词数 | EN | CN | 前缀 |")
            lines.append(f"|------|------|---|--------|---------|----|----|------|")

        stages_str = ', '.join(r['stages']) if r['stages'] else '—'
        en = '✅' if r['has_english'] else '❌'
        cn = '✅' if r['has_chinese'] else '❌'
        pf = '✅' if r.get('has_inline_prefix', True) else '➕'
        lines.append(f"| {r['name']} | {r['type']} | {'★' * r['stars']} | {len(r['stages'])} ({stages_str}) | {r['prompt_count']} | {en} | {cn} | {pf} |")

    # 问题清单
    if missing_eng or missing_chn or no_prompts:
        lines.append("\n---\n")
        lines.append("## ⚠️ 待修复问题\n")
        if no_prompts:
            lines.append("### 无提示词的圣经\n")
            for r in no_prompts:
                lines.append(f"- {r['name']} ({r['type']}, {'★' * r['stars']})")
        if missing_eng:
            lines.append("\n### 缺少英文提示词\n")
            for r in missing_eng:
                lines.append(f"- {r['name']} ({r['type']})")
        if missing_chn:
            lines.append("\n### 缺少中文提示词\n")
            for r in missing_chn:
                lines.append(f"- {r['name']} ({r['type']})")

    # 前缀信息（仅参考，前缀可动态拼接）
    if no_inline_prefix:
        lines.append("\n---\n")
        lines.append("## ℹ️ 未内含全局前缀的圣经（API 调用时可动态拼接）\n")
        for r in no_inline_prefix:
            lines.append(f"- {r['name']} ({r['type']})")

    # 完整提示词明细（供 Seedream 直接使用）
    lines.append("\n---\n")
    lines.append("## 完整提示词明细\n")
    for r in results:
        if not r['prompts']:
            continue
        lines.append(f"### {r['name']} ({r['type']}, {'★' * r['stars']}, {r['priority']})\n")
        for idx, p in enumerate(r['prompts'], 1):
            stage_tag = f" [{p['stage_id']}]" if p.get('stage_id') else ""
            lines.append(f"#### {idx}. {p['title']}{stage_tag}\n")
            if p['english']:
                lines.append("**English：**\n```")
                lines.append(p['english'])
                lines.append("```\n")
            if p['chinese']:
                lines.append("**中文：**\n```")
                lines.append(p['chinese'])
                lines.append("```\n")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return total_prompts, len(missing_eng), len(no_prefix), len(no_prompts)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="从 Step 3 圣经中提取 AI 绘图提示词")
    parser.add_argument('--base-dir', default=DEFAULT_BASE, help='production 目录路径')
    parser.add_argument('--output', default=None, help='输出文件路径 (默认: production/step4-assets/prompts_plan.md)')
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    output = args.output or os.path.join(base, "step4-assets", "prompts_plan.md")
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print(f"扫描圣经目录: {base}")
    results, prefix = scan_bibles(base)
    print(f"找到 {len(results)} 个圣经文件")

    total, miss_eng, no_pfx, no_prm = write_plan(results, prefix, output)
    no_inline = sum(1 for r in results if not r.get('has_inline_prefix', True) and r['prompt_count'] > 0)
    print(f"\n✅ 提示词计划已输出: {output}")
    print(f"   总提示词: {total}")
    if miss_eng:
        print(f"   ⚠️ {miss_eng} 个缺少英文提示词")
    if no_prm:
        print(f"   ⚠️ {no_prm} 个圣经无任何提示词")
    if no_inline:
        print(f"   ℹ️ {no_inline} 个未内含全局前缀（可在 API 调用时动态拼接）")


if __name__ == '__main__':
    main()
