# Step 6 — 首帧合成脚本集

为分镜脚本中的锚点镜头生成 Seedream 首帧图（keyframe），作为 Step 7 Seedance 2.0 image-to-video 的起点。

## 架构概览

```
分镜脚本 (SC001-SC192)
        │
        ▼
┌─────────────────┐
│ classify_shots   │  解析连续性链，分类全部镜头
│                  │  输出: shot_classification.json
└────────┬────────┘
         ▼
┌─────────────────┐
│ assemble_prompts │  拼接 Layer 1/2/4 + 参考图
│                  │  Layer 3 直接使用中文画面描述（layer3_source_cn）
│                  │  输出: prompt_assembly.json
└────────┬────────┘
         ▼
┌──────────────────┐
│ generate_keyframes│  读取 prompt_assembly.json
│                   │  调用 Seedream API 批量生成锚点帧
│                   │  输出: step6-keyframes/{SC}/{镜号}_first.png + _prompt.md
└────────┬─────────┘
         ▼
┌──────────────────────┐
│ build_keyframe_index  │  扫描结果，生成 keyframe_index.md
│                       │  输出: step6-keyframes/keyframe_index.md
└────────┬─────────────┘
         ▼
┌──────────────────────┐
│ validate_keyframes    │  校验完整性与一致性
└──────────────────────┘
```

## 依赖

```bash
pip install requests --break-system-packages
```

## 快速开始

```bash
# 0. 设置环境变量
export ARK_API_KEY="your-volcengine-ark-api-key"

# 1. 镜头分类（纯脚本，无需 API）
python3 classify_shots.py
python3 classify_shots.py --stats          # 只看统计

# 2. 组装半成品 prompt（纯脚本）
python3 assemble_prompts.py
python3 assemble_prompts.py --dry-run      # 只看计划

# 3. 生成锚点帧（需要 Seedream API）
#    prompt_assembly.json 中 Layer 3 已直接包含中文画面描述（layer3_source_cn）
python3 generate_keyframes.py
python3 generate_keyframes.py --dry-run    # 只看计划
python3 generate_keyframes.py --limit 5    # 只生成 5 个

# 4. 生成索引
python3 build_keyframe_index.py

# 5. 校验
python3 validate_keyframes.py
```

## 脚本说明

### 1. `storyboard_utils.py` — 共享工具

分镜脚本解析器，提供：

- `parse_storyboard_file()` — 解析单个分镜脚本文件
- `load_all_storyboards()` — 加载全部 192 个分镜脚本
- `load_asset_index()` — 解析 asset_index.md 为查找表
- `get_global_style_prefix()` — 提取全局 style prompt 前缀
- `translate_scale()` / `translate_angle()` — 景别/机位中英映射
- `get_ref_weights()` — 根据景别查参考图权重
- `get_scene_negative()` — 生成场景特定负面提示词
- `SCALE_MAP` / `ANGLE_MAP` / `REF_WEIGHT_TABLE` — 常量表

### 2. `classify_shots.py` — 镜头分类

解析分镜脚本中的"首帧合成提示"段落，将全部镜头分为四类：

| 类型 | 说明 | step6 生成 |
|------|------|-----------|
| `chain_head` | 连续性链的第一个镜头 | ✅ |
| `chain_internal` | 连续性链内部后续镜头 | ❌（step7 提供） |
| `independent` | 无连续性需求 | ✅ |
| `shot_reverse_shot` | 正反打序列 | ✅ |

输出 `shot_classification.json`，包含：镜头列表、连续性链、正反打组、优先级队列、统计。

### 3. `assemble_prompts.py` — Prompt 组装

为每个 step6 需生成的镜头组装完整 prompt：

- Layer 1：全局 style prefix（固定文本）
- Layer 2：景别 + 机位英文术语（查表）
- Layer 3：**中文画面描述**（layer3_source_cn，直接来自分镜脚本的 foreground/midground/background + frozen_moment）
- Layer 4：全局 + 场景特定负面提示词
- 参考图：从 asset_index.md 查找路径 + 按景别计算权重

**说明**：Layer 3 直接使用中文描述，无需翻译。Seedream 原生支持中文，保留原文避免翻译过程中丧失场景细节。

### 4. 脚本已移除：`translate_prompts.py` 和 `layer3_translations.json`

> **已移除**：不再需要翻译步骤。
>
> 原方案：通过 Claude Desktop 对话或 API 调用将中文画面描述翻译为英文。
>
> **新方案的原因**：
> - Seedream 原生支持中文输入
> - 保留中文原文避免翻译过程中丧失细节描写
> - 简化工作流程，减少中间步骤

### 4. `generate_keyframes.py` — 锚点帧生成（需要 Seedream API）

读取 `prompt_assembly.json`（已包含中文 Layer 3），然后调用 Seedream API 批量生成：

- 组装最终 prompt（Layer 1 + 2 + 中文 Layer 3 + Negative）
- 收集参考图（肖像锚点 + 阶段参考 + 场景参考）
- 调用 API 生成图片
- 保存到 `step6-keyframes/{场次}/{镜号}_first.png`
- 生成 `{镜号}_prompt.md` 记录文件

支持断点续跑、速率控制、重试机制。

### 5. `build_keyframe_index.py` — 索引生成

扫描实际文件，输出 `keyframe_index.md`（step7 核心输入），包含：

- 统计总览
- 连续性链清单
- 正反打序列清单
- 逐镜头索引（帧类型 + 路径 + 链关系 + 生成状态）

### 6. `validate_keyframes.py` — 完整性校验

5 项校验：

1. 锚点帧完整性（所有 step6_generates 镜头是否有文件）
2. Prompt 记录完整性（有图片的是否都有 _prompt.md）
3. 链内镜头检查（chain_internal 不应有多余文件）
4. 连续性链完整性（链头锚点帧是否存在）
5. 文件大小检查（疑似损坏文件）

## 数据流

```
production/
├── step2-visual-design/art_direction.md     ← 全局 style prefix
├── step4-assets/asset_index.md              ← 参考图索引
├── step4-assets/{type}/{name}/{stage}/      ← 实际参考图
├── step5-storyboard/storyboard/SC*.md       ← 分镜脚本（输入）
└── step6-keyframes/                         ← 输出
    ├── shot_classification.json             ← 镜头分类
    ├── prompt_assembly.json                 ← prompt 骨架（Layer 3 含中文画面描述）
    ├── keyframe_index.md                    ← 锚点帧索引（step7 输入）
    ├── generation_log.jsonl                 ← 生成日志
    └── SC{NNN}/
        ├── SC{NNN}-{MMM}_first.png          ← 锚点帧
        └── SC{NNN}-{MMM}_prompt.md          ← prompt 记录
```

## 设计原则

1. **保留中文原文** — Layer 3 直接使用分镜脚本中的中文画面描述（layer3_source_cn），无需翻译。Seedream 原生支持中文，保留原文避免翻译过程中丧失细节
2. **80% 脚本 + 20% Seedream** — 将确定性逻辑（解析、分类、拼接、编排）用脚本完成，调用 Seedream API 生成图像
3. **复用 step4 模式** — API 调用、重试、断点续跑等逻辑与 step4 generate_images.py 一致
4. **中间产物可审查** — 每一步都有 JSON 输出，可以人工审核后再进入下一步
5. **幂等 & 断点续跑** — 所有脚本默认跳过已有结果，可安全重跑
