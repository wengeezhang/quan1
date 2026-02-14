---
name: novel-to-film
description: 将小说转化为可视化影视作品的端到端制作流程。从原始小说文本出发，经过元素提取、Art Direction、圣经编写、视觉资产生成、场次分解与分镜、首帧合成、视频生成、剪辑后期八个阶段，最终产出可直接用于AI视频生成（Seedream/Seedance）或传统影视制作的全套资料与成片。
---

# 小说转影视可视化制作

## 目标

依赖 AI 将一部完整的小说自动化制作成世界级别的电影。

最终产出不是文学分析，也不仅是制作资料——而是**可观看的视频成片**。整个流程参考好莱坞大片的制作规范（前期开发 → 概念设计 → 分镜 → 拍摄/生成 → 后期），同时适配当前 AI 能力的限制与优势（Seedream 图片生成、Seedance 2.0 视频生成，单次 8-15s 上限）。

## 整体流程

```
原始小说 (chapters/)
       │
       ▼
┌──────────────────────────────┐
│  阶段1：元素提取               │  step1-film-elements-extractor/
│  从小说中提取所有视觉元素       │
│  产出：元素清单                 │  → production/step1-extraction/
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  阶段2：Art Direction          │  step2-art-direction/
│  定义全局视觉风格基调          │
│  产出：全局视觉风格定义         │  → production/step2-art-direction/
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  阶段3：圣经编写               │  step3-element-writing-bible/
│  为每个重要元素编写制作圣经      │
│  产出：角色/场景/道具圣经       │  → production/step3-bibles/
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  阶段4：视觉资产生成            │  step4-visual-asset-generator/
│  用 Seedream 生成参考图并确认   │
│  产出：角色肖像、场景图、道具图  │  → production/step4-assets/
└──────────┬───────────────────┘
           │  ↑ 一致性验证循环
           │
           ▼
┌──────────────────────────────┐
│  阶段5：场次分解与分镜          │  step5-film-storyboard-extractor/
│  小说→场次表→镜头表→分镜脚本   │
│  产出：场次表 + 分镜脚本        │  → production/step5-storyboard/
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  阶段6：首帧合成               │  step6-keyframe-composer/
│  为每个镜头合成首帧/尾帧图      │
│  产出：镜头首帧图集             │  → production/step6-keyframes/
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  阶段7：视频生成               │  step7-video-generator/
│  首帧+参考图+prompt→8-15s片段  │
│  产出：视频片段                 │  → production/step7-clips/
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│  阶段8：剪辑与后期             │  step8-post-production/
│  片段拼接、转场、音频、调色     │
│  产出：最终成片                 │  → production/step8-final/
└──────────────────────────────┘
```

## 阶段说明

### 阶段1：元素提取

**技能**：`step1-film-elements-extractor/SKILL.md` ✅

从原始小说中提取所有影视可视化制作所需的核心元素，生成结构化清单。以"能否被画出来、拍出来"为筛选标准。

**输入**：`chapters/` 下的全部小说章节
**产出**：`production/step1-extraction/` 下的元素清单（角色、场景、道具、事件、世界观、时间线）

### 阶段2：Art Direction（全局视觉风格定义）

**技能**：`step2-art-direction/SKILL.md` ✅

在编写任何元素圣经之前，先确定整部影片的**全局视觉风格基调**。这是好莱坞制作中 Look Development / Art Direction 阶段的对应——定义统领全片的视觉语言，确保后续所有元素（角色、场景、道具）在风格上统一。

**工作内容**：
- **整体风格定位**：写实 / 半写实 / 风格化 / 动画风？确定基本视觉路线
- **色彩体系**：全片的主色调、辅助色、禁用色；不同情绪段落的色彩倾向
- **光影风格**：自然光 / 戏剧光 / 高对比 / 柔光？不同场景类型的光影规范
- **时代质感**：影片所处时代的视觉特征（建筑、服饰、器物的年代感）
- **画面构图偏好**：宽银幕比例、对称/非对称构图、景深偏好
- **全局 style prompt 前缀**：提炼一段标准化的风格描述，作为后续所有 Seedream 生成时的 prompt 前缀，保证画风一致

**输入**：阶段1的元素清单 + 原始小说章节（整体氛围判断）
**产出**：`production/step2-art-direction/` 下的全局视觉风格定义文件

### 阶段3：圣经编写

**技能**：`step3-element-writing-bible/SKILL.md`（待编写）

在全局视觉风格的约束下，为阶段1提取出的每个重要元素（★★★★★ 和 ★★★★☆），编写详细的制作圣经。不同类型的元素使用不同的子技能：

| 元素类型 | 技能 | 产出位置 | 状态 |
|---------|------|---------|------|
| 角色 | `step3-.../character-writing-bible/SKILL.md` | `production/step3-bibles/characters/` | ✅ 已完成 |
| 场景/地点 | `step3-.../location-writing-bible/SKILL.md` | `production/step3-bibles/locations/` | 🔲 计划中 |
| 道具 | `step3-.../prop-writing-bible/SKILL.md` | `production/step3-bibles/props/` | 🔲 计划中 |
| 世界观 | `step3-.../world-writing-bible/SKILL.md` | `production/step3-bibles/world/` | 🔲 计划中 |
| 关键事件 | `step3-.../event-writing-bible/SKILL.md` | `production/step3-bibles/events/` | 🔲 计划中 |

**关键约束**：每个元素圣经中的视觉描述和 AI 绘图提示词，必须符合阶段2定义的全局视觉风格。圣经中的 AI 提示词应自动继承全局 style prompt 前缀。

**输入**：阶段1的元素清单 + 原始小说章节 + 阶段2的全局视觉风格定义
**产出**：`production/step3-bibles/` 下的各类圣经文件

### 阶段4：视觉资产生成

**技能**：`step4-visual-asset-generator/SKILL.md`（待编写）

将阶段3圣经中的 AI 绘图提示词，通过 Seedream 实际执行生成图片，经人工筛选确认后形成**视觉资产库**。这是连接"文字描述"与"可用画面"的关键桥梁——没有这一步，后续的首帧合成和视频生成无从谈起。

**工作内容**：
- 用圣经中的肖像提示词生成角色多角度参考图（正面/侧面/3/4），建立角色视觉基线
- 用场景提示词生成场景概念图（不同时段、不同氛围）
- 用道具提示词生成道具设计图
- 对生成结果进行**一致性筛选**：确保同一角色在不同图片中外貌一致
- 将确认后的图片编入资产库，建立资产索引（角色名→图片路径、场景名→图片路径）

**AI工具**：Seedream（图片生成），Seedream 4.0+ 的角色一致性融合功能
**输入**：阶段3的圣经文件（含 AI 提示词）+ 阶段2的全局视觉风格定义
**产出**：`production/step4-assets/` 下的视觉资产库（图片文件 + 资产索引）

### 阶段5：场次分解与分镜

**技能**：`step5-film-storyboard-extractor/SKILL.md`（待编写）

将小说转化为可拍摄/可生成的分镜脚本。参考好莱坞标准流程，分三个子步骤：

**5a. 场次分解（Scene Breakdown）**
将小说按叙事段落拆分为独立的"场次"，每个场次对应一个连续的时空单元。这决定了整部影片的结构骨架。

每个场次须标注：场次编号、对应章节/段落、地点、时间（日/夜）、出场角色、情绪基调、预估时长。

**5b. 镜头设计（Shot List）**
为每个场次设计具体的镜头序列。每个镜头须标注：镜号、景别（远/中/近/特写）、机位角度、运镜方式（推/拉/摇/固定）、画面内容描述、时长（适配 Seedance 2.0 的 8-15s 限制）。

**关键约束**：单个镜头时长不超过 15s（Seedance 2.0 上限），理想时长 8-10s。超过 15s 的连续动作须拆分为多个镜头，并设计衔接点。

**5c. 分镜脚本（Storyboard）**
为每个镜头撰写详细的分镜描述，包含画面构图、角色动作、表情、光影氛围、音效提示。分镜描述须引用阶段3圣经和阶段4资产库中的具体角色/场景定义。

**输入**：原始小说章节 + `production/step3-bibles/` 下的圣经文件 + `production/step4-assets/` 下的视觉资产索引
**产出**：`production/step5-storyboard/` 下的场次表 + 镜头表 + 分镜脚本

### 阶段6：首帧合成

**技能**：`step6-keyframe-composer/SKILL.md`（待编写）

为每个镜头生成"首帧图"（keyframe），作为 Seedance 2.0 image-to-video 的起点。这是当前 AI 视频生成中保证角色一致性和画面质量的最关键一步。

**工作内容**：
- 根据分镜脚本中每个镜头的画面描述，从视觉资产库中调取对应的角色参考图、场景参考图
- 使用 Seedream 结合参考图 + 镜头描述，生成该镜头的首帧图
- 首帧图须满足：角色外貌与资产库一致、构图匹配分镜设计、光影氛围符合场次情绪
- **连续性规划**：需要提前判断相邻镜头之间是否需要画面连续（如同一动作的多镜头拆分、正反打对话等）。对于需要连续衔接的镜头，必须同时规划并生成首帧和尾帧——前一个镜头的尾帧与后一个镜头的首帧保持画面衔接，以此保证连续性（利用 Seedance 2.0 的 First/Last Frame 模式）。对于不需要连续的独立镜头（如场次切换、跳切），只需生成首帧即可

**AI工具**：Seedream（图片生成/合成），参考图一致性模式
**输入**：阶段5的分镜脚本 + `production/step4-assets/` 下的视觉资产库
**产出**：`production/step6-keyframes/` 下的镜头首帧图集（每个镜头对应一张或两张图）

### 阶段7：视频生成

**技能**：`step7-video-generator/SKILL.md`（待编写）

将每个镜头的首帧图 + 运动提示词 + 参考图，输入 Seedance 2.0 生成 8-15s 的视频片段。

**工作内容**：
- 为每个镜头组装多模态输入包：
  - **首帧图**（来自阶段6）——定义画面起点
  - **参考图**（来自阶段4资产库）——约束角色/场景一致性
  - **运动提示词**（text prompt）——描述镜头内的动作、运镜、情绪变化
  - **音频提示**（可选）——Seedance 2.0 支持同步音频生成
- 执行生成，对结果进行质量和一致性检查
- 不合格的片段标记问题并重新生成

**AI工具**：Seedance 2.0（视频生成），支持 First/Last Frame 模式和 Full Reference 模式
**输入**：阶段6的首帧图 + 阶段4的资产库 + 阶段5的分镜脚本
**产出**：`production/step7-clips/` 下的视频片段（每个镜头一个 8-15s 的视频文件）

### 阶段8：剪辑与后期

**技能**：`step8-post-production/SKILL.md`（待编写）

将所有视频片段按分镜脚本的顺序拼接成完整影片，并完成后期处理。

**工作内容**：
- **片段拼接**：按场次和镜头顺序组装视频片段
- **转场设计**：场次间的转场（淡入淡出、硬切、叠化等）
- **节奏控制**：调整片段时长、剪辑节奏，确保叙事流畅
- **音频处理**：对白、配乐、环境音、音效的整合与混音（Seedance 2.0 可同步生成部分音频，但对白和配乐可能需要额外处理）
- **调色**：全片色彩一致性校正，确保符合全局视觉风格定义
- **字幕/标题**（如需要）

**工具**：剪辑软件（CapCut/DaVinci Resolve 等）
**输入**：`production/step7-clips/` 下的全部视频片段 + 分镜脚本（作为剪辑蓝图）+ 全局视觉风格定义
**产出**：`production/step8-final/` 下的最终成片

---

## 技能目录结构

```
skills/novel-to-film/
├── SKILL.md                                    # 本文件：整体流程描述
├── references.md                               # 参考资料链接
│
├── step1-film-elements-extractor/              # 阶段1：元素提取
│   └── SKILL.md                                # ✅
│
├── step2-art-direction/                        # 阶段2：全局视觉风格定义
│   └── SKILL.md                                # ✅
│
├── step3-element-writing-bible/                # 阶段3：圣经编写
│   ├── character-writing-bible/                # 角色圣经 ✅
│   │   └── SKILL.md
│   ├── location-writing-bible/                 # 场景圣经（planned）
│   │   └── SKILL.md
│   ├── prop-writing-bible/                     # 道具圣经（planned）
│   │   └── SKILL.md
│   ├── world-writing-bible/                    # 世界观圣经（planned）
│   │   └── SKILL.md
│   └── event-writing-bible/                    # 关键事件视觉圣经（planned）
│       └── SKILL.md
│
├── step4-visual-asset-generator/               # 阶段4：视觉资产生成（planned）
│   └── SKILL.md
│
├── step5-film-storyboard-extractor/            # 阶段5：场次分解与分镜
│   └── SKILL.md                                # （待编写）
│
├── step6-keyframe-composer/                    # 阶段6：首帧合成（planned）
│   └── SKILL.md
│
├── step7-video-generator/                      # 阶段7：视频生成
│   └── SKILL.md                                # （待编写）
│
└── step8-post-production/                      # 阶段8：剪辑与后期（planned）
    └── SKILL.md
```

## 产出文件结构

所有阶段的产出统一存放在 `production/` 根目录下，以 `step{N}-` 前缀对应各阶段：

```
production/
├── step1-extraction/              # 阶段1产出：元素清单
│   ├── characters.md
│   ├── locations.md
│   ├── props.md
│   ├── events.md
│   ├── world_settings.md
│   ├── timeline.md
│   └── coverage_report.md
│
├── step2-art-direction/           # 阶段2产出：全局视觉风格定义
│   └── art_direction.md
│
├── step3-bibles/                  # 阶段3产出：各类元素圣经
│   ├── characters/                # 角色圣经
│   │   ├── 主角/
│   │   ├── 配角/
│   │   └── 群像/
│   ├── locations/                 # 场景圣经
│   ├── props/                     # 道具圣经
│   ├── world/                     # 世界观圣经
│   └── events/                    # 关键事件视觉圣经
│
├── step4-assets/                  # 阶段4产出：视觉资产库
│   ├── characters/                # 角色参考图（多角度）
│   ├── locations/                 # 场景概念图
│   ├── props/                     # 道具设计图
│   └── asset_index.md             # 资产索引（元素名→图片路径）
│
├── step5-storyboard/              # 阶段5产出：场次表 + 分镜脚本
│   ├── scene_breakdown.md         # 场次分解表
│   ├── shot_list.md               # 镜头表
│   └── storyboard/                # 分镜脚本（按场次分文件）
│
├── step6-keyframes/               # 阶段6产出：镜头首帧图
│
├── step7-clips/                   # 阶段7产出：视频片段
│
└── step8-final/                   # 阶段8产出：最终成片
```

## 核心原则

1. **视觉导向**——整个流程的最终目标是产出可观看的视频成片，每一步的产出都应以"能否被画出来、拍出来、生成出来"为标准
2. **风格先行**——必须先完成阶段2（全局视觉风格定义），才能开始阶段3（编写各元素圣经）。全局风格统领一切视觉产出
3. **先全局后局部**——必须先完成阶段1（全局元素提取），才能开始阶段2/3；阶段3须在全局风格约束下编写各元素圣经
4. **上游决定下游**——每个阶段的产出是下一阶段的输入，上游质量直接决定下游质量
5. **一致性是生命线**——角色在第 1 个镜头和第 100 个镜头中必须长得一样。一致性通过三重机制保障：圣经文字约束（阶段3）→ 视觉资产库锁定（阶段4）→ 参考图注入生成（阶段6/7）
6. **适配 AI 限制**——单镜头时长 ≤15s（Seedance 2.0 上限），理想 8-10s；超长动作须在阶段5拆分为多镜头并设计衔接点
7. **阶段可独立执行**——虽然有顺序依赖，但每个阶段的技能文件包含完整的输入/输出定义和工作流程，可以独立阅读和执行

## AI 工具链

| 阶段 | 工具 | 用途 |
|------|------|------|
| 阶段1 | Claude / LLM | 文本分析、元素提取 |
| 阶段2 | Claude / LLM | 全局视觉风格分析与定义 |
| 阶段3 | Claude / LLM | 圣经编写（在全局风格约束下） |
| 阶段4 | Seedream 4.0+ | 角色肖像、场景概念图、道具图生成；角色一致性融合 |
| 阶段5 | Claude / LLM | 场次分解、镜头设计、分镜脚本编写 |
| 阶段6 | Seedream 4.0+ | 基于参考图+镜头描述合成首帧图 |
| 阶段7 | Seedance 2.0 | First/Last Frame 模式 + Full Reference 模式生成视频片段 |
| 阶段8 | CapCut / 剪辑工具 | 片段拼接、转场、音频、调色 |
