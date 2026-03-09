#!/usr/bin/env python3
"""
assemble_prompts.py — 为每个锚点帧组装半成品 Prompt

核心功能：
1. 读取 shot_classification.json（由 classify_shots.py 生成）
2. 对每个 step6_generates=true 的镜头：
   - 拼接 Layer 1（全局 style prefix）
   - 拼接 Layer 2（景别 + 机位角度英文术语）
   - Layer 3 留空占位（待 translate_prompts.py 填充）
   - 拼接 Layer 4（全局负面提示词 + 场景特定负面提示词）
   - 查找参考图路径 + 计算权重
3. 输出 prompt_assembly.json（translate_prompts.py 的输入）

用法：
    python3 assemble_prompts.py [--base-dir /path/to/production]
    python3 assemble_prompts.py --dry-run     # 只看计划
"""

import os
import sys
import json
import argparse
import logging

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from storyboard_utils import (
    load_all_storyboards,
    load_asset_index,
    get_global_style_prefix,
    translate_scale,
    translate_angle,
    get_ref_weights,
    get_scene_negative,
    GLOBAL_NEGATIVE,
    DEFAULT_BASE,
)

# ---------------------------------------------------------------------------
# 日志
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("assemble")


# ---------------------------------------------------------------------------
# 参考图查找
# ---------------------------------------------------------------------------
def find_ref_images(shot_data: dict, asset_index: dict, base_dir: str) -> list:
    """
    根据镜头的元素标注，在 asset_index 中查找参考图路径。

    返回: [
        {"purpose": "角色一致性锚点", "element": "老吴", "ref_path": "characters/老吴/_portrait/",
         "weight": 0.45, "note": "面部基线"},
        {"purpose": "角色阶段参考", "element": "老吴", "ref_path": "characters/老吴/山居重生期/",
         "weight": 0.55, "note": "服装+整体形象"},
        {"purpose": "场景参考", "element": "户政室", "ref_path": "locations/户政室/默认期/",
         "weight": 0.45, "note": "环境氛围"},
        ...
    ]
    """
    refs = []
    elements = shot_data.get("elements", [])
    scale = shot_data.get("scale", "中景")
    portrait_w, stage_w, scene_w = get_ref_weights(scale)

    # 角色参考图（最多前 3 个角色）
    char_elements = [e for e in elements if e.get("type") == "角色"]
    for idx, elem in enumerate(char_elements[:3]):
        name = elem.get("name", "")
        stage_id = elem.get("stage_id")

        # 主视角 vs 次要角色：降低权重
        weight_adjust = 0.0 if idx == 0 else -0.15

        # 肖像锚点
        portrait_key = ("characters", name, "_portrait")
        portrait_paths = asset_index.get(portrait_key, [])
        if portrait_paths:
            refs.append({
                "purpose": "角色一致性锚点",
                "element": name,
                "ref_path": portrait_paths[0],
                "weight": round(max(0.1, portrait_w + weight_adjust), 2),
                "note": "面部基线",
            })

        # 阶段参考图
        if stage_id:
            stage_key = ("characters", name, stage_id)
            stage_paths = asset_index.get(stage_key, [])
            if stage_paths:
                refs.append({
                    "purpose": "角色阶段参考",
                    "element": name,
                    "ref_path": stage_paths[0],
                    "weight": round(max(0.1, stage_w + weight_adjust), 2),
                    "note": f"服装+整体形象 ({stage_id})",
                })

    # 场景参考图
    loc_elements = [e for e in elements if e.get("type") == "场景"]
    for elem in loc_elements[:1]:  # 通常只有一个场景
        name = elem.get("name", "")
        stage_id = elem.get("stage_id")
        if stage_id:
            loc_key = ("locations", name, stage_id)
        else:
            loc_key = ("locations", name, "默认")
        loc_paths = asset_index.get(loc_key, [])
        if loc_paths:
            refs.append({
                "purpose": "场景参考",
                "element": name,
                "ref_path": loc_paths[0],
                "weight": round(scene_w, 2),
                "note": "环境氛围",
            })

    # 道具参考图（仅明显可见的）
    prop_elements = [e for e in elements if e.get("type") == "道具"]
    for elem in prop_elements:
        name = elem.get("name", "")
        stage_id = elem.get("stage_id")
        if stage_id:
            prop_key = ("props", name, stage_id)
        else:
            prop_key = ("props", name, "默认期")
        prop_paths = asset_index.get(prop_key, [])
        if prop_paths:
            refs.append({
                "purpose": "道具参考",
                "element": name,
                "ref_path": prop_paths[0],
                "weight": 0.35,
                "note": "道具外观",
            })

    return refs


# ---------------------------------------------------------------------------
# Prompt 组装
# ---------------------------------------------------------------------------
def assemble_one_prompt(shot_data: dict, global_prefix: str, asset_index: dict,
                        scene_info: dict, base_dir: str) -> dict:
    """
    为单个镜头组装半成品 prompt。

    返回: {
        "shot_id": "SC001-001",
        "scene_id": "SC001",
        "layer1_global_prefix": "cinematic, dark fantasy, ...",
        "layer2_shot_spec": "full shot, slightly high angle",
        "layer3_visual_content": "",  ← 留空，待 translate_prompts.py 填充
        "layer3_source_cn": "...",    ← 中文画面描述原文（翻译用）
        "frozen_moment_cn": "...",    ← 冻结时刻中文原文
        "foreground_cn": "...",
        "midground_cn": "...",
        "background_cn": "...",
        "negative_global": "...",
        "negative_scene": "...",
        "ref_images": [...],
        "metadata": {
            "scale_cn": "全景",
            "angle_cn": "正面偏高",
            "duration": "10s",
            "chapter": "ch1",
        },
    }
    """
    sid = shot_data["shot_id"]

    # Layer 1: 全局 style prefix
    layer1 = global_prefix

    # Layer 2: 景别 + 机位
    scale_en = translate_scale(shot_data.get("scale", ""))
    angle_en = translate_angle(shot_data.get("angle", ""))
    layer2 = f"{scale_en}, {angle_en}"

    # Layer 3: 留空 — 中文原文作为翻译源
    layer3_source = shot_data.get("visual_desc", "")
    frozen_moment = shot_data.get("frozen_moment", "")
    foreground = shot_data.get("foreground", "")
    midground = shot_data.get("midground", "")
    background = shot_data.get("background", "")

    # Layer 4: 负面提示词
    negative_scene = get_scene_negative(shot_data, scene_info)

    # 参考图
    ref_images = find_ref_images(shot_data, asset_index, base_dir)

    return {
        "shot_id": sid,
        "scene_id": shot_data.get("scene_id", ""),
        "layer1_global_prefix": layer1,
        "layer2_shot_spec": layer2,
        "layer3_visual_content": "",  # 待填充
        "layer3_source_cn": layer3_source,
        "frozen_moment_cn": frozen_moment,
        "foreground_cn": foreground,
        "midground_cn": midground,
        "background_cn": background,
        "negative_global": GLOBAL_NEGATIVE,
        "negative_scene": negative_scene,
        "ref_images": ref_images,
        "metadata": {
            "scale_cn": shot_data.get("scale", ""),
            "angle_cn": shot_data.get("angle", ""),
            "duration": shot_data.get("duration", ""),
            "chapter": shot_data.get("chapter", ""),
            "event": shot_data.get("event", ""),
        },
    }


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="为每个锚点帧组装半成品 Prompt")
    parser.add_argument("--base-dir", default=DEFAULT_BASE, help="production 目录")
    parser.add_argument("--classification", default=None,
                        help="shot_classification.json 路径 (默认: production/step6-keyframes/shot_classification.json)")
    parser.add_argument("--output", default=None,
                        help="输出文件路径 (默认: production/step6-keyframes/prompt_assembly.json)")
    parser.add_argument("--dry-run", action="store_true", help="不写文件，只统计")
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    class_path = args.classification or os.path.join(base, "step6-keyframes", "shot_classification.json")
    output = args.output or os.path.join(base, "step6-keyframes", "prompt_assembly.json")

    # 1. 加载分类结果
    if not os.path.exists(class_path):
        log.error(f"分类文件不存在: {class_path}")
        log.error("请先运行: python3 classify_shots.py")
        sys.exit(1)

    with open(class_path, 'r', encoding='utf-8') as f:
        classification = json.load(f)
    log.info(f"加载分类结果: {len(classification['shots'])} 个镜头")

    # 2. 提取需要 step6 生成的镜头 ID 集合
    step6_ids = set()
    for entry in classification["shots"]:
        if entry.get("step6_generates"):
            step6_ids.add(entry["shot_id"])
    log.info(f"需要 step6 生成的锚点帧: {len(step6_ids)}")

    # 3. 加载分镜脚本（获取完整的镜头数据）
    all_shots, scene_infos = load_all_storyboards(base)
    shot_data_map = {s["shot_id"]: s for s in all_shots}
    scene_info_map = {s["scene_id"]: s for s in scene_infos}
    log.info(f"加载分镜脚本: {len(all_shots)} 个镜头")

    # 4. 加载 asset_index
    asset_index = load_asset_index(base)
    log.info(f"加载资产索引: {len(asset_index)} 个条目")

    # 5. 获取全局 style prefix
    global_prefix = get_global_style_prefix(base)
    if global_prefix:
        log.info(f"全局 style prefix: {global_prefix[:60]}...")
    else:
        log.warning("⚠️ 未找到全局 style prefix")

    # 6. 逐镜头组装
    assemblies = []
    missing_data = 0
    missing_refs = 0

    for sid in sorted(step6_ids):
        shot_data = shot_data_map.get(sid)
        if not shot_data:
            log.warning(f"⚠️ 镜头 {sid} 在分镜脚本中未找到")
            missing_data += 1
            continue

        scene_info = scene_info_map.get(shot_data.get("scene_id", ""), {})
        assembly = assemble_one_prompt(shot_data, global_prefix, asset_index, scene_info, base)

        if not assembly["ref_images"]:
            missing_refs += 1

        assemblies.append(assembly)

    log.info(f"组装完成: {len(assemblies)} 个半成品 prompt")
    if missing_data:
        log.warning(f"  ⚠️ {missing_data} 个镜头在分镜脚本中未找到")
    if missing_refs:
        log.warning(f"  ⚠️ {missing_refs} 个镜头无参考图（asset_index 中未找到）")

    # 统计
    with_l3 = sum(1 for a in assemblies if a["layer3_source_cn"])
    without_l3 = len(assemblies) - with_l3
    log.info(f"  有中文画面描述（可翻译）: {with_l3}")
    log.info(f"  无中文画面描述: {without_l3}")

    # 7. 输出
    if not args.dry_run:
        os.makedirs(os.path.dirname(output), exist_ok=True)
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(assemblies, f, ensure_ascii=False, indent=2)
        log.info(f"✅ 半成品 prompt 已写入: {output}")
    else:
        log.info("DRY RUN — 不写入文件")
        # 输出前 3 个示例
        for a in assemblies[:3]:
            print(f"\n--- {a['shot_id']} ---")
            print(f"  Layer 1: {a['layer1_global_prefix'][:50]}...")
            print(f"  Layer 2: {a['layer2_shot_spec']}")
            print(f"  Layer 3 源(CN): {a['layer3_source_cn'][:80]}...")
            print(f"  Negative: {a['negative_global'][:40]}... + {a['negative_scene'][:40]}...")
            print(f"  参考图: {len(a['ref_images'])} 个")
            for r in a["ref_images"]:
                print(f"    - [{r['purpose']}] {r['element']}: {r['ref_path']} (w={r['weight']})")


if __name__ == "__main__":
    main()
