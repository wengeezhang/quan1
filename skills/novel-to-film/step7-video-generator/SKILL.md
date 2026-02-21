---
name: video-generator
description: 将每个镜头的首帧图+参考图+运动提示词输入 Seedance 2.0 生成 8-15 秒视频片段。核心职责包括：从分镜脚本的导演动态描述翻译为 Seedance motion prompt、组装多模态输入包（首帧/尾帧+参考图+文本+音频）、选择生成模式（First Frame / First-Last Frame / Full Reference）、执行生成并验证质量与一致性。
---

# 视频生成

## 定位

视频生成是整条流水线中**从静态画面到动态影像的飞跃**。

前六个阶段的全部工作——元素提取、风格定义、圣经编写、资产生成、分镜设计、首帧合成——都是为这一步做准备。本阶段将每个镜头的首帧图"激活"为 8-15 秒的视频片段，让角色动起来、让镜头推拉摇移、让光影随时间流动。

在好莱坞制作流程中，这对应 **Principal Photography（主摄影/拍摄）** 阶段——一切准备就绪，开机拍摄。区别在于：传统流程中"拍摄"由摄影师和演员完成；AI 制作流中，"拍摄"由 Seedance 2.0 根据首帧图 + 运动提示词 + 参考图自动生成。

**本阶段的核心技术挑战有三个**：
1. **Motion Prompt 工程**——将 step5 的中文导演动态描述翻译为 Seedance 可执行的英文运动指令，这与 step6 的 Image Prompt 工程是同构但不同的翻译任务
2. **生成模式选择**——Seedance 2.0 支持多种模式（First Frame / First-Last Frame / Full Reference），每个镜头需要根据连续性需求和画面复杂度选择最合适的模式
3. **运动质量控制**——AI 生成的运动可能出现抖动、穿模、动作失真等问题，需要建立质量评估标准和重新生成策略

## 核心原则

1. **首帧是基准**——视频的画面质量上限已被 step6 的首帧锁定。本阶段的工作是"让画面正确地动起来"，而不是修正首帧中的任何问题。如果首帧有问题，必须回到 step6 修正，不可在本阶段尝试弥补
2. **运动克制**——AI 视频生成对大幅度、快速、复杂的运动容易失控。宁可让动作比分镜描述稍慢、稍小，也不要让画面崩溃。如有需要，可在 step8 后期通过加速或剪辑节奏调整来弥补
3. **prompt 是桥梁**——与 step6 相同，本阶段需要将 step5 的导演意图翻译为 AI 工具的技术语言，但翻译目标从"静态画面"变为"运动过程"
4. **模式匹配场景**——不同类型的镜头适合不同的 Seedance 生成模式。选错模式会导致运动质量大幅下降
5. **一致性仍是生命线**——视频片段中的角色面貌必须与首帧一致，不能在运动过程中"变脸"。参考图注入是防止变脸的关键手段

## 输入

- `production/step6-keyframes/`——首帧/尾帧图集
  - `{场次}/{镜号}_first.png`——每个镜头的首帧图
  - `{场次}/{镜号}_last.png`——连续性镜头的尾帧图（如有）
  - `keyframe_index.md`——首帧索引（镜号→路径→连续性关系）
- `production/step5-storyboard/storyboard/{SC{NNN}}.md`——分镜脚本（动态描述、运镜方式、音效提示、时长）
- `production/step5-storyboard/shot_list.md`——镜头表（运镜方式、时长的快速总览）
- `production/step4-assets/asset_index.md`——资产索引（参考图路径）
- `production/step4-assets/`——视觉资产库（角色肖像、阶段参考图）
- `production/step2-art-direction/art_direction.md`——全局视觉风格定义

**研究方法**：
1. 先读 `keyframe_index.md`，明确总镜头数、连续性镜头对
2. 读 `shot_list.md`，总览全部镜头的运镜和时长
3. 按场次顺序读取分镜脚本，逐镜头执行 motion prompt 翻译和生成

## 输出

`production/step7-clips/` 下的视频片段和生成日志：

```
production/step7-clips/
├── SC001/
│   ├── SC001-001.mp4                # 视频片段（8-15s）
│   ├── SC001-001_motion.md          # 该镜头的完整 motion prompt 记录
│   ├── SC001-002.mp4
│   ├── SC001-002_motion.md
│   └── ...
├── SC002/
│   └── ...
├── ...
├── clip_index.md                    # 视频片段索引（镜号 → 文件路径 → 时长 → 质量评级）
└── generation_log.md                # 生成日志（参数、尝试次数、调整记录）
```

**文件命名规则**：
- 视频片段：`{镜号}.mp4`
- Motion prompt 记录：`{镜号}_motion.md`
- 按场次分子目录，目录名 = 场次编号

---

## Seedance 2.0 生成模式

### 三种模式及其适用场景

| 模式 | 输入 | 输出 | 适用场景 |
|------|------|------|---------|
| **First Frame** | 首帧图 + text prompt | 视频片段 | 独立镜头（无连续性需求）、场次开头镜头 |
| **First-Last Frame** | 首帧图 + 尾帧图 + text prompt | 视频片段 | 连续性镜头对（动作衔接、多镜头拆分） |
| **Full Reference** | 首帧图 + 参考图 + text prompt | 视频片段 | 角色一致性要求极高的镜头（角色特写、近景对话） |

### 模式选择决策树

```
该镜头是否有连续性需求？（查 keyframe_index.md）
  │
  ├── 是 → 有尾帧图吗？
  │         ├── 是 → First-Last Frame 模式
  │         └── 否 → 错误！回到 step6 补生成尾帧
  │
  └── 否 → 该镜头是否有角色特写/近景？
              ├── 是 → Full Reference 模式（注入角色肖像锚点）
              └── 否 → First Frame 模式（最通用）
```

### 模式组合策略

实际使用中，三种模式可以组合：

- **First-Last Frame + Full Reference**：连续性镜头 + 角色一致性双重保障。适用于：正反打对话（需要衔接 + 角色面部一致）
- **First Frame + Full Reference**：独立镜头但有角色。这是最常用的组合——大多数包含角色的镜头都应使用

---

## Motion Prompt 工程：从导演动态描述到运动指令

### 与 step6 Image Prompt 工程的区别

| 维度 | step6 Image Prompt | step7 Motion Prompt |
|------|-------------------|-------------------|
| 描述对象 | 静止画面（第 0 秒） | 运动过程（0-Ns） |
| 核心内容 | 构图、光影、色彩、空间 | 动作、运镜、速度、节奏 |
| 来源段落 | step5"画面描述" | step5"动态描述"+"运镜方式" |
| 输出语言 | 英文，名词/形容词为主 | 英文，动词/副词为主 |
| 时间轴 | 无（冻结时刻） | 有（按秒描述变化） |

### Motion Prompt 结构

每个镜头的 motion prompt 由三个部分组成：

#### 部分一：镜头运动（Camera Motion）

来源：step5 镜头表的"运镜方式"字段。

将 step5 的中文运镜术语翻译为 Seedance 识别的英文指令：

| step5 中文 | Motion Prompt | 补充参数 |
|-----------|--------------|---------|
| 固定 | `static camera, locked shot` | — |
| 推（Dolly In） | `camera slowly dollies in` | `slow` / `steady` |
| 拉（Dolly Out） | `camera slowly dollies out` | `slow` / `revealing` |
| 摇（Pan） | `camera pans [left/right]` | `smooth pan` |
| 跟（Tracking） | `camera tracks the character, following movement` | `steady tracking` |
| 升（Crane Up） | `camera cranes up, rising` | `smooth crane` |
| 降（Crane Down） | `camera descends, craning down` | `smooth descent` |
| 环绕（Orbit） | `camera slowly orbits around the subject` | `360 orbit` / `partial orbit` |
| 手持 | `handheld camera, slight shake` | `documentary style` |
| 变焦推 | `camera zooms in` | `slow zoom` |
| 变焦拉 | `camera zooms out` | `slow zoom out` |

**运镜速度关键词**：
- 慢速：`slowly`, `gently`, `gradually`
- 中速：`steadily`, `smoothly`
- 快速：`quickly`, `rapidly`, `swiftly`（慎用——快速运镜容易导致画面撕裂）

#### 部分二：主体运动（Subject Motion）

来源：step5 分镜脚本的"动态描述"段落。

将角色/道具/环境的中文动作描述翻译为英文运动指令：

**翻译规则**：

1. **动词优先**——Motion prompt 的核心是动词，不是名词。`the man walks` 比 `a walking man` 更有效
2. **速度和力度要明确**——`slowly raises his hand` vs `quickly raises his hand` 会产生完全不同的运动
3. **角色不用真名**——与 step6 一致，使用通用描述（`the man`, `the woman`, `the figure`）
4. **分阶段描述**——与 step5 动态描述的时间轴对应，用 `then` / `after that` / `gradually` 等连接词串联
5. **环境运动也要描述**——风吹树叶、水面波纹、火焰跳动，这些环境动态对画面生动感至关重要

**翻译示例**：

```
step5 动态描述（中文）:
  0-3s: 朱围庸一动不动站在码头边，海风持续吹动衣衫
  3-7s: 他缓缓抬起右手，从怀中取出一个小瓷瓶，举到眼前端详
  7-10s: 他握紧瓷瓶，手臂缓缓放下，目光投向远处海面

      ↓ 翻译

Motion Prompt（部分二）:
  the man stands still at the dock edge, his robe gently
  fluttering in the sea breeze; then he slowly raises his
  right hand, pulling a small white porcelain bottle from
  inside his robe, holding it up to examine it closely;
  then he grips the bottle tightly, slowly lowers his arm,
  and gazes out toward the distant sea
```

#### 部分三：氛围与风格（Mood & Style）

来源：step5 分镜脚本的"音效提示"+ step2 Art Direction 的风格要素。

```
# 情绪氛围关键词
melancholic, contemplative, slow pace, somber mood

# 光影变化（如果镜头内光影有变化）
consistent golden hour lighting throughout

# 画面质感
cinematic, film grain, shallow depth of field
```

### Motion Prompt 组装

完整的 motion prompt 按以下顺序组装：

```
[部分一：镜头运动] + [部分二：主体运动] + [部分三：氛围风格]
```

**示例完整 prompt**：

```
static camera, locked shot;
the man stands still at the dock edge, his robe gently
fluttering in the sea breeze, then he slowly raises his
right hand pulling a small white porcelain bottle from
inside his robe, holding it up to examine it, then grips
the bottle tightly and slowly lowers his arm gazing toward
the distant sea;
melancholic contemplative mood, consistent golden hour
lighting, cinematic, subtle film grain
```

### Motion Prompt 记录文件格式

每个镜头生成一份 `{镜号}_motion.md`：

```markdown
# Motion Record: {镜号}

## 来源

- 分镜脚本：storyboard/{SC{NNN}}.md → 镜头 {镜号}
- 首帧图：step6-keyframes/{场次}/{镜号}_first.png
- 尾帧图：{路径 或 无}

## 生成模式

{First Frame / First-Last Frame / Full Reference}

## Motion Prompt

\```
{部分一 + 部分二 + 部分三 的完整组装}
\```

## 参考图

| 用途 | 文件路径 | 说明 |
|------|---------|------|
| 首帧 | step6-keyframes/{场次}/{镜号}_first.png | 视频起点 |
| 尾帧 | step6-keyframes/{场次}/{镜号}_last.png | 视频终点（如有） |
| 角色一致性 | characters/朱围庸/_portrait/正面半身像.png | Full Reference 锚点 |
| 角色阶段 | characters/朱围庸/占身乞丐期/*.png | Full Reference 形象参考 |

## 生成参数

| 参数 | 值 |
|------|-----|
| 时长 | {N}s |
| 分辨率 | {W}x{H} |
| Seed | {seed} |
| 生成批次 | {N} 次尝试 |
| 选中 | 第 {N} 次 |

## 质量评估

| 维度 | 评分 | 说明 |
|------|------|------|
| 运动自然度 | {A/B/C} | 动作是否流畅自然 |
| 角色一致性 | {A/B/C} | 运动过程中面貌是否保持一致 |
| 运镜执行 | {A/B/C} | 镜头运动是否与 prompt 匹配 |
| 物理合理性 | {A/B/C} | 有无穿模、漂浮、抖动 |
| 画面稳定性 | {A/B/C} | 有无闪烁、撕裂、模糊帧 |
| 首尾衔接 | {A/B/C/NA} | 与前后镜头的画面连续性 |
```

---

## 运动复杂度控制

### Seedance 2.0 的运动能力边界

AI 视频生成对不同复杂度的运动有不同的成功率：

| 运动复杂度 | 成功率 | 示例 | 策略 |
|-----------|--------|------|------|
| 低 | 高（>80%） | 静态画面+环境微动（风吹、水波）、角色微表情变化、缓慢运镜 | 直接生成 |
| 中低 | 较高（60-80%） | 角色行走、缓慢转身、简单手势、平稳推拉镜头 | 直接生成，可能需 2-3 次尝试 |
| 中 | 中等（40-60%） | 角色跑步、物体交互（拿取/放下）、快速运镜 | 降低动作幅度，简化描述 |
| 中高 | 较低（20-40%） | 多角色同时动作、复杂手部动作、快速追逐 | 拆分动作、减少同屏运动元素 |
| 高 | 低（<20%） | 打斗、超自然特效+角色同时运动、群体场景运动 | 必须降级处理 |

### 降级策略

当分镜脚本要求的运动复杂度超出 Seedance 能力时，采取以下降级策略：

**策略一：运动简化**
- 将复杂动作简化为核心动作（如"翻滚后起身出拳"→"出拳"）
- 减少同屏运动元素数量（如"三个人同时跑"→"主角跑，背景人物模糊"）
- 降低运动速度（`quickly` → `steadily` → `slowly`）

**策略二：镜头拆分**
- 如果一个镜头内有多个复杂动作阶段，进一步拆分为更短的片段（如 10s→5s+5s）
- 拆分后的片段各自只包含一个简单动作
- 需要回到 step6 为新增的分割点补生成首帧/尾帧
- **注意**：这会增加总镜头数和总工作量，仅在运动质量无法保障时使用

**策略三：静态替代**
- 极端情况下，将运动镜头降级为"微动态静态镜头"
- 角色保持静态姿势，仅有环境微动（风吹衣衫、光影变化、粒子飘动）
- 配合 step8 的剪辑节奏（快切+音效）弥补动态感
- 适用于：超自然特效场面、大规模群战的远景镜头

**策略四：后期弥补**
- 生成相对静态的片段，在 step8 中通过后期手段增加动态感
- 可用手段：加速播放、缩放裁切模拟推拉、叠加粒子特效、音效强化
- 适用于：运镜效果无法通过 Seedance 实现的情况

---

## 连续性生成

### 连续性镜头对的生成顺序

连续性镜头对必须按依赖关系顺序生成，不可打乱：

```
SC005-003（有后接连续性 → SC005-004）
SC005-004（有前接连续性 ← SC005-003）

生成顺序：
  1. 生成 SC005-003 视频
     - 模式: First-Last Frame
     - 首帧: SC005-003_first.png
     - 尾帧: SC005-003_last.png
     - 验证: 视频末帧是否接近尾帧图？

  2. 生成 SC005-004 视频
     - 模式: First-Last Frame 或 First Frame
     - 首帧: SC005-004_first.png（已在 step6 中基于 SC005-003 尾帧生成）
     - 验证: 视频首帧是否与 SC005-003 视频末帧衔接？
```

### 正反打对话的特殊处理

正反打序列（A→B→A→B→...）的每个镜头虽然景别和视角不同，但空间关系必须保持一致：

```
镜头1 (A视角): 拍B说话，A的肩在前景左侧
镜头2 (B视角): 拍A说话，B的肩在前景右侧
镜头3 (A视角): 拍B反应，A的肩在前景左侧（与镜头1一致）
镜头4 (B视角): 拍A反应，B的肩在前景右侧（与镜头2一致）

策略：
  - 镜头1和镜头3使用同一组参考图和相似的 prompt
  - 镜头2和镜头4使用同一组参考图和相似的 prompt
  - 人物动作和表情不同，但空间关系和光影方向保持一致
```

---

## 工作流程

### 第一步：准备工作

1. 读取 `keyframe_index.md`，建立镜头→首帧/尾帧路径的映射
2. 读取 `shot_list.md`，统计总镜头数，提取每个镜头的运镜方式和时长
3. 识别全部连续性镜头对，规划生成顺序（连续性镜头对必须按序生成）
4. 读取 `asset_index.md`，建立角色参考图查找表（供 Full Reference 模式使用）
5. 制定生成优先级

### 第二步：生成优先级规划

| 优先级 | 对象 | 说明 |
|-------|------|------|
| P0 | 连续性镜头对 | 必须按序生成，且前后验证衔接 |
| P1 | ★★★★★ 事件关键镜头 | 影片高潮，运动质量要求最高 |
| P2 | 角色特写/近景运动镜头 | 面部一致性最敏感 |
| P3 | 简单运动镜头（固定机位+微动） | 成功率高，快速推进 |
| P4 | 复杂运动镜头 | 可能需要降级处理，放到最后 |

### 第三步：逐镜头 Motion Prompt 翻译与生成

对每个镜头执行以下子流程：

```
1. 读取分镜脚本中该镜头的"动态描述"和"运镜方式"
      ↓
2. 评估运动复杂度 → 确定是否需要降级处理
      ↓
3. 翻译运镜方式 → 部分一（Camera Motion）
      ↓
4. 翻译动态描述 → 部分二（Subject Motion）
      ↓
5. 提取音效提示 + Art Direction 风格 → 部分三（Mood & Style）
      ↓
6. 组装完整 motion prompt
      ↓
7. 确定生成模式（First Frame / First-Last Frame / Full Reference）
      ↓
8. 加载首帧图（+ 尾帧图 + 参考图，视模式而定）
      ↓
9. 执行 Seedance 2.0 生成
      ↓
10. 质量评估（运动自然度、角色一致性、物理合理性、画面稳定性）
      ↓
11. 不合格 → 调整策略重新生成（见重新生成策略）
      ↓
12. 合格 → 存入 step7-clips/{场次}/{镜号}.mp4
      ↓
13. 记录 motion prompt 和生成参数 → {镜号}_motion.md
```

### 第四步：连续性验证

所有连续性镜头对生成完毕后，进行专项验证：

1. 将每对连续镜头的视频首尾相接播放
2. 检查项：
   - 画面是否自然衔接（无跳变、无突兀的位置偏移）？
   - 角色动作是否延续（前一镜头的末尾动作 → 后一镜头的开头动作）？
   - 光影方向是否一致？
   - 运动速度是否匹配（不能前一镜头慢速、后一镜头突然快速）？
3. 不合格的镜头对标记，根据问题类型决定：
   - 运动不衔接 → 重新生成后一镜头（调整 motion prompt 的开头描述）
   - 光影不一致 → 重新生成（在 prompt 中强化光影描述）
   - 角色面貌变化 → 切换到 Full Reference 模式重新生成

### 第五步：编写 clip_index.md

所有视频片段生成并确认后，编写索引文件：

```markdown
# 视频片段索引

> 本文件由阶段7（视频生成）产出。
> 阶段8（剪辑后期）通过本索引按顺序加载全部视频片段。

## 统计

| 指标 | 值 |
|------|-----|
| 总片段数 | {N} |
| 总时长 | {MM:SS} |
| 平均片段时长 | {N.N}s |
| 降级处理片段数 | {N} |
| 重新生成次数 | {N} |

## 质量分布

| 评级 | 数量 | 占比 |
|------|------|------|
| A（优秀） | {N} | {N}% |
| B（合格） | {N} | {N}% |
| C（勉强可用） | {N} | {N}% |

## 索引

| 镜号 | 文件路径 | 时长 | 生成模式 | 质量评级 | 降级 | 备注 |
|------|---------|------|---------|---------|------|------|
| SC001-001 | SC001/SC001-001.mp4 | 10s | First Frame | A | 否 | — |
| SC001-002 | SC001/SC001-002.mp4 | 8s | Full Reference | B | 否 | — |
| SC005-003 | SC005/SC005-003.mp4 | 10s | First-Last Frame | A | 否 | 后接 SC005-004 |
| SC005-004 | SC005/SC005-004.mp4 | 8s | First Frame | B | 否 | 前接 SC005-003 |
| SC042-007 | SC042/SC042-007.mp4 | 12s | First Frame | B | 是(策略一) | 原始动作过复杂，已简化 |
| ... | ... | ... | ... | ... | ... | ... |
```

### 第六步：全局质量审查

1. **角色一致性审查**：随机抽取同一角色的 10 个视频片段，检查运动过程中角色面貌是否保持一致（尤其关注快速运动时）
2. **运镜质量审查**：检查所有运镜是否与分镜设计一致（如分镜要求推镜，视频是否真的有推镜效果）
3. **连续性审查**：将全部连续性镜头对的视频首尾播放，验证衔接自然度
4. **降级片段审查**：所有标记"降级处理"的片段，审查降级后的效果是否可接受
5. **节奏预览**：按场次顺序快速播放全部片段（无转场），感受整体节奏是否合理
6. **覆盖完整性**：shot_list.md 中的每个镜头，是否都有对应的视频片段？无遗漏？

---

## 重新生成策略

当生成结果不合格时，按以下优先级调整：

| 级别 | 策略 | 适用场景 |
|------|------|---------|
| L1 | 换 seed | 运动方向大致正确但细节不理想 |
| L2 | 简化 motion prompt | 运动过于复杂导致失控——减少同时运动的元素 |
| L3 | 降低运动速度 | 快速运动导致画面撕裂/模糊——将 `quickly` 改为 `slowly` |
| L4 | 切换/组合生成模式 | 角色变脸→加 Full Reference；衔接不连续→加 First-Last Frame |
| L5 | 拆分镜头 | 多个动作阶段同时存在——拆为更短的片段各处理一个动作 |
| L6 | 静态替代 | 极端情况——降级为微动态静态镜头，后期弥补 |
| L7 | 回溯修改首帧 | 首帧构图导致运动空间不足——回到 step6 调整首帧 |

**重新生成上限**：单个镜头最多重新生成 5 次。超过 5 次仍不合格：
- 如果是运动复杂度问题 → 强制降级（策略五或策略六）
- 如果是一致性问题 → 检查参考图质量，可能需要回到 step4 或 step6
- 记录问题类型和最终解决方案，供后续相似镜头参考

---

## 与下游阶段的数据接口

### → 阶段8（剪辑后期）

本阶段为 step8 提供：

1. **视频片段**——按镜号命名的 mp4 文件，step8 按 `clip_index.md` 的顺序加载
2. **clip_index.md**——片段索引，包含每个片段的时长、质量评级、连续性关系、降级标记
3. **降级标记**——标记为"降级处理"的片段，step8 需要通过后期手段（加速、特效、音效）弥补动态感不足
4. **质量评级**——C 级片段可能需要 step8 做额外处理（如微调色彩、裁切画面、添加特效遮盖）

**step8 的加载流程**：
```
读取 clip_index.md
    → 按镜号顺序加载 mp4 文件
    → 根据 step5 shot_list.md 的"衔接方式"添加转场
    → 降级片段做后期补偿
    → 拼接为完整影片
```

---

## 常见错误（必须避免）

| 错误 | 后果 | 预防 |
|------|------|------|
| Motion prompt 过于复杂 | 运动失控，画面崩溃 | 先评估复杂度，高复杂度必须降级 |
| 未对角色特写/近景使用 Full Reference | 运动过程中角色"变脸" | 所有角色特写/近景必须注入肖像参考 |
| 连续性镜头对打乱顺序生成 | 前后视频衔接断裂 | 严格按依赖关系顺序生成 |
| 快速运动未降速 | 画面撕裂、运动模糊过重 | 宁慢勿快，后期可加速 |
| 忽略环境微动描述 | 静态背景导致画面"假"感 | prompt 中补充环境动态（风、水波、光影变化） |
| 运镜与首帧构图冲突 | 推镜时画面超出首帧可视范围 | 确认首帧构图为运镜留出足够空间 |
| 时长参数与分镜不一致 | 片段过长/过短，剪辑时对不上 | 从 shot_list.md 直接提取时长参数 |
| 多次重新生成未记录 | 后续相似镜头重复踩坑 | 每次调整记录在 generation_log.md |
| 降级片段未标记 | step8 不知道哪些片段需要后期补偿 | clip_index.md 中必须标注降级标记和策略 |
| 视频分辨率与首帧不一致 | 剪辑时画面尺寸不匹配 | Seedance 生成分辨率与首帧分辨率保持一致 |
| 正反打违反空间一致性 | 角色左右位置在镜头间跳变 | 同一对话序列的 A/B 视角使用一致的空间描述 |

## 质量标准

合格的视频片段集必须满足：

1. **全面覆盖**：shot_list.md 中的每个镜头都有对应的视频片段，无遗漏
2. **运动自然**：角色动作流畅自然，无明显抖动、穿模、漂浮
3. **角色一致**：运动过程中角色面貌保持一致，与首帧和肖像锚点匹配
4. **运镜执行**：镜头运动方式与分镜设计一致（推/拉/摇/跟/固定）
5. **物理合理**：重力、惯性、碰撞等物理效果基本合理
6. **画面稳定**：无帧间闪烁、无画面撕裂、无突然模糊
7. **连续性衔接**：所有连续性镜头对的视频首尾自然衔接
8. **时长正确**：每个片段时长在 8-15s 范围内，与分镜设计一致
9. **prompt 可追溯**：每个片段都有对应的 motion prompt 记录文件，参数完整可复现
10. **下游可用**：step8 可直接按 clip_index.md 顺序加载片段，结合 shot_list.md 的衔接方式完成剪辑
