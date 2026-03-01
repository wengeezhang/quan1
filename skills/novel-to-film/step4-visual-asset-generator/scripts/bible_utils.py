#!/usr/bin/env python3
"""
bible_utils.py — Step 4 脚本的共享工具函数

提供统一的圣经解析逻辑，避免4个脚本各自维护不同版本的解析器。

所有圣经已统一为标准格式：
  | stage_id | 阶段描述/状态描述 | 章节范围 | 视觉变化摘要/功能状态 |
stage_id 始终位于第一列（列0），不再兼容任何老格式。
"""

import re
import os


# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp'}

BIBLE_DIRS = {
    "characters": "step3-bibles/characters",
    "locations":  "step3-bibles/locations",
    "props":      "step3-bibles/props",
}

# 表头关键词——用于识别并跳过表头行
STAGE_HEADER_WORDS = {
    'stage_id', '阶段描述', '状态描述', '章节范围', '视觉变化摘要', '功能状态',
}


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------
def count_stars(text: str) -> int:
    """从文件内容中提取重要性星级"""
    m = re.search(r'[★⭐]{1,5}', text)
    if m:
        return len(m.group().replace('⭐', '★'))
    m = re.search(r'重要性.*?(\d)\s*[星/]', text)
    if m:
        return int(m.group(1))
    return 0


def has_stage_registry(text: str) -> bool:
    """检查文件是否包含阶段注册表"""
    return '阶段注册表' in text


def _parse_table_cells(line: str) -> list:
    """解析一行 Markdown 表格，返回去空白后的单元格列表"""
    cells = [c.strip() for c in line.split('|')]
    return [c for c in cells if c]


def _is_separator(cells: list) -> bool:
    """判断是否为分隔行 |---|---|"""
    return all(re.match(r'^-+$', c) for c in cells)


def _is_header(cells: list) -> bool:
    """判断是否为表头行（至少一个单元格匹配表头关键词）"""
    return any(c.lower() in STAGE_HEADER_WORDS for c in cells)


def extract_stages(text: str) -> list:
    """
    提取阶段注册表中的 stage_id 列表。

    标准格式: | stage_id | 阶段描述 | 章节范围 | 视觉变化摘要 |
    stage_id 始终位于第0列。
    """
    stages = []
    in_registry = False

    for line in text.splitlines():
        if '阶段注册表' in line:
            in_registry = True
            continue
        if in_registry and line.startswith('## '):
            break
        if in_registry and '|' in line:
            cells = _parse_table_cells(line)
            if not cells:
                continue
            if _is_separator(cells):
                continue
            if _is_header(cells):
                continue

            # 数据行——第0列即为 stage_id
            stage_id = cells[0].strip()
            if stage_id:
                stages.append(stage_id)

    return stages


def extract_stage_chapters(text: str) -> dict:
    """
    提取 stage_id → 章节范围 映射。

    标准格式: | stage_id | 阶段描述 | 章节范围 | 视觉变化摘要 |
    stage_id = 列0, 章节范围 = 列2
    """
    mapping = {}
    in_registry = False
    chapter_col = 2  # 标准格式固定列2

    for line in text.splitlines():
        if '阶段注册表' in line:
            in_registry = True
            continue
        if in_registry and line.startswith('## '):
            break
        if in_registry and '|' in line:
            cells = _parse_table_cells(line)
            if not cells:
                continue
            if _is_separator(cells):
                continue
            if _is_header(cells):
                # 动态确认章节范围列位置（以防 prop 表列顺序略有不同）
                for idx, c in enumerate(cells):
                    if c in ('章节范围',):
                        chapter_col = idx
                        break
                continue

            # 数据行
            stage_id = cells[0].strip()
            if stage_id:
                chapter = '—'
                if chapter_col < len(cells):
                    chapter = cells[chapter_col].strip()
                mapping[stage_id] = chapter

    return mapping


def count_images(directory: str) -> int:
    """统计目录中的图片文件数"""
    if not os.path.isdir(directory):
        return 0
    return sum(1 for f in os.listdir(directory)
               if os.path.splitext(f)[1].lower() in IMAGE_EXTS)
