# 对话存档：Step 4 图片生成脚本开发与 API 适配

## 日期
2026-03-04

## 核心工作

### 1. API 选型与适配
- 初始方案：火山引擎方舟 Seedream API（需付费）
- 尝试替代：调研了 MiniMax（海螺AI）、即梦（Dreamina）、阿里 Z-Image、硅基流动等
- MiniMax 适配：改写脚本适配 MiniMax image-01 API，但测试发现余额不足
- 即梦调研：发现即梦 API 本质就是火山方舟 Seedream，绕回原点
- 最终决定：回归火山方舟 Seedream API

### 2. 脚本去 SDK 化
- 问题：`volcenginesdkarkruntime` SDK 安装失败（pip 找不到包）
- 方案：改用纯 `requests` 调用 REST API（`POST https://ark.cn-beijing.volces.com/api/v3/images/generations`）
- 结果：零额外依赖，只需 Python 标准库 + requests

### 3. 模型升级
- 从 `doubao-seedream-4-0-250828` 升级到 `doubao-seedream-5-0-260128`
- 用户在火山方舟开通了新模型并本地测试通过

### 4. 新增 --limit 参数
- 支持 `--limit N` 限制单次生成图片数量
- 方便测试单张效果

### 5. 两阶段角色生成（核心改动）
- **Phase 1（文生图）**：生成角色基准肖像（正面半身像）+ 所有场景/道具，共 272 张
- **Phase 2（参考图生图）**：以基准肖像为参考图（通过 `image_urls` 传入 base64），生成角色其余图片，共 187 张
- 新增 `--phase` CLI 参数（0=全部, 1=基准+场景道具, 2=角色参考图生图）
- Phase 2 自动检测基准肖像是否存在，未就绪则跳过并警告
- 场景和道具不加参考图（阶段变化是重点，不需要身份一致性）

### 6. 连续性分析
- 用户发现生成图片连续性很好，询问原因
- 分析：seed 确定性（基于元素名哈希）+ 全局 Style Prefix + prompt 内的颜色代码和风格描述
- 没有传参考图，纯靠 prompt 工程 + seed 控制

### 7. build_index.py 说明
- 扫描 step4-assets/ 实际图片，交叉引用圣经阶段注册表
- 输出 asset_index.md（下游 Step 5/6 的查表依据）
- 需要手动运行，generate_images.py 不会自动触发

## 关键文件变更
- `scripts/generate_images.py` — 重写：纯 requests、Seedream 5.0、两阶段、--limit、--phase
- `scripts/README.md` — 更新：两阶段工作流、新参数表、新工作流示例

## 运行流程
```bash
# Phase 1: 基准肖像 + 场景 + 道具
python3 generate_images.py --phase 1

# 人工审查，不满意的删掉重跑
python3 generate_images.py --phase 1 --element 某角色 --no-skip

# Phase 2: 参考图生图
python3 generate_images.py --phase 2

# 更新索引
python3 build_index.py

# 校验
python3 validate_assets.py
```

### 8. 场景/道具是否需要参考图生图（设计决策讨论）

**问题**：场景和道具也有分阶段的情况（如恶灵区有默认期/唤醒期/决战期/战后期，数字人躯体有空壳期/注魂期），是否也应该像角色一样用两阶段参考图生成？

**结论：不需要，维持现状（纯文生图）。**

**理由**：
- **角色需要参考图的核心原因是"身份一致性"**——同一个人的脸、体型、五官比例，纯靠文字描述很难跨图保持一致，必须靠参考图锚定
- **场景的阶段变化本质是"同一个地方在不同时间的状态"**（如从秩序→动荡→崩溃→重建），希望它们之间有明显的视觉差异。如果传参考图，API 反而会过度保留第一张的样子，压制阶段间的变化效果
- **道具同理**，比如数字人躯体从空壳期到注魂期，状态变化就是重点
- **场景/道具的一致性靠 prompt 就够**：建筑结构、物体外形等特征用文字描述（颜色代码、材质、尺寸）已经足够控制
- **保留扩展性**：如果后续发现某个场景跨阶段建筑结构差异太大，可以单独对那个场景加参考图，脚本已支持 `ref_image_path`，只需小改 `build_tasks()` 即可

### 9. Bible 提示词标题规范化（Step 3 回溯修复）

**严格两种标题形式**：
- `### 提示词N：肖像-{视角}` — 角色肖像，stage_id = None
- `### 提示词N：{stage_id}` — 阶段场景

**已完成的修复**：
1. **标题格式统一**：fix_titles_v2.py 批量修正 245 处 + 6 处手动修正（剥离 `-描述` 后缀、规范肖像视角名称）
2. **空壳标题清理**：fix_empty_titles.py 删除 13 个文件中的 72 行空壳提示词（无 English 内容的标题）
3. **肖像→阶段重分类**：6 个文件中同视角不同阶段的肖像改为 `{stage_id}` 形式（丁路、刘振、卢静、杨伯礼、小小顶、旅行团群像）
4. **非标准块清理**：8 个文件中的全局前缀 / 使用指南 / 文档完成块移除
5. **一标题多 prompt 拆分**：fix_multi_prompts.py 拆分 4 个旧格式 location 文件（定达国都 3→10、永安镇 3→7、泊岗镇 3→6、十八层塔 4→6）
6. **extract_prompts.py 简化**：移除 Format D、移除 `-` split 逻辑，只处理标准两种形式

**最终扫描结果（118 个文件）**：
- 问题1（标题不规范）：✅ 0 违规
- 问题2（重复标题）：49 个文件有重复 —— **全部合理**，同一 stage_id 下多个场景（如 "默认" 下有全景/中景/特写），extract_prompts.py 按序号区分，不影响下游
- 问题3（一标题多 prompt）：✅ 0 违规

**设计决策：重复标题为何不需要修复**：
- 同一 stage_id 下本来就可以有多个提示词，每个描述不同场景/镜位/时间
- extract_prompts.py 按文件内出现顺序编号（prompt_001, prompt_002...），stage_id 相同不影响唯一性
- generate_images.py 的 `build_tasks()` 输出路径为 `{element}/{stage_id}/prompt_{N}.png`，N 保证唯一
- 如果强制在标题中加场景描述（如 `默认-全景`），会打破严格两种形式的规则

### 10. 三阶段重构（Phase 拆分）

- 原 Phase 1 包含角色基准肖像 + 场景 + 道具，过于混杂
- 拆分为三阶段：Phase 1 = 角色基准肖像，Phase 2 = 角色参考图生图，**Phase 3 = 场景 + 道具**
- `--phase` 参数从 `choices=[0,1,2]` 扩展为 `choices=[0,1,2,3]`
- dry-run 摘要和运行时日志同步更新

### 11. 全局前缀精简（art_direction.md 第七章）

**问题**：生成的角色肖像面部轮廓和肤色过于相似，角色之间缺乏辨识度。

**根因分析**：
- `get_global_prefix()` 返回的通用前缀过于具体，包含"weathered appearance"、"traditional Chinese clothing in muted browns and greys"、"muted earthy color palette"等内容描述
- 这些内容描述本应由各角色圣经自行控制，全局前缀不应干涉
- 即使区分了角色/场景/超自然三类前缀，角色通用前缀本身仍包含同质化描述（所有角色都"weathered"、都穿"muted browns"），无法解决差异化问题

**解决方案**：将 art_direction.md 第七章精简为仅 5 个纯格式关键词：
```
Cinematic still, 2.39:1 widescreen, 35mm film grain texture, medium-high contrast, photorealistic
```
删除了角色前缀、场景前缀、超自然前缀的全部内容描述。色彩、光影、服装、氛围等全部交由各圣经 prompt 自行控制。

**随后清理**：从 118 个圣经文件中删除了所有内嵌的 `Cinematic still, 2.39:1 widescreen, ` 和 `电影感静帧，2.39:1宽银幕，` 前缀（共 70 个文件，270+149 处），因为全局前缀现在由 `generate_images.py` 在 API 调用时动态拼接。

### 12. 角色身份锚点系统（Identity Anchor）— 核心架构决策

**问题**：即使精简了全局前缀，生成的角色肖像仍然面部相似。文生图模型在缺乏强差异化特征时，会收敛到"默认亚洲中年男性"的均值脸。

**方案设计**（三步机制）：

**第一步：角色区分矩阵**。用一张表强制规定每个角色在 6 个维度上的唯一组合——年龄段、体型、脸型、发型、肤色、标志性特征。任何两个角色不能在 3 个以上维度重合。这张表本身就是一个校验工具。

**第二步：身份锚点（Identity Anchor）**。从矩阵中提炼出每个角色一句话的"视觉指纹"（英文+中文各一行，最多 25 词），作为硬约束，在该角色的**每一条** prompt 最前面前置，优先级高于全局前缀和场景描述。

**第三步：脚本层保障**。`generate_images.py` 在拼接 prompt 时，自动从角色圣经中提取身份锚点并前置。

**最终 Prompt 拼接顺序**：`[身份锚点] + [全局前缀] + [圣经原始 Prompt]`

**实施结果**：
- 53 个角色全部写入身份锚点（位于各圣经"外貌与形态"章节顶部的 `### 身份锚点 / Identity Anchor` 子节）
- `extract_prompts.py` 新增 `extract_identity_anchor()` 函数
- `generate_images.py` 的 `build_tasks()` 为角色类型自动前置锚点
- 生成文件：`identity_anchors.json`（结构化数据）、`identity_anchors.md`（6 维矩阵 + 碰撞检查）

**锚点对比示例**（展示差异化效果）：
- 宋小仙：`Athletic lean man, 30-35, piercing narrow eyes like a deep well, sharp angular face, relentless analytical bearing`
- 朱围庸：`Stocky powerful man, 30-40, deep sunken eyes with piercing gaze, thick black sword brows, squared strong jaw, sun-darkened weathered skin, cold immobile face`
- 李仁：`Weathered old farmer, late 50s, gaunt angular face with deep wrinkles, receding grey-white short hair, dark leathery sun-baked skin, thick black brows over piercing strategist eyes, stooped laborer posture`
- 杨弘：`Imposing military commander, 50s, tall powerful frame, close-cropped iron-grey hair, deep scar across left jawline, hawk nose, cold calculating narrow eyes, ramrod-straight military posture`
- 老吴：`Aged fisherman, 70s, gaunt hollow cheeks, wispy white beard, deep-set weary eyes, weathered leather skin, labor-marked gnarled hands`

**设计决策的核心洞察**：
> 文生图模型的"均值脸"问题不能靠删除干扰信息（全局前缀精简）来解决，必须靠**主动注入差异化信号**（身份锚点）来打破。两者是互补的：前者减少同质化拉力，后者增加差异化推力。

### 13. 资产画廊（gallery.html）

- 静态 HTML 资产预览页，内嵌 JSON 数据（Python 脚本注入）
- 分类筛选（角色/场景/道具）、状态筛选（全部/已生成/待生成）、灯箱查看
- 深色前卫 UI，响应式布局

## 关键文件变更（本轮追加）

- `scripts/generate_images.py` — 三阶段重构 + 身份锚点拼接
- `scripts/extract_prompts.py` — 新增 `extract_identity_anchor()` + `scan_bibles()` 返回 `identity_anchor` 字段
- `scripts/README.md` — 三阶段文档 + Prompt 拼接顺序 + 关联文件说明
- `step2-art-direction/art_direction.md` — 第七章精简为纯格式前缀
- `step3-bibles/identity_anchors.json` — 53 个角色锚点数据
- `step3-bibles/identity_anchors.md` — 6 维区分矩阵 + 碰撞检查
- 53 个角色圣经 — 各自新增 `### 身份锚点 / Identity Anchor` 子节
- 118 个圣经文件 — 清除内嵌的 `Cinematic still` 前缀
- `step4-assets/gallery.html` — 新增资产预览页

## 待办
- 用户正在分批执行 Phase 1 生成
- Phase 2 尚未开始（等 Phase 1 全部基准肖像确认后）
- 待删除 7 个错位资产目录（天德城、定达国都、恶灵区、泊岗镇、牛台山、美女榕-location、美女榕-props），用户控制时机
