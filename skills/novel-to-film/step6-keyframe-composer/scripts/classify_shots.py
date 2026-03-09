#!/usr/bin/env python3
"""
classify_shots.py — 解析全部分镜脚本，识别连续性链，分类镜头

核心功能：
1. 扫描 192 个分镜脚本的"首帧合成提示"段落
2. 从"前接/后接"关系构建连续性链图
3. 将全部镜头分为四类：链头锚点、链内（step7提供）、独立锚点、正反打锚点
4. 输出 shot_classification.json（下游脚本的核心输入）

用法：
    python3 classify_shots.py [--base-dir /path/to/production]
    python3 classify_shots.py --stats          # 只输出统计
    python3 classify_shots.py --dry-run        # 不写文件
"""

import os
import sys
import re
import json
import argparse
import logging
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from storyboard_utils import load_all_storyboards, DEFAULT_BASE

# ---------------------------------------------------------------------------
# 日志
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("classify")


# ---------------------------------------------------------------------------
# 连续性链构建
# ---------------------------------------------------------------------------
def build_continuity_chains(shots: list) -> tuple:
    """
    从全部镜头的 continuity.prev / continuity.next 构建连续性链。

    连续性链定义：
    - 前后镜头存在帧级连续性（动作衔接、动作拆分、环绕拆分）
    - 用图的方式表示：shot A → shot B 表示 B 的首帧应来自 A 的尾帧

    返回:
        chains: [
            {"chain_id": "chain-01", "shots": ["SC005-003", "SC005-004", ...], "head": "SC005-003"},
            ...
        ]
        shot_chain_map: {"SC005-003": "chain-01", "SC005-004": "chain-01", ...}
    """
    # 构建邻接表
    next_map = {}   # shot_id → next_shot_id
    prev_map = {}   # shot_id → prev_shot_id
    all_ids = set()
    shot_scene = {}  # shot_id → scene_id

    for shot in shots:
        sid = shot["shot_id"]
        all_ids.add(sid)
        shot_scene[sid] = shot.get("scene_id", "")
        cont = shot.get("continuity", {})
        # 只有同场次的前接/后接才构成连续性链
        # 跨场次的链接是"场次切换"（叠化/硬切），不是帧级连续
        if cont.get("next"):
            nxt = cont["next"]
            nxt_scene = nxt.rsplit('-', 1)[0] if '-' in nxt else ""
            if nxt_scene == shot.get("scene_id", ""):
                next_map[sid] = nxt
        if cont.get("prev"):
            prv = cont["prev"]
            prv_scene = prv.rsplit('-', 1)[0] if '-' in prv else ""
            if prv_scene == shot.get("scene_id", ""):
                prev_map[sid] = prv

    # 验证双向一致性
    warnings = []
    for sid, nxt in next_map.items():
        if nxt in prev_map and prev_map[nxt] != sid:
            warnings.append(f"链接不一致: {sid}→{nxt}, 但 {nxt}.prev={prev_map.get(nxt)}")

    # 找所有链头：有 next 但没有 prev（或 prev 不在 next_map 的值中）
    chain_heads = []
    for sid in all_ids:
        if sid in prev_map:
            continue  # 有前驱，不是链头
        if sid in next_map:
            chain_heads.append(sid)  # 无前驱但有后继 → 链头

    # 从每个链头开始遍历
    chains = []
    shot_chain_map = {}
    chain_idx = 0

    for head in sorted(chain_heads):
        chain_idx += 1
        chain_id = f"chain-{chain_idx:03d}"
        chain_shots = [head]
        current = head

        while current in next_map:
            nxt = next_map[current]
            if nxt in shot_chain_map:
                warnings.append(f"链环检测: {current}→{nxt} 已属于 {shot_chain_map[nxt]}")
                break
            chain_shots.append(nxt)
            current = nxt

        chains.append({
            "chain_id": chain_id,
            "shots": chain_shots,
            "head": head,
            "length": len(chain_shots),
        })

        for s in chain_shots:
            shot_chain_map[s] = chain_id

    return chains, shot_chain_map, warnings


# ---------------------------------------------------------------------------
# 正反打序列识别
# ---------------------------------------------------------------------------
def identify_shot_reverse_shot(shots: list) -> list:
    """
    识别正反打（shot/reverse shot）序列。

    正反打特征：
    - 连续 2-4 个镜头在同一场次
    - 景别为过肩/中景/中近景/近景
    - 元素标注中出现相同的 2 个角色交替作为焦点
    - 衔接说明中可能提到"正反打"或"over-the-shoulder"

    返回: [{"group_id": "srs-01", "shots": ["SC008-001", "SC008-002", ...]}, ...]
    """
    srs_groups = []
    # 简单启发式：查找分镜中包含"正反打"或"过肩"关键词的连续镜头
    # 更精确的方案需要分析角色交替模式，但这里用关键词先做
    i = 0
    group_idx = 0
    while i < len(shots):
        shot = shots[i]
        # 检查当前镜头是否有正反打特征
        has_srs_hint = False
        angle = shot.get("angle", "")
        ref_hint = shot.get("continuity", {}).get("ref_hint", "")
        visual = shot.get("visual_desc", "")

        if "正反打" in ref_hint or "正反打" in visual or "过肩" in angle:
            has_srs_hint = True

        if has_srs_hint:
            group_idx += 1
            group_shots = [shot["shot_id"]]
            scene = shot["scene_id"]
            j = i + 1
            # 向后扫描同场次的连续正反打镜头
            while j < len(shots) and shots[j]["scene_id"] == scene:
                s = shots[j]
                a = s.get("angle", "")
                rh = s.get("continuity", {}).get("ref_hint", "")
                v = s.get("visual_desc", "")
                if "正反打" in rh or "正反打" in v or "过肩" in a:
                    group_shots.append(s["shot_id"])
                    j += 1
                else:
                    break

            if len(group_shots) >= 2:
                srs_groups.append({
                    "group_id": f"srs-{group_idx:03d}",
                    "shots": group_shots,
                })
            i = j
        else:
            i += 1

    return srs_groups


# ---------------------------------------------------------------------------
# 镜头分类
# ---------------------------------------------------------------------------
def classify_all_shots(shots: list) -> dict:
    """
    对全部镜头进行分类。

    分类规则：
    1. 有 continuity.prev 且属于某条链 → chain_internal（step7提供首帧）
    2. 链头（链的第一个镜头）→ chain_head（step6 生成锚点帧）
    3. 属于正反打序列 → shot_reverse_shot（step6 独立生成但保持空间一致）
    4. 其余 → independent（step6 生成锚点帧）

    返回: {
        "shots": [
            {
                "shot_id": "SC001-001",
                "frame_type": "independent" | "chain_head" | "chain_internal" | "shot_reverse_shot",
                "chain_id": "chain-01" | null,
                "chain_position": "1/4" | null,
                "srs_group": "srs-01" | null,
                "step6_generates": true | false,
                "scene_id": "SC001",
                "scale": "全景",
                "chapter": "ch1",
            }, ...
        ],
        "chains": [...],
        "srs_groups": [...],
        "stats": {...},
    }
    """
    # 1. 构建连续性链
    chains, shot_chain_map, warnings = build_continuity_chains(shots)

    # 2. 识别正反打序列
    srs_groups = identify_shot_reverse_shot(shots)
    srs_shot_map = {}
    for g in srs_groups:
        for s in g["shots"]:
            srs_shot_map[s] = g["group_id"]

    # 3. 逐镜头分类
    classified = []
    stats = {
        "total_shots": 0,
        "chain_head": 0,
        "chain_internal": 0,
        "independent": 0,
        "shot_reverse_shot": 0,
        "step6_generates": 0,
        "step7_provides": 0,
        "total_chains": len(chains),
        "total_srs_groups": len(srs_groups),
    }

    # 建立链内位置索引
    chain_position = {}
    for chain in chains:
        for idx, sid in enumerate(chain["shots"]):
            chain_position[sid] = f"{idx + 1}/{chain['length']}"

    for shot in shots:
        sid = shot["shot_id"]
        stats["total_shots"] += 1

        entry = {
            "shot_id": sid,
            "scene_id": shot["scene_id"],
            "chapter": shot.get("chapter", ""),
            "scale": shot.get("scale", ""),
            "angle": shot.get("angle", ""),
            "duration": shot.get("duration", ""),
            "chain_id": None,
            "chain_position": None,
            "srs_group": None,
            "frame_type": "",
            "step6_generates": False,
        }

        if sid in shot_chain_map:
            entry["chain_id"] = shot_chain_map[sid]
            entry["chain_position"] = chain_position.get(sid)

            # 判断是链头还是链内
            chain_obj = next(c for c in chains if c["chain_id"] == shot_chain_map[sid])
            if sid == chain_obj["head"]:
                entry["frame_type"] = "chain_head"
                entry["step6_generates"] = True
                stats["chain_head"] += 1
                stats["step6_generates"] += 1
            else:
                entry["frame_type"] = "chain_internal"
                entry["step6_generates"] = False
                stats["chain_internal"] += 1
                stats["step7_provides"] += 1
        elif sid in srs_shot_map:
            entry["srs_group"] = srs_shot_map[sid]
            entry["frame_type"] = "shot_reverse_shot"
            entry["step6_generates"] = True
            stats["shot_reverse_shot"] += 1
            stats["step6_generates"] += 1
        else:
            entry["frame_type"] = "independent"
            entry["step6_generates"] = True
            stats["independent"] += 1
            stats["step6_generates"] += 1

        classified.append(entry)

    return {
        "shots": classified,
        "chains": chains,
        "srs_groups": srs_groups,
        "warnings": warnings,
        "stats": stats,
    }


# ---------------------------------------------------------------------------
# 优先级排序
# ---------------------------------------------------------------------------
def assign_priorities(classification: dict, shots_data: list) -> list:
    """
    为需要 step6 生成的镜头分配优先级。

    P0: ★★★★★ 事件相关镜头
    P1: 连续性链头镜头
    P2: 主角特写/近景
    P3: 场景建立镜头（每个场次的第一个镜头）
    P4: 其余镜头
    """
    # 建立 shot_id → shot_data 映射
    shot_data_map = {s["shot_id"]: s for s in shots_data}

    # 建立场次第一个镜头集合
    scene_first = set()
    seen_scenes = set()
    for entry in classification["shots"]:
        if entry["scene_id"] not in seen_scenes:
            seen_scenes.add(entry["scene_id"])
            scene_first.add(entry["shot_id"])

    prioritized = []
    for entry in classification["shots"]:
        if not entry["step6_generates"]:
            continue

        sid = entry["shot_id"]
        shot_orig = shot_data_map.get(sid, {})

        # 判断优先级
        if entry["frame_type"] == "chain_head":
            priority = "P1"
        elif sid in scene_first:
            priority = "P3"
        elif "特写" in entry.get("scale", "") or "近景" in entry.get("scale", ""):
            priority = "P2"
        else:
            priority = "P4"

        # TODO: P0 需要检查 ★★★★★ 事件，暂时留作扩展
        # 可以通过匹配 shot.event 字段中的关键事件来提升优先级

        entry_copy = dict(entry)
        entry_copy["priority"] = priority
        prioritized.append(entry_copy)

    # 排序
    p_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3, "P4": 4}
    prioritized.sort(key=lambda x: (p_order.get(x["priority"], 9), x["shot_id"]))

    return prioritized


# ---------------------------------------------------------------------------
# 输出
# ---------------------------------------------------------------------------
def write_classification(classification: dict, output_path: str):
    """将分类结果写入 JSON"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(classification, f, ensure_ascii=False, indent=2)
    log.info(f"✅ 分类结果已写入: {output_path}")


def print_stats(stats: dict):
    """打印统计信息"""
    print(f"\n{'='*50}")
    print(f"镜头分类统计")
    print(f"{'='*50}")
    print(f"  总镜头数:              {stats['total_shots']}")
    print(f"  ─ 链头锚点:           {stats['chain_head']}")
    print(f"  ─ 链内(step7提供):    {stats['chain_internal']}")
    print(f"  ─ 独立锚点:           {stats['independent']}")
    print(f"  ─ 正反打锚点:         {stats['shot_reverse_shot']}")
    print(f"  ────────────────────")
    print(f"  step6 需生成:          {stats['step6_generates']}")
    print(f"  step7 提供首帧:        {stats['step7_provides']}")
    print(f"  连续性链总数:          {stats['total_chains']}")
    print(f"  正反打序列组数:        {stats['total_srs_groups']}")
    print(f"{'='*50}\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="解析分镜脚本，识别连续性链，分类全部镜头")
    parser.add_argument("--base-dir", default=DEFAULT_BASE, help="production 目录")
    parser.add_argument("--output", default=None, help="输出文件路径 (默认: production/step6-keyframes/shot_classification.json)")
    parser.add_argument("--stats", action="store_true", help="只输出统计")
    parser.add_argument("--dry-run", action="store_true", help="不写文件")
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    output = args.output or os.path.join(base, "step6-keyframes", "shot_classification.json")

    # 1. 加载全部分镜脚本
    log.info(f"加载分镜脚本: {base}")
    all_shots, scene_infos = load_all_storyboards(base)
    log.info(f"共加载 {len(all_shots)} 个镜头, {len(scene_infos)} 个场次")

    # 2. 分类
    classification = classify_all_shots(all_shots)

    # 3. 优先级排序
    prioritized = assign_priorities(classification, all_shots)
    classification["prioritized_queue"] = prioritized

    # 4. 统计
    print_stats(classification["stats"])

    if classification["warnings"]:
        print(f"⚠️ 链接一致性警告 ({len(classification['warnings'])}):")
        for w in classification["warnings"][:10]:
            print(f"  - {w}")
        if len(classification["warnings"]) > 10:
            print(f"  ... 还有 {len(classification['warnings']) - 10} 条")

    # 5. 输出
    if args.stats:
        return

    if not args.dry_run:
        write_classification(classification, output)
        log.info(f"  step6 待生成队列: {len(prioritized)} 个锚点帧")
        # 按优先级统计
        by_p = defaultdict(int)
        for p in prioritized:
            by_p[p["priority"]] += 1
        for k in sorted(by_p):
            log.info(f"    {k}: {by_p[k]}")
    else:
        log.info(f"DRY RUN — 不写入文件")
        log.info(f"  step6 待生成: {len(prioritized)} 个锚点帧")


if __name__ == "__main__":
    main()
