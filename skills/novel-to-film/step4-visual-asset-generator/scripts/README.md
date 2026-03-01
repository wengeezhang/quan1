# Step 4 — Visual Asset Generator Scripts

本目录包含 Step 4（视觉资产生成）的全部执行脚本，按工作流顺序排列。

## 执行顺序

```
1. extract_prompts.py   提取提示词 → prompts_plan.md
2. scaffold_assets.py   搭建目录树 → step4-assets/{type}/{name}/{stage_id}/
3. [人工] 调用 Seedream API 生成图片，放入对应目录
4. build_index.py       扫描图片 → asset_index.md
5. validate_assets.py   校验完整性 → 校验报告
```

## 脚本说明

### bible_utils.py — 共享工具模块

所有脚本的公共依赖。提供统一的圣经文件解析逻辑，包括：

- `count_stars(text)` — 从圣经文件中提取重要性星级（★数量）
- `extract_stages(text)` — 提取阶段注册表中的 stage_id 列表，兼容标准格式与老格式
- `extract_stage_chapters(text)` — 提取 stage_id → 章节范围映射
- `has_stage_registry(text)` — 检查是否包含阶段注册表
- `count_images(directory)` — 统计目录中的图片文件数

不可独立运行，仅供其他脚本 import。

### extract_prompts.py — 提示词提取器

从全部 Step 3 圣经（角色/场景/道具）中批量提取 AI 绘图提示词，输出结构化的生成计划。

**输入**：`production/step3-bibles/` 下所有 `.md` 圣经文件 + `step2-art-direction/art_direction.md`

**输出**：`production/step4-assets/prompts_plan.md`

**功能**：
- 扫描并解析中英双语提示词对（支持 6 种格式变体）
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
