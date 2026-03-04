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

## 待办
- 用户正在分批执行 Phase 1 生成
- Phase 2 尚未开始（等 Phase 1 全部基准肖像确认后）
