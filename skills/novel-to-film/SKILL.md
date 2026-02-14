---
name: novel-to-film
description: 将小说转化为可视化影视作品的端到端制作流程。从原始小说文本出发，经过元素提取、圣经编写、分镜脚本、视频生成提示词四个阶段，最终产出可直接用于AI视频生成或传统影视制作的全套资料。
---

# 小说转影视可视化制作

## 目标

将一部完整的小说，转化为可以被**画出来、拍出来、生成出来**的全套影视制作资料。

最终产出不是文学分析，而是视觉制作团队（概念设计师、导演、特效、AI视频生成工具）可以直接使用的工作文件。

## 整体流程

```
原始小说 (chapters/)
       │
       ▼
┌─────────────────────────┐
│  阶段1：元素提取          │  film-elements-extractor/
│  从小说中提取所有视觉元素  │
│  产出：元素清单            │  → _extraction/
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  阶段2：圣经编写          │  film-elements-extractor/character-writing-bible/
│  为每个重要元素编写圣经    │  film-elements-extractor/location-writing-bible/ (planned)
│  产出：角色圣经、场景圣经等 │  → production/
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  阶段3：分镜脚本          │  film-storyboard-extractor/
│  基于小说和圣经制作分镜    │
│  产出：分镜脚本            │  → storyboard/ (planned)
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  阶段4：视频生成提示词     │  video-prompt-generator/
│  结合分镜和圣经生成prompt  │
│  产出：视频生成提示词       │  → video_prompts/ (planned)
└─────────────────────────┘
```

## 阶段说明

### 阶段1：元素提取

**技能**：`film-elements-extractor/SKILL.md`

从原始小说中提取所有影视可视化制作所需的核心元素，生成结构化清单。以"能否被画出来、拍出来"为筛选标准。

**输入**：`chapters/` 下的全部小说章节
**产出**：`_extraction/` 下的元素清单（角色、场景、道具、事件、世界观、时间线）

### 阶段2：圣经编写

为阶段1提取出的每个重要元素（★★★★★ 和 ★★★★☆），编写详细的制作圣经。不同类型的元素使用不同的子技能：

| 元素类型 | 技能 | 产出位置 | 状态 |
|---------|------|---------|------|
| 角色 | `character-writing-bible/SKILL.md` | `production/02_characters/` | ✅ 已完成 |
| 场景/地点 | `location-writing-bible/SKILL.md` | `production/03_locations/` | 🔲 计划中 |
| 道具 | `prop-writing-bible/SKILL.md` | `production/04_props/` | 🔲 计划中 |
| 世界观 | （待定） | `production/01_story_bible/` | 🔲 计划中 |

**输入**：阶段1的元素清单 + 原始小说章节
**产出**：`production/` 下的各类圣经文件

### 阶段3：分镜脚本

**技能**：`film-storyboard-extractor/SKILL.md`（待编写）

基于原始小说内容，结合业界标准的电影分镜头脚本规范，为每个场景/段落制作分镜头脚本。分镜需要引用阶段2产出的圣经文件来确保角色外貌、场景氛围、道具细节的一致性。

**输入**：原始小说章节 + `production/` 下的全部圣经文件
**产出**：分镜脚本文件

### 阶段4：视频生成提示词

**技能**：`video-prompt-generator/SKILL.md`（待编写）

将分镜脚本的每个镜头转化为可直接喂给AI视频生成工具的提示词。提示词需要整合分镜中的镜头信息和圣经中的视觉细节，确保生成的视频在角色外貌、场景风格、色彩基调等方面保持一致。

**输入**：分镜脚本 + `production/` 下的全部圣经文件
**产出**：视频生成提示词文件

## 目录结构

```
skills/novel-to-film/
├── SKILL.md                              # 本文件：整体流程描述
├── references.md                         # 参考资料链接
│
├── film-elements-extractor/              # 阶段1：元素提取
│   ├── SKILL.md                          # 元素提取技能
│   └── character-writing-bible/          # 阶段2：角色圣经
│       └── SKILL.md
│   （后续扩展：location-writing-bible/, prop-writing-bible/ 等）
│
├── film-storyboard-extractor/            # 阶段3：分镜脚本
│   └── SKILL.md                          # （待编写）
│
└── video-prompt-generator/               # 阶段4：视频生成提示词
    └── SKILL.md                          # （待编写）
```

产出文件的存放位置：

```
_extraction/                  # 阶段1产出：元素清单
production/                   # 阶段2产出：各类圣经
├── 01_story_bible/
├── 02_characters/
│   ├── 主角/
│   ├── 配角/
│   └── 群像/
├── 03_locations/
├── 04_props/
└── ...
storyboard/                   # 阶段3产出：分镜脚本（planned）
video_prompts/                # 阶段4产出：视频生成提示词（planned）
```

## 核心原则

1. **视觉导向**——整个流程的最终目标是产出可视化内容。每一步的产出都应以"能否被画出来、拍出来、生成出来"为标准
2. **先全局后局部**——必须先完成阶段1（全局元素提取），才能开始阶段2（逐个编写圣经）。不可跳过或并行
3. **上游决定下游**——每个阶段的产出是下一阶段的输入。上游质量直接决定下游质量
4. **一致性贯穿全程**——同一个角色在元素清单、角色圣经、分镜脚本、视频提示词中的描述必须一致
5. **阶段可独立执行**——虽然有顺序依赖，但每个阶段的技能文件包含完整的输入/输出定义和工作流程，可以独立阅读和执行
