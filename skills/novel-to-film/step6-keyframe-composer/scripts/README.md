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
│ assemble_prompts │  拼接 Layer 1/2/4 + 参考图，Layer 3 留空
│                  │  输出: prompt_assembly.json
└────────┬────────┘
         ▼
┌─────────────────────┐
│ Claude 对话生成       │  在 Claude Desktop 对话中，逐批次将
│ (替代 translate_     │  中文画面描述翻译为英文 Layer 3
│  prompts.py)         │  输出: layer3_translations.json
└────────┬────────────┘
         ▼
┌──────────────────┐
│ generate_keyframes│  合并 prompt_assembly + translations，
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

# 3. 翻译画面描述（Claude 对话生成，见下方说明）
#    在 Claude Desktop 对话中下达指令，Claude 读取 prompt_assembly.json 中的
#    中文画面描述，逐批次生成英文 Layer 3，输出到 layer3_translations.json。
#    prompt_assembly.json 保持不变（Layer 3 留空）。
#    无需 API key，无需运行 translate_prompts.py。

# 4. 生成锚点帧（需要 Seedream API）
python3 generate_keyframes.py
python3 generate_keyframes.py --dry-run    # 只看计划
python3 generate_keyframes.py --limit 5    # 只生成 5 个

# 5. 生成索引
python3 build_keyframe_index.py

# 6. 校验
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

为每个 step6 需生成的镜头组装半成品 prompt：

- Layer 1：全局 style prefix（固定文本）
- Layer 2：景别 + 机位英文术语（查表）
- Layer 3：**留空**（待翻译填充）
- Layer 4：全局 + 场景特定负面提示词
- 参考图：从 asset_index.md 查找路径 + 按景别计算权重

同时提取中文画面描述原文（foreground/midground/background + frozen_moment）作为翻译源。

### 4. `translate_prompts.py` — Prompt 翻译（已废弃）

> **已废弃**：此脚本需要 Anthropic API key。当前改用 Claude Desktop 对话模式直接生成 Layer 3。
> 脚本保留作为备用方案，如果后续获得 API key 可重新启用。

原设计：调用 Claude API 将中文画面描述翻译为 Seedream 结构化英文 prompt。

### 4a. Claude 对话生成 Layer 3（当前方案）

在 Claude Desktop（Cowork 模式）中，由 Claude 直接读取 `prompt_assembly.json` 中的中文画面描述，逐批次翻译为英文 Seedream prompt，输出到独立文件 `layer3_translations.json`。

`prompt_assembly.json` 保持不变（`layer3_visual_content` 留空），翻译结果单独存储，便于审核和版本管理。`generate_keyframes.py` 运行时自动合并两个文件。

**翻译规则**：
- 冻结时刻：取 `frozen_moment_cn`，描述第 0 秒的静态画面
- 空间分层：foreground → midground → background
- 光影具体化：将模糊描述转为具体的光源方向、色温、阴影方向
- 色彩具体化：使用具体英文色名（`deep burgundy` 而非 `dark`）
- 目标长度：80-150 词
- 输出结构：[主体+姿态] + [服装/道具] + [环境] + [光影] + [氛围]

**输出文件**：`layer3_translations.json`（`shot_id → 英文 prompt` 的映射表）

```json
{
  "SC001-001": "Foreground: stainless steel queue barriers...",
  "SC002-001": "Dining table edge occupies the bottom...",
  ...
}
```

**工作流程**：
1. 用户在 Claude Desktop 对话中下达"翻译第 N-M 条"指令
2. Claude 读取 `prompt_assembly.json` 中对应条目的 `foreground_cn` / `midground_cn` / `background_cn` / `frozen_moment_cn`
3. Claude 生成英文 prompt，写入 `layer3_translations.json`
4. `generate_keyframes.py` 运行时自动读取两个文件并合并

### 5. `generate_keyframes.py` — 锚点帧生成（需要 Seedream API）

读取 `prompt_assembly.json`（骨架）+ `layer3_translations.json`（翻译），运行时自动合并，然后调用 Seedream API 批量生成：

- 合并 Layer 3 翻译到 prompt 骨架
- 组装最终 prompt（Layer 1 + 2 + 3 + Negative）
- 收集参考图（肖像锚点 + 阶段参考 + 场景参考）
- 调用 API 生成图片
- 保存到 `step6-keyframes/{场次}/{镜号}_first.png`
- 生成 `{镜号}_prompt.md` 记录文件

支持断点续跑、速率控制、重试机制。

### 6. `build_keyframe_index.py` — 索引生成

扫描实际文件，输出 `keyframe_index.md`（step7 核心输入），包含：

- 统计总览
- 连续性链清单
- 正反打序列清单
- 逐镜头索引（帧类型 + 路径 + 链关系 + 生成状态）

### 7. `validate_keyframes.py` — 完整性校验

5 项校验：

1. 锚点帧完整性（所有 step6_generates 镜头是否有文件）
2. Prompt 记录完整性（有图片的是否都有 _prompt.md）
3. 链内镜头检查（chain_internal 不应有多余文件）
4. 连续性链完整性（链头锚点帧是否存在）
5. 文件大小检查（疑似损坏文件）

## 数据流

```
production/
├── step2-art-direction/art_direction.md     ← 全局 style prefix
├── step4-assets/asset_index.md              ← 参考图索引
├── step4-assets/{type}/{name}/{stage}/      ← 实际参考图
├── step5-storyboard/storyboard/SC*.md       ← 分镜脚本（输入）
└── step6-keyframes/                         ← 输出
    ├── shot_classification.json             ← 镜头分类
    ├── prompt_assembly.json                 ← prompt 骨架（Layer 3 留空）
    ├── layer3_translations.json            ← Layer 3 翻译（shot_id → 英文 prompt）
    ├── keyframe_index.md                    ← 锚点帧索引（step7 输入）
    ├── generation_log.jsonl                 ← 生成日志
    └── SC{NNN}/
        ├── SC{NNN}-{MMM}_first.png          ← 锚点帧
        └── SC{NNN}-{MMM}_prompt.md          ← prompt 记录
```

## 设计原则

1. **60% 脚本 + 30% LLM + 10% Seedream** — 将确定性逻辑（解析、分类、拼接、编排）用脚本完成，创作性翻译由 Claude 对话直接完成（替代原 API 调用方案）
2. **复用 step4 模式** — API 调用、重试、断点续跑等逻辑与 step4 generate_images.py 一致
3. **中间产物可审查** — 每一步都有 JSON 输出，可以人工审核后再进入下一步
4. **幂等 & 断点续跑** — 所有脚本默认跳过已有结果，可安全重跑；Claude 对话生成同理，已有 layer3_visual_content 的条目跳过
