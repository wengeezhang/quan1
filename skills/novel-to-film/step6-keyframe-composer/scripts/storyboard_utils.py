#!/usr/bin/env python3
"""
storyboard_utils.py — Step 6 脚本的共享工具函数

提供分镜脚本解析、连续性链识别、镜头分类等通用逻辑。

核心数据结构：
  Shot = {
      "shot_id":        "SC001-001",
      "scene_id":       "SC001",
      "chapter":        "ch1",
      "scale":          "全景",            # 景别
      "angle":          "正面偏高（俯瞰15度）",
      "camera_move":    "固定",            # 运镜
      "duration":       "10s",
      "visual_desc":    "...",            # 画面描述全文
      "foreground":     "...",            # 前景描述
      "midground":      "...",            # 中景描述
      "background":     "...",            # 背景描述
      "motion_desc":    "...",            # 动态描述全文
      "frozen_moment":  "...",            # 冻结时刻（第 0 秒状态）
      "dialogue":       "...",            # 对白
      "elements":       [...],            # 元素标注列表
      "continuity": {
          "prev":       "SC001-000" | None,
          "next":       "SC001-002" | None,
          "ref_hint":   "...",            # 参考图使用建议
      },
  }
"""

import os
import re
from typing import Optional


# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------
DEFAULT_BASE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "production")

# 景别中英映射
SCALE_MAP = {
    "大远景": "extreme wide shot",
    "远景":   "wide shot",
    "全景":   "full shot",
    "中景":   "medium shot",
    "中近景": "medium close-up",
    "近景":   "close-up",
    "特写":   "close-up",
    "大特写": "extreme close-up",
}

# 机位角度中英映射
ANGLE_MAP = {
    "平视":   "eye-level angle",
    "俯视":   "high angle",
    "仰视":   "low angle",
    "鸟瞰":   "bird's eye view",
    "荷兰角": "dutch angle",
    "过肩":   "over-the-shoulder shot",
}

# 参考图权重表（按景别）
# {scale_cn: (portrait_weight, stage_weight, scene_weight)}
REF_WEIGHT_TABLE = {
    "大特写": (0.65, 0.75, 0.25),
    "特写":   (0.65, 0.75, 0.25),
    "近景":   (0.55, 0.65, 0.35),
    "中近景": (0.55, 0.65, 0.35),
    "中景":   (0.45, 0.55, 0.45),
    "全景":   (0.35, 0.45, 0.55),
    "远景":   (0.25, 0.25, 0.65),
    "大远景": (0.25, 0.25, 0.65),
}

# 全局负面提示词
GLOBAL_NEGATIVE = (
    "modern elements, anachronistic objects, bright neon colors, "
    "anime style, cartoon, watermark, text overlay, blurry, low quality, "
    "distorted faces, extra limbs, deformed hands"
)


# ---------------------------------------------------------------------------
# 场景级解析
# ---------------------------------------------------------------------------
def parse_scene_header(text: str) -> dict:
    """解析场次头部信息表"""
    info = {
        "scene_id": "",
        "chapter": "",
        "location": "",
        "location_stage": "",
        "time": "",
        "mood_arc": "",
        "shot_count": 0,
        "est_duration": "",
    }
    # 提取场次编号
    m = re.search(r'场次编号\s*\|\s*(SC\d+)', text)
    if m:
        info["scene_id"] = m.group(1)
    # 章节
    m = re.search(r'对应章节\s*\|\s*(ch\d+)', text)
    if m:
        info["chapter"] = m.group(1)
    # 地点 + stage_id
    m = re.search(r'地点\s*\|\s*(.+?)(?:\（|（|\()', text)
    if m:
        info["location"] = m.group(1).strip()
    m = re.search(r'stage_id[：:]\s*(.+?)\s*[）\)）]', text)
    if m:
        info["location_stage"] = m.group(1).strip()
    elif re.search(r'地点\s*\|\s*(.+)', text):
        # 没有 stage_id 标注时
        loc_line = re.search(r'地点\s*\|\s*(.+)', text).group(1).strip()
        info["location"] = loc_line
    # 时间
    m = re.search(r'时间\s*\|\s*(.+)', text)
    if m:
        info["time"] = m.group(1).strip()
    # 镜头数
    m = re.search(r'镜头数\s*\|\s*(\d+)', text)
    if m:
        info["shot_count"] = int(m.group(1))
    # 预估时长
    m = re.search(r'预估时长\s*\|\s*(.+)', text)
    if m:
        info["est_duration"] = m.group(1).strip()
    # 情绪弧线
    m = re.search(r'情绪弧线\s*\|\s*(.+)', text)
    if m:
        info["mood_arc"] = m.group(1).strip()
    return info


def parse_element_table(text: str) -> list:
    """
    解析元素标注表格。
    返回: [{"type": "角色", "name": "老吴", "stage_id": "山居重生期", "ref_path": "..."}, ...]
    """
    elements = []
    lines = text.strip().splitlines()
    in_table = False
    for line in lines:
        if '|' not in line:
            if in_table:
                break
            continue
        cells = [c.strip() for c in line.split('|')]
        cells = [c for c in cells if c]
        if not cells:
            continue
        # 跳过表头和分隔符
        if any(c in ('类型', '元素', 'stage_id', '参考图来源') for c in cells):
            in_table = True
            continue
        if all(re.match(r'^-+$', c) for c in cells):
            continue
        if len(cells) >= 3:
            in_table = True
            elem = {
                "type": cells[0],
                "name": cells[1],
                "stage_id": cells[2] if cells[2] != '—' else None,
                "ref_hint": cells[3] if len(cells) > 3 else "",
            }
            elements.append(elem)
    return elements


# ---------------------------------------------------------------------------
# 镜头级解析
# ---------------------------------------------------------------------------
def parse_shot(shot_text: str, scene_id: str) -> dict:
    """
    解析单个镜头的完整描述块。
    shot_text: 从 "### 镜头 SCXXX-YYY" 到下一个 "### 镜头" 之间的文本。
    """
    shot = {
        "shot_id": "",
        "scene_id": scene_id,
        "chapter": "",
        "scale": "",
        "angle": "",
        "camera_move": "",
        "duration": "",
        "event": "",
        "elements": [],
        "visual_desc": "",
        "foreground": "",
        "midground": "",
        "background": "",
        "motion_desc": "",
        "frozen_moment": "",
        "dialogue": "",
        "continuity": {
            "prev": None,
            "next": None,
            "ref_hint": "",
        },
    }

    # 镜号
    m = re.search(r'镜号\s*\|\s*(SC\d+-\d+)', shot_text)
    if m:
        shot["shot_id"] = m.group(1)
    # 章节
    m = re.search(r'章节\s*\|\s*(ch\d+)', shot_text)
    if m:
        shot["chapter"] = m.group(1)
    # 景别
    m = re.search(r'景别\s*\|\s*(.+)', shot_text)
    if m:
        shot["scale"] = m.group(1).strip()
    # 机位
    m = re.search(r'机位\s*\|\s*(.+)', shot_text)
    if m:
        shot["angle"] = m.group(1).strip()
    # 运镜
    m = re.search(r'运镜\s*\|\s*(.+)', shot_text)
    if m:
        shot["camera_move"] = m.group(1).strip()
    # 时长
    m = re.search(r'时长\s*\|\s*(.+)', shot_text)
    if m:
        shot["duration"] = m.group(1).strip()
    # 关联事件
    m = re.search(r'关联事件\s*\|\s*(.+)', shot_text)
    if m:
        shot["event"] = m.group(1).strip()

    # ---- 元素标注 ----
    elem_m = re.search(r'\*\*元素标注\*\*(.*?)(?=\*\*画面描述\*\*|\*\*动态描述\*\*|$)', shot_text, re.S)
    if elem_m:
        shot["elements"] = parse_element_table(elem_m.group(1))

    # ---- 画面描述 ----
    visual_m = re.search(r'\*\*画面描述\*\*(.*?)(?=\*\*动态描述\*\*|$)', shot_text, re.S)
    if visual_m:
        desc = visual_m.group(1).strip()
        shot["visual_desc"] = desc
        # 分层提取
        fg = re.search(r'\*\*前景\*\*[：:]\s*(.*?)(?=\*\*中景\*\*|\*\*背景\*\*|$)', desc, re.S)
        mg = re.search(r'\*\*中景\*\*[：:]\s*(.*?)(?=\*\*背景\*\*|$)', desc, re.S)
        bg = re.search(r'\*\*背景\*\*[：:]\s*(.*?)$', desc, re.S)
        if fg:
            shot["foreground"] = fg.group(1).strip()
        if mg:
            shot["midground"] = mg.group(1).strip()
        if bg:
            shot["background"] = bg.group(1).strip()

    # ---- 动态描述 ----
    motion_m = re.search(r'\*\*动态描述\*\*(.*?)(?=\*\*对白\*\*|\*\*音效提示\*\*|\*\*衔接说明\*\*|$)', shot_text, re.S)
    if motion_m:
        motion_text = motion_m.group(1).strip()
        shot["motion_desc"] = motion_text
        # 提取冻结时刻（第 0 秒状态 = 第一段动态）
        # 格式通常是 "1. 0-Xs：..."
        first_m = re.search(r'1\.\s*0-\d+s[：:]\s*(.*?)(?=\n\d+\.|$)', motion_text, re.S)
        if first_m:
            shot["frozen_moment"] = first_m.group(1).strip()
        else:
            # 有时只有一段动态描述
            shot["frozen_moment"] = re.sub(r'^\d+\.\s*', '', motion_text.split('\n')[0]).strip()

    # ---- 对白 ----
    dial_m = re.search(r'\*\*对白\*\*(.*?)(?=\*\*音效提示\*\*|\*\*衔接说明\*\*|$)', shot_text, re.S)
    if dial_m:
        shot["dialogue"] = dial_m.group(1).strip()

    # ---- 首帧合成提示 / 连续性需求 ----
    hint_m = re.search(r'\*\*首帧合成提示\*\*.*?连续性需求[：:](.*?)(?=- 参考图使用建议|$)', shot_text, re.S)
    if hint_m:
        cont_text = hint_m.group(1)
        prev_m = re.search(r'前接[：:]\s*(SC\d+-\d+)', cont_text)
        next_m = re.search(r'后接[：:]\s*(SC\d+-\d+)', cont_text)
        if prev_m:
            shot["continuity"]["prev"] = prev_m.group(1)
        if next_m:
            shot["continuity"]["next"] = next_m.group(1)

    # 参考图使用建议
    ref_m = re.search(r'参考图使用建议[：:]\s*(.*?)(?=\n---|\n###|\Z)', shot_text, re.S)
    if ref_m:
        shot["continuity"]["ref_hint"] = ref_m.group(1).strip()

    return shot


def parse_storyboard_file(filepath: str) -> dict:
    """
    解析一个完整的分镜脚本文件。
    返回: {
        "scene": {场次头部信息},
        "shots": [Shot, Shot, ...],
    }
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 提取场次头部
    scene_info = parse_scene_header(text)
    scene_id = scene_info["scene_id"]

    # 按 "### 镜头" 分割
    shot_sections = re.split(r'(?=### 镜头\s+SC\d+-\d+)', text)
    shots = []
    for section in shot_sections:
        if not re.match(r'### 镜头\s+SC\d+-\d+', section):
            continue
        shot = parse_shot(section, scene_id)
        if shot["shot_id"]:
            shots.append(shot)

    return {
        "scene": scene_info,
        "shots": shots,
    }


def load_all_storyboards(base_dir: str = None) -> list:
    """
    加载全部分镜脚本，返回所有 Shot 的有序列表。
    """
    if base_dir is None:
        base_dir = DEFAULT_BASE
    sb_dir = os.path.join(base_dir, "step5-storyboard", "storyboard")
    if not os.path.isdir(sb_dir):
        raise FileNotFoundError(f"分镜脚本目录不存在: {sb_dir}")

    all_shots = []
    scene_infos = []
    for fname in sorted(os.listdir(sb_dir)):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(sb_dir, fname)
        result = parse_storyboard_file(fpath)
        scene_infos.append(result["scene"])
        all_shots.extend(result["shots"])

    return all_shots, scene_infos


# ---------------------------------------------------------------------------
# 参考图查找
# ---------------------------------------------------------------------------
def load_asset_index(base_dir: str = None) -> dict:
    """
    解析 asset_index.md，构建 (元素类型, 元素名, stage_id) → 图片路径列表 映射。
    返回: { ("characters", "老吴", "山居重生期"): ["characters/老吴/山居重生期/"],
             ("characters", "老吴", "_portrait"): ["characters/老吴/_portrait/"],
             ("locations", "户政室", "默认期"): ["locations/户政室/默认期/"],
             ... }
    """
    if base_dir is None:
        base_dir = DEFAULT_BASE
    index_path = os.path.join(base_dir, "step4-assets", "asset_index.md")
    if not os.path.exists(index_path):
        return {}

    with open(index_path, 'r', encoding='utf-8') as f:
        text = f.read()

    index = {}
    current_type = None

    for line in text.splitlines():
        if '## 角色资产' in line:
            current_type = 'characters'
            continue
        elif '## 场景资产' in line:
            current_type = 'locations'
            continue
        elif '## 道具资产' in line:
            current_type = 'props'
            continue

        if current_type and '|' in line:
            cells = [c.strip() for c in line.split('|')]
            cells = [c for c in cells if c]
            if not cells or all(re.match(r'^-+$', c) for c in cells):
                continue
            # 跳过表头
            if any(c in ('角色名', '场景名', '道具名', '类型', 'stage_id', '参考图路径') for c in cells):
                continue

            if current_type == 'characters' and len(cells) >= 5:
                name = cells[0]
                sub_type = cells[1]  # 肖像 / 阶段
                stage_id = cells[2] if cells[2] != '—' else '_portrait'
                ref_path = cells[4] if len(cells) > 4 else cells[3]
                key = (current_type, name, stage_id)
                index.setdefault(key, []).append(ref_path)
            elif current_type in ('locations', 'props') and len(cells) >= 4:
                name = cells[0]
                stage_id = cells[1]
                ref_path = cells[3] if len(cells) > 3 else cells[2]
                key = (current_type, name, stage_id)
                index.setdefault(key, []).append(ref_path)

    return index


def get_global_style_prefix(base_dir: str = None) -> str:
    """从 art_direction.md 提取全局 style prompt 前缀"""
    if base_dir is None:
        base_dir = DEFAULT_BASE
    art_path = os.path.join(base_dir, "step2-art-direction", "art_direction.md")
    if not os.path.exists(art_path):
        return ""
    with open(art_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # 找第七章代码块
    m = re.search(r'##\s*七[、.．]\s*(.*?)(?=\n##\s|\Z)', text, re.S)
    if m:
        section = m.group(1)
        code = re.findall(r'```[^\n]*\n(.*?)```', section, re.S)
        if code:
            return code[0].strip().split('\n')[0].strip()
    # fallback
    for line in text.splitlines():
        if 'Cinematic still' in line or 'cinematic' in line.lower():
            return line.strip().strip('`').strip('"').strip("'")
    return ""


# ---------------------------------------------------------------------------
# 景别翻译
# ---------------------------------------------------------------------------
def translate_scale(scale_cn: str) -> str:
    """将中文景别转为英文"""
    for cn, en in SCALE_MAP.items():
        if cn in scale_cn:
            return en
    return "medium shot"  # 默认中景


def translate_angle(angle_cn: str) -> str:
    """将中文机位角度转为英文"""
    for cn, en in ANGLE_MAP.items():
        if cn in angle_cn:
            return en
    # 尝试提取角度信息
    if '偏高' in angle_cn or '俯' in angle_cn:
        return "slightly high angle"
    if '偏低' in angle_cn or '仰' in angle_cn:
        return "slightly low angle"
    if '侧' in angle_cn:
        return "side angle"
    return "eye-level angle"


def get_ref_weights(scale_cn: str) -> tuple:
    """根据景别获取参考图权重 (portrait_w, stage_w, scene_w)"""
    for cn, weights in REF_WEIGHT_TABLE.items():
        if cn in scale_cn:
            return weights
    return (0.45, 0.55, 0.45)  # 默认中景权重


# ---------------------------------------------------------------------------
# 场景特定负面提示词
# ---------------------------------------------------------------------------
def get_scene_negative(shot: dict, scene_info: dict = None) -> str:
    """根据镜头特征生成场景特定负面提示词"""
    negatives = []

    # 时间判断
    time_str = scene_info.get("time", "") if scene_info else ""
    if "夜" in time_str or "晚" in time_str:
        negatives.append("bright daylight, blue sky, harsh shadows")
    if "黎明" in time_str or "拂晓" in time_str:
        negatives.append("bright midday sun, harsh shadows")

    # 景别判断
    scale = shot.get("scale", "")
    if "特写" in scale or "近景" in scale:
        negatives.append("full body visible, wide landscape, distant view")
    if "远景" in scale or "大远景" in scale:
        negatives.append("facial details, close-up features")

    # 角色数量判断
    char_elements = [e for e in shot.get("elements", []) if e.get("type") == "角色"]
    if len(char_elements) == 1:
        negatives.append("multiple people, crowd, extra figures")
    elif len(char_elements) == 0:
        negatives.append("people, human figures, faces")

    # 古代/现代判断（根据场景圣经或分镜信息）
    visual = shot.get("visual_desc", "")
    if any(w in visual for w in ["古", "城墙", "客栈", "马车", "长衫", "长袍"]):
        negatives.append("modern buildings, cars, power lines, concrete, asphalt road")

    return ", ".join(negatives)
