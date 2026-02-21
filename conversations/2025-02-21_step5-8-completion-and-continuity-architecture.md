# 2025-02-21 Session: Step5-8 SKILL.md 完成 & 连续性帧架构讨论

## 概要

本次会话（跨两个 context window）完成了三项关键工作：
1. **创建 step5-step8 的 SKILL.md**——完成了整个8步 pipeline 的 skill 定义
2. **修复角色性别字段缺失**——在 step1、step3、production 数据中补全性别信息
3. **讨论连续性帧架构优化**——发现 step6 尾帧生成过重的问题，探讨将尾帧职责移至 step7

---

## 一、Step5-Step8 SKILL.md 创建

### Step5: film-storyboard-extractor（分镜脚本提取器）

4个子步骤：
- **5a 事件预视觉化**：筛选★★★★★事件，生成概念图，事件编号 E{XX}
- **5b 场景拆分**：SC{NNN} 编号，章节→stage_id 映射表，6种场景类型及时长估算
- **5c 镜头表**：SC{NNN}-{NNN} 编号，8种景别+8种运镜+5种拆分策略+5种转场类型
- **5d 分镜脚本**：逐场景文件，每个镜头包含技术参数、元素标注（stage_id + asset_index 路径）、视觉描述、动态描述（带时间戳）、音频提示、连续性注记、关键帧构图提示
- 6套镜头模式模板（对话/追逐/揭示/超自然/情感/战斗）
- 下游 step6/7/8 数据接口规范

### Step6: keyframe-composer（关键帧合成器）

核心设计——**4层 Prompt 组装**：
1. **Layer 1 全局风格前缀**：从 art_direction.md 提取，全片不变
2. **Layer 2 镜头规格**：景别/机位中→英翻译表（8种景别 + 5种机位）
3. **Layer 3 视觉内容**：叙事翻译规则（无角色真名、冻结瞬间提取、空间层次、光照/色彩）
4. **Layer 4 负面提示**：全局 + 场景特定

其他关键设计：
- 参考图权重矩阵（按景别5档：特写角色权重0.7-0.8，全景0.2-0.3）
- 多角色参考图策略（前2-3角色给参考图，其余仅 prompt 描述）
- 角色 Prompt 模板系统（每角色每阶段固定英文基础描述，跨镜头复用）
- 连续性规划：首→尾帧生成流程，正反打180度法则
- 6级再生策略，prompt 记录文件确保可溯源
- 输出：`production/step6-keyframes/{SC{NNN}}/{镜号}_first.png` + `_last.png` + `_prompt.md` + `keyframe_index.md`

### Step7: video-generator（视频生成器）

核心设计——**3部分运动 Prompt**：
1. **Camera motion**：运镜中→英翻译表（10种运镜 + 速度修饰符）
2. **Subject motion**：动词前置、速度/力度显式、无真名、带连接词分阶段、包含环境运动
3. **Mood & style**：音效 + 氛围

其他关键设计：
- Seedance 3种模式 + 决策树：First Frame（独立镜头）/ First-Last Frame（连续性对）/ Full Reference（角色一致性）
- 运动复杂度分级（5级，从低>80%成功率到高<20%）
- 4种降级策略：简化运动、拆分镜头、静态替代、后期补偿
- 7级再生策略，最多5次尝试
- 连续性生成排序 + 正反打空间一致性
- 输出：`production/step7-clips/{SC{NNN}}/{镜号}.mp4` + `_motion.md` + `clip_index.md`（含质量评级 A/B/C + 降级标记）

### Step8: post-production（后期制作）

5步工作流：Assembly Cut → Fine Cut → Sound Design → Color Grading → Final Review

关键设计：
- **精剪**：7种叙事类型的剪辑节奏矩阵、8种转场设计表、降级补偿表（4种 step7 策略→具体后期方法）、C 级片段补救
- **声音设计**：4轨音频（Dialogue > SFX > Music > Ambience），超自然声效设计指南（灵魂=低频嗡鸣+高泛音、附身=频率扫描+静默、灵魂出窍=混响拉伸等），混音优先级与 Ducking 策略
- **调色**：全局 LUT（来自 Art Direction）+ 场景情绪偏移表（7种情绪→具体调整）
- **输出参数**：1920×816 或 1920×1080, 24fps, H.264/H.265, 15-25Mbps
- Edit Decision List 格式记录与分镜脚本的偏差

---

## 二、Prompt 翻译架构决策（Option A）

### 问题

step5 的分镜脚本描述是中文导演语言，不能直接作为 AI 图片/视频生成的 prompt。三个关键鸿沟：
1. **时间维度**：分镜描述是动态过程（8-15秒），但首帧需要冻结在 frame 0
2. **语言格式**：中文叙事 vs 英文关键词/结构化 prompt
3. **信息筛选**：叙事语境 vs 生成参数

### 三种方案

- **方案 A（采纳）**：step6 和 step7 各自处理 prompt 翻译——消费者侧翻译
- **方案 B**：加入 step5.5 集中翻译
- **方案 C**：step5 同时输出导演描述和 prompt-ready 版本

### 选择方案 A 的理由

- step6（图片）和 step7（视频）对 prompt 的需求完全不同
- 避免 step5.5 成为耦合瓶颈
- 每个 step 独立迭代、独立优化 prompt 策略
- step5 保持纯导演文档的定位不变

---

## 三、角色性别字段修复

### 问题

角色基础信息中缺少性别字段，导致 step6 做 prompt engineering 时无法生成准确的英文描述（如 "a Chinese man" vs "a Chinese woman"）。

### 修复范围

| 文件 | 修改内容 |
|------|---------|
| `step3 character-writing-bible SKILL.md` | 基本信息章节增加"性别"为第2个字段（原8字段→9字段） |
| `step1 SKILL.md` | 角色提取模板表增加"性别"列（原8列→9列） |
| `production/step1-extraction/characters.md` 主角 | 朱围庸(男)、吴文顶(男)、宋小仙(男) |
| `production/step1-extraction/characters.md` 配角 | 人类按实际性别标注；神兽标注"雄性（神兽）" |
| `production/step1-extraction/characters.md` 群像 | 人类按性别标注；灵魂体标注"无（灵魂体）"；神灵体标注"无（神灵体）"；人造体标注"男（人造体）"；群像角色标注"混合" |

---

## 四、连续性帧架构讨论（待决策）

### 当前设计的问题

step6 承担双重职责：
1. 为每个镜头生成首帧（必要）
2. 为连续性镜头"想象"尾帧（本质是预测视频结果）

问题：step6 用图片生成去猜"镜头结束时画面是什么样"，但 step7 实际生成的视频末尾未必匹配，导致工作量翻倍且连续性保障是虚的。

### 用户提议

对于连续性镜头，直接使用 step7 视频的实际尾帧作为下一个镜头的首帧，而非 step6 预生成的想象尾帧。

### 两种实现方式

**方式 A（推荐）：step6 只管锚点帧，step7 内部自带反馈循环**

```
step6 输出：
  ├── SC001-001_first.png  ← 连续性链 A 的锚点（第一帧）
  ├── SC001-005_first.png  ← 独立镜头
  ├── SC001-008_first.png  ← 连续性链 B 的锚点
  └── ...

step7 执行（以连续性链 A 为例）：
  SC001-001: 用 step6 首帧 → 生成视频 → 提取尾帧
  SC001-002: 用上一个尾帧作首帧 → 生成视频 → 提取尾帧
  SC001-003: 用上一个尾帧作首帧 → 生成视频 → 提取尾帧
  SC001-004: 用上一个尾帧作首帧 → 生成视频（链条结束）
```

优势：step6 工作量减少 40-60%，连续性基于真实视频画面，逻辑内聚在 step7。

**方式 B：step6 全量生成首帧作为 fallback，step7 实际尾帧覆盖**

step6 为所有镜头生成首帧，但连续性链内部的首帧只作为 fallback。step7 生成视频后用实际尾帧替代。

优势：有兜底，但会浪费大量 step6 的生成资源。

### 风险与对策

如果连续性链中某个视频质量很差（C 级），其尾帧会污染后续所有镜头。对策：step7 再生策略中加入"链条中断处理"——质量低于阈值时回退到 step6 重新生成锚点帧，断开污染链。

### 状态：✅ 已决策——采用方式 A

---

## 五、连续性帧架构实施（方式 A）

用户决策采用方式 A 后，对 step6 和 step7 的 SKILL.md 进行了全面重构。

### step6 变更要点

1. **描述更新**：从"规划镜头间连续性（首帧/尾帧对）"改为"识别连续性链并仅为链头和独立镜头生成首帧"
2. **核心原则第4条**：从"连续性提前规划（首帧+尾帧）"改为"锚点帧思维"
3. **输出结构**：移除 `_last.png`，明确 step6 仅生成锚点帧（链头+独立+正反打），链内镜头无首帧文件
4. **连续性规划**：完全重写为"锚点帧模式"，定义三类镜头（链头锚点/链内/独立锚点）
5. **正反打处理**：明确正反打不属于连续性链（各镜头独立生成，但保持空间一致性）
6. **新增 step7 链条中断回退机制**：当 step7 请求时，step6 为中断点后的镜头应急生成新锚点帧
7. **keyframe_index.md 重构**：新增连续性链清单表、帧类型字段（独立锚点/链头锚点/step7提供/正反打锚点/中断回退锚点）
8. **工作流程**：第三步增加"链内镜头跳过"逻辑，第四步改为正反打空间一致性验证
9. **常见错误**：将"连续性镜头对逐个独立生成"替换为"为链内镜头生成了首帧"
10. **质量标准**：从"全面覆盖所有镜头"改为"锚点帧完整覆盖+链内镜头正确跳过"

### step7 变更要点

1. **描述更新**：增加反馈循环和链条中断处理的说明
2. **核心挑战**：从3个增加到4个，新增"连续性反馈循环"和"链条中断"
3. **输入**：从"首帧/尾帧图集"改为"锚点帧图集"，新增"首帧来源规则"（3种来源）
4. **输出**：新增 `{镜号}_tail.png`（从视频末帧提取的尾帧）
5. **生成模式**：从3种模式（含 First-Last Frame）简化为2种核心模式（First Frame + Full Reference），去掉 First-Last Frame
6. **新增"连续性反馈循环"章节**：详细描述尾帧提取→传递→下一镜头首帧的完整流程
7. **新增"链条中断处理"章节**：定义中断阈值（角色一致性C/画面稳定性C）、4步中断流程、示例、step8处理建议
8. **工作流程第三步**：增加首帧来源确定（步骤1）和尾帧提取+中断判断（步骤14）
9. **clip_index.md 重构**：新增"首帧来源""连续性"列、链条中断记录表（含 step8 建议转场）
10. **再生策略**：新增 L8 链条中断策略
11. **下游数据接口**：增加链条中断记录的传递，step8 加载流程增加中断点转场处理
12. **常见错误**：新增3条（链内C级未触发中断、中断后未请求新锚点帧、提取尾帧时做了后处理）

---

## 六、修改文件清单

| 文件 | 操作 |
|------|------|
| `skills/novel-to-film/step5-film-storyboard-extractor/SKILL.md` | 创建 |
| `skills/novel-to-film/step6-keyframe-composer/SKILL.md` | 创建 → 后重构（锚点帧模式） |
| `skills/novel-to-film/step7-video-generator/SKILL.md` | 创建 → 后重构（反馈循环+链条中断） |
| `skills/novel-to-film/step8-post-production/SKILL.md` | 创建 |
| `skills/novel-to-film/SKILL.md` | 更新（step5-8 标记 ✅） |
| `skills/novel-to-film/step1-film-elements-extractor/SKILL.md` | 更新（增加性别列） |
| `skills/novel-to-film/step3-element-writing-bible/character-writing-bible/SKILL.md` | 更新（增加性别字段） |
| `production/step1-extraction/characters.md` | 更新（三个分区全部增加性别列） |

## 七、待办事项

- [x] 用户决策连续性帧架构 → 采用方式 A
- [x] 根据决策更新 step6 SKILL.md（锚点帧模式）
- [x] 根据决策更新 step7 SKILL.md（反馈循环+链条中断）
- [x] location-writing-bible SKILL.md → 已确认完成
- [x] prop-writing-bible SKILL.md → 已确认完成
- [x] step3 umbrella SKILL.md → 用户明确暂不需要，跳过

## 八、当前项目总状态

### SKILL.md 体系（全部完成 ✅）

| 步骤 | SKILL.md | 状态 |
|------|----------|------|
| 总入口 | `skills/novel-to-film/SKILL.md` | ✅ |
| Step1 元素提取 | `step1-film-elements-extractor/SKILL.md` | ✅ |
| Step2 美术方向 | `step2-art-direction/SKILL.md` | ✅ |
| Step3 角色圣经 | `step3-element-writing-bible/character-writing-bible/SKILL.md` | ✅ |
| Step3 场景圣经 | `step3-element-writing-bible/location-writing-bible/SKILL.md` | ✅ |
| Step3 道具圣经 | `step3-element-writing-bible/prop-writing-bible/SKILL.md` | ✅ |
| Step4 视觉资产生成 | `step4-visual-asset-generator/SKILL.md` | ✅ |
| Step5 分镜脚本 | `step5-film-storyboard-extractor/SKILL.md` | ✅ |
| Step6 关键帧合成 | `step6-keyframe-composer/SKILL.md` | ✅（锚点帧模式） |
| Step7 视频生成 | `step7-video-generator/SKILL.md` | ✅（反馈循环+链条中断） |
| Step8 后期制作 | `step8-post-production/SKILL.md` | ✅ |

### 制作产出（Production）

| 步骤 | 状态 | 说明 |
|------|------|------|
| Step1 元素提取 | ✅ 完成 | 7个文档（characters/locations/props/events/world_settings/timeline/coverage_report） |
| Step2 美术方向 | ✅ 完成 | 光影设计 + 色彩脚本 |
| Step3 圣经 | ✅ 完成 | 3主角 + 9配角 + 18场景 + 6道具 = 38份圣经文档 |
| Step4 视觉资产 | ⏳ 待执行 | 目录已建，等待 Seedream 生成 |
| Step5 分镜脚本 | ⏳ 待执行 | 目录已建 |
| Step6 关键帧 | ⏳ 待执行 | 目录已建 |
| Step7 视频 | ⏳ 待执行 | 目录已建 |
| Step8 后期 | ⏳ 待执行 | 目录已建 |
