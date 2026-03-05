# Step 4 — Visual Asset Generator Scripts

本目录包含 Step 4（视觉资产生成）的全部执行脚本，按工作流顺序排列。

## 执行顺序

```
1. extract_prompts.py    提取提示词 → prompts_plan.md
2. scaffold_assets.py    搭建目录树 → step4-assets/{type}/{name}/{stage_id}/
3. generate_images.py    调用 Seedream API 批量生成图片（自动落盘到对应目录）
4. build_index.py        扫描图片 → asset_index.md
5. validate_assets.py    校验完整性 → 校验报告
```

## 脚本说明

### bible_utils.py — 共享工具模块

所有脚本的公共依赖。提供统一的圣经文件解析逻辑，包括：

- `count_stars(text)` — 从圣经文件中提取重要性星级（★数量）
- `extract_stages(text)` — 提取阶段注册表中的 stage_id 列表（标准格式，stage_id 固定第0列）
- `extract_stage_chapters(text)` — 提取 stage_id → 章节范围映射
- `has_stage_registry(text)` — 检查是否包含阶段注册表
- `count_images(directory)` — 统计目录中的图片文件数

不可独立运行，仅供其他脚本 import。

### extract_prompts.py — 提示词提取器

从全部 Step 3 圣经（角色/场景/道具）中批量提取 AI 绘图提示词，输出结构化的生成计划。

**输入**：`production/step3-bibles/` 下所有 `.md` 圣经文件 + `step2-art-direction/art_direction.md`

**输出**：`production/step4-assets/prompts_plan.md`

**`prompts_plan.md` 的定位**：仅供人工查看的提示词总览报告，不参与图片生成流程。`generate_images.py` 在生成时直接调用 `scan_bibles()` 实时读取圣经原文件，不依赖此文件。

**功能**：
- 扫描并解析中英双语提示词对（标准格式：`**English：**` 在前，`**中文：**` 在后）
- 校验全局 Style Prefix 是否内含
- 按 SKILL.md 定义的优先级（P0→P5）排序输出
- 统计缺失英文/中文/前缀的圣经

```bash
python3 extract_prompts.py [--base-dir /path/to/production]
```

### scaffold_assets.py — 资产目录搭建器

根据圣经的阶段注册表，预建 Step 4 资产的完整目录结构。

**输入**：`production/step3-bibles/` 下所有圣经文件

**输出**：`production/step4-assets/` 下的目录树

**目录结构规则**：
- 角色：`characters/{角色名}/_portrait/` + `characters/{角色名}/{stage_id}/`
- 场景：`locations/{场景名}/{stage_id}/`
- 道具：`props/{道具名}/{stage_id}/`（所有道具统一有阶段注册表，无状态变化的为"默认期"）

```bash
python3 scaffold_assets.py [--base-dir /path/to/production] [--dry-run]
```

### generate_images.py — 图片批量生成器

调用火山引擎方舟 (Volcengine Ark) Seedream API，支持三阶段生成，按优先级批量生成视觉资产图片。

**前置依赖**：

```bash
pip install requests   # 大多数环境已预装
export ARK_API_KEY="your-api-key-here"
```

**输入**：`production/step3-bibles/` 下所有圣经文件（通过 `extract_prompts.scan_bibles()` 直接读取源数据）

**输出**：生成的 `.png` 图片落盘到 `production/step4-assets/{type}/{name}/{stage_id}/` + 生成日志 `generation_log.jsonl`

**三阶段生成**：

- **Phase 1（角色基准肖像）**：生成角色正面半身像（纯文生图）。人工审核满意后进入 Phase 2。
- **Phase 2（角色参考图生图）**：以基准肖像为参考图，生成角色的其余图片（其他视角肖像 + 各阶段场景图）。自动将基准肖像编码为 base64 传入 `image` 字段。
- **Phase 3（场景 + 道具）**：生成所有场景和道具图片（纯文生图）。与 Phase 1/2 独立，可并行。

Phase 2 任务会自动检测基准肖像是否存在，未就绪的任务自动跳过并提示先跑 Phase 1。

**Prompt 拼接顺序**（最终发送给 API 的 prompt 由三层拼接）：

```
[身份锚点 Identity Anchor] + [全局前缀 Global Prefix] + [圣经原始 Prompt]
```

- **身份锚点**：从角色圣经 `### 身份锚点 / Identity Anchor` 提取，仅角色类型有。包含年龄、体型、脸型、标志性特征等视觉指纹，确保不同角色生成图片有明显外貌差异。锚点数据的总表在 `step3-bibles/identity_anchors.json` 和 `identity_anchors.md`（详见下方"关联文件"一节）。
- **全局前缀**：从 `art_direction.md` 第七章提取，仅含画面格式（`Cinematic still, 2.39:1 widescreen, 35mm...`），不涉及内容描述。
- **圣经原始 Prompt**：圣经第九章中各提示词的 English 代码块内容。

**核心流程**：

1. 调用 `scan_bibles()` 直接从圣经原文件中提取提示词、身份锚点，标记 phase 和参考图路径
2. 对角色类型，在 prompt 最前面拼接身份锚点
3. 对未内嵌全局前缀的提示词，拼接全局前缀
4. 按优先级排序（P0/P1 角色肖像 → P2 主要场景 → P3 配角 → P4 道具 → P5 低优先级）
5. Phase 1/3 纯文生图，Phase 2 传入基准肖像作为参考图
6. 断点续跑：输出路径已有图片时自动跳过，中途中断后重跑只会生成剩余图片；加 `--no-skip` 可关闭此行为，强制覆盖重新生成

**关键特性**：

- 三阶段：Phase 1 角色基准肖像 → Phase 2 角色参考图生图 → Phase 3 场景+道具，各阶段可独立运行
- 可复现：每个提示词的 seed 基于元素名+序号确定性计算
- 速率控制：默认 1.5s/张间隔 + 指数退避重试（最多 3 次）
- 生成日志：`generation_log.jsonl` 记录每张图的 phase、参考图路径、成功/失败等

**推荐工作流**：

```bash
# ① Phase 1: 生成角色基准肖像
python3 generate_images.py --phase 1

# ② 人工检查 _portrait/正面半身像.png，不满意则用 --no-skip 强制覆盖重新生成
python3 generate_images.py --phase 1 --element 某角色 --no-skip

# ③ 全部基准肖像 OK 后，Phase 2: 以肖像为参考图生成角色剩余图片
python3 generate_images.py --phase 2

# ④ Phase 3: 生成场景和道具（可与 Phase 1/2 并行）
python3 generate_images.py --phase 3
```

**其他用法**：

```bash
# 查看完整生成计划
python3 generate_images.py --dry-run

# 不分阶段全量生成（Phase 2 自动检测参考图）
python3 generate_images.py

# 只跑1张测试
python3 generate_images.py --phase 1 --element 吴文顶 --limit 1

# 只跑指定优先级
python3 generate_images.py --priority "P0/P1"
```

**全部参数**：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--base-dir` | 自动定位 | production 目录路径 |
| `--model` | `doubao-seedream-5-0-260128` | Seedream 模型 ID |
| `--size` | `2K` | 图片尺寸（`2K` / `4K` / `1024x1024`） |
| `--phase` | `0` (全部) | `1`=角色基准肖像, `2`=角色参考图生图, `3`=场景+道具, `0`=全部 |
| `--priority` | 全部 | 只生成指定优先级（`P0/P1` / `P2` / `P3` / `P4` / `P5`） |
| `--element` | 全部 | 只生成指定元素名 |
| `--type` | 全部 | 只生成指定类型（`characters` / `locations` / `props`） |
| `--dry-run` | false | 只输出计划，不调 API |
| `--no-skip` | false | 关闭断点续跑，即使输出路径已有图片也强制覆盖重新生成。典型用途：基准肖像不满意时配合 `--element` 重跑指定角色 |
| `--limit` | 0 (不限) | 最多生成 N 张图片 |
| `--delay` | 1.5 | API 调用间隔秒数 |
| `--ark-api-url` | `https://ark.cn-beijing.volces.com/api/v3/images/generations` | 方舟 API 地址 |

### build_index.py — 资产索引构建器

扫描 `step4-assets/` 下的实际图片文件，交叉引用圣经阶段注册表，生成下游 Step 5/6 的核心映射表。

**输入**：`production/step4-assets/` 目录 + `production/step3-bibles/` 圣经文件

**输出**：`production/step4-assets/asset_index.md`

**功能**：
- 遍历所有资产目录，统计每个 stage_id 下的图片数量
- 从圣经中提取 stage_id 对应的章节范围
- 生成 SKILL.md 规定格式的索引表（元素名、stage_id、章节范围、图片路径）
- 目录为空时也生成骨架索引（图片数=0），方便预览结构

```bash
python3 build_index.py [--base-dir /path/to/production]
```

### validate_assets.py — 资产校验器

对 Step 4 资产库进行完整性和一致性校验，输出分级报告。

**输入**：`production/step4-assets/` + `production/step3-bibles/` + `asset_index.md`

**输出**：终端校验报告（错误/警告/信息三级）

**校验项**：
- 目录 vs 圣经覆盖率：每个圣经的 stage_id 是否有对应目录
- 索引 vs 实际文件：`asset_index.md` 中的路径是否真实存在
- 图片覆盖率：每个 stage_id 目录是否至少有 1 张图片
- 角色肖像完整性：★★★★★/★★★★☆ 角色是否有完整肖像集
- 返回 exit code 0（通过）或 1（有错误），可用于 CI 集成

```bash
python3 validate_assets.py [--base-dir /path/to/production]
```

## 关联文件（production/step3-bibles/）

以下文件不在 scripts 目录中，但与图片生成流程直接相关：

### identity_anchors.json — 角色身份锚点数据

53 个角色的身份锚点（Identity Anchor）结构化数据。`extract_prompts.py` 的 `extract_identity_anchor()` 函数从各角色圣经中逐文件提取锚点，此 JSON 文件是批量生成时的参考总表。

格式：`{ "角色名": { "anchor_en": "...", "anchor_cn": "..." } }`

### identity_anchors.md — 角色区分矩阵与锚点总览

人可读的文档，包含：

1. **6 维区分矩阵**：按年龄段、体型、脸型、发型、肤色、标志性特征 6 个维度为每个角色分配唯一组合，确保任意两个角色至少在 3 个维度上不同。
2. **全部 53 个角色的身份锚点**（中英文），按主角/配角/群像分组。
3. **碰撞检查结果**：验证矩阵中无重复组合。

此文件在新增角色或修改角色外貌时应同步更新，以保持差异化约束。

### 各角色圣经中的 `### 身份锚点 / Identity Anchor`

每个角色圣经的"外貌与形态"章节（第三章）顶部都有此子节，格式：

```markdown
### 身份锚点 / Identity Anchor

> **EN:** Athletic lean man, 30-35, piercing narrow eyes...
>
> **CN:** 精干瘦长男子，三十多岁，狭长眼眸深邃如井...
```

`generate_images.py` 在生成时自动提取 EN 锚点并前置到该角色的所有 prompt 最前面，确保模型每次生图都优先理解该角色的独特外貌特征。

## 通用参数

所有脚本都接受 `--base-dir` 参数指定 `production/` 目录的路径。省略时默认相对于脚本位置自动定位到项目的 `production/` 目录。

## 典型工作流示例

```bash
cd skills/novel-to-film/step4-visual-asset-generator/scripts/

# ① 提取提示词，确认数量无误
python3 extract_prompts.py
# → 459 prompts, 0 missing

# ② 搭建目录骨架
python3 scaffold_assets.py
# → 272 directories

# ③ 先 dry-run 确认计划
python3 generate_images.py --dry-run

# ④ Phase 1: 生成角色基准肖像
python3 generate_images.py --phase 1

# ⑤ 人工审查角色基准肖像，不满意则 --no-skip 强制覆盖重新生成（无需手动删旧图）
python3 generate_images.py --phase 1 --element 某角色 --no-skip

# ⑥ Phase 2: 以基准肖像为参考图，生成角色剩余图片
python3 generate_images.py --phase 2

# ⑦ Phase 3: 生成场景和道具（可与上面并行）
python3 generate_images.py --phase 3

# ⑧ 构建索引
python3 build_index.py

# ⑨ 校验完整性
python3 validate_assets.py
```
