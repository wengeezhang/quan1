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
- 道具：`props/{道具名}/{stage_id}/`（有阶段注册表）或 `props/{道具名}/`（无阶段）

```bash
python3 scaffold_assets.py [--base-dir /path/to/production] [--dry-run]
```

### generate_images.py — 图片批量生成器

调用火山引擎方舟 (Volcengine Ark) Seedream API，按优先级批量生成视觉资产图片并自动保存到对应目录。

**前置依赖**：

```bash
pip install volcenginesdkarkruntime --break-system-packages
export ARK_API_KEY="your-api-key-here"
```

**输入**：`production/step3-bibles/` 下所有圣经文件（通过 `extract_prompts.scan_bibles()` 直接读取源数据）

**输出**：生成的 `.png` 图片落盘到 `production/step4-assets/{type}/{name}/{stage_id}/` + 生成日志 `generation_log.jsonl`

**核心流程**：

1. 从 118 个圣经文件中提取 459 条提示词，构建生成任务队列
2. 对未内嵌全局前缀的提示词，自动在 prompt 头部拼接 `Cinematic still, 2.39:1 widescreen, 35mm film grain...`
3. 按优先级排序（P0/P1 角色肖像 → P2 主要场景 → P3 配角 → P4 道具 → P5 低优先级）
4. 逐条调用 Seedream API，以 `b64_json` 格式接收图片，解码后直接写入 `.png`
5. 断点续跑：已有图片的路径自动跳过，中断后重跑只生成缺失的部分

**关键特性**：

- 可复现：每个提示词的 seed 基于元素名+序号确定性计算，同 prompt+seed 产出相同图片
- 速率控制：默认 1.5s/张间隔 + 指数退避重试（最多 3 次）
- 生成日志：每张图生成后写入 `generation_log.jsonl`，记录 timestamp、seed、model、成功/失败等

**用法**：

```bash
# 查看完整生成计划（不调 API，不花钱）
python3 generate_images.py --dry-run

# 只生成最高优先级角色肖像（P0/P1，39 张）
python3 generate_images.py --priority "P0/P1"

# 只生成指定角色
python3 generate_images.py --element 吴文顶

# 只生成场景类型
python3 generate_images.py --type locations

# 全量生成（459 张，约 ¥115 / $16 @ $0.035/张）
python3 generate_images.py

# 指定模型版本和分辨率
python3 generate_images.py --model doubao-seedream-4-5-251128 --size 4K

# 调整 API 调用间隔（默认 1.5s）
python3 generate_images.py --delay 2.0
```

**全部参数**：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--base-dir` | 自动定位 | production 目录路径 |
| `--model` | `doubao-seedream-4-0-250828` | Seedream 模型 ID |
| `--size` | `2K` | 图片尺寸（`2K` / `4K` / `1024x1024`） |
| `--priority` | 全部 | 只生成指定优先级（`P0/P1` / `P2` / `P3` / `P4` / `P5`） |
| `--element` | 全部 | 只生成指定元素名 |
| `--type` | 全部 | 只生成指定类型（`characters` / `locations` / `props`） |
| `--dry-run` | false | 只输出计划，不调 API |
| `--no-skip` | false | 不跳过已有图片（强制重新生成） |
| `--delay` | 1.5 | API 调用间隔秒数 |
| `--ark-base-url` | `https://ark.cn-beijing.volces.com/api/v3` | 方舟 API 地址 |

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
# → 459 images to generate

# ④ 分批生成：先跑主角肖像
python3 generate_images.py --priority "P0/P1"

# ⑤ 跑主要场景
python3 generate_images.py --priority P2

# ⑥ 跑其余（配角、道具、低优先级）
python3 generate_images.py

# ⑦ 构建索引
python3 build_index.py

# ⑧ 校验完整性
python3 validate_assets.py
```
