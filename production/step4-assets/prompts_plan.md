# 视觉资产生成计划 (Prompt Extraction Report)

> 自动生成 by extract_prompts.py
> 全局 Style Prefix: `Cinematic still, 2.39:1 widescreen, 35mm film grain texture,...`
> 注意：全局前缀可在 Seedream API 调用时动态拼接，不强制要求写在圣经提示词中

## 统计总览

| 指标 | 数值 |
|------|------|
| 圣经文件总数 | 118 |
| 提示词总数 | 459 |
| 缺少英文提示词 | 0 |
| 缺少中文提示词 | 0 |
| 未内含全局前缀（可动态拼接） | 49 |
| 无提示词的圣经 | 0 |

---

## P0/P1 — 角色肖像+主角阶段图

| 元素 | 类型 | ★ | 阶段数 | 提示词数 | EN | CN | 前缀 |
|------|------|---|--------|---------|----|----|------|
| 吴文顶 | characters | ★★★★★ | 6 (初到泊岗期, 成家立业期, 决裂逃亡期, 抗战热血期, 沉疴临终期, 灵魂期) | 12 | ✅ | ✅ | ➕ |
| 宋小仙 | characters | ★★★★★ | 7 (民警执勤期, 便装追踪期, 伪装潜伏期, 奔走联络期, 谋士征战期, 神使斡旋期, 执法终局期) | 13 | ✅ | ✅ | ✅ |
| 朱围庸 | characters | ★★★★★ | 8 (灵魂期, 辗转附身期, 乞丐潜行期, 泊岗蛰伏期, 起兵崛起期, 统帅衰颓期, 红甲决战期, 轮回归途期) | 14 | ✅ | ✅ | ➕ |
---

## P2 — 主要场景

| 元素 | 类型 | ★ | 阶段数 | 提示词数 | EN | CN | 前缀 |
|------|------|---|--------|---------|----|----|------|
| 天德城 | locations | ★★★★★ | 3 (繁华期, 沦陷期, 大本营期) | 3 | ✅ | ✅ | ✅ |
| 定达国都 | locations | ★★★★★ | 3 (权力期, 腐败期, 崩溃期) | 10 | ✅ | ✅ | ✅ |
| 恶灵区 | locations | ★★★★★ | 4 (默认期, 唤醒期, 决战期, 战后期) | 9 | ✅ | ✅ | ✅ |
| 泊岗镇 | locations | ★★★★★ | 3 (繁忙期, 诡寂期, 要塞期) | 6 | ✅ | ✅ | ➕ |
| 牛台山 | locations | ★★★★★ | 4 (宁静期, 守护期, 战略期, 回归期) | 8 | ✅ | ✅ | ✅ |
| 美女榕 | locations | ★★★★★ | 1 (默认) | 7 | ✅ | ✅ | ✅ |
| 荣康城 | locations | ★★★★★ | 3 (防御期, 渗透期, 陷落期) | 3 | ✅ | ✅ | ✅ |
---

## P3 — 配角阶段图

| 元素 | 类型 | ★ | 阶段数 | 提示词数 | EN | CN | 前缀 |
|------|------|---|--------|---------|----|----|------|
| 威刚 | characters | ★★★★ | 3 (潜伏仆人期, 神力初显期, 元神降世期) | 7 | ✅ | ✅ | ➕ |
| 小周 | characters | ★★★★ | 4 (旅行者期, 失魂受难期, 康复证人期, 抵抗军战士期) | 8 | ✅ | ✅ | ✅ |
| 李仁 | characters | ★★★★ | 6 (恶灵期, 乞丐还阳期, 老农重生期, 军师征战期, 哀兵决战期, 归魂期) | 10 | ✅ | ✅ | ✅ |
| 杨弘 | characters | ★★★★ | 4 (铁血将军期, 无冕之王期, 暴君独裁期, 末路穷途期) | 8 | ✅ | ✅ | ➕ |
| 灵尤 | characters | ★★★★ | 3 (隐谷幼兽期, 山巅躁兽期, 战场凶兽期) | 7 | ✅ | ✅ | ➕ |
| 白巨 | characters | ★★★★ | 3 (族长全家期, 囚徒启悟期, 山巅守望期) | 7 | ✅ | ✅ | ➕ |
| 老吴 | characters | ★★★★ | 5 (山居重生期, 蛰伏协助期, 伪装潜入期, 抵抗军师期, 泉断衰败期) | 9 | ✅ | ✅ | ✅ |
| 胡酹 | characters | ★★★★ | 5 (恶灵期, 还阳适应期, 悍将崛起期, 倦将征战期, 殒命期) | 9 | ✅ | ✅ | ✅ |
| 黄亮伟 | characters | ★★★★ | 4 (商贾兴盛期, 被遣离场期, 抵抗军支柱期, 遗志守护期) | 8 | ✅ | ✅ | ✅ |
---

## P4 — 道具+次要场景

| 元素 | 类型 | ★ | 阶段数 | 提示词数 | EN | CN | 前缀 |
|------|------|---|--------|---------|----|----|------|
| 十八层塔 | props | ★★★★★ | 0 (—) | 5 | ✅ | ✅ | ➕ |
| 数字人躯体 | props | ★★★★★ | 2 (空壳期, 注魂期) | 8 | ✅ | ✅ | ➕ |
| 泉水 | props | ★★★★★ | 0 (—) | 6 | ✅ | ✅ | ✅ |
| 美女榕 | props | ★★★★★ | 2 (完好期, 断根期) | 10 | ✅ | ✅ | ➕ |
| 上神界 | locations | ★★★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 凤廊山脉 | locations | ★★★★ | 1 (默认) | 4 | ✅ | ✅ | ✅ |
| 十八层塔 | locations | ★★★★ | 1 (默认) | 6 | ✅ | ✅ | ✅ |
| 大蒜 | props | ★★★★ | 0 (—) | 4 | ✅ | ✅ | ✅ |
| 水晶棒 | props | ★★★★ | 0 (—) | 5 | ✅ | ✅ | ✅ |
| 永安镇 | locations | ★★★★ | 3 (市井期, 紧张期, 撤离期) | 7 | ✅ | ✅ | ➕ |
| 电磁枪 | props | ★★★★ | 0 (—) | 3 | ✅ | ✅ | ✅ |
| 老吴山间小屋 | locations | ★★★★ | 1 (默认) | 8 | ✅ | ✅ | ✅ |
| 黑布阵 | props | ★★★★ | 0 (—) | 4 | ✅ | ✅ | ✅ |
---

## P5 — 低优先级

| 元素 | 类型 | ★ | 阶段数 | 提示词数 | EN | CN | 前缀 |
|------|------|---|--------|---------|----|----|------|
| 于崇宝 | characters | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 于永智 | characters | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 于永龙 | characters | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 元刚智刚 | characters | ★★★ | 2 (元刚初生期, 智刚觉醒期) | 6 | ✅ | ✅ | ➕ |
| 分割带 | props | ★★★ | 0 (—) | 3 | ✅ | ✅ | ✅ |
| 卢卫寿 | characters | ★★★ | 2 (精明老板期, 傀儡期) | 5 | ✅ | ✅ | ✅ |
| 卢静 | characters | ★★★ | 3 (活泼少女期, 危机母亲期, 独立寡妇期) | 6 | ✅ | ✅ | ✅ |
| 县城破庙 | locations | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 向天志 | characters | ★★★ | 3 (沉稳国主期, 倦怠转折期, 虚君沦落期) | 6 | ✅ | ✅ | ✅ |
| 吴启思 | characters | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 吴启思实验室 | locations | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ➕ |
| 吴婶 | characters | ★★★ | 2 (泉边安居期, 逃难守护期) | 4 | ✅ | ✅ | ✅ |
| 和寻灵 | characters | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ➕ |
| 城主府 | locations | ★★★ | 1 (默认) | 4 | ✅ | ✅ | ✅ |
| 天德城城墙 | locations | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 小小顶 | characters | ★★★ | 1 (默认) | 4 | ✅ | ✅ | ✅ |
| 智寻道 | characters | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ➕ |
| 曹元艺 | characters | ★★★ | 3 (精致掩护期, 身份动摇期, 暴露对峙期) | 3 | ✅ | ✅ | ✅ |
| 朱围庸住处 | locations | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 江新成 | characters | ★★★ | 1 (默认) | 4 | ✅ | ✅ | ✅ |
| 泡泡 | props | ★★★ | 0 (—) | 3 | ✅ | ✅ | ✅ |
| 温伯封 | characters | ★★★ | 1 (默认) | 5 | ✅ | ✅ | ✅ |
| 温伯封府邸 | locations | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 灵闽 | characters | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 灵魂收集容器 | props | ★★★ | 0 (—) | 2 | ✅ | ✅ | ✅ |
| 皇宫 | locations | ★★★ | 1 (默认) | 4 | ✅ | ✅ | ➕ |
| 裘万财 | characters | ★★★ | 2 (恶霸期, 傀儡期) | 4 | ✅ | ✅ | ✅ |
| 观音庙神水 | props | ★★★ | 0 (—) | 4 | ✅ | ✅ | ✅ |
| 郝大川 | characters | ★★★ | 1 (默认) | 5 | ✅ | ✅ | ➕ |
| 郭云成 | characters | ★★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 丁路 | characters | ★★ | 2 (正常期, 被附身期) | 2 | ✅ | ✅ | ➕ |
| 五名古代恶灵 | characters | ★★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 仙人掌 | props | ★★ | 0 (—) | 3 | ✅ | ✅ | ➕ |
| 刘振 | characters | ★★ | 2 (流浪汉宿体期, 卢老板傀儡期) | 5 | ✅ | ✅ | ✅ |
| 北岸新码头 | locations | ★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 天都山脉 | locations | ★★ | 1 (默认期) | 1 | ✅ | ✅ | ➕ |
| 宁国红 | characters | ★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 宁阁码头 | locations | ★★ | 1 (默认期) | 1 | ✅ | ✅ | ➕ |
| 封 | characters | ★★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 小顶天德城住所 | locations | ★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 杜金标 | characters | ★★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 杨伯礼 | characters | ★★ | 2 (毁容前, 毁容后) | 4 | ✅ | ✅ | ✅ |
| 永安镇会议厅 | locations | ★★ | 1 (默认) | 4 | ✅ | ✅ | ➕ |
| 永安镇客栈 | locations | ★★ | 1 (默认) | 4 | ✅ | ✅ | ➕ |
| 江新成宅邸 | locations | ★★ | 1 (默认) | 3 | ✅ | ✅ | ✅ |
| 泊岗镇1200居民 | characters | ★★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 泥垛子建筑 | props | ★★ | 0 (—) | 3 | ✅ | ✅ | ➕ |
| 灵王 | characters | ★★ | 1 (默认) | 2 | ✅ | ✅ | ✅ |
| 熊大宝 | characters | ★★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 王轻无 | characters | ★★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 红领巾 | props | ★★ | 0 (—) | 3 | ✅ | ✅ | ➕ |
| 苏伟力 | characters | ★★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 茶馆 | locations | ★★ | 1 (默认期) | 1 | ✅ | ✅ | ➕ |
| 葛有利 | characters | ★★ | 0 (—) | 2 | ✅ | ✅ | ✅ |
| 郑伟玉 | characters | ★★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 郝大川破败小屋 | locations | ★★ | 1 (默认期) | 1 | ✅ | ✅ | ➕ |
| 铁链 | props | ★★ | 0 (—) | 3 | ✅ | ✅ | ➕ |
| 集市 | locations | ★★ | 1 (默认期) | 1 | ✅ | ✅ | ➕ |
| 马戈逸 | characters | ★★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 冯德友 | characters | ★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 刘默雨 | characters | ★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 匿名纸条 | props | ★ | 0 (—) | 3 | ✅ | ✅ | ➕ |
| 巫方镇 | locations | ★ | 1 (默认期) | 1 | ✅ | ✅ | ➕ |
| 干柿子与肉干 | props | ★ | 0 (—) | 3 | ✅ | ✅ | ➕ |
| 户政室 | locations | ★ | 1 (默认期) | 1 | ✅ | ✅ | ➕ |
| 旅行团群像 | characters | ★ | 1 (默认) | 4 | ✅ | ✅ | ➕ |
| 白思元 | characters | ★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 罗勇 | characters | ★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 葛立 | characters | ★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| 齐年康 | characters | ★ | 1 (默认) | 2 | ✅ | ✅ | ➕ |
| AA大学 | locations |  | 3 (校园侦察, 表面探查, 地下秘密) | 1 | ✅ | ✅ | ✅ |
| 千秋星岗 | locations |  | 2 (战斗期, 战败期) | 2 | ✅ | ✅ | ✅ |
| 半山腰秘密仓库 | locations |  | 2 (秘密期, 发现后) | 2 | ✅ | ✅ | ✅ |
| 卢老板餐馆 | locations |  | 3 (日常引入, 暗流涌动, 战争阴影) | 1 | ✅ | ✅ | ✅ |
| 周庄 | locations |  | 3 (逃离与到达, 休整与连接, 危机前兆) | 1 | ✅ | ✅ | ✅ |
| 少林寺 | locations |  | 1 (默认期) | 2 | ✅ | ✅ | ✅ |
| 山谷旅行团被困 | locations |  | 2 (被困期, 救援期) | 2 | ✅ | ✅ | ✅ |
| 望海河 | locations |  | 3 (河岸侦察, 夜间渡河, 对岸脱险) | 1 | ✅ | ✅ | ✅ |
| 杨弘秘密实验室 | locations |  | 3 (秘密进入, 真相揭露, 最后对抗) | 1 | ✅ | ✅ | ✅ |
| 清平镇 | locations |  | 3 (占领初期, 管制建立, 深层黑暗) | 1 | ✅ | ✅ | ✅ |
| 白巨神兽的隐谷 | locations |  | 3 (隐谷发现, 兽的呈现, 困境始现) | 1 | ✅ | ✅ | ✅ |
| 石岭关 | locations |  | 3 (防御准备, 激烈对抗, 英勇坚守) | 1 | ✅ | ✅ | ✅ |
| 老码头 | locations |  | 2 (初到期, 探索期) | 2 | ✅ | ✅ | ✅ |
| 葛家堡 | locations |  | 3 (堡垒运作, 渗透激活, 内部崩坏) | 1 | ✅ | ✅ | ✅ |
| 虎口镇 | locations |  | 2 (默认期, 投降后) | 2 | ✅ | ✅ | ✅ |
| 黄阳镇 | locations |  | 2 (默认期, 战后) | 2 | ✅ | ✅ | ✅ |

---

## ℹ️ 未内含全局前缀的圣经（API 调用时可动态拼接）

- 吴文顶 (characters)
- 朱围庸 (characters)
- 泊岗镇 (locations)
- 威刚 (characters)
- 杨弘 (characters)
- 灵尤 (characters)
- 白巨 (characters)
- 十八层塔 (props)
- 数字人躯体 (props)
- 美女榕 (props)
- 永安镇 (locations)
- 元刚智刚 (characters)
- 吴启思实验室 (locations)
- 和寻灵 (characters)
- 智寻道 (characters)
- 皇宫 (locations)
- 郝大川 (characters)
- 丁路 (characters)
- 五名古代恶灵 (characters)
- 仙人掌 (props)
- 天都山脉 (locations)
- 宁阁码头 (locations)
- 封 (characters)
- 杜金标 (characters)
- 永安镇会议厅 (locations)
- 永安镇客栈 (locations)
- 泊岗镇1200居民 (characters)
- 泥垛子建筑 (props)
- 熊大宝 (characters)
- 王轻无 (characters)
- 红领巾 (props)
- 苏伟力 (characters)
- 茶馆 (locations)
- 郑伟玉 (characters)
- 郝大川破败小屋 (locations)
- 铁链 (props)
- 集市 (locations)
- 马戈逸 (characters)
- 冯德友 (characters)
- 刘默雨 (characters)
- 匿名纸条 (props)
- 巫方镇 (locations)
- 干柿子与肉干 (props)
- 户政室 (locations)
- 旅行团群像 (characters)
- 白思元 (characters)
- 罗勇 (characters)
- 葛立 (characters)
- 齐年康 (characters)

---

## 完整提示词明细

### 吴文顶 (characters, ★★★★★, P0/P1)

#### 1. 

**English：**
```
Portrait of a young Chinese man around 20 years old, slender lean build, oval face with soft jawline, thin naturally arched eyebrows giving a scholarly gentle appearance, large double-lidded dark brown eyes that are exceptionally clear and bright as if light radiates from within, straight medium nose, healthy-toned lips of moderate fullness, smooth youthful fair skin, short neat black hair, neutral expression with a slight natural upward curve at mouth corners suggesting inherent warmth, wearing a plain light-colored cotton shirt, white neutral background, front-facing bust shot, shoulders visible, soft warm-toned side lighting, 35mm film grain, medium contrast
```

**中文：**
```
一名约20岁中国年轻男性的肖像，瘦削精瘦体格，瓜子脸下颌线条柔和，细长自然弯弧眉毛呈现书卷文气，大而清澈的双眼皮深褐色眼睛异常明亮仿佛有光芒从内部散发，挺直适中的鼻梁，健康唇色厚薄适中的嘴唇，光洁年轻偏白净的皮肤，黑色短发整齐利落，中性表情嘴角略带自然上扬暗示天生的温暖感，穿素色浅色棉质衬衫，白色中性背景，正面半身照可见肩部，柔和暖调侧光，35mm胶片颗粒感，中等对比度
```

#### 2. 

**English：**
```
Three-quarter view portrait of a young Chinese man around 20, slender build, soft oval face with gentle jawline clearly visible in angled lighting, thin arched eyebrows, large bright double-lidded dark brown eyes with exceptional clarity, medium straight nose, fair youthful skin with smooth texture, short black hair neatly trimmed, wearing plain light-colored cotton shirt, white neutral background, three-quarter angle bust shot from slight left, warm-toned natural lighting emphasizing gentle facial features, 35mm film grain, medium contrast
```

**中文：**
```
一名约20岁中国年轻男性的四分之三侧面肖像，瘦削体格，柔和瓜子脸温和下颌线在角度光线下清晰可见，细长弯弧眉毛，大而明亮的双眼皮深褐色眼睛清澈度极高，挺直适中鼻梁，白净年轻光滑质感皮肤，黑色短发利落修剪，穿素色浅色棉质衬衫，白色中性背景，略偏左的四分之三角度半身照，暖调自然光强调温和面部特征，35mm胶片颗粒感，中等对比度
```

#### 3. 

**English：**
```
Pure side profile portrait of a young Chinese man around 20, slender neck and narrow shoulders visible, soft oval jawline in silhouette with gentle chin, moderate forehead, thin arched eyebrow ridge, large eye socket with prominent lashes visible in profile, medium straight nose bridge, lips naturally relaxed, smooth fair skin along jaw and neck, short black hair close to head, wearing plain light-colored cotton shirt, white neutral background, exact right-facing profile bust shot, soft rim lighting on face edge, 35mm film grain, medium contrast
```

**中文：**
```
一名约20岁中国年轻男性的纯正侧面肖像，可见纤细颈部和窄肩，轮廓中呈现柔和瓜子脸下颌线和温和下巴，适中额头，细长弯弧眉骨，大眼窝侧面可见明显睫毛，挺直适中的鼻梁，嘴唇自然放松，下颌和颈部白净光滑的皮肤，黑色短发贴头，穿素色浅色棉质衬衫，白色中性背景，精确的右向正侧面半身照，柔和面部边缘轮廓光，35mm胶片颗粒感，中等对比度
```

#### 4. 

**English：**
```
Full-body front-facing portrait of a young Chinese man around 20, approximately 170cm tall, slender lean build with narrow shoulders and thin limbs, standing with a slight natural forward lean suggesting eagerness, hands loosely at sides with open relaxed posture, oval face with large bright clear eyes looking directly at viewer with warmth, wearing plain light-colored cotton shirt tucked into dark trousers, simple canvas shoes, white neutral background, full body visible from head to feet, soft warm even lighting, 35mm film grain, medium contrast
```

**中文：**
```
一名约20岁中国年轻男性的全身正面肖像，身高约170cm，瘦削精瘦体格窄肩细肢，站姿略带自然前倾暗示热忱感，双手自然垂于两侧呈开放放松姿态，瓜子脸配大而明亮清澈的眼睛直视观者带有温暖，穿素色浅色棉质衬衫扎入深色长裤，简素帆布鞋，白色中性背景，从头到脚全身可见，柔和温暖均匀灯光，35mm胶片颗粒感，中等对比度
```

#### 5. 

**English：**
```
Full-body rear view of a young Chinese man around 20, approximately 170cm, slender lean build visible through clothing, narrow shoulders and slim waist, short black hair revealing thin neck, standing with hands loosely at sides in a relaxed youthful posture, wearing plain light-colored cotton shirt tucked into dark trousers, simple canvas shoes, white neutral background, full body from head to feet seen from directly behind, soft warm even lighting, 35mm film grain, medium contrast
```

**中文：**
```
一名约20岁中国年轻男性的全身背面像，身高约170cm，瘦削精瘦体格透过衣物可见，窄肩细腰，黑色短发露出纤细颈部，双手自然垂于两侧呈放松年轻姿态站立，穿素色浅色棉质衬衫扎入深色长裤，简素帆布鞋，白色中性背景，从正后方可见头到脚全身，柔和温暖均匀灯光，35mm胶片颗粒感，中等对比度
```

#### 6. 

**English：**
```
Extreme close-up of a young Chinese man's eyes, large double-lidded dark brown irises with exceptional clarity and brightness, light seems to emanate from within the pupils creating a luminous quality, thin naturally arched eyebrows above, smooth fair youthful skin around eye area without wrinkles, slight natural upward crinkle at outer corners suggesting habitual warmth and smiling, long dark lashes, catch light prominently reflecting in both pupils, white neutral background, macro lens detail showing iris texture and luminous quality, soft warm lighting, 35mm film grain, medium contrast emphasizing eye brightness
```

**中文：**
```
一名中国年轻男性眼部极致特写，大而清澈明亮的双眼皮深褐色瞳孔，光芒仿佛从瞳孔内部散发创造出发光般的质感，上方细长自然弯弧的眉毛，眼周白净年轻光滑皮肤无皱纹，外眼角略带自然上翘的纹路暗示习惯性的温暖和微笑，浓密深色睫毛，两只瞳孔中都有醒目的眼神光反射，白色中性背景，微距镜头细节展现虹膜纹理和发光质感，柔和暖调灯光，35mm胶片颗粒感，中等对比度强调眼部明亮
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young Chinese man around 20, slender scholarly build, wearing a plain inexpensive light grey cotton shirt with sleeves rolled up to elbows, dark simple trousers, cheap canvas shoes, a basic restaurant apron tied loosely around waist with minor grease stains, face clean and fair-skinned with a youthful glow, large bright eyes shining with curiosity and hope, thin arched eyebrows relaxed, slight sweat on forehead suggesting physical labor, short neat black hair, standing in an eager slightly forward-leaning posture, plain dark background, soft warm side lighting emphasizing youthful radiance, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约20岁中国年轻男性的全身定妆参考，瘦削书生型体格，穿素色廉价浅灰棉质衬衫袖口挽至肘部，深色简单长裤，廉价帆布鞋，腰间松松系着一条基本款餐馆围裙带有少许油渍，面容干净白净带有年轻的光泽，大而明亮的眼睛闪烁着好奇和希望的光芒，细长弯弧眉毛放松，额头微有汗珠暗示体力劳动，黑色短发整齐利落，以热忱的略微前倾姿态站立，素色深色背景，柔和暖调侧光强调年轻光彩，35mm胶片颗粒感，中等对比度
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young Chinese man around 22, slender but slightly more filled-out build than before, wearing a better-quality dark warm-brown casual shirt over lighter undershirt, dark trousers, simple leather shoes, a wristwatch as subtle sign of improved status, face retaining youthful features but expression more mature and grounded, large bright eyes now carrying a faint layer of worry beneath the warmth, thin eyebrows occasionally furrowed, short neat black hair, standing in a steady composed posture with hands naturally at sides, plain dark background, warm amber-toned lighting with subtle cool undertone, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约22岁中国年轻男性的全身定妆参考，瘦削但比之前略微饱满的体格，穿质感更好的深暖棕色休闲衬衫内搭浅色内衣，深色长裤，简素皮鞋，一只手表作为地位改善的微妙标志，面容保留年轻特征但表情更加成熟沉稳，大而明亮的眼睛在温暖之下现在带有一层隐约的忧虑，细眉偶尔微蹙，黑色短发整齐利落，以稳健沉着的姿态站立双手自然垂于两侧，素色深色背景，暖琥珀色调灯光带微妙冷色底调，35mm胶片颗粒感，中等对比度
```

#### 9. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young Chinese man around 23, slender build appearing slightly gaunt from stress, wearing a wrinkled casual shirt with collar loosely open and sleeves pushed up, dusty dark trousers with minor wear marks, scuffed shoes, face pale with reddened eye rims and visible emotional strain, large eyes now sharp with alertness and pain instead of warmth, jaw set tight, thin eyebrows drawn together in permanent furrow, hair slightly disheveled, carrying a small simple travel pack slung over one shoulder, standing in a tense guarded posture, plain dark background, cool-toned flat lighting emphasizing pallor and tension, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约23岁中国年轻男性的全身定妆参考，瘦削体格因压力显得略微憔悴，穿褶皱的休闲衬衫衣领松敞袖子推起，沾灰的深色长裤带有轻微磨损痕迹，磨花的鞋，面色苍白眼眶红肿可见情绪创伤的痕迹，大眼睛现在不再温暖而是充满警觉和痛苦的锐利，下颌紧咬，细眉紧锁呈永久性皱起，头发略显凌乱，肩上斜挎一只简单小行李包，以紧张戒备的姿态站立，素色深色背景，冷调平面灯光强调苍白和紧张感，35mm胶片颗粒感，中高对比度
```

#### 10. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young Chinese man around 25, slender but noticeably more muscular than before from training, wearing a plain khaki military-style jacket over simple dark shirt, dark sturdy trousers, worn leather boots, a crude short sword or knife at belt, face matured with sharper angles losing earlier softness, visible scar across left forearm and a small healed cut near right eyebrow, skin sun-darkened to healthy wheat tone, large eyes still bright but now blazing with fierce determination rather than innocence, short black hair slightly longer and less tidy, standing in a wide grounded combat-ready stance, plain dark background, dramatic warm-cool mixed side lighting, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约25岁中国年轻男性的全身定妆参考，瘦削但因训练比之前明显更加结实，穿素色卡其军装风格外套内搭深色简单衬衫，深色结实长裤，磨损皮靴，腰带上挂一把粗糙的短刀或匕首，面容成熟棱角更加分明失去了早期的柔软，左前臂可见一道疤痕右眉骨处有一条已愈合的小伤口，皮肤晒黑至健康的小麦色，大眼睛依然明亮但现在燃烧着激烈的决心而非天真，黑色短发略长且不太整齐，以宽阔扎实的备战姿态站立，素色深色背景，戏剧性冷暖混合侧光，35mm胶片颗粒感，高对比度
```

#### 11. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young Chinese man around 30 but appearing aged beyond his years, extremely emaciated with clothes hanging loosely on wasted frame, wearing an oversized plain light beige cotton robe that emphasizes his skeletal thinness, sitting propped up slightly as if on a bed edge, face gaunt with sunken cheeks and prominent cheekbones, lips colorless pale white, large eyes half-closed and dimmed yet retaining a faint residual spark of determination deep within, thin eyebrows relaxed with no strength to furrow, hair slightly unkempt, hands resting limply on lap showing visible veins and bone structure, plain dark background, soft diffused warm window-like lighting from one side creating gentle shadows, 35mm film grain, low contrast emphasizing fragility
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约30岁但外表超越实际年龄衰老的中国年轻男性的全身定妆参考，极度消瘦衣物松垮地挂在枯瘦的身形上，穿宽大的素净浅米色棉质长袍更加突出骨感般的消瘦，微微靠坐如同倚在床沿，面容憔悴双颊凹陷颧骨突出，嘴唇无血色苍白如纸，大眼睛半闭黯淡但深处仍保留一丝微弱的残存坚定光芒，细眉放松无力紧锁，头发略显凌乱，双手无力地搁在膝上可见突出的血管和骨骼结构，素色深色背景，柔和漫射的暖色窗光从一侧投入创造温柔阴影，35mm胶片颗粒感，低对比度强调脆弱感
```

#### 12. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body reference of a semi-transparent ethereal figure of a young Chinese man around 20, restored to youthful appearance without illness or battle scars, slender build visible through translucent form, face serene and peaceful with a gentle half-smile, large eyes clear and luminous once again as in youth, overall form glows with soft warm white light, clothing appears as faint outline of simple everyday attire, on the chest and arms faint purple sigil-like markings (#5B3A6B) are etched into the translucent form — resembling chain patterns or seal stamps indicating spiritual punishment, the purple marks contrast against the warm white glow of the spirit body, standing in a relaxed gentle posture, plain black background, soft ethereal self-illumination with no external light source, 35mm film grain, low contrast, atmosphere of bittersweet peace
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一个半透明空灵人形的全身参考——约20岁的中国年轻男性，恢复了年轻外貌没有病容和战伤，半透明形态下可见瘦削体格，面容安详平和带着温柔的半笑，大眼睛再次清澈明亮如同年少时期，整体形态散发柔和温暖的白色光芒，衣物呈现为简单日常装的微弱轮廓，胸部和手臂上刻有淡紫色印记般的纹样(#5B3A6B)——类似锁链图案或封印印记表示灵魂惩罚，紫色标记与灵魂体的温暖白色光芒形成对比，以放松温和的姿态站立，纯黑背景，柔和的空灵自发光无外部光源，35mm胶片颗粒感，低对比度，苦乐参半的安宁氛围
```

### 宋小仙 (characters, ★★★★★, P0/P1)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese man in his early 30s, short black hair parted to the side exposing forehead, narrow eyes with deep black irises and penetrating gaze, straight eyebrows with slightly raised peaks, high cheekbones on a lean angular face with clean sharp jawline, thin lips naturally pressed into a flat line, fair skin with subtle weathering, wearing a simple dark grey collarless cotton jacket, neutral expression with controlled intensity behind the eyes, white neutral background, soft front lighting with gentle shadows under cheekbones and jawline, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性的正面半身肖像，黑色短发向侧面梳开露出额头，狭长形眼睛有深黑色虹膜和穿透性目光，直眉微挑眉峰，长脸偏瘦颧骨微高下颌线条锐利有棱角，薄唇自然抿成一条平线，白净皮肤带有轻微风化痕迹，穿简素的深灰色无领棉布夹衣，中性表情但眼神深处蕴含克制的锐利，白色中性背景，柔和正面光在颧骨和下颌下方投出轻微阴影，35mm胶片颗粒感，中高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a Chinese man in his early 30s, short black hair revealing ear and temple, narrow eyes with deep black irises showing penetrating alertness, straight nose bridge with sharp profile, high cheekbones casting subtle shadows, thin pressed lips with slight asymmetry, fair skin with natural texture, lean build visible at shoulders, wearing a simple dark grey collarless cotton jacket, neutral analytical expression with head tilted approximately 5 degrees as if assessing something, white neutral background, side lighting from camera-left emphasizing facial bone structure, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性的四分之三侧面半身肖像，黑色短发露出耳朵和太阳穴，狭长形眼睛有深黑色虹膜展现穿透性的警觉，鼻梁挺直侧面轮廓硬朗，颧骨微高投出细微阴影，薄唇紧抿带轻微不对称，白净皮肤有自然纹理，肩部可见精干体型，穿简素深灰色无领棉布夹衣，中性分析式表情头部微侧约5度如同在审视什么，白色中性背景，左侧光强调面部骨骼结构，35mm胶片颗粒感，中高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, pure profile bust portrait of a Chinese man in his early 30s, short black hair with clean edge at nape, straight high nose bridge and defined nose tip, thin lips in flat line, clean sharp jawline with angular chin, high cheekbone creating shadow below, subtle Adam's apple visible on neck, wearing a simple dark grey collarless cotton jacket, neutral composed expression, white neutral background, rim lighting from behind outlining profile silhouette, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性的纯正侧面半身肖像，黑色短发在颈后边缘整齐，鼻梁挺直偏高鼻尖线条明确，薄唇呈平线，下颌线条锐利收向有棱角的下巴，颧骨高在下方形成阴影，颈部可见不突出的喉结，穿简素深灰色无领棉布夹衣，中性沉着表情，白色中性背景，背后轮廓光勾勒侧面剪影，35mm胶片颗粒感，中高对比度
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a Chinese man in his early 30s, short black hair parted to side, penetrating dark narrow eyes, lean and wiry athletic build with moderate shoulders and taut waist, medium height, standing with weight evenly distributed and arms naturally at sides, wearing a simple dark grey collarless cotton jacket over lighter inner shirt and dark wide-leg trousers, flat-soled dark cloth shoes, no accessories, posture upright with subtle forward lean suggesting readiness, white neutral background, even front lighting, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性的全身正面肖像，黑色短发向侧面分开，深邃穿透性的狭长黑色眼睛，身形精干结实肩宽适中腰身紧实，中等身高，双脚均匀承重双臂自然垂于身侧站立，穿简素深灰色无领棉布夹衣内衬浅色衬衫配深色宽腿裤，深色平底布鞋，无配饰，身姿挺拔微微前倾暗示随时准备行动，白色中性背景，均匀正面光，35mm胶片颗粒感，中高对比度
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body rear view of a Chinese man in his early 30s, short black hair with clean-cut edge at nape of neck, moderate shoulders with straight posture, wearing a simple dark grey collarless cotton jacket and dark wide-leg trousers, flat-soled dark cloth shoes, arms hanging naturally at sides, standing with quiet alertness, lean athletic build visible through clothing silhouette, white neutral background, soft back lighting creating subtle rim light on hair and shoulder edges, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性的全身背面像，黑色短发在颈后整齐剪裁，肩宽适中挺直身姿，穿简素深灰色无领棉布夹衣配深色宽腿裤，深色平底布鞋，双臂自然垂于身侧，以安静的警觉姿态站立，精干结实的体型通过服装轮廓可见，白色中性背景，柔和背光在发丝和肩部边缘形成微弱轮廓光，35mm胶片颗粒感，中高对比度
```

#### 6. 

**English：**
```
Cinematic still, 2.39:1 widescreen, extreme close-up of the eyes of a Chinese man in his early 30s, narrow eyes with deep black irises that appear almost bottomless, clean white sclera, straight eyebrows with slightly raised peaks and tightened tails, faint dark circles beneath lower lids suggesting chronic fatigue, fine skin texture around eye area, eyelashes natural and not prominent, the gaze is the defining feature — penetrating and analytical as if seeing through the subject, a quality of cold intelligence tempered by hidden compassion, white neutral background, macro lens detail, ring light reflection in pupils, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性的眼部极近特写，狭长形眼睛有深黑色虹膜深邃近乎无底，眼白干净，直眉微挑眉峰眉尾收紧，下眼睑下方有淡淡黑眼圈暗示长期疲劳，眼周皮肤纹理自然，睫毛自然不突出，目光是决定性特征——穿透性的分析式凝视仿佛透视被观察者，冷静智慧中暗藏悲悯的气质，白色中性背景，微距镜头细节，瞳孔中有环形灯反光，35mm胶片颗粒感，高对比度
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s wearing a standard dark navy winter police uniform, uniform pressed and immaculate with visible shoulder insignia and chest badge, black leather duty belt with flashlight and notebook holster at waist, black regulation leather boots, short black hair neatly parted, lean angular face with calm professional expression and controlled intensity in the eyes, standing in a composed upright posture with hands clasped behind back, plain dark background, cool even front lighting emphasizing the crisp uniform lines, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性的全身定妆参考，穿标准深藏蓝色冬季警服，制服熨烫整洁可见肩章和胸牌，腰间黑色皮质装备带挂手电筒和记事本套，黑色制式皮靴，黑色短发整齐分开，瘦削有棱角的面孔呈冷静专业的表情眼中带有克制的锐利，以沉着的挺直姿态站立双手背于身后，素色深色背景，冷色均匀正面光强调制服的笔挺线条，35mm胶片颗粒感，中高对比度
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s dressed as a traveling commoner, dark grey cross-collared cotton jacket over greyish-white inner shirt, dark wide-leg trousers, low leather-topped cloth boots, woven bamboo hat tilted slightly casting shadow over upper face, a simple cloth bundle slung over one shoulder, a small antique bottle tucked at waist belt, short black hair slightly longer with wind-tousled strands, lean face showing sun exposure and travel fatigue, eyes sharp and vigilant beneath hat brim, standing in a watchful pose weight shifted to back foot, plain dark background, dramatic side lighting from left creating half-shadow across face, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性的全身定妆参考，装扮成旅行平民，深灰色对襟棉布夹衣内衬灰白色衬衫，深色宽腿裤，低帮皮面布底靴，竹编斗笠微微倾斜在上半脸投下阴影，一个简单布包裹斜挎肩上，腰带处别着一只古朴小瓶，黑色短发略长有风吹凌乱的发丝，瘦削面孔显示日晒和旅途疲劳痕迹，斗笠帽檐下的眼睛锐利而警觉，以警惕姿态站立重心偏后脚，素色深色背景，左侧戏剧性侧光在面部形成半阴影，35mm胶片颗粒感，中高对比度
```

#### 9. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s disguised as an office assistant, short black hair restyled with different parting, wearing plain frameless glasses to alter facial impression, eyebrows subtly modified with darkened edges, wearing a dark navy-blue dress shirt and dark grey trousers, black leather belt, black dress shoes, carrying a notebook and pen in hand, body language deliberately subdued with lowered shoulders and deferential posture, face showing practiced meekness masking sharp attentive eyes behind glasses, plain dark background, neutral office-style overhead lighting casting even illumination, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性伪装成办公室助理的全身定妆参考，黑色短发重新梳理改变分线方向，佩戴素框眼镜改变面部印象，眉毛边缘用碳笔微调加深，穿深藏蓝色衬衫配深灰色西裤，黑色皮带，黑色皮鞋，手持笔记本和钢笔，刻意收敛的肢体语言肩膀放低呈恭敬姿态，面部呈练习过的谦逊表情但眼镜后的眼神锐利专注，素色深色背景，中性办公室风格顶光投出均匀照明，35mm胶片颗粒感，中等对比度
```

#### 10. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s in practical travel attire, short black hair restored to natural look, lean angular face with bright determined eyes, wearing a dark cross-collared cotton short jacket over wide-leg trousers, grey-green rough cloth overcoat draped over shoulders, thick-soled cloth shoes, a travel pack slung over back containing provisions, no accessories or decoration, standing in a ready-to-move posture with one foot slightly forward, plain dark background, natural warm side lighting suggesting dawn, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性穿实用旅行装束的全身定妆参考，黑色短发恢复自然面貌，瘦削有棱角的面孔有明亮坚定的眼神，穿深色斜襟棉布短衫配宽腿裤，灰青色粗布风衣搭在肩上，厚底布鞋，背后斜挎装有干粮的旅行包裹，无配饰无装饰，以随时准备出发的姿态站立一脚微微前探，素色深色背景，自然暖调侧光暗示晨曦，35mm胶片颗粒感，中高对比度
```

#### 11. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s dressed as a military strategist, visibly thinner face with pronounced cheekbones and slightly sunken eye sockets, a faint worry line between brows, wearing a dark blue-grey cross-collared inner robe beneath a lightweight dark brown leather breastplate covering chest and shoulders, wide leather belt with map tube and water flask, leather-topped long boots for marching, leather armor showing scratches rain stains and wear from campaign use, short black hair slightly unkempt from field conditions, eyes carrying both strategic sharpness and weight of battlefield losses, standing with arms crossed studying an unseen map, plain dark background, warm-cool mixed lighting suggesting campfire from below-left and moonlight from above-right, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性以军事谋士装扮的全身定妆参考，面容明显消瘦颧骨突出眼窝微凹，眉间一道浅浅的忧虑纹，穿深蓝灰色交领中衣外罩轻便暗棕色皮甲覆盖前胸和双肩，宽皮带挂地图筒和水壶，便于行军的皮面长靴，皮甲上有划痕雨渍和战事磨损痕迹，黑色短发因野外条件略显凌乱，眼中兼有战略锐利和战场失利的沉重，以双臂交叉审视无形地图的姿态站立，素色深色背景，冷暖混合光源——左下方篝火暖光与右上方月光冷光交织，35mm胶片颗粒感，中高对比度
```

#### 12. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s in solemn spiritual envoy attire, face pale but serene with an otherworldly composure, wearing a plain dark blue-grey (#3A4A6B) long robe of fabric between cotton and silk in texture, a subtle dark sash at waist, black soft-soled tall boots, holding a metallic soul vessel at waist level emitting faint royal blue (#4169E1) luminescence, no patterns or ornaments on clothing, short black hair immaculate, eyes deep with mingled authority and compassion, standing in a dignified upright posture with the blue glow of the vessel casting cold light upward onto face and hands, plain dark background, cool blue key light from the vessel supplemented by neutral ambient fill, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性穿肃穆灵使服饰的全身定妆参考，面色苍白但宁静带有超凡的沉着，穿素净的暗蓝灰色（#3A4A6B）长袍面料质地介于棉麻与丝绸之间，腰间系一条不显眼的暗色绶带，黑色软底长靴，腰部高度托持一只金属灵魂容器发出微弱的皇家蓝（#4169E1）荧光，衣物上无花纹无装饰，黑色短发整洁，眼神深邃兼有威严与悲悯，以庄严挺拔姿态站立容器蓝光向上映照面部和双手，素色深色背景，容器蓝色冷光为主光源辅以中性环境补光，35mm胶片颗粒感，中高对比度
```

#### 13. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s in divine enforcer gear, wearing a dark specialized protective suit of material between leather and otherworldly textile, faint blue (#4169E1) circuit-like patterns across the suit surface that shimmer subtly under light, holding a massive scissors-like instrument with dark metallic blue-tinged blades at his right side, short black hair, lean angular face showing the aftermath of intense emotional turmoil — reddened eyes with dried tear tracks on cheeks yet jaw set with renewed resolve, the expression is not iron control but hard-won peace after breaking, standing in a firm wide stance with the giant shears resting point-down, plain dark background, dramatic split lighting — cool blue from left and warm amber from right meeting at face center symbolizing the convergence of duty and humanity, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性穿神使执法装备的全身定妆参考，穿暗色特制防护服材质介于皮革和超自然织物之间，服装表面有微弱的蓝色（#4169E1）电路状纹路在光线下隐约闪烁，右手持一把巨大的剪刀状器械刀刃泛暗蓝色金属光泽，黑色短发，瘦削有棱角的面孔显示剧烈情绪风暴过后的痕迹——眼圈泛红面颊有干涸泪痕但下颌紧咬重新凝聚决心，表情不是铁面控制而是崩溃后艰难获得的平静，以稳固宽站姿站立巨型剪刀尖端朝下触地，素色深色背景，戏剧性分裂光——左侧冷蓝光与右侧暖琥珀光在面部中央交汇象征职责与人性的融合，35mm胶片颗粒感，高对比度
```

### 朱围庸 (characters, ★★★★★, P0/P1)

#### 1. 

**English：**
```
Portrait of a Chinese man in his early 30s, sturdy muscular build, square jaw with prominent cheekbones, thick straight eyebrows slightly angled upward, deep-set single-lidded dark brown eyes with an unnaturally penetrating gaze that seems older than his years, high straight nose with slightly wide tip, thin dark lips pressed into a firm line, rough weathered skin with visible pores and sun-darkened complexion, short black hair neatly trimmed, neutral expression with subtle downward tension at mouth corners, wearing a dark brown mandarin-collar tunic, white neutral background, front-facing bust shot, shoulders visible, cinematic lighting with soft side light from left, 35mm film grain, medium-high contrast
```

**中文：**
```
一名30岁出头的中国男性肖像，壮实肌肉型体格，方形下颌颧骨微突，浓黑剑眉微微上挑，深陷的单眼皮深褐色眼睛带有一种超越年龄的异常穿透性目光，高挺直鼻鼻头略宽，深色薄唇紧抿成一条线，粗糙饱经风霜的皮肤毛孔可见肤色偏黑，黑色短发利落修剪，中性表情嘴角微微下压带有细微张力，穿深褐色立领中式上衣，白色中性背景，正面半身照，可见肩部，电影感布光左侧柔和侧光，35mm胶片颗粒感，中高对比度
```

#### 2. 

**English：**
```
Three-quarter view portrait of a Chinese man in his early 30s, sturdy build, square jawline and angular facial structure clearly visible in dimensional lighting, thick dark eyebrows, deep-set single-lidded eyes with piercing dark brown irises, high nose bridge creating strong profile shadow, thin lips slightly parted, rough textured skin with weathering marks, short black hair, wearing dark brown mandarin-collar tunic, white neutral background, three-quarter angle bust shot from slight left, natural side lighting emphasizing facial bone structure, 35mm film grain, medium-high contrast
```

**中文：**
```
一名30岁出头中国男性的四分之三侧面肖像，壮实体格，方形下颌和棱角分明的面部结构在立体光线下清晰可见，浓黑眉毛，深陷单眼皮配穿透性深褐色瞳孔，高鼻梁投射出明显的侧面阴影，薄唇微启，粗糙有纹理的风化皮肤，黑色短发，穿深褐色立领中式上衣，白色中性背景，略偏左的四分之三角度半身照，自然侧光强调面部骨骼结构，35mm胶片颗粒感，中高对比度
```

#### 3. 

**English：**
```
Pure side profile portrait of a Chinese man in his early 30s, sturdy neck and broad shoulders visible, strong jawline and square chin in silhouette, high forehead, thick dark eyebrow ridge, deep-set eye socket, prominent straight nose bridge with slightly wide tip, thin lips pressed together, rough skin texture visible along jaw and neck, short black hair close to head, wearing dark brown mandarin-collar tunic, white neutral background, exact right-facing profile bust shot, rim lighting on face edge, 35mm film grain, medium-high contrast
```

**中文：**
```
一名30岁出头中国男性的纯正侧面肖像，可见粗壮颈部和宽阔肩膀，轮廓中呈现硬朗下颌线和方形下巴，高额头，浓黑眉骨，深陷眼窝，突出的高直鼻梁鼻头略宽，薄唇紧闭，下颌和颈部可见粗糙皮肤纹理，黑色短发贴头，穿深褐色立领中式上衣，白色中性背景，精确的右向正侧面半身照，面部边缘轮廓光，35mm胶片颗粒感，中高对比度
```

#### 4. 

**English：**
```
Full-body front-facing portrait of a Chinese man in his early 30s, approximately 175cm tall, sturdy muscular build with broad shoulders and thick chest, strong limbs, standing with feet shoulder-width apart in a grounded stable stance, hands at sides with slight fist tension, square-jawed face with penetrating dark eyes looking directly at viewer, wearing dark brown mandarin-collar long tunic over dark trousers, simple cloth shoes, white neutral background, full body visible from head to feet, soft even lighting, 35mm film grain, medium-high contrast
```

**中文：**
```
一名30岁出头中国男性的全身正面肖像，身高约175cm，壮实肌肉型体格宽肩厚胸四肢有力，双脚与肩同宽稳扎站立，双手垂于两侧微微握拳带有张力，方形下颌配穿透性深色眼睛直视观者，穿深褐色立领长衫配深色长裤，简素布鞋，白色中性背景，从头到脚全身可见，柔和均匀打光，35mm胶片颗粒感，中高对比度
```

#### 5. 

**English：**
```
Full-body rear view of a Chinese man in his early 30s, approximately 175cm, sturdy muscular build visible through clothing, broad shoulders tapering to firm waist, short black hair revealing strong neck, standing with hands clasped behind back in a contemplative commanding pose, wearing dark brown mandarin-collar long tunic over dark trousers, simple cloth shoes, white neutral background, full body from head to feet seen from directly behind, soft even lighting, 35mm film grain, medium-high contrast
```

**中文：**
```
一名30岁出头中国男性的全身背面像，身高约175cm，壮实肌肉型体格透过衣物可见，宽肩收至结实的腰部，黑色短发露出粗壮颈部，双手背后相扣呈沉思指挥姿态站立，穿深褐色立领长衫配深色长裤，简素布鞋，白色中性背景，从正后方可见头到脚全身，柔和均匀打光，35mm胶片颗粒感，中高对比度
```

#### 6. 

**English：**
```
Extreme close-up of a Chinese man's eyes, single-lidded or subtle inner double-fold, deep-set dark brown irises nearly black, unnaturally penetrating and aged gaze that contradicts apparent youth, thick straight dark eyebrows angled slightly upward, rough weathered skin around eye area with visible crow's feet beginning, faint purple-tinged veins barely visible at temples, catch light reflecting in pupils, white neutral background, macro lens detail showing iris texture and skin pores, cinematic soft side lighting, 35mm film grain, high contrast on eye area
```

**中文：**
```
一名中国男性眼部极致特写，单眼皮或微内双，深陷的深褐近黑色瞳孔，带有与外表年轻矛盾的异常穿透性和沧桑目光，浓黑直眉微微上挑，眼周粗糙风化皮肤可见初现的鱼尾纹，太阳穴处隐约可见淡青紫色血管纹路，瞳孔中反射眼神光，白色中性背景，微距镜头细节展现虹膜纹理和皮肤毛孔，电影感柔和侧光，35mm胶片颗粒感，眼部区域高对比度
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen, a dark purple irregular luminous orb against pure black background, the orb approximately basketball-sized with wrinkled rippling surface like disturbed water, edges pulsating with rhythmic wave patterns, color is deep violet #6432C8 with slight reddish tint at the pulsating edges, faint purple glow extending 50-80cm as a soft halo, bioluminescent quality with rapid falloff, the orb appears dense and compact with a stubborn luminosity, restrained supernatural glow, eerie unsettling presence, extreme low-key lighting with only the orb as light source, 35mm film grain texture
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一团暗紫色不规则发光球体置于纯黑背景前，球体约篮球大小表面有褶皱般的涟漪纹理如被搅动的水面，边缘以节律性波纹脉动，颜色为深紫罗兰#6432C8脉动边缘微带红调，微弱紫光向外延伸50-80cm形成柔和光晕，生物发光质感且快速衰减，球体呈致密紧实状态带有执拗的光泽，克制的超自然光效，诡异不安的存在感，极低调打光仅以球体为光源，35mm胶片颗粒质感
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young Chinese man in his early 20s, healthy athletic build, wearing a modern outdoor hiking jacket in muted green-grey over casual T-shirt and cargo pants, hiking boots, face deathly pale with cold sweat on forehead contrasting his youthful appearance, eyes unnaturally deep and aged — a piercing ancient gaze trapped in a young body that doesn't match his age, short neat black hair, standing in neutral pose, plain dark background, soft side lighting emphasizing the unsettling contrast between youthful body and ancient eyes, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名20岁出头中国青年男性的全身定妆参考，健康运动型体格，穿灰绿色调的现代户外冲锋衣内搭休闲T恤和工装裤，登山靴，面色死灰额头冷汗密布与年轻外表形成反差，眼神异常深邃苍老——一种被困在年轻躯体中的与年龄不匹配的穿透性古老目光，黑色整齐短发，保持中性站姿，素色深色背景，柔和侧光强调年轻身体与古老眼神之间的不安反差，35mm胶片颗粒感，中高对比度
```

#### 9. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a sturdy Chinese man in his 30s, muscular build visible beneath clothing, wearing torn filthy padded cotton jacket with multiple patches and stains, matching tattered cotton trousers, shoes patched with tree bark, a heavy iron chain locked around his left ankle trailing on the ground, face covered in grime with wind-burnt skin cracked bleeding lips and deeply sunken eye sockets, tangled matted black hair, eyes burning with desperate survival determination despite wretched appearance, a modern hiking backpack incongruously strapped to his back with cloth bags of dried provisions, standing in neutral pose, plain dark background, harsh directional lighting emphasizing grime textures and facial weathering, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30多岁壮实中国男性的全身定妆参考，衣物下可见肌肉型体格，穿破烂肮脏的多补丁多污渍棉袄，配同样破烂的棉裤，树皮补丁鞋，左脚踝锁着粗大铁链拖在地上，面部覆盖污垢皮肤被风灼伤嘴唇干裂出血眼窝深陷，黑发蓬乱打结，尽管外表凄惨但双眼燃烧着绝望的求生意志，背上不协调地背着现代登山背包挂有干粮布袋，保持中性站姿，素色深色背景，硬质方向性灯光强调污垢纹理和面部风化痕迹，35mm胶片颗粒感，高对比度
```

#### 10. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s, sturdy muscular build with sun-darkened rough skin, wearing a dark brown high-quality mandarin-collar long tunic over dark trousers, simple leather shoes, neatly trimmed short black hair, face clean and composed with deep-set penetrating dark eyes conveying hidden depth and melancholy, square jaw, thick dark eyebrows, thin lips pressed in a slight downward line, hands at sides in a calm grounded stance, a simple wristwatch as the only accessory, plain dark background with warm-cool mixed lighting — amber side light from left and cool fill from right, 35mm film grain, medium-high contrast, atmosphere of restrained power beneath ordinary appearance
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性的全身定妆参考，壮实肌肉型体格皮肤粗糙被海风晒黑，穿深褐色质感考究的立领长衫配深色长裤，简素皮鞋，黑色短发利落修剪，面容整洁沉稳深陷的穿透性深色眼睛传递着隐藏的深度和忧郁，方形下颌，浓黑眉毛，薄唇微微下压呈一条线，双手垂于两侧保持平静沉稳站姿，一只简约手表作为唯一配饰，素色深色背景配冷暖混合灯光——左侧暖琥珀色侧光右侧冷色补光，35mm胶片颗粒感，中高对比度，平凡外表下克制力量的氛围
```

#### 11. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s with square jaw and commanding imposing presence, wearing a dark charcoal Chinese tunic suit (zhongshan zhuang) with polished leather belt and subtle metal buckle accessories, sturdy black leather boots, standing with hands clasped behind his back and chin slightly raised in an authoritative pose, face cold and resolute with sharp cheekbones highlighted by dramatic side lighting, thick dark eyebrows furrowed, eyes burning with mad determination and frigid authority, muscular build filling the tunic with structured tension, plain dark background, low camera angle looking slightly upward at figure, 35mm film grain, high contrast, oppressive powerful atmosphere
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头方形下颌气场威压的中国男性的全身定妆参考，穿深炭色中山装配抛光皮带和精致金属扣配饰，结实黑色皮靴，双手背后下巴微抬呈权威姿态站立，面容冰冷决绝锐利颧骨在戏剧性侧光下凸显，浓黑眉毛紧锁，眼神燃烧着疯狂的决绝和冰冷的权威，肌肉型体格撑满中山装呈现结构性张力，素色深色背景，低角度略微仰拍人物，35mm胶片颗粒感，高对比度，压迫性的权力氛围
```

#### 12. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s but appearing prematurely aged and gaunt, wearing a loosely fitting dark military overcoat that hangs slack on his visibly thinned frame, the same charcoal tunic underneath now wrinkled and unkempt, dark trousers, one hand subtly gripping a simple wooden walking cane, unnaturally pale complexion with grey undertone, cracked dry lips, cheekbones more prominent from weight loss, eyes no longer burning but dimmed with exhaustion and hidden despair, slight stoop in posture, plain dark background, cool desaturated blue-grey toned lighting, soft flat front light emphasizing pallor and weariness, 35mm film grain, low contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头但显得过早衰老消瘦的中国男性的全身定妆参考，穿一件松垮的深色军大衣松塌地挂在明显消瘦的身形上，内搭同款炭色中山装如今褶皱不整洁，深色长裤，一只手微微握着简素木质拐杖，面色不自然苍白带灰色底调，嘴唇干裂，颧骨因消瘦更加突出，眼神不再燃烧而是黯淡带着疲惫和隐藏的绝望，姿态微微驼背，素色深色背景，冷去饱和蓝灰色调灯光，柔和平面正面光强调苍白和疲惫感，35mm胶片颗粒感，低对比度
```

#### 13. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s wearing dark crimson layered armor (#8B1A1A) with a flowing red cape draped over shoulders, fur-lined shoulder piece and fur collar for severe cold weather, a ceremonial sword sheathed at his hip, sturdy armored boots, face showing fierce tragic determination with reignited fire in deep-set dark eyes, thick eyebrows furrowed, streaks of blood and grime across his jaw and cheek, skin weathered and battle-worn, short black hair slightly disheveled, standing in a wide commanding stance, the red armor and cape are the most vivid color elements on the figure, plain dark background, dramatic side lighting from left emphasizing armor texture and facial resolve, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性的全身定妆参考，穿暗红色分层铠甲(#8B1A1A)配红色披风垂于双肩，肩部兽皮衬里和皮毛领口用于严寒，腰间佩仪式性佩刀入鞘，结实的铠甲靴，面部展现激烈而悲壮的决绝神情深陷的深色眼睛中重新燃起火焰，浓眉紧锁，下颌和面颊上有血污和尘垢的痕迹，皮肤风化且带有战痕，黑色短发微微凌乱，以宽阔的指挥姿态站立，红色铠甲和披风是人物身上最鲜明的色彩元素，素色深色背景，左侧戏剧性侧光强调铠甲质感和面部决绝神情，35mm胶片颗粒感，高对比度
```

#### 14. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 30s wearing a plain light grey-beige linen long robe, simple cloth shoes, a woolen scarf wrapped tenderly around his neck — clearly a cherished keepsake not his own and the most prominent accessory on the figure, no armor no weapons no belt, face clean without battle grime, expression peaceful and transcendent with a tender half-smile, eyes clear and luminous showing complete inner resolution and warmth, skin tone returned to normal neither pale nor darkened, faint barely-visible pale purple mist rising from shoulders hinting at spiritual nature, standing in a relaxed gentle posture with hands loosely at sides, plain dark background, soft warm-cool mixed lighting with silver-blue rim light, 35mm film grain, medium-low contrast, atmosphere of serenity and quiet farewell
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头中国男性的全身定妆参考，穿素净浅灰米色棉麻长袍，简素布鞋，颈间温柔地缠绕着一条毛织围巾——明显是他人珍贵的遗物而非自己之物且是人物身上最醒目的配饰，无铠甲无武器无腰带，面容干净无战争痕迹，表情安详超脱带着温柔的半笑，眼神清澈明亮展现出彻底的内心释然和温暖，肤色恢复正常既不苍白也不黝黑，肩部升起几乎不可见的淡紫色薄雾暗示灵魂本质，以放松温和的姿态站立双手自然垂于两侧，素色深色背景，柔和冷暖混合灯光配银蓝色轮廓光，35mm胶片颗粒感，中低对比度，宁静与安详告别的氛围
```

### 天德城 (locations, ★★★★★, P2)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, ancient inland city marketplace,
approximately 100,000 population, thick adobe walls encircling,
bustling merchant streets, warm golden-brown atmosphere #8B7355,
clear daylight with strong shadows, shop fronts and crowded passages,
vibrant activity, horse carriages and traders, intact architecture,
natural sunlight creating warm contrast, no white elements,
cinematic color grading, professional production quality
```

**中文：**
```
电影截帧，2.39:1 宽屏幅，内陆大型城市市集场景，
约十万人口规模，厚重城墙围绕，
繁华的商业街道，枯草黄氛围 #8B7355，
清晰的日光与强烈的阴影对比，店铺正面与拥挤通道，
人群活跃，马车与商人，建筑完整，
自然日光营造暖色对比，禁用纯白色，
电影色彩分级，专业制作质感
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, ancient city under dark control,
divided into five sectors with checkpoints, desolate streets,
sickly dark purple atmosphere #5B3A6B, oppressive hazy fog obscuring details,
people hiding in shadows, abandoned market areas, dimmed natural light,
eerie unnatural glow from unknown sources, dystopian color scheme,
buildings casting deep shadows, claustrophobic composition,
cinematic horror aesthetics, professional production quality, no white elements
```

**中文：**
```
电影截帧，2.39:1 宽屏幅，被黑暗势力控制的古代城市，
分为五个区域及检查站，空荡的街道，
病态暗紫色氛围 #5B3A6B，压抑的诡异雾霭模糊细节，
人们躲藏于阴影中，荒废的市集，自然光被削弱，
来自非自然源头的诡异微光，反乌托邦色彩方案，
建筑投射深重阴影，幽闭压抑构图，
电影恐怖美学，专业制作质感，禁用白色
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, fortified medieval city under siege,
military infrastructure and defensive structures, watchtowers and ramparts,
dark crimson and deep red color palette #8B1A1A, burning fires and
smoke clouds, dramatic backlighting from flames, soldiers in formation,
strategic command center activity, apocalyptic war atmosphere,
high contrast shadows and fire-lit zones, dramatic cinematic lighting,
destruction and fortification coexisting, no white elements,
professional production quality
```

**中文：**
```
电影截帧，2.39:1 宽屏幅，被围困的堡垒化中世纪城市，
军事基础设施与防御工事，箭塔与城墙堡垒，
暗红与深红色彩调板 #8B1A1A，烈火与烟云，
来自火焰的戏剧性逆光，士兵整队布防，
战略指挥中心的紧张活动，末日战争氛围，
高对比阴影与火光区域，戏剧性电影光影，
摧毁与防御共存，禁用白色，
专业制作质感
```

### 定达国都 (locations, ★★★★★, P2)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen. A grand palace with golden domes catching the afternoon sun, symmetrical architecture with towering columns. Formal atmosphere, clear sharp shadows, wealthy aristocrats in pristine clothing walking through marble corridors. Classical art on walls. Perfect order and control. Warm gold and cream color palette. Soft diffused light. Shot from low angle emphasizing grandeur and power.
```

**中文：**
```
Cinematic still, 2.39:1 widescreen. 壮丽的宫殿，黄金穹顶在午后阳光下闪烁，对称的建筑与高耸的石柱。正式的气氛，清晰的阴影边界，衣着精致的贵族漫步在大理石走廊。墙上装饰着古典艺术品。完美的秩序与控制。暗金与暖白的色调。柔和的扩散光线。从低角度拍摄，强调宏伟与权力。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Interior of aristocratic school, perfect rows of desks, wealthy youth in uniform sitting upright. High ceilings with intricate decorative patterns. Noon light streaming through tall windows creating geometric shadows. Clean, orderly, oppressively neat. Color palette of dark gold and cream with touches of dark purple accent. Shot from hallway perspective showing rigid discipline.
```

**中文：**
```
Cinematic still, 2.39:1 widescreen. 贵族学校内部，整齐排列的课桌，穿着制服的富家子弟坐得笔直。高挑的天花板装饰着复杂的图案。正午光线从高大的窗户倾泻而入，形成几何阴影。干净、有序、压抑的整洁。暗金与暖白的色调，点缀暗紫色。从走廊视角拍摄，显示严格的纪律。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen. City walls at golden hour, imposing fortifications with clear outlines. Uniformed guards standing at attention on ramparts, perfectly positioned. Beyond walls, distant landscape visible. Clear visibility, sense of security and control. Warm gold light casting long shadows. Emphasize the solidity and permanence of defensive structure.
```

**中文：**
```
Cinematic still, 2.39:1 widescreen. 城墙在黄金时刻，高耸的防御工事轮廓清晰。穿着制服的卫兵笔直站在城垛上。城墙外可以看到遥远的风景。视野清晰，安全与控制的感觉。暖金色光线投射长影。强调防御结构的坚固与永恒。
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Underground laboratory hidden beneath elegant building facade. Cold fluorescent lighting creating harsh shadows and unnatural pallor. Complex machinery and equipment with sinister purpose. Dark tiled walls, stainless steel surfaces. Evidence of suffering hidden in corners. Atmosphere of oppression and concealed horror. Color palette: cold white, dark purple tones. Shot from cramped perspective, claustrophobic.
```

**中文：**
```
Cinematic still, 2.39:1 widescreen. 隐藏在优雅建筑外表下的地下实验室。冷色荧光灯创造刺眼的阴影与不自然的苍白。复杂的机器与设备透露不祥意图。黑色瓷砖墙壁、不锈钢表面。苦难的痕迹隐藏在角落。压抑与隐蔽恐怖的气氛。冷白与暗紫色调。从狭窄的角度拍摄，幽闭感强烈。
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Aristocratic mansion at dusk, once opulent now showing decay. Flickering candlelight casting unstable shadows on decaying frescoes. Expensive furnishings gathering dust. Sense of hidden corruption beneath elegant surface. Doors and locks multiplying, fortress-like interior. Color palette transitioning from warm gold to sickly cream. Ominous, decaying beauty.
```

**中文：**
```
Cinematic still, 2.39:1 widescreen. 贵族宅邸在黄昏时分，曾经奢华如今开始衰败。摇晃的烛光在褪色的壁画上投射不稳定的阴影。昂贵的家具积满灰尘。优雅外表下隐藏着腐败的感觉。门锁增多，内部像堡垒。色调从温暖的金色逐渐转变为病态的奶白色。不祥的、衰败的美。
```

#### 6. 

**English：**
```
Cinematic still, 2.39:1 widescreen. City marketplace at dusk showing cracks in social order. Dim lighting, scattered fires providing uneven illumination. Crowds of common people looking anxious, speaking in hushed tones. Evidence of suppression visible: damaged storefronts, armed presence, barriers. Contrast between maintained central district and neglected periphery. Color palette: dark gold fading, touches of dark purple. Tension palpable.
```

**中文：**
```
Cinematic still, 2.39:1 widescreen. 城市集市在黄昏时分，社会秩序出现裂缝。昏暗的光线，零散的火焰提供不均匀的照明。普通民众面带焦虑，低声交谈。压制的证据随处可见：被毁的店铺、武装人员、路障。被维护的中心区与被忽视的外围形成对比。色调：暗金逐渐褪色，点缀暗紫色。紧张感十足。
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen. City walls under siege, explosions and flames consuming the fortifications. Dramatic fire light illuminating smoke-filled air. Defenders fighting desperately among rubble and wreckage. Chaos and destruction. Color palette: dark purple night sky, dark red and orange flames, ash gray. Shot from low angle showing the scale of destruction and futility of defense.
```

**中文：**
```
Cinematic still, 2.39:1 widescreen. 城墙遭受围攻，爆炸与火焰吞没防御工事。戏剧性的火光照亮烟雾弥漫的空气。防守者在瓦砾与废墟中绝望战斗。混乱与毁灭。色调：暗紫色的夜空、暗红与橙色火焰、灰色烟灰。从低角度拍摄，显示毁灭的规模与防守的徒劳。
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen. City burning at night, once-grand buildings collapsing into flames. Golden dome of palace burning like funeral pyre. Smoke obscuring most details, only silhouettes of burning structures visible. Overwhelming sense of apocalypse. Color palette: dark purple-black sky, dark red flames, orange glow, shadows. Wide establishing shot showing complete devastation.
```

**中文：**
```
Cinematic still, 2.39:1 widescreen. 夜间的城市燃烧，曾经宏伟的建筑倒塌在火焰中。宫殿的黄金穹顶燃烧如葬礼的火堆。烟雾遮挡大部分细节，只能看到燃烧建筑的轮廓。压倒性的末日感。色调：暗紫黑色的夜空、暗红火焰、橙色余光、阴影。宽幅的建立镜头显示完全的破坏。
```

#### 9. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Refugee camp within city ruins, makeshift shelters and scattered fires. Exhausted faces illuminated by firelight, families huddled together. Once-aristocratic district now filled with desperate survivors. Contrast between destroyed ornate buildings and primitive survival shelters. Color palette: dark purple night, orange firelight, dark red destruction. Close-up perspective on human suffering.
```

**中文：**
```
Cinematic still, 2.39:1 widescreen. 城市废墟内的难民营，临时搭建的庇护所与零散的篝火。疲惫的脸孔被火光照亮，家人们紧紧依偎。曾经的贵族区如今挤满了绝望的幸存者。被摧毁的精美建筑与原始生存庇护所形成对比。色调：暗紫色的夜晚、橙色火光、暗红毁灭。近距离视角捕捉人类的痛苦。
```

#### 10. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Last stronghold of palace, reinforced defenses and final line of defenders. Exhausted soldiers standing guard, wounded and weary. Fire illuminating desperate faces determined to hold ground. Combines architectural grandeur with signs of deterioration and damage. Color palette: dark purple shadows, dark red firelight, ash tones. Shot emphasizing both defiance and desperation.
```

**中文：**
```
Cinematic still, 2.39:1 widescreen. 宫殿的最后堡垒，加固的防御与最后一线守卫者。疲惫的士兵守卫，伤痕累累、精疲力尽。火光照亮决心坚守的绝望面孔。建筑宏伟与破坏迹象的结合。色调：暗紫色阴影、暗红火光、灰烬色调。拍摄强调既有的反抗与绝望。
```

### 恶灵区 (locations, ★★★★★, P2)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen. A colossal subterranean tower
structure suspended in an infinite void, filled with countless
luminescent orbs (representing souls) floating in slow, drifting motion.
The tower features 18 concentric spiral layers, each separated by
geometric crystalline energy grids glowing in deep blue-purple hues.
The dominant color palette is muted twilight blue and char-brown,
with zero natural light sources. Gravity appears non-existent. The
atmosphere is oppressive yet serene, evoking absolute order and
constraint. Central apex illuminated by a pulsing source, casting
sharp geometric shadows across the tiers. Ultra-realism with 20%
supernatural stylization in the luminous entities and energy grids.
Cinematic depth of field with shallow focus on floating orbs in
foreground. 80% photorealistic textures, 20% ethereal glow effects.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。一个巨大的地下塔状结构悬浮在无限空洞中，
塔内漂浮着无数发光球体（代表灵魂），呈缓慢漂流状。塔由18层同心螺旋环
组成，每层间隔由几何晶格能量网分隔，网格发出深蓝-暗紫光芒。主色调为
暮蓝和焦褐，完全无自然光源。重力似乎不存在。整体氛围压抑而宁静，传达
绝对的秩序感与束缚感。塔顶灵核源发出脉动光芒，投射出锐利的几何阴影。
80%写实加20%超自然风格化（体现在发光实体和能量网上）。电影级景深，
浅焦点聚焦前景漂浮的光球。80%照相级质感，20%幽灵般的辉光效果。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen. A mid-tier observation platform
extends from a massive tower interior. Millions of small luminous orbs
(souls) cluster in dense, layered formations like a living ocean. Each
orb emits a soft pale blue or warm amber light, creating a network of
overlapping glows. The crystalline energy grid behind them pulses with
narrow purple lines. The viewing platform's foreground is rendered in
dark char-brown, heavily shadowed. A solitary human silhouette stands
at the platform's edge, dwarfed by the scale. The overhead apex of
the tower fades into infinite darkness. The overall mood is one of
profound isolation and melancholic grandeur. No artificial lighting
other than the self-luminous orbs. Cinematic lighting with razor-sharp
shadows emphasizing the geometry of the grid. Color grading: desaturated,
cool-toned, with hints of twilight blue dominating the composition.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。一个中层观测平台从巨大的塔内壁伸出。数百
万个发光小球（灵魂）密集地聚集成分层结构，如同一片活体海洋。每个光球
发出柔和的冷蓝或暖琥珀光，形成重叠的光晕网络。背景的晶格能量网以狭窄
的紫色线条脉动。前景观测平台以暗焦褐色呈现，投影深重。一个孤独的人类
剪影站在平台边缘，在这巨大的尺度面前显得渺小。塔的顶部天顶向上消失在
无限的黑暗中。整体气氛为深层孤寂与悲壮宏大。除了自发光的球体外，无其他
人工光源。电影级光影，锐利的影子强调能量网的几何特征。色彩分级：去饱和、
冷调，暮蓝色主导整个构图。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Chaos descends upon the tower.
Millions of luminous orbs swirl in turbulent, chaotic patterns—some
colliding, some merging into larger entities. The energy grid flickers
erratically, its purple lines stuttering and breaking. The color palette
shifts: twilight blue fades into deep purple and sickly amber, creating
a dissonant, unsettling visual disharmony. The tower's layers are now
barely discernible as the orbs form roiling, tornado-like formations.
Luminous trails streak behind moving entities. The platform is half-
hidden in shadow and particle haze. Visual noise increases—electromagnetic
glitches, flickering light artifacts, subtle chromatic aberration. The
atmosphere transitions from serene oppression to visceral unease. Cinematic
depth of field is compromised by particle density. Color grading:
desaturated purples and burnt oranges replace the cool blues. Supernatural
glow effects intensify to 40% of visual composition.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。混沌降临塔内。数百万个发光球体在湍流状、
混乱的轨迹中旋转—有的碰撞，有的融合成更大的实体。能量网不规律地闪烁，
紫色线条断续并破裂。色彩调色盘转变：暮蓝褪去，转为深紫与病态琥珀，产生
刺耳的视觉不协和。塔的分层变得模糊，光球形成翻滚的龙卷风状队形。发光的
轨迹条纹在移动实体身后拖长。观测平台半隐于阴影与粒子雾霭中。视觉噪点
增加—电磁故障、闪烁光学伪影、微妙的色差。氛围从宁静压抑转向内脏级别
的不安。电影级景深被粒子密度破坏。色彩分级：去饱和的紫色与焦褐橙色取代
冷蓝。超自然辉光效果强化至视觉构成的40%。
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen. A catastrophic moment: the crystalline
energy grid that has held everything in place suddenly fragments. The
purple-glowing grid lines shatter like broken glass, their light strobing
wildly. For a split second, the tower fills with absolute darkness—then
brilliant, blinding white light erupts as trapped energy discharges.
Luminous orbs flicker erratically, some dimming, others blazing intensely.
The platform's geometry becomes hard to distinguish in the light chaos.
Electromagnetic visual artifacts intensify—chromatic aberration, lens flares,
ghosting effects. The color palette is now a violent clash of deep purples,
stark whites, and burnt shadows. Visual noise is extreme. The supernatural
element reaches 60% of the visual texture. A sense of imminent collapse
permeates the composition. Cinematic lighting is highly dramatic with
extreme contrast ratios.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。灾难时刻：维持一切的晶格能量网突然碎裂。
紫色发光的网格线如玻璃破碎，其光芒狂野地闪烁。瞬间，塔充满绝对黑暗—
然后受困能量释放产生的耀眼白光爆发。发光球体闪烁不定，有的变暗，有的
炽烈发光。平台的几何形态在光的混乱中难以分辨。电磁视觉伪影加剧—色差、
镜头光晕、鬼影效果。色彩调色盘现为深紫、冷白与焦黑的暴力碰撞。视觉噪点
极端。超自然元素达到视觉纹理的60%。整个构图弥漫着迫在眉睫的崩溃感。
电影级光影极度戏剧化，对比度比例极端。
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen. The apex of destruction. The tower's
entire interior is now a maelstrom of colliding energies. Millions of
luminous orbs have partially merged into several colossal, radiant entities—
some representing accumulated malice, others transcendence. The central
spirit core at the tower's peak erupts with blinding white-purple light,
its power overwhelming and absolute. Reality itself appears fractured:
the tower's structure is barely visible, dissolved in the chaos of light
and shadow. Extreme chromatic aberration, motion blur, and lens distortion
effects dominate. The color palette is now exclusively dark purples, char-
black, and searing whites—no blues or amber remain. A human silhouette,
impossibly small, stands against the tide of light. The atmosphere is one
of ultimate despair, transcendence, or annihilation. Supernatural
stylization reaches 80% of composition. Cinematic depth of field is
nearly obliterated by particle density and light intensity. Visual noise
is overwhelming but compositionally intentional, creating a sense of
sensory overload and cosmic significance.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。毁灭的顶峰。塔内部现为能量碰撞的大漩涡。
数百万个发光球体已部分融合成数个巨大的耀眼实体—有的代表累积的恶意，有的
代表升华。塔顶的中央灵核爆发出耀眼的白-紫光，其力量绝对压倒一切。现实本身
似乎破碎了：塔的结构在光与影的混乱中几不可见。极端的色差、运动模糊与镜头
扭曲效果主导。色彩调色盘现为独占的深紫、焦黑与灼热白光—不再有蓝色或琥珀。
一个人类剪影，渺小得不可思议，屹立在光潮面前。整体氛围为终极的绝望、升华或
湮灭。超自然风格化达到构图的80%。电影级景深几乎被粒子密度与光强度湮没。
视觉噪点压倒性但构图上刻意，创造感官过载与宇宙意义感。
```

#### 6. 

**English：**
```
Cinematic still, 2.39:1 widescreen. A transcendent horror: multiple massive
luminous entities have fused into a unified, singular consciousness—or perhaps
fractured into many-headed configurations. The combined entity radiates
intense purple-white light, creating a halo of smaller orbiting souls. The
tower's interior space now appears liquid, as if physics have been replaced
by pure spiritual will. Concentric rings of energy pulse outward from the
central fusion point. The platform observer is rendered in silhouette,
utterly dwarfed. Color palette: deep purples blending into searing whites,
with dark char-brown shadows. Visual effects include radial blur, energy
waves, and aura cascades emanating from the entity. The composition feels
simultaneously sacred and profane. Supernatural element comprises 70% of
visual texture. Cinematic lighting emphasizes the entity's otherworldly
dominance. The atmosphere evokes both awe and terror.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。超越的恐怖：多个巨大的发光实体融合成一个
统一的、单一的意识—或许裂变成众多头部的配置。融合实体辐射出强烈的紫-白光，
形成环绕轨道的较小灵魂光晕。塔内部空间现为液态般，仿佛物理学被纯精神意志
替代。同心圆能量脉冲从中央融合点向外扩散。平台上的观察者被渲染成剪影，
彻底渺小。色彩调色盘：深紫融入灼热白光，伴随深焦褐色阴影。视觉效果包括径向
模糊、能量波与从实体发出的光晕级联。构图同时感受到神圣与亵渎。超自然元素
构成视觉纹理的70%。电影级光影强调实体的超越性主宰。整体氛围唤起敬畏与恐怖。
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Profound silence has returned to the
tower. The catastrophic chaos has subsided. The luminous orbs are now
fewer in number but somehow more defined, their light clearer and less
frantic. A new geometric pattern emerges from the settling energy—not
identical to the previous grid, but a different harmony. The crystalline
structure slowly stabilizes into new configurations. Fewer souls remain,
but they move with deliberate intention rather than reactive chaos. The
color palette begins a slow transition: deep purples persist, but now
infused with hints of silver or amber (new hope or new melancholy?).
The tower's layers are visible again, though their arrangement differs
from before. The observation platform is bathed in gentle, diffused light.
The atmosphere is one of exhausted peace—neither triumphant nor wholly
despairing, but transcendent in a quieter register. Supernatural element
reduces to 40% as material reality reasserts itself. Cinematic lighting
is balanced, neither harsh nor overly soft. Visual noise decreases
significantly, replaced by subtle texture and depth. The composition feels
like a moment of held breath before new dawn.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。深层的寂静回归塔内。灾难性的混乱已消退。
发光的球体现在数量更少但定义更清晰，其光芒更清澈、不再疯狂。一个新的几何
图案从沉淀的能量中浮现—不与前任网格相同，而是不同的和谐。晶格结构缓慢
稳定为新的配置。幸存的灵魂更少，但以刻意的意图移动而非反应性混乱。色彩
调色盘开始缓慢过渡：深紫持存，但现被银色或琥珀色的暗示浸入（新希望或新
哀伤？）。塔的分层再次可见，虽然它们的排列与之前不同。观测平台沐浴在
温柔的、散射的光中。整体氛围为疲惫的和平—既非胜利也非完全绝望，而是
以更静谧的音调超越。超自然元素减少至视觉的40%，物质现实重新肯定自身。
电影级光影平衡，既非刺耳也非过度柔和。视觉噪点显著减少，被微妙的纹理与
深度替代。构图感受如同黎明前屏息等待的时刻。
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen. A wide establishing shot from the
observation platform. The tower stretches infinitely above and below the
observer. The luminous orbs have found new equilibrium—some ascend slowly,
some remain suspended, some descend into depths. The human figure in the
center stands in profile, gazing upward or downward—direction ambiguous,
suggesting introspection. The lighting is soft and diffused, neither the
harsh brilliance of the tower's apex nor the void of the abyss. The color
palette retains twilight blue and char-brown, but in warmer, more harmonious
ratios—perhaps 50-50, suggesting balance. The energy grid is visible but
subdued, its rhythm steady rather than frantic. The overall mood is one of
hard-won wisdom, acceptance of paradox, and profound solitude. The
supernatural element has receded to 25-30%, allowing human emotion to
dominate. Cinematic composition emphasizes scale, isolation, and introspective
depth. The atmosphere is meditative, cinematic, and deliberately ambiguous
regarding resolution. This is the still of a story that ends not with
closure, but with contemplation.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。从观测平台宽阔的全景镜头。塔向上和向下
无限延伸，观察者居中。发光球体已找到新的平衡—有些缓慢上升，有些悬浮，
有些下沉入深度。人类身影侧面站立，凝视向上或向下—方向模糊，暗示内省。
光线柔和而散射，既非塔顶的刺耳亮度也非深渊的空洞。色彩调色盘保持暮蓝与
焦褐，但以更温暖、更和谐的比例—或许50-50，暗示平衡。能量网可见但柔和，
其节奏稳定而非疯狂。整体氛围为艰难争取的智慧、悖论的接纳与深层孤寂。
超自然元素已退缩至视觉的25-30%，允许人类情感主导。电影级构图强调尺度、
孤立与内省深度。整体氛围冥想化、电影化、关于结局的故意模糊。这是一张以
沉思而非落幕结束的故事的定格。
```

#### 9. 

**English：**
```
Cinematic still, 2.39:1 widescreen. The spirit core at the tower's apex
begins its opening sequence. Its surface cracks with brilliant white-gold
light seeping through the fissures, creating a corona effect. The light
cascades downward, illuminating the interior layers in a way never before
seen. Millions of remaining souls are bathed in this new light, some
resonating in harmony, others fragmenting. The color palette shifts from
purple-dominated to gold-infused, representing a threshold moment between
two eras. The tower's structure is momentarily clear—an architectural
revelation. Visual effects include light rays cutting through particle-laden
air, creating god-rays (volumetric light). The atmosphere is one of
unveiling, of truth exposed, of hope or horror suddenly made manifest.
Cinematic lighting is theatrical and revelation-focused. Supernatural
element comprises 50% as both physical and metaphysical realms converge.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。塔顶的灵核开始其开启序列。其表面以耀眼的
白-金光从裂隙中渗出而开裂，形成日冕效应。光级联向下，以前所未有的方式
照亮内层。数百万个幸存的灵魂浴于这新光中，有的和谐共鸣，有的破裂。色彩
调色盘从紫色主导转向金色浸透，代表两个时代间的阈值时刻。塔的结构瞬间清晰
—一次建筑启示。视觉效果包括光线切割粒子充满的空气，创造上帝光线
（体积光）。氛围为揭示、真理暴露、希望或恐怖突然显现。电影级光影戏剧化
并启示聚焦。超自然元素构成50%，物质与形而上领域融合。
```

### 泊岗镇 (locations, ★★★★★, P2)

#### 1. 

**English：**
```
A bustling coastal trading town during midday. Weathered wooden docks with boats moored along the pier, fishing nets spread across stone platforms. The central market square overflows with wooden stalls and vendors selling fresh fish and vegetables, creating dense shadows. Buildings in faded mustard-brown #8B7355 line the unpaved streets. People move through the frame in various directions—fishermen, merchants, locals—bringing life and activity. The sea reflects harsh sunlight, and seagulls circle overhead. The atmosphere is crowded, noisy, and full of mundane vitality. No white light—soft golden-brown tones dominate.
```

**中文：**
```
一个沿海贸易小镇的正午时分。破旧的木制码头，渔船沿着栈道停泊，渔网铺散在石墩上。镇中心的市集广场被木板摊位密布，卖菜者和鱼贩的摊位形成深黑的阴影。建筑物呈褪色的枯草黄#8B7355，沿着泥土街道排列。人影在画面中往来穿梭——渔民、商人、镇民——带来了活力与热闹。海面反射刺眼的阳光，海鸥在上空盘旋。整体氛围拥挤、嘈杂、充满日常生命力。禁用纯白——枯草黄和棕色调主导画面。
```

#### 2. 

**English：**
```
Evening light falls across the town's market square. Long shadows of wooden stalls stretch across the ground. The old wooden warehouses and residential buildings are silhouetted against a sky transitioning from orange to deep blue #3A4A6B. A few oil lamps begin to glow warm yellow. The sea becomes still, reflecting the fading light. A few figures move slowly through the square, heading toward homes or the restaurant. The atmosphere shifts from daytime chaos to evening calm, with a hint of melancholy. Warm but cool tones blend together.
```

**中文：**
```
傍晚光线洒落在镇子的市集广场。木制摊位投出长长的阴影。旧木仓库和住宅在从橙色渐变为深蓝#3A4A6B的天空衬托下呈现剪影。几盏油灯开始发出温暖的黄色光晕。海面平静，反射着暮光。一些人影缓慢穿过广场，朝向家园或餐馆走去。氛围从白日的混乱转为傍晚的宁静，带有一丝乡愁。温暖与冷硬的色调混合交织。
```

#### 3. 

**English：**
```
A coastal town at midday, yet the light feels drained. The sky is overcast and grey, casting no clear shadows. The market square is empty—stalls toppled, goods scattered and rotting. Human figures stand motionless in unnatural postures throughout the town, their posture synchronized, their eyes wide but unfocused. The buildings retain their mustard-brown color but look sick and faded. The sea is a dull grey-green, reflecting no light. The overall tone is eerie, still, oppressive. Deep blue #3A4A6B and dark purple #5B3A6B tones creep into every shadow. No normal human movement—only the faint suggestion of collective breathing. Dread fills the frame.
```

**中文：**
```
沿海小镇的正午，但光线仿佛被吸干了。天空阴沉灰蒙，无法投出清晰的阴影。市集广场空荡荡的——摊位倒塌，商品散乱腐烂。人形傀儡在镇子各处无动于衷地站立，姿态诡异一致，眼睛睁得很大但无焦点。建筑物保留着枯草黄色调，但显得病态而褪色。海面呈灰绿色，不反射光线。整体基调诡异、静寂、压抑。深蓝#3A4A6B和暗紫#5B3A6B的色调渗入每个阴影。没有正常的人类活动——只有模糊的集体呼吸感。恐怖笼罩整个画面。
```

#### 4. 

**English：**
```
Night in the cursed town. Figures stand in rows facing the old wooden dock, their silhouettes barely visible against the dark purple #5B3A6B background. The few remaining lights (oil lamps) seem weak and isolated, unable to dispel the surrounding darkness. The sea at night is black, reflecting nothing. A faint, inexplicable luminescence seems to emanate from the direction of the dock itself. No sound suggested by the image, yet oppressive silence is implied. The collective breathing of the townspeople—invisible but felt—fills the atmosphere. A sense of wrongness permeates the scene. Reality feels corrupted.
```

**中文：**
```
诅咒小镇的夜晚。人形傀儡成排地面向老码头站立，它们的剪影在暗紫#5B3A6B的背景中几乎无法辨认。仅有的灯光（油灯）显得微弱而孤立，无法驱散周围的黑暗。夜晚的海呈绝对的黑色，毫不反射光线。某种难以名状的光芒仿佛从码头方向发出。画面中没有声音提示，但压抑的寂静被隐喻。镇民的集体呼吸——无形却能感知——充满整个氛围。一种难以名状的诡异感渗透整个场景。现实显得被腐蚀了。
```

#### 5. 

**English：**
```
A small coastal town transformed into a military stronghold. The market square is now occupied by canvas tents arranged in precise rows, military flags flying. Wooden barricades and defensive structures of grey #4A4A4A dominate the foreground. Armed soldiers stand patrol or work on fortifications. The original mustard-brown buildings are now dwarfed and obscured by military infrastructure. The old docks are converted into a military landing point with reinforced pilings and supply piles. The atmosphere is one of occupation and control—rigid, orderly, oppressive. Cold grey and dark tones replace the warm earth-browns. Flags, banners, and military insignia mark the transformation. This is no longer a town; it is a fortress.
```

**中文：**
```
小镇被改造成军事要塞。市集广场现在被精确排列的军用帐篷占据，军旗飘扬。木制的防御工事和灰色#4A4A4A的堡垒结构占据前景。武装士兵在巡查或进行防御工程。原来的枯草黄建筑被军事基础设施遮挡并显得渺小。老码头被改建成带有加固木桩和物资堆积的军事登陆点。氛围是占领与控制——刻板、有序、压抑。冷硬的灰色和暗色调取代了温暖的土黄。旗帜、横幅和军事标识标记了这一变化。这不再是一个镇子；它是一个堡垒。
```

#### 6. 

**English：**
```
War-torn coastal town at dusk. Military fires and torches illuminate the makeshift camp scattered across what was once a vibrant market. Smoke rises from various points. Soldiers move efficiently through the scene, carrying supplies or standing watch. The few remaining civilians are visible in the background, compressed into marginal spaces. Rubble mixes with military equipment. The light is harsh and cold, casting sharp shadows. The sea in the distance is now irrelevant—the human drama of occupation and survival dominates. Dark grey #4A4A4A, dark purple #5B3A6B, and the lingering earth-tones create a vision of subjugation. The town's original character has been erased; only warfare remains.
```

**中文：**
```
战争蹂躏过的沿海小镇在黄昏时分。军营的火焰和火把照亮了散布在曾经繁忙市集上的临时营地。烟雾从多个地点升起。士兵高效地穿行于场景中，搬运物资或站岗。少数留下的民间人口在背景中可见，被压缩到边缘空间。废墟与军事设备混杂在一起。光线是刺眼而冷硬的，投出锐利的阴影。远处的海变得无关紧要——人类的占领与生存戏剧主导了一切。暗灰#4A4A4A、暗紫#5B3A6B和挥之不去的土黄色调创造了一幅被奴役的景象。小镇原有的特征已被抹去；只有战争仍在继续。
```

### 牛台山 (locations, ★★★★★, P2)

#### 1. 提示词1：泉水源头（宁静期） [泉水源头（宁静期）]

**English：**
```
Cinematic still, 2.39:1 widescreen. A pristine mountain spring pool
nestled deep in an ancient forest. Crystal-clear circular pond fed by
mountain spring from rocky crevice, surrounded by moss-covered boulders
and dense verdant canopy. Ethereal light filtering through leaves creates
dancing golden-green dapple patterns on water surface. Faint mist rising
from cool spring. Tranquil atmosphere with hints of hidden mystery.
Color palette: moss green, ochre earth tones, deep forest shadows.
Shot from 50mm lens perspective at water level, mirror-like reflection
of overhanging branches on glassy water surface.
```

**中文：**
```
电影质感静帧，2.39:1超宽银幕。深藏于古老山林中的清澈山泉池。
圆形泉池晶莹透明，由岩缝涌出的泉水注入，周围苔藓覆盖的卵石与
密集翠绿的树冠环绕。透过叶隙的柔和光线在水面形成舞动的金绿色
光斑。淡淡雾气自清冷泉水升起。宁静祥和的氛围中暗藏神秘感。
色彩：苔绿、焦褐土色、深林阴影。50mm焦距水面平视视角，树枝
在镜面般的水面完美倒映。
```

#### 2. 提示词2：美女榕（灵气汇聚） [美女榕（灵气汇聚）]

**English：**
```
Cinematic still, 2.39:1 widescreen. Ancient banyan tree with sprawling
dense canopy creating natural cathedral in heart of misty mountain forest.
Thousand-year-old gnarled trunk with aerial roots forming labyrinthine
patterns. Ethereal quality of dappled sunlight piercing through layered
leaves, illuminating floating dust particles. Mystical atmosphere with
palpable spiritual energy. Surrounding understory plants lean toward the
ancient tree as if in reverence. Moss and ferns carpet the ground.
Color palette: deep moss green, golden amber light, dark bronze shadows.
Shot from 35mm, wide depth of field, tree occupies center-frame.
```

**中文：**
```
电影质感静帧，2.39:1超宽银幕。古老榕树横展繁密树冠，在雾气
缭绕的山林深处形成天然殿堂。千年老树扭曲树干与气生根构成繁
复的迷宫般纹理。层层叶片间透出的柔和光线照亮浮尘，呈现空灵
质感。可感知的灵气充盈空间。周边植被仿佛朝拜般向古树倾倾。
苔藓与蕨类铺陈地面。色彩：深苔绿、金琥珀光、深青铜阴影。
35mm焦距，宽景深，树木占据画幅中央。
```

#### 3. 提示词3：老吴小屋（温暖与隐蔽） [老吴小屋（温暖与隐蔽）]

**English：**
```
Cinematic still, 2.39:1 widescreen. Weathered wooden cottage nestled
among dense mountain vegetation, almost camouflaged into forest. Smoke
gently rising from chimney, visible from distance. Warm amber light
spilling from windows into surrounding gloom. Hand-built wooden structure
showing age and character, weathered by decades. Small clearing around
cottage with evidence of simple life: firewood stacked, clothes drying,
tools scattered. Fading afternoon light creates contrast between warm
interior glow and deepening forest shadows. Color palette: warm browns,
amber glow, forest moss green transitioning to deep shadows. Shot from
distance through trees, human scale emphasized by surrounding vastness.
```

**中文：**
```
电影质感静帧，2.39:1超宽银幕。古旧木质小屋隐没于密集山林植被
之中，几近与森林融为一体。烟囱升起缕缕炊烟，在远处可见。温暖
琥珀色灯火从窗户泻出，照亮周围昏暗。手工木质建筑显露岁月沧桑，
经数十年风雨侵蚀。小屋周围的空地见证简朴生活：堆积的柴火、晾
晒的衣物、散落的工具。午后暖光强化了温暖室内与深重林影的对比。
色彩：温暖褐色、琥珀光、苔绿逐渐转入深阴影。距离外隔着树木的
视角，周围浩瀚森林强调了小屋的人类尺度。
```

#### 4. 提示词4：秘密仓库（危险与压抑） [秘密仓库（危险与压抑）]

**English：**
```
Cinematic still, 2.39:1 widescreen. Hidden cave entrance camouflaged
by overhanging rocks and dense vegetation on mountainside. Concealed
mouth barely visible in shadow. Interior darkness suggesting vast unknown
depth. Minimal natural light at threshold creates high contrast between
outside world and impenetrable interior. Cold stone surfaces, metallic
glint suggesting stored artifacts or weapons. Oppressive atmosphere with
palpable danger. Occasional water drips echo in unseen depths. Color
palette: cold grays, dark browns, near-black interior, minimal blue-gray
exterior light. Shot from distance among trees, entrance almost
imperceptible, evoking mystery and dread.
```

**中文：**
```
电影质感静帧，2.39:1超宽银幕。隐蔽的洞穴入口被悬垂岩石与密集
植被伪装在山腰。洞口在阴影中几乎不可见。内部黑暗暗示着无尽深
渊。入口处的微弱光线与无法穿透的内部形成极端对比。冷硬的石面、
金属光泽暗示存储的物品与武器。压抑的氛围充盈危险感。水滴声音
在无形深处回响。色彩：冷灰、深棕、近黑的内部、微弱蓝灰的外部
光。距离间隔树木的视角，入口近乎隐形，唤起神秘与恐惧。
```

#### 5. 提示词5：牛台山整体俯瞰（战略期全景） [牛台山整体俯瞰（战略期全景）]

**English：**
```
Cinematic still, 2.39:1 widescreen. Aerial view of vast mountain landscape
with dense forest canopy covering complex terrain. Multiple hidden valleys,
hidden streams cutting through woodland, singular massive ancient tree
(banyan) visible as landmark in sea of green. Small weathered cottage
barely perceptible in middle distance. Mountain slopes rising toward hazy
summit. Layered depth of forest receding into atmospheric perspective.
Overcast light creating moody, strategic atmosphere. Color palette:
dominant moss green with variations of olive and forest shadows, brown
earth tones visible on slopes, cold overcast sky. Shot from 300-400 meter
altitude, perspective emphasizing vastness and strategic complexity.
```

**中文：**
```
电影质感静帧，2.39:1超宽银幕。广阔山地的航拍视角，密集森林树冠
覆盖复杂地形。多个隐蔽山谷、溪流蜿蜒切割林海、一棵孤立的巨大古
榕树作为绿色海洋中的标志物清晰可见。小的古旧木屋在中远景几乎难以
察觉。山坡向着雾霭笼罩的山顶逐渐上升。森林的分层深度在空气透视中
递进。阴沉的光线营造压抑的战略氛围。色彩：主导的苔绿与橄榄、林影
的深度变化，山坡可见的褐色土质，冷调阴沉天空。300-400米高度俯视，
视角强调了浩瀚与战略的复杂性。
```

#### 6. 提示词6：牛台山雨夜（战略期转折） [牛台山雨夜（战略期转折）]

**English：**
```
Cinematic still, 2.39:1 widescreen. Mountain forest in heavy rainfall at
night, moody and ominous atmosphere. Rain sheets visible in minimal moon
light breaking through thick clouds. Water cascades down steep slopes,
swollen stream rushes with violent force. Ancient banyan tree silhouetted
against lightning flash. Small cottage light visible as sole warmth in
infinite darkness. Mist and rain meld into monochromatic palette.
Danger and urgency palpable. Color palette: dark blue-grays, near-black
shadows, cold white lightning illumination, warm cottage amber barely
visible. Shot from ground level among trees, wide lens capturing torrential
rain and sense of being overwhelmed by natural forces.
```

**中文：**
```
电影质感静帧，2.39:1超宽银幕。夜晚的山林暴雨场景，压抑而不祥。
微弱月光透过厚重乌云映照雨幕。水流沿陡坡奔泻，肿胀的溪流暴怒奔
腾。古榕树在闪电一瞬被勾勒成剪影。小屋灯火成为无尽黑暗中唯一的
温暖。雾气与雨幕融合成单色调。危险与急迫感充盈。色彩：深蓝灰、
近黑的阴影、冰冷的闪电白光、勉强可见的温暖琥珀屋光。地面低角度
穿行树木的视角，超广角镜头捕捉倾盆大雨与被自然力量淹没的感受。
```

#### 7. 提示词7：牛台山黎明（回归期新生） [牛台山黎明（回归期新生）]

**English：**
```
Cinematic still, 2.39:1 widescreen. Mountain forest at dawn, moment of
transition between night and day. First golden light breaks over eastern
ridge, illuminating mist rising from forest floor and streams. Deep forest
shadows still dominant but gradually yielding to growing light. Spring pool
catches first rays, surface glowing with promise. Ancient tree backlit,
becoming silhouette transitioning to solid form as light grows. Quiet
stillness after night, before day awakens. Atmosphere of renewal and
reckoning. Color palette: deep indigo and dark green gradually shifting to
gold and warm amber at horizon, transitional gray tones. Shot from valley
floor looking east, wide depth of field, emphasis on emerging light and
atmospheric depth.
```

**中文：**
```
电影质感静帧，2.39:1超宽银幕。黎明时分的山林，夜与昼的过渡时刻。
首缕金光越过东方山脊，照亮升起自林地与溪流的晨雾。深林阴影仍占
主导，但逐渐向增长的光线退让。泉水池塘捕捉首道光线，水面泛起希望
的光芒。古榕树逆光成剪影，随光线增强而逐渐转为实体。夜后的静寂，
日未醒时的宁静。重生与清算的氛围。色彩：深靛蓝与深绿逐渐转向地平
线处的金色与温暖琥珀，过渡的灰色调。从山谷地面向东看，宽景深，强
调新生的光线与空气深度。
```

#### 8. 提示词8：牛台山的灵气表现（超自然元素） [牛台山的灵气表现（超自然元素）]

**English：**
```
Cinematic still, 2.39:1 widescreen. Mountain forest with subtle supernatural
elements. Ancient spiritual energy manifests as faint luminescent mist
coalescing around massive banyan tree and spring pool. Light appears to
flow upward against gravity in certain areas. Air shimmers with otherworldly
quality. Colors seem more saturated and vivid than possible in nature -
deep greens almost glowing, water surface with ethereal phosphorescence.
Regular forest soundscape interlaced with high-frequency harmonic tones
barely perceptible to conscious mind. Boundary between material and spiritual
world appears gossamer-thin. Color palette: impossible vibrant greens,
silver-blue luminescence, golden light with supernatural quality, ambient
glow. Shot with wide lens, slight lens flare and optical distortion suggesting
higher dimensional presence.
```

**中文：**
```
电影质感静帧，2.39:1超宽银幕。山林中隐约呈现的超自然元素。古老的
灵气以微弱的发光雾气形式显现，在巨大榕树与泉池周围凝聚。光线在某
些区域逆重力向上流动。空气闪烁着非此世的质感。色彩的饱和度与生动
程度超越自然可能——深绿近乎发光，水面显现空灵的磷光。常规的林地
声景中混织着可觉察边界之外的高频谐音。物质与精神世界的边界如薄纱。
色彩：不可能的艳丽绿色、银蓝色发光、超自然质感的金色光、环境发光。
超广角镜头拍摄，轻微镜头光晕与光学扭曲暗示更高维度的存在。
```

### 美女榕 (locations, ★★★★★, P2)

#### 1. 提示词1：基础场景描述（通用所有阶段） [基础场景描述（通用所有阶段）]

**English：**
```
Cinematic still, 2.39:1 widescreen.
Ancient banyan tree with massive twisted roots resembling a reclining woman's figure, head, torso, and limbs spread across the ground. The tree canopy is impossibly dense, creating a natural cathedral ceiling that blocks out most daylight. Thick moss and lichen cover the gnarled bark. The roots form intricate networks with deep crevices. Atmospheric, mystical, ancient, primordial. Cinematic lighting. Shot on 50mm lens.
```

**中文：**
```
电影截图，2.39:1 宽屏。
古老的榕树，根系粗壮，形似仰卧女性的躯体——头部、躯干、四肢分布于地面。树冠密集巨大，形成天然教堂般的穹顶，几乎完全遮挡日光。树皮沧桑，覆盖厚重苔藓和地衣。根系纵横交错，形成深邃的裂隙。大气、诡异、古老、原始感。电影感光影。50mm镜头拍摄。
```

#### 2. 提示词2：阶段一：默认状态（平静） [阶段一]

**English：**
```
Cinematic still, 2.39:1 widescreen.
Ancient banyan tree with roots like a reclining woman, covered in moss and aged lichen. Scattered dappled sunlight filters through the dense canopy, creating patches of warm golden light on the moss-covered roots and dark earth. Cool moss-green and deep brown color palette. Natural, serene atmosphere, but with an underlying sense of age and mystery. Earthy humidity visible in the air. Shot on 50mm lens, f/5.6.
Color palette: moss-green (#4A6741), burnt brown (#2C1810), warm gold light.
```

**中文：**
```
电影截图，2.39:1 宽屏。
古老榕树，根系形如仰卧女性，覆盖苔藓和年代久远的地衣。零散的金黄色阳光透过茂密树冠洒下，在苔藓根系和深色土壤上形成光斑。苔藓绿色（#4A6741）和焦褐色（#2C1810）为主色调。自然、寂静的氛围，但隐含着深层的年代感和神秘感。空气中弥漫泥土的潮湿感。50mm镜头，f/5.6光圈拍摄。
主色调：苔绿、焦褐、暖金色光。
```

#### 3. 提示词3：阶段二：通道开启期（激活初期） [阶段二]

**English：**
```
Cinematic still, 2.39:1 widescreen.
Ancient banyan tree with roots forming a reclining female figure. Ethereal dark purple and violet bioluminescence begins to glow from within the root system, creating an otherworldly contrast with the natural environment. The tree seems to breathe. Moss-green and dark purple color palette with hints of cold blue light emanating from deep root crevices. Temperature drops. Subtle supernatural atmosphere, time feels distorted. Shot on 50mm lens, f/4.
Color palette: moss-green (#4A6741), dark purple (#5B3A6B), cold blues, burnt brown (#2C1810).
```

**中文：**
```
电影截图，2.39:1 宽屏。
古老榕树，根系形似仰卧女性躯体。从根系深处泛出幽深的紫色和紫罗兰色的生物荧光，形成与自然环境的超现实对比。树体似乎在呼吸。苔藓绿色（#4A6741）与暗紫色（#5B3A6B）为主色调，根系缝隙泛出冷蓝色光芒。温度骤降。开始出现超自然氛围，时间感扭曲。50mm镜头，f/4光圈。
主色调：苔绿、暗紫、冷蓝、焦褐。
```

#### 4. 提示词4：阶段二续：通道开启期（激活加强） [阶段二续]

**English：**
```
Cinematic still, 2.39:1 widescreen.
Ancient banyan tree with roots resembling a reclining woman, now visibly pulsing with dark purple and violet light. The bioluminescence intensifies, creating dramatic shadows and highlights on the root textures. The roots appear almost vein-like, as if alive. Cold supernatural glow dominates over natural sunlight. Atmosphere is increasingly eerie and hypnotic. The boundary between the physical and supernatural becomes visible. Shot on 50mm lens, f/4.
Color palette: dominant dark purple (#5B3A6B), deep moss-green (#4A6741), cold whites and deep blues.
```

**中文：**
```
电影截图，2.39:1 宽屏。
古老榕树，根系形似仰卧女性，现在清晰地闪烁着深紫色和紫罗兰色的光芒。生物荧光增强，在根系纹理上形成戏剧性的光影对比。根系如血管般蠕动，仿佛活物。冷色超自然光线完全压制自然光。氛围越来越诡异与催眠性。物质世界与超自然界的边界变得可见。50mm镜头，f/4光圈。
主色调：主导暗紫（#5B3A6B）、深苔绿（#4A6741）、冷白和冷蓝。
```

#### 5. 提示词5：阶段三：终局期（最高激活） [阶段三]

**English：**
```
Cinematic still, 2.39:1 widescreen.
Ancient banyan tree completely transformed. Roots resembling a reclining woman glow intensely with dark purple and violet light, as if veins carrying primordial energy. The tree pulses with life and otherworldliness. Supernatural light completely overwhelms the natural environment. The roots appear three-dimensional, almost translucent, revealing shadowy passages into an unseen underworld. Apocalyptic, transcendent, reality-bending atmosphere. The two worlds intersect visibly. Shot on 50mm lens, f/2.8.
Color palette: dominant dark purple (#5B3A6B), deep indigo, cold blues, occasional amber highlights, burnt brown shadows (#2C1810).
```

**中文：**
```
电影截图，2.39:1 宽屏。
古老榕树完全变态。根系形似仰卧女性，发出强烈的深紫色和紫罗兰色光芒，仿佛远古能量的血管。树体以生命的节奏脉动，既古老又超自然。超自然光线完全压倒自然环境。根系变得近乎透明，三维感极强，隐约透露出通向冥界的隐秘通道。启示录感、超越感、现实崩塌感。两个世界在此交汇。50mm镜头，f/2.8光圈。
主色调：主导暗紫（#5B3A6B）、深靛蓝、冷蓝、琥珀色亮点、焦褐阴影（#2C1810）。
```

#### 6. 提示词6：特殊：俯瞰视角 [特殊]

**English：**
```
Cinematic still, 2.39:1 widescreen aerial overhead shot.
Ancient banyan tree with the complete root system visible from above, forming the distinct shape of a reclining woman's body - head sphere at north, torso at center, limbs extending outward. Massive tree canopy surrounds and frames the roots. Viewpoint as if floating high above. Emphasizes the surreal, supernatural scale of the landscape. Mystical and ancient atmosphere.
```

**中文：**
```
电影截图，2.39:1 宽屏俯瞰全景。
古老榕树，从上方俯视整个根系，清晰地呈现仰卧女性的轮廓——北侧球形头部、中央躯干、向外延伸的四肢。巨大的树冠围绕并框架化根系。视角如同悬浮于高空。强调超现实、超自然的地理尺度。诡异古老的氛围，令人敬畏。
```

#### 7. 提示词7：特殊：深层通道视角 [特殊]

**English：**
```
Cinematic still, 2.39:1 widescreen downward perspective.
Looking down into the cavernous space created by the ancient banyan's root system descending into darkness. The roots act as a natural tunnel toward an otherworldly underworld. Purple and violet bioluminescence gradually fades to deeper indigo and black as the roots descend. Claustrophobic yet infinite. Cold, supernatural, primordial atmosphere. The viewer feels both pulled toward and repelled from the depths.
```

**中文：**
```
电影截图，2.39:1 宽屏俯视视角。
俯视古老榕树的根系形成的天然洞穴，向下延伸至无尽黑暗。根系如隧道般指向超自然的冥界。紫色和紫罗兰色的生物荧光逐步消褪至深靛蓝和纯黑。幽闭感与无限感并存。冷色、超自然、原始感。观看者同时感到被吸引与被排斥的矛盾。
```

### 荣康城 (locations, ★★★★★, P2)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, medieval fortified city at full readiness.
Towering double walls of pale brick and stone (#8B7355 ochre tone),
watchtowers with lit beacon fires casting long shadows.
Wide moat (10 meters) surrounds the city, murky water reflecting evening sky.
Soldiers in formation atop walls, banners fluttering.
Academic buildings visible within inner city, organized and controlled.
Golden hour lighting, warm amber tones, clear visibility.
Military precision, calm before storm, scholarly order coexists with martial readiness.
Cinematic color grading, deep shadows, heroic composition.
```

**中文：**
```
电影质感截图，2.39:1 宽屏画幅，中世纪要塞城市全面防御状态。
高耸的双层砖石城墙（#8B7355 枯草黄色调），顶部可见巡逻卫兵。
瞭望塔上燃起信号火盆，光线拉长士兵影子，显示战备状态。
宽达10米的护城壕沟环绕全城，水面平静，倒映暮色。
城墙顶部士兵整齐排列，旗帜猎猎飘扬，弓手拉弦。
城内学术建筑清晰可见，秩序井然，军民各司其职。
金色时刻光线，温暖琥珀调，能见度高。
军事精准感与学术秩序并存，宁静却紧张，风暴前的平静。
电影级色彩分级，深邃阴影，英雄主义构图。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, fortified city under infiltration and chaos.
Double walls still standing but cracked and scarred, sections damaged.
Dark red (#8B1A1A) fire spreading across multiple districts within the city.
Smoke rising from breached sections, visibility increasingly obscured.
Soldiers in disarray, some fighting on walls, some fleeing into inner city.
Academy buildings showing signs of conflict, windows dark or flickering with fire.
Moat waters disturbed, wooden spikes visible at breach points.
Color palette shifts to warm ochre (#8B7355) corrupted by deep red (#8B1A1A) flames.
Tension and uncertainty dominate; defense lines fragmented; shadows deepen dramatically.
Cinematic tension, layered smoke effects, fragmented lighting.
```

**中文：**
```
电影质感截图，2.39:1 宽屏画幅，要塞城市陷入内部渗透与混乱。
双层城墙依然屹立但出现裂纹与伤口，部分防线受损。
暗红色 #8B1A1A 火焰在城内多个区域蔓延。
浓烟升起，能见度急剧下降，白天与黄昏界限模糊。
士兵陷入混乱，部分在城墙顶部苦战，部分逃向内城。
学术建筑显示交战迹象，窗户昏暗或闪烁火光。
护城壕沟水面翻腾，水下尖桩在破口处暴露。
色彩调色盘从枯草黄 #8B7355 向暗红 #8B1A1A 倾斜，火焰色扩大。
紧张与不确定感主导；防线分化；阴影急剧加深。
电影级紧张感，多层烟雾效果，破碎光线。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, fortified city in final collapse and devastation.
Double walls partially destroyed, large breaches visible, rubble everywhere.
Dark purple (#5B3A6B) sky suffocates the city, twilight-like atmosphere persists at all hours.
Massive fires engulf entire districts, thick black smoke obscures visibility.
Invading forces pour through breached gates, city completely overrun.
Few remaining defenders make last stand in inner city, badly outnumbered.
Moat waters choked with debris, city walls crumble into it.
Color is dominated by deep purple (#5B3A6B) haze, dark reds (#8B1A1A) of intense flames, blacks of destruction.
NO WHITE (#FFFFFF) anywhere - absolute darkness where hope should be.
Cinematic apocalyptic devastation, extreme contrast, day/night completely lost.
```

**中文：**
```
电影质感截图，2.39:1 宽屏画幅，要塞城市陷入最终崩溃与废墟。
双层城墙大部分摧毁，出现巨大缺口，废墟遍布。
暗紫色 #5B3A6B 天空笼罩全城，类似黄昏的压抑光线昼夜不变。
巨大火焰吞没整个城区，浓黑烟雾阻挡视线。
入侵军队从破口处涌入，城市完全沦陷。
仅存的少数守军在内城进行绝望的最后抵抗，人数严重不足。
护城壕沟被碎石与尸体填满，城墙坍塌入水。
色彩主调：暗紫 #5B3A6B 的雾霾、暗红 #8B1A1A 的烈火、黑色的毁灭。
禁止任何白色 #FFFFFF —— 希望消亡的地方。
电影级末日废墟，极端对比，昼夜概念彻底消失。
```

### 威刚 (characters, ★★★★, P3)

#### 1. 

**English：**
```
Portrait of a lean Chinese man in his late 30s, front view from chest up. Thin angular face with slightly prominent cheekbones, clean-shaven. Deep dark eyes that appear ordinary but carry an almost imperceptible depth beyond normal human range — a subtle transcendent quality. Skin pale and clean, not weathered like a typical servant. Hair pulled back in simple low knot, practical and unadorned. Wearing plain dark navy-blue (#1A1A3E) servant's short robe with simple cloth belt, no decorations. Expression calm, composed, and inscrutably neutral — neither servile nor commanding. A thin silver-white (#C0C0C0) bracelet/band visible on one wrist — the only distinctive accessory. Dark neutral background. Photorealistic Chinese historical portrait, soft even lighting that does not draw attention to the subject — reflecting his hidden nature. Shot with 85mm equivalent lens, shallow depth of field.
```

**中文：**
```
瘦削中国男性正面半身像，年约三十多岁末。清瘦棱角分明的面容，颧骨微突，面部干净无须。深色瞳孔看似普通但携带几乎不可察觉的超越凡人范畴的深邃——微妙的超凡质感。皮肤白净干净，非典型仆人的风吹日晒质感。头发向后束成简单低髻，实用而无装饰。穿着朴素深藏蓝色（#1A1A3E）仆人短褐配简单布腰带，无任何装饰。表情平静、沉稳、不可捉摸的中性——既不卑微也不威严。一只手腕上可见一条细银白色（#C0C0C0）手环/带——唯一的特殊配饰。深色中性背景。写实中国古代肖像风格，柔和均匀照明不引人注目——映射其隐藏的本质。等效85mm镜头，浅景深。
```

#### 2. 

**English：**
```
Three-quarter view portrait of a lean Chinese man in his late 30s, from chest up. Head slightly turned showing angular profile with thin cheekbone line and clean jawline. One deep dark eye visible, catching a subtle gleam of light that hints at something beyond mortal — not supernatural glow, just an unusual depth of intelligence and presence. Hair in simple low knot, dark navy-blue (#1A1A3E) servant robe collar visible. Neck tendons lean and defined. Expression of quiet watchfulness — observing everything while appearing to notice nothing. Silver-white (#C0C0C0) wrist band partially visible. Dark neutral background. Photorealistic, subtle Rembrandt lighting with gentle shadow on far side — minimal drama, reflecting character's desire to remain unnoticed. Shot with 85mm equivalent lens.
```

**中文：**
```
瘦削中国男性四分之三侧面半身像，年约三十多岁末。头部微转展示清瘦颧骨线和干净颌线的棱角轮廓。一只深色眼睛可见，捕捉到一丝微妙的光芒暗示超越凡人的存在——并非超自然发光，只是不寻常的智慧与存在深度。简单低髻发型，深藏蓝色（#1A1A3E）仆人短褐衣领可见。颈部肌腱精瘦分明。安静警觉的表情——观察一切却看似毫无注意。银白色（#C0C0C0）手腕环带部分可见。深色中性背景。写实风格，微妙伦勃朗式布光在远侧形成柔和阴影——最小戏剧性，映射角色不被注意的愿望。等效85mm镜头。
```

#### 3. 

**English：**
```
Pure side profile portrait of a lean Chinese man in his late 30s, from chest up. Side view reveals clean angular silhouette: simple low hair knot, smooth forehead, slightly prominent brow, deep-set eye in profile, straight nose bridge, thin neutral lips, lean defined jaw, long neck with visible tendons. Wearing plain dark navy-blue (#1A1A3E) servant robe, collar sharp against neck. Silver-white (#C0C0C0) wrist band visible below sleeve hem. Overall silhouette unremarkable yet subtly elegant — the paradox of a divine being in servant's clothing. Dark neutral background. Photorealistic, edge lighting creating thin bright rim on profile to subtly suggest hidden inner light. Shot with 85mm equivalent lens.
```

**中文：**
```
瘦削中国男性纯正侧面半身像，年约三十多岁末。侧面展示干净棱角的轮廓剪影：简单低髻，光滑额头，微突眉骨，侧面深眼窝，直挺鼻梁，薄而中性的嘴唇，精瘦分明的颌线，可见肌腱的长颈。穿着朴素深藏蓝色（#1A1A3E）仆人短褐，衣领在颈部形成利落线条。银白色（#C0C0C0）手腕环带在袖口下方可见。整体轮廓不起眼却微妙优雅——神级存在穿着仆人衣物的悖论。深色中性背景。写实风格，边缘光在轮廓上形成细薄明亮轮廓线以微妙暗示内在隐藏之光。等效85mm镜头。
```

#### 4. 

**English：**
```
Full body front view of a lean Chinese man in his late 30s standing in natural relaxed posture. Height approximately 180cm, thin wiry build with long limbs and natural grace. Wearing complete plain dark navy-blue (#1A1A3E) servant outfit: short robe reaching mid-thigh, simple cloth belt at waist, darker trousers underneath, plain cloth shoes suitable for silent movement. Silver-white (#C0C0C0) band/bracelet on left wrist — the only accessory. Arms at sides in non-threatening posture. Hair in simple low knot. Face calm and neutral. Overall impression: completely forgettable servant that you would pass without noticing — yet something indefinably refined about his proportions and bearing. Dark neutral background. Photorealistic Chinese historical figure, full-body even lighting emphasizing ordinariness. Shot with 35mm equivalent lens.
```

**中文：**
```
瘦削中国男性全身正面像，年约三十多岁末，以自然放松姿态站立。身高约180cm，精干纤细体型，四肢修长带有天然优雅感。穿着完整朴素深藏蓝色（#1A1A3E）仆人装束：短褐至大腿中部，简单布腰带束腰，内穿深色裤子，朴素布鞋适合无声移动。左手腕银白色（#C0C0C0）环带/手镯——唯一配饰。双臂自然垂于身侧，非威胁姿态。简单低髻发型。面部平静中性。整体印象：一个完全不起眼的仆人，擦肩而过不会注意——然而其身体比例和气度有一种不可名状的精致。深色中性背景。写实中国古代人物风格，全身均匀照明强调平凡性。等效35mm镜头。
```

#### 5. 

**English：**
```
Lean Chinese servant in his late 30s walking through a crowded city street at night, blending perfectly with ordinary people. Wearing plain dark navy-blue (#1A1A3E) servant short robe with cloth belt, cloth shoes. Thin silver-white (#C0C0C0) wrist band barely visible under sleeve. Face calm and unremarkable, moving through crowd without drawing any attention. Slightly moonlit scene with warm lantern light from nearby shops casting orange glow on street. Other servants and merchants around him appear more noticeable than he does — he is deliberately the least visible person in the frame. Atmosphere of hidden power within mundane disguise. Photorealistic Chinese historical street scene, cinematic night lighting, 80% realism + 20% supernatural stylization — the supernatural element being his almost unnatural ability to vanish into a crowd.
```

**中文：**
```
瘦削中国仆人，年约三十多岁末，夜间穿行于拥挤城市街道，与普通人完美融合。穿朴素深藏蓝色（#1A1A3E）仆人短褐配布腰带，布鞋。细银白色（#C0C0C0）手腕环带在袖口下勉强可见。面部平静不起眼，穿过人群不引起任何注意。微弱月光场景配合近处店铺暖色灯笼光在街面投射橙色光晕。周围其他仆人和商人比他更显眼——他刻意成为画面中最不可见的人。隐藏力量于平凡伪装中的氛围。写实中国古代街道场景，电影级夜间照明，80%写实+20%超自然风格化——超自然元素在于其几乎非自然的融入人群能力。
```

#### 6. 

**English：**
```
Massive semi-transparent glowing humanoid figure rising from churning water in a deep city moat at night, towering above 50-meter city walls. Figure height approximately 20-30 meters, maintaining human proportions but scaled to giant size. Entire body emitting warm white light (#FFF8DC), semi-transparent with faint visibility of background structures through the form. Eyes blazing with intense royal blue light (#4169E1) like twin searchlights cutting through darkness. White light burst emanating from crown of head — the transformation trigger point. Water cascading off the luminous form as it rises. One massive glowing hand lifting a huge rope bridge mechanism from underwater. Enemy archers on city wall firing arrows that dissolve harmlessly upon contact with the light body. Surrounding water surface lit from below by the glow, creating ethereal reflection. Atmosphere of divine revelation — the servant's true nature finally exposed. Photorealistic with supernatural elements, cinematic dramatic lighting where the figure IS the primary light source, 80% realism + 20% supernatural stylization following Eastern aesthetic of restrained divine manifestation.
```

**中文：**
```
巨大半透明发光人形从翻涌的城池深沟水面中升起，夜间场景，高度远超50米城墙。人形高约20-30米，保持人类身体比例但放大至巨型。全身散发温暖白光（#FFF8DC），半透明质感可隐约透过形体看到背景建筑。双眼燃烧着强烈的皇家蓝色光芒（#4169E1），如两盏探照灯切穿黑暗。头顶冠部爆发白光——变身触发点。水流从发光体上倾泻而下。一只巨大发光手掌从水下举起巨型悬梯机关。城墙上敌军弓箭手射出的箭矢在接触光体时无害消融。周围水面被下方光芒照亮形成空灵倒影。神性揭示的氛围——仆人的真实本质终于暴露。写实风格带超自然元素，电影级戏剧性照明，人形本身即主要光源，80%写实+20%超自然风格化，遵循东方美学的克制神性显现。
```

#### 7. 

**English：**
```
Massive semi-transparent glowing divine humanoid figure standing on open grassland battlefield in daylight, one hand extended forward blowing a giant semi-transparent blue-tinted bubble from mouth. Inside the bubble, a 4-5 meter white-furred divine beast (Lingyu) thrashes violently but cannot break the containment. The glowing figure approximately 20-30 meters tall, entire body warm white light (#FFF8DC), semi-transparent with landscape visible through form. Eyes steady royal blue (#4169E1). Other hand showing silver-white (#C0C0C0) wrist band poised to flick the separation tool. Bubble surface refracts surrounding light creating rainbow prismatic effects. Below, a small human figure (Zhu Weiyong) falls safely from a burst bubble section toward grass. Sunlight and the figure's own glow create double-illumination on the grassland. Atmosphere of absolute divine authority executing cosmic judgment with surgical precision. Photorealistic with supernatural elements, cinematic daylight + divine glow combined lighting, 80% realism + 20% supernatural stylization.
```

**中文：**
```
巨大半透明发光神性人形站立于开阔草原日间战场上，一手前伸口中吹出巨型半透明蓝色调泡泡。泡泡内部一只4-5米高的白毛神兽（灵尤）疯狂挣扎但无法突破囚禁。发光人形约20-30米高，全身温暖白光（#FFF8DC），半透明可透过形体看到风景。双眼稳定的皇家蓝光（#4169E1）。另一手展示银白色（#C0C0C0）手腕环带蓄势弹射分割工具。泡泡表面折射周围光线产生彩虹棱镜效果。下方一个渺小人形（朱围庸）从爆裂的泡泡半边安全落向草地。日光与人形自身光芒在草原上形成双重照明。以外科手术般精准执行宇宙审判的绝对神性权威氛围。写实风格带超自然元素，电影级日光+神性光芒组合照明，80%写实+20%超自然风格化。
```

### 小周 (characters, ★★★★, P3)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese man around 30 years old with a wholesome rural appearance, short neat black hair, thick straight dark eyebrows giving an honest dependable look, large bright clear eyes with dark irises radiating sincerity and quiet determination, oval-shaped face with soft features but a firm jawline, medium straight nose, medium lips pressed together in a characteristic resolute line, deeply tanned dark brown skin from extended outdoor farmwork, sturdy build visible at the broad shoulders beneath a simple faded cotton shirt, expression combining warmth and quiet resolve — the face of someone you would instinctively trust, white neutral background, warm natural front lighting emphasizing the healthy tanned skin, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约30岁中国男性的正面半身肖像，朴实的乡村青年外貌，黑色短发整洁，浓密平直的黑眉给人忠厚可靠的感觉，大而明亮的清澈眼睛黑色虹膜散发真诚和安静的决心，椭圆面孔线条柔和但下颌坚毅，中等端正鼻梁，中等厚度嘴唇抿成标志性的坚毅线条，因长期户外农活而深度日晒的深褐色皮肤，简素褪色棉布衬衫下可见宽阔肩膀的壮实体型，表情融合温暖和安静的决意——一张让人本能信任的面孔，白色中性背景，暖调自然正面光强调健康的古铜肤色，35mm胶片颗粒感，中等对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a Chinese man around 30 years old with a wholesome rural appearance, short neat black hair, thick straight eyebrows, large clear eyes with an attentive focused gaze directed slightly off-camera, oval face with firm jaw, deeply tanned dark brown weathered skin, sturdy shoulders beneath a simple cotton shirt, right hand raised to chest level with palm flat against the chest in a characteristic gesture of making a pledge, expression earnest and determined with a faint upward curve at the lip corners suggesting dependability, white neutral background, warm side lighting from camera-left highlighting the tanned facial contours and the gesture of commitment, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约30岁中国男性的四分之三侧面半身肖像，朴实乡村青年外貌，黑色短发整洁，浓密平直的眉毛，大而清澈的眼睛带着专注聚焦的目光微微偏离镜头，椭圆面孔下颌坚毅，深度日晒的深褐色风化皮肤，简素棉布衬衫下壮实的肩膀，右手抬至胸口掌心平贴在胸前呈标志性的承诺宣誓姿态，表情诚恳坚定嘴角微微上扬暗示可靠，白色中性背景，左侧暖调侧光突出古铜色面部轮廓和承诺手势，35mm胶片颗粒感，中等对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, pure profile bust portrait of a Chinese man around 30 years old with a wholesome rural appearance, short neat black hair, thick straight eyebrow visible in profile, large clear eye with forward gaze, soft oval face contour with firm chin in profile, medium nose with straight bridge, lips pressed together in determined line, deeply tanned dark brown skin with slight weathering from farmwork, sturdy thick neck connecting to broad shoulders beneath simple cotton shirt, posture straight and slightly forward-leaning suggesting readiness for action, white neutral background, rim lighting from behind outlining the honest sturdy profile, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约30岁中国男性的纯正侧面半身肖像，朴实乡村青年外貌，黑色短发整洁，侧面可见浓密平直的眉毛，大而清澈的眼睛目光直视前方，侧面柔和椭圆脸型轮廓下巴坚毅，中等鼻梁端正，嘴唇抿成坚定的线条，深度日晒的深褐色皮肤带有农活的轻微风化痕迹，粗壮颈部连接简素棉布衬衫下的宽阔肩膀，姿态挺直微微前倾暗示随时准备行动，白色中性背景，背后轮廓光勾勒出忠厚结实的侧面轮廓，35mm胶片颗粒感，中等对比度
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a Chinese man around 30 years old with a wholesome rural appearance, short neat black hair, large bright eyes on an honest oval face with thick straight brows, medium-tall height with a stocky sturdy build from farmwork, wearing a simple faded cotton shirt with sleeves pushed up to elbows, dark work trousers, rubber work shoes, deeply tanned dark brown skin visible on forearms and neck, standing in a grounded natural pose with feet shoulder-width apart, right hand loosely at his side left hand slightly curled at hip, posture upright and solid suggesting quiet strength and reliability, the overall impression is of an ordinary good man — unremarkable but dependable in every way that matters, white neutral background, warm even natural lighting, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约30岁中国男性的全身正面肖像，朴实乡村青年外貌，黑色短发整洁，椭圆忠厚面孔上大而明亮的眼睛浓密平直的眉毛，中等偏高身高因农活而体型壮实敦厚，穿简素褪色棉布衬衫袖子推到肘部，深色工装裤，橡胶工鞋，前臂和颈部可见深度日晒的深褐色皮肤，以双脚与肩同宽的扎实自然姿态站立，右手松弛垂于身侧左手微微弯曲在髋部，姿态挺拔稳固暗示安静的力量和可靠性，整体印象是一个普通的好人——不起眼但在每一个重要方面都值得信赖，白色中性背景，暖调均匀自然光，35mm胶片颗粒感，中等对比度
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man around 30 years old as a modern outdoor traveler, short black hair, large clear eyes with a complex expression mixing barely concealed fear with forced calm, oval honest face now drained of color turning pale despite the tan, wearing a dark green waterproof hiking jacket partly unzipped over a lighter base layer, khaki outdoor trousers with zippered pockets, sturdy hiking boots, a travel backpack with one strap slipping off the shoulder, both hands clenched into tight fists at his sides with knuckles white from the grip, body slightly hunched forward as if bracing against something unseen, the contrast between the healthy outdoor gear and the terrified pale face creates visual tension, plain dark background, cold overhead lighting with warm underfill creating an uneasy atmosphere, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约30岁中国男性作为现代户外旅行者的全身定妆参考，黑色短发，大而清澈的眼睛带着混合难以掩饰的恐惧和强装镇定的复杂表情，椭圆忠厚的面孔尽管有日晒仍然失去血色变得苍白，穿深绿色防水冲锋衣半拉开拉链内搭浅色底层，卡其色户外裤带拉链口袋，结实登山鞋，旅行背包一根肩带滑落肩膀，双手在身侧攥紧成拳指节因握力而发白，身体微微前倾佝偻如同在抵御看不见的什么，健康户外装备与恐惧苍白面孔之间的反差制造视觉张力，素色深色背景，冷色顶光配暖色底光制造不安氛围，35mm胶片颗粒感，中高对比度
```

#### 6. 

**English：**
```
Cinematic still, 2.39:1 widescreen, a bright white semi-transparent humanoid light figure curled in a fetal position floating in void, the figure retains the vague outline of a young Chinese man — oval face visible through the translucence, large eyes wide with sorrow and helplessness, arms wrapped around knees, the white luminescence is brighter and more condensed than typical spirit forms suggesting strong life force, edges flickering and pulsing irregularly conveying distress and unwillingness, scattered white light particles drift away from the figure like tears dissolving into darkness, the overall impression is of a soul stripped of everything — body identity home — left with nothing but the will to exist, plain dark background, the figure's own white radiance provides the sole light source contrasting starkly with the surrounding void, 35mm film grain, very high contrast between the bright white form and absolute darkness
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一个明亮白色半透明人形光影以胎儿姿态蜷缩悬浮于虚空中，人形保留了一名年轻中国男性的模糊轮廓——透过半透明可见椭圆面孔，大眼睛大睁满是悲伤和无助，双臂环抱膝盖，白色光辉比一般灵魂形态更明亮更凝聚暗示强烈的生命力，边缘不规则闪烁脉动传达痛苦和不甘，散落的白色光粒子如同泪水般从人形漂散消融于黑暗中，整体印象是一个被剥夺了一切——身体身份家园——只剩下存在意志的灵魂，素色深色背景，人形自身的白色辐射是唯一光源与周围虚空形成强烈反差，35mm胶片颗粒感，明亮白色形体与绝对黑暗之间的极高对比度
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man around 30 years old in recovery from severe spiritual trauma, short black hair slightly unkempt, gaunt face with sunken cheeks and visible dark circles under large eyes that retain their characteristic clarity but now carry a haunted quality — the look of someone who has seen the worst and survived, skin sallow and pale with traces of the former tan beneath, wearing loose comfortable home clothes — a faded long-sleeve cotton shirt hanging from diminished shoulders, simple cotton trousers, cloth slippers, frame noticeably thinner than his natural stocky build, standing with one hand gripping the edge of a chair for support, the other hand unconsciously clutching at the shirt hem, posture slightly stooped suggesting physical weakness but chin raised showing determination to stand, plain dark background, soft warm-to-neutral lighting suggesting indoor recovery environment, 35mm film grain, medium contrast emphasizing the contrast between weakness and willpower
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约30岁中国男性从严重灵魂创伤中恢复的全身定妆参考，黑色短发略显凌乱，面容消瘦面颊凹陷大眼睛下可见黑眼圈但仍保持标志性的清澈但如今带着一种幽暗质感——看过最恐怖的事情并活了下来的人的眼神，皮肤蜡黄苍白底下仍有此前日晒的痕迹，穿宽松舒适的家居服——褪色长袖棉布衬衫从缩小的肩膀上垂下，简素棉裤，布拖鞋，身架比自然的壮实体型明显消瘦，一手扶住椅子边缘支撑站立另一手无意识地攥着衬衫衣摆，姿态微微佝偻暗示身体虚弱但下巴抬起显示站立的决心，素色深色背景，柔和暖色到中性的光线暗示室内养病环境，35mm胶片颗粒感，中等对比度强调虚弱与意志力的反差
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man around 30 years old as a resistance fighter of rural origin, short black hair, large bright determined eyes on an honest tanned oval face with thick straight brows, deeply tanned dark brown skin fully recovered to robust health, stocky muscular build from combined farmwork and combat training, wearing simple village combat attire — a dark cotton shirt with one sleeve torn exposing a tanned muscular arm, a makeshift leather chest guard crudely stitched, dark work trousers reinforced at the knees, rubber work shoes scuffed and muddied, a simple short blade tucked in a cloth waist belt, right hand pressed flat against chest over heart in his signature pledge gesture, expression combining earnest warmth with unmistakable resolve — the face of an ordinary man who has chosen to stand, plain dark background, warm-to-neutral mixed lighting with slight amber tint suggesting sunset before battle, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名约30岁中国男性作为乡村出身的抵抗军战士的全身定妆参考，黑色短发，椭圆忠厚的古铜面孔上大而明亮的坚定眼睛浓密平直眉毛，深度日晒的深褐色皮肤完全恢复到健壮健康状态，因农活和战斗训练而体型壮实肌肉结实，穿简素乡村战斗装束——深色棉布衬衫一只袖子撕裂露出晒黑的肌肉手臂，粗制皮质胸甲粗线缝合，深色工装裤膝部加固，橡胶工鞋磨损沾泥，布腰带中插一把简朴短刀，右手掌心平贴在心口呈标志性的承诺宣誓姿态，表情融合诚恳温暖和不容置疑的决意——一个选择站出来的普通人的面孔，素色深色背景，暖色到中性的混合光带微弱琥珀色调暗示战斗前的黄昏，35mm胶片颗粒感，中高对比度
```

### 李仁 (characters, ★★★★, P3)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese man in his late 50s with a weathered farmer appearance, short grey-white hair receding at hairline exposing a broad forehead, thick dark eyebrows with deep furrow between them, narrow elongated eyes with sharp penetrating black irises radiating a calculated intelligence far beyond a simple farmer, high prominent cheekbones on a lean angular face, straight nose with defined ridge, thin lips with corners slightly turned down giving a naturally cold calm expression, deeply tanned dark brown rough skin covered in pronounced wrinkles especially forehead lines and nasolabial folds, thick coarse hands with enlarged knuckles, wearing a plain dark brown cotton short jacket, neutral composed expression with watchful alertness hidden beneath surface calm, white neutral background, soft front lighting with cool undertone emphasizing the weathered skin texture, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50多岁末中国男性的正面半身肖像，风霜农夫外貌，花白短发发际线后退露出宽阔前额，浓密黑眉眉心有深刻竖纹，细长眼睛锐利穿透性的黑色虹膜散发出远超普通农夫的精密智慧，高颧骨长脸棱角分明，鼻梁挺直轮廓硬朗，薄唇嘴角自然微微下垂给人天生冷静甚至冷漠的面相，深度日晒的黝黑粗糙皮肤布满显著皱纹尤其是额头横纹和法令纹，粗糙厚实的手指节粗大，穿朴素深褐色棉布短衫，中性沉着表情表面平静下暗藏警觉，白色中性背景，柔和正面光带冷色底调强调风化皮肤纹理，35mm胶片颗粒感，中高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a Chinese man in his late 50s with a weathered farmer appearance, short grey-white hair thinning at temples, thick dark eyebrows with deep vertical furrow between them, narrow eyes with piercing gaze directed slightly off-camera as if analyzing something unseen, high cheekbones casting subtle shadows on the lean angular face, straight defined nose in three-quarter profile, thin lips with the faintest upward curve at one corner suggesting hidden calculation, deeply tanned wrinkled skin with prominent nasolabial folds, broad shoulders visible beneath a plain dark cotton jacket suggesting a stocky build despite the lean face, right hand raised with index finger slightly extended as if about to tap a surface in thought, white neutral background, cool-toned side lighting from camera-left creating dramatic shadows that emphasize the facial bone structure, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50多岁末中国男性的四分之三侧面半身肖像，风霜农夫外貌，花白短发太阳穴处稀疏，浓密黑眉眉心深刻竖纹，细长眼睛穿透性目光微微偏离镜头如同在分析某些看不见的事物，高颧骨在瘦削棱角分明的脸上投下微妙阴影，四分之三角度可见挺直鼻梁轮廓硬朗，薄唇一侧嘴角有几乎不可察觉的上扬暗示隐藏的计算，深度日晒的布满皱纹的皮肤法令纹显著，朴素深色棉布外套下可见宽厚肩膀暗示尽管面部瘦削但体型敦实，右手抬起食指微微伸出如同即将敲击某个平面进行思考，白色中性背景，左侧冷调侧光制造戏剧性阴影强调面部骨骼结构，35mm胶片颗粒感，中高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, pure profile bust portrait of a Chinese man in his late 50s with a weathered farmer appearance, short grey-white hair sparse at crown, thick dark eyebrow visible in profile creating a strong brow ridge, narrow eye with sharp focused gaze directed forward, high cheekbone prominent in silhouette, straight long nose with defined bridge, thin lips with slightly downturned corner, strong jawline with angular chin, deeply tanned rough skin showing deep creases and weathering, stocky neck connecting to broad shoulders beneath a plain dark cotton jacket, posture slightly hunched forward at shoulders suggesting habitual stoop from years of labor, white neutral background, rim lighting from behind outlining the angular profile and emphasizing the contrast between the farmer exterior and the sharp intelligent silhouette, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50多岁末中国男性的纯正侧面半身肖像，风霜农夫外貌，花白短发头顶稀疏，侧面可见浓密黑眉形成突出的眉骨，细长眼睛锐利聚焦的目光直视前方，高颧骨在侧影中突出，鼻梁挺直偏长轮廓硬朗，薄唇嘴角微微下垂，硬朗的下颌线棱角分明的下巴，深度日晒的粗糙皮肤可见深刻皱纹和风化痕迹，粗壮颈部连接朴素深色棉布外套下的宽厚肩膀，肩部微微前倾的姿态暗示多年劳作形成的习惯性佝偻，白色中性背景，背后轮廓光勾勒棱角分明的侧面轮廓强调农夫外表与锐利智慧剪影的反差，35mm胶片颗粒感，中高对比度
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a Chinese man in his late 50s with a weathered farmer appearance, short grey-white receding hair, narrow penetrating eyes on a lean angular face with high cheekbones and pronounced wrinkles, medium height with a stocky build, broad shoulders slightly hunched forward from years of manual labor, wearing a plain dark brown cotton short jacket over a lighter inner shirt, dark patched work trousers, simple cloth shoes, large-knuckled calloused hands hanging at sides with right index finger slightly curled as if ready to tap, standing in a grounded stance with weight evenly distributed feet shoulder-width apart, posture suggesting both the earthiness of a farmer and the contained readiness of a strategist, white neutral background, even cool-toned lighting, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50多岁末中国男性的全身正面肖像，风霜农夫外貌，花白短发发际线后退，瘦削棱角面孔上细长穿透性眼神高颧骨和显著皱纹，中等身高敦实体型，宽厚肩膀因多年体力劳动微微前倾，穿朴素深褐色棉布短衫内衬浅色衬衣，深色打补丁工装裤，简素布鞋，指节粗大布满老茧的双手垂于两侧右手食指微微弯曲如同随时准备敲击，双脚与肩同宽重心均匀分布的扎实站姿，姿态兼具农夫的质朴和谋士的内敛准备感，白色中性背景，均匀冷调光线，35mm胶片颗粒感，中高对比度
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, a pale purple irregular luminous orb floating in void, slightly smaller and lighter in hue than the deep purple orb beside it, surface rippling with rapid anxious energy waves, edges flickering with faint lavender light particles, no face no body — pure spiritual energy form, the orb pulses with a faster rhythm suggesting concern and loyalty, positioned close to the larger purple orb as if drawn by emotional gravity, plain dark background, deep purple ambient glow from below, scattered dim light particles in surrounding void, 35mm film grain, low-key lighting, high contrast between the luminous form and the surrounding darkness
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一团淡紫色不规则发光球体悬浮于虚空中，比旁边的深紫色球体略小色调略淡，表面波纹以焦虑急促的能量波动起伏，边缘闪烁微弱的薰衣草色光粒子，无面孔无身体——纯粹的灵魂能量形态，球体以更快的节奏脉动暗示关切与忠诚，位置紧贴较大的紫色球体如同被情感引力牵引，素色深色背景，底部深紫色环境光，周围虚空中散落微弱光粒子，35mm胶片颗粒感，低调照明，发光形态与周围黑暗的高对比度
```

#### 6. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young emaciated Chinese man who has just awakened in a beggar's body, thin frail frame with visible collarbones and lean limbs, sallow yellowish skin showing malnourishment, messy unkempt hair partially covering forehead, wearing tattered filthy beggar's rags — a torn cotton shirt exposing one shoulder, frayed trousers patched with different fabrics, bare feet, the most striking feature is the eyes — they carry an impossible depth and ancient intelligence that completely contradicts the young starving face, expression showing a mixture of disorientation and dawning sharp awareness, body slightly trembling as if adjusting to unfamiliar limbs, plain dark background, cold overhead lighting with faint purple tint suggesting supernatural origin, 35mm film grain, high contrast emphasizing the gaunt features
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名刚在乞丐身体中苏醒的骨瘦如柴的中国年轻男性的全身定妆参考，瘦弱纤细的身架锁骨突出四肢纤瘦，蜡黄皮肤显示营养不良，凌乱蓬松的头发部分遮住前额，穿破烂肮脏的乞丐衣衫——破洞棉衬衫露出一边肩膀，不同布料拼补的磨损裤子，赤脚，最引人注目的特征是眼睛——它们带有与年轻饥饿面孔完全矛盾的不可思议的深度和古老智慧，表情是迷失方向与逐渐浮现的锐利觉知的混合，身体微微颤抖如同在适应陌生的肢体，素色深色背景，冷色顶光带微弱紫色调暗示超自然来源，35mm胶片颗粒感，高对比度强调消瘦特征
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his late 50s recently reborn in a farmer's body, short grey-white hair unkempt, deeply tanned dark brown skin covered in wrinkles, high cheekbones and lean angular face, narrow eyes with piercing sharpness that belies the humble exterior, thick dark eyebrows with deep furrow between them, wearing a rough cotton short jacket in faded brown with patches at elbows, dark work trousers patched at knees with mismatched fabric, worn cloth shoes with mud stains, carrying a hoe resting on right shoulder with one hand, left hand hanging with calloused enlarged knuckles, posture slightly hunched at shoulders but stance solid and grounded, expression simultaneously humble and watchful — the face of an old farmer but the gaze of a general surveying his terrain, plain dark background, warm-to-neutral mixed lighting suggesting transition from rural daylight, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名刚以农夫之躯重生的50多岁末中国男性的全身定妆参考，花白短发未加整理，深度日晒的黝黑粗糙皮肤布满皱纹，高颧骨瘦削棱角分明的面孔，细长眼睛穿透性的锐利与卑微外表形成反差，浓密黑眉眉心深刻竖纹，穿褪色褐色粗棉布短衫肘部有补丁，深色工装裤膝盖处拼接不同布料的补丁，沾泥的旧布鞋，右手扛锄头搭在肩上，左手垂下指节粗大布满老茧，肩部微微佝偻但站姿稳固扎实，表情同时谦卑而警觉——一张老农的脸但目光如同将军在审视他的领地，素色深色背景，暖色到中性的混合光暗示从乡间日光过渡，35mm胶片颗粒感，中高对比度
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his late 50s transformed from farmer to military strategist, short grey-white hair now neatly kept, lean angular face with high cheekbones looking more commanding than before, narrow eyes ice-cold and calculating with absolute precision, thin lips with a faint knowing curve at one corner suggesting strategic confidence, wearing a well-fitted dark navy-blue long jacket over dark inner garments suggesting practical military authority, dark trousers, leather boots replacing former cloth shoes, standing with hands clasped behind back in a contemplative pose, chin slightly raised, shoulders still slightly hunched but now suggesting coiled readiness rather than manual labor, a rolled map tucked under one arm, the overall impression is a farmer's body housing a military genius — the rough skin and wrinkles cannot hide the cold authority radiating from within, plain dark background, cool blue-toned side lighting from camera-right suggesting strategic calculation, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名从农夫蜕变为军师的50多岁末中国男性的全身定妆参考，花白短发如今整理整齐，高颧骨瘦削棱角面孔比前期更具威严，细长眼睛冰冷精准充满绝对的计算力，薄唇一侧嘴角有微弱的了然弧度暗示战略自信，穿合身的深藏蓝色长衣外套内搭深色衣物暗示实用的军事权威感，深色裤子，皮靴取代了此前的布鞋，双手背在身后呈沉思姿态站立，下巴微微抬起，肩部仍微微前倾但如今暗示蓄势待发而非体力劳动，一卷地图夹在臂下，整体印象是农夫的身体中住着一个军事天才——粗糙的皮肤和皱纹无法掩盖从内在散发的冷厉权威，素色深色背景，右侧冷蓝调侧光暗示战略计算，35mm胶片颗粒感，中高对比度
```

#### 9. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his late 50s as a battle-worn military commander, face showing deepened wrinkles and heavy dark circles under narrow eyes, skin more weathered and gaunt than previous stages, grey-white hair disheveled from prolonged campaigning, wearing a returned-being soldier's armor — dark leather vest over layered dark fabric, arm guards, scuffed boots, the armor showing scratches and wear from extended warfare, dried tear tracks visible on the left cheek cutting through dust and grime on the face, thin lips pressed tightly together with jaw muscles clenched, eyes red-rimmed but blazing with cold determination — the look of a man who has just lost his closest brother but refuses to break, standing rigid with one hand gripping a sword hilt and the other clenched in a fist at his side, plain dark background, harsh cold desaturated lighting with no warmth suggesting battlefield grief, 35mm film grain, high contrast emphasizing the gauntness and emotional devastation
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名身经百战的50多岁末中国男性军事指挥官的全身定妆参考，面部皱纹比前期更深细长眼睛下有浓重黑眼圈，皮肤比前几个阶段更加风化消瘦，花白短发因长期征战凌乱不堪，穿还阳者士兵铠甲——深色皮质背心覆在多层深色布料上配有臂甲磨损的靴子，铠甲上可见长期作战的划痕和磨损，左脸颊上可见干涸的泪痕穿过面部的灰尘和污垢，薄唇紧紧抿住下颌肌肉紧绷，眼眶泛红但目光燃烧着冰冷的决心——刚刚失去最亲近的兄弟但拒绝崩溃的男人的表情，笔直站立一手握剑柄另一手在身侧攥拳，素色深色背景，严酷冷色去饱和度的光线不带任何暖意暗示战场的悲痛，35mm胶片颗粒感，高对比度强调消瘦和情感的毁灭性
```

#### 10. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a semi-transparent spiritual form of a Chinese man in his late 50s — the farmer's weathered features still recognizable but now rendered in translucent pale purple luminescence, narrow eyes wide open with desperate anxiety and reluctance, both arms reaching forward as if trying to grasp something just beyond reach, fingers splayed and straining, mouth slightly open as if calling out, the body surrounded by a soft lavender glow that intensifies at the edges, form gradually becoming more transparent from the feet upward suggesting absorption into a spiritual vessel, the lean angular face and high cheekbones still visible through the translucence, expression conveying profound loyalty and unwillingness to part, plain dark background, the figure's own spiritual luminescence providing the primary light source, ethereal purple glow with scattered light particles being drawn downward, 35mm film grain, low contrast with emphasis on the supernatural glow
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50多岁末中国男性的半透明灵魂形态全身定妆参考——农夫的风化面容仍可辨认但如今以半透明淡紫色光芒呈现，细长眼睛大睁充满绝望的焦急与不舍，双臂向前伸出如同试图抓住刚刚超出触及范围的什么，手指张开紧绷用力，嘴巴微张如同在呼喊，身体周围环绕柔和的薰衣草色光晕边缘处更为强烈，形体从脚部向上逐渐变得更加透明暗示正被灵魂容器吸收，瘦削棱角面孔和高颧骨透过半透明仍可辨识，表情传达出深挚的忠诚和不愿分离，素色深色背景，人物自身的灵魂光芒提供主要光源，空灵的紫色光辉伴随散落的光粒子向下被牵引，35mm胶片颗粒感，低对比度强调超自然光芒
```

### 杨弘 (characters, ★★★★, P3)

#### 1. 

**English：**
```
Portrait of a stern Chinese military general in his late 40s, front view from chest up. Square jaw with high cheekbones and deep-set eye sockets under prominent brow ridge. Sharp, narrow piercing eyes with hawk-like intensity. High straight nose bridge, thin lips pressed tightly together in permanent stern expression. Weathered yellowish-brown skin from years of military campaigns. Hair pulled into traditional warrior topknot secured with dark metal crown. Slight grey at temples. Wearing newly polished marshal-grade armor with dark copper-green (#5F7A61) base plates and dark gold (#DAA520) trim accents. Collar of iron-grey chainmail visible at neck. Expression of absolute cold authority and iron discipline. Dark neutral background. Photorealistic Chinese historical military portrait, cinematic side lighting emphasizing bone structure and armor metallic reflections. Shot with 85mm equivalent lens, shallow depth of field.
```

**中文：**
```
严厉的中国军事将领正面半身像，年约四十多岁末。国字脸高颧骨，深眼窝在突出的眉骨下方。锐利狭长的鹰眼目光。高挺鼻梁，薄唇紧抿呈永久性严肃表情。多年军旅风吹日晒的黄黑色粗糙皮肤。头发束成传统武将发髻，以深色金属发冠固定。两鬓微白。身穿新近擦拭铮亮的元帅级铠甲，铜绿色（#5F7A61）底板配暗金色（#DAA520）边饰。颈部可见铁灰色锁子甲领。表情呈绝对冷酷的权威与铁律纪律。深色中性背景。写实中国古代军事肖像风格，电影级侧光强调骨骼结构和铠甲金属反射。等效85mm镜头，浅景深。
```

#### 2. 

**English：**
```
Three-quarter view portrait of a stern Chinese military general in his late 40s, from chest up. Head slightly turned showing the angular profile of square jaw and high cheekbone. Deep-set eye catching light with hawk-like intensity, one eye fully visible, second partially shadowed. Prominent brow ridge casting shadow over eye socket. Traditional warrior topknot with dark metal crown visible from side angle. Grey temples visible. Wearing polished marshal-grade armor with dark copper-green (#5F7A61) shoulder plates and dark gold (#DAA520) decorative studs. Strong neck tendons visible above chainmail collar. Expression of cold tactical calculation. Dark neutral background. Photorealistic, Rembrandt lighting with dramatic shadow on far side of face emphasizing bone structure. Shot with 85mm equivalent lens.
```

**中文：**
```
严厉中国军事将领四分之三侧面半身像，年约四十多岁末。头部微转展示国字脸方颌和高颧骨的棱角轮廓。深眼窝中鹰眼目光捕捉光线，一只眼完整可见，另一只部分被阴影遮挡。突出眉骨在眼窝上投射阴影。传统武将发髻和深色金属发冠从侧面可见。两鬓白发可见。身穿擦亮的元帅级铠甲，铜绿色（#5F7A61）肩甲板配暗金色（#DAA520）装饰铆钉。颈部肌腱在锁子甲领上方清晰可见。冷静战术计算的表情。深色中性背景。写实风格，伦勃朗式布光在面部远侧形成戏剧性阴影强调骨骼结构。等效85mm镜头。
```

#### 3. 

**English：**
```
Pure side profile portrait of a stern Chinese military general in his late 40s, from chest up. Side view reveals strong angular silhouette: traditional warrior topknot with metal crown, sloping forehead into prominent brow ridge, deep eye socket, high straight nose bridge, thin tight lips, strong square jaw, muscular neck. Grey hair at temple clearly visible against dark hair. Wearing marshal-grade armor with dark copper-green (#5F7A61) shoulder plate visible in profile, dark gold (#DAA520) edge trim catching light. Chainmail collar visible at neck. Posture perfectly upright with military bearing — spine straight as a spear. Dark neutral background. Photorealistic, edge lighting creating bright rim on profile outline. Shot with 85mm equivalent lens.
```

**中文：**
```
严厉中国军事将领纯正侧面半身像，年约四十多岁末。侧面展示强硬棱角的轮廓剪影：传统武将发髻配金属发冠，额头斜入突出眉骨，深眼窝，高挺鼻梁，薄唇紧抿，方硬下颌，肌肉颈部。两鬓白发在深色头发衬托下清晰可见。身穿元帅级铠甲，铜绿色（#5F7A61）肩甲板在侧面可见，暗金色（#DAA520）边饰捕捉光线。颈部锁子甲领可见。完美挺拔的军人姿态——脊柱直如标枪。深色中性背景。写实风格，边缘光在轮廓线上形成明亮轮廓光。等效85mm镜头。
```

#### 4. 

**English：**
```
Full body front view of a stern Chinese military general in his late 40s standing at attention in formal military posture. Height approximately 175-180cm, lean muscular build with broad shoulders. Wearing complete marshal-grade armor set: dark copper-green (#5F7A61) chest plate and leg guards with dark gold (#DAA520) trim and decorative studs, iron-grey (#4A4A4A) chainmail underlayer visible at joints, dark leather military boots. Left hand resting on sword pommel at hip, right hand at side. Traditional warrior topknot with dark metal crown. Face showing cold stern expression with hawk eyes scanning forward. Military belt with command insignia. Posture ramrod straight, feet shoulder-width apart in commanding stance. Dark neutral background. Photorealistic Chinese historical military figure, full-body even lighting to show complete armor detail. Shot with 35mm equivalent lens.
```

**中文：**
```
严厉中国军事将领全身正面像，年约四十多岁末，以正式军姿立正站立。身高约175-180cm，精壮肌肉体型，宽阔肩膀。穿着完整元帅级铠甲套装：铜绿色（#5F7A61）胸甲和腿甲配暗金色（#DAA520）边饰和装饰铆钉，铁灰色（#4A4A4A）锁子甲内层在关节处可见，深色皮质军靴。左手搭在腰间剑柄上，右手自然垂于身侧。传统武将发髻配深色金属发冠。面部冷峻严厉表情，鹰眼直视前方。军用腰带配指挥官徽章。姿态笔直如标枪，双脚与肩同宽呈指挥姿态。深色中性背景。写实中国古代军事人物风格，全身均匀照明展示完整铠甲细节。等效35mm镜头。
```

#### 5. 

**English：**
```
Stern Chinese military general in his late 40s standing on city wall battlements at dusk, reviewing defensive positions. Wearing newly polished marshal-grade armor with dark copper-green (#5F7A61) plates and dark gold (#DAA520) trim, iron-grey chainmail visible underneath. No decorative additions — purely functional military equipment. Face cold and stern with hawk-like scanning eyes, square jaw clenched tight. Traditional warrior topknot, neat and precise. Behind him, rows of black cloth barriers stretching along city walls (his tactical invention). Soldiers stand rigidly at attention around him. Dusk light casting long shadows, warm golden edge light on armor surface contrasting cold blue-grey shadows. Atmosphere of absolute iron discipline and wartime efficiency. Photorealistic Chinese historical military scene, cinematic dusk lighting, 80% realism + 20% dramatic stylization.
```

**中文：**
```
严厉中国军事将领，年约四十多岁末，黄昏时分立于城墙雉堞上检阅防御工事。身穿新近擦亮的元帅级铠甲，铜绿色（#5F7A61）甲板配暗金色（#DAA520）边饰，铁灰色锁子甲在内层可见。无任何装饰性附加——纯实用军事装备。面部冷峻严厉，鹰眼扫视，方颌紧咬。传统武将发髻，整齐利落。身后是沿城墙延伸的成排黑布屏障（他的战术发明）。士兵在其周围笔直立正。黄昏光线投射长影，温暖金色边缘光在铠甲表面与冷蓝灰阴影形成对比。绝对铁律纪律和战时效率的氛围。写实中国古代军事场景，电影级黄昏照明，80%写实+20%戏剧性风格化。
```

#### 6. 

**English：**
```
Chinese military general in his late 40s standing elevated on a war chariot during victory parade, receiving adulation from crowds below. Still wearing marshal-grade armor but now with added luxurious dark red (#8B1A1A) cape flowing behind and additional dark gold (#DAA520) ornamental pieces on shoulders and chest. Face still angular but expression shifted from cold efficiency to self-assured arrogance — subtle cold smile of intellectual superiority. Eyes looking down at crowds with possessive pride. Traditional warrior topknot now secured with more elaborate gold-decorated crown. Surrounding crowds reaching upward in worship. Hero-style top lighting creating golden halo effect around his figure. Warm color temperature suggesting the intoxicating warmth of power. Photorealistic Chinese historical scene, cinematic heroic lighting, 80% realism + 20% dramatic stylization.
```

**中文：**
```
中国军事将领，年约四十多岁末，胜利游行中站立于战车高处接受人群欢呼。仍穿元帅级铠甲但现已增添奢华暗红色（#8B1A1A）披风在身后飘动，肩部和胸甲上增加暗金色（#DAA520）装饰件。面部仍保持棱角但表情从冷酷效率转为自信傲慢——微妙的智识优越冷笑。眼神俯视人群带有占有性的骄傲。传统武将发髻现以更精致的金饰发冠固定。周围人群向上仰望崇拜。英雄式顶光在其身形周围形成金色光环效果。温暖色温暗示权力陶醉的虚假暖意。写实中国古代场景，电影级英雄照明，80%写实+20%戏剧性风格化。
```

#### 7. 

**English：**
```
Chinese autocrat ruler in his early 50s seated on ornate golden throne in lavish palace chamber, arms spread wide in grandiose gesture while declaring his immortality plan. Armor completely gone — now wearing luxurious dark tarnished-gold (#B8860B) imperial robe with dark purple (#5B3A6B) embroidered patterns, gold belt, silk inner layers. Face noticeably puffier than military period, jawline softened by indulgence. Eyes alternating between fanatical gleam and ice-cold calculation. Hair in elaborate but slightly disheveled topknot with golden ornamental crown. Slightly heavier build from palace life. Surrounded by sycophantic attendants and golden furnishings. Half his face lit by warm candlelight, other half in deep shadow — dual nature visual metaphor. Atmosphere of corrupted magnificence and megalomaniac delusion. Photorealistic, cinematic chiaroscuro palace lighting, 80% realism + 20% dramatic stylization.
```

**中文：**
```
中国独裁统治者，年约五十出头，坐于奢华宫殿金碧辉煌的龙椅上，双臂向两侧展开做宏大宣言姿态宣布其永生计划。铠甲已完全消失——现穿奢华暗枯金色（#B8860B）龙袍配暗紫色（#5B3A6B）刺绣纹样，金腰带，丝绸内层。面部较军人时期明显浮肿，颌线因放纵而变软。眼神在狂热光芒与冰冷算计间交替。发型为精致但略有散乱的发髻配金色装饰冠。体型因宫廷生活略微发福。周围环绕谄媚侍从和金色家具。面部一半被温暖烛光照亮，另一半深陷阴影——双面人格的视觉隐喻。腐败华丽与自大妄想的氛围。写实风格，电影级明暗对比宫殿照明，80%写实+20%戏剧性风格化。
```

#### 8. 

**English：**
```
Gaunt, broken Chinese man in his early 50s sitting alone in vast empty palace hall, staring at the ground with completely hollow vacant eyes. All ornate robes gone — now wearing plain dark (#1C1C1C) commoner clothes, no gold, no ornaments, no symbols of power. Face haggard and emaciated, cheekbones and jaw now prominent through sunken flesh, deep dark circles under vacant eyes. Hair partially undone from topknot, grey-white strands falling across forehead. Body hunched and curved in posture of utter defeat, shoulders collapsed inward. Hands limp at sides, left hand no longer clenching. Surrounded by empty seats and cold grey stone walls. Single thin beam of light from high window cutting across dark space, barely reaching his figure. Extreme low-key lighting, almost entirely shadow with minimal illumination. Atmosphere of absolute desolation and spiritual death. Photorealistic, cinematic minimal lighting, 80% realism + 20% dramatic stylization.
```

**中文：**
```
枯槁破碎的中国男人，年约五十出头，独坐于空旷巨大的宫殿大堂中，双眼完全空洞无神地盯着地面。一切华服已消失——现仅穿素暗色（#1C1C1C）平民衣物，无金饰，无装饰，无权力象征。面容憔悴枯瘦，颧骨和颌骨在凹陷的肌肉中突出，空洞双眼下方深重的黑色眼圈。头发从发髻中部分散落，灰白发丝垂落额前。身体佝偻弯曲呈彻底失败姿态，双肩向内坍塌。双手无力垂于身侧，左手不再握拳。周围是空座和冰冷灰石墙壁。一道细窄的光线从高窗射入切过黑暗空间，勉强触及他的身形。极低key照明，几乎全为阴影仅有最少照明。绝对荒凉与精神死亡的氛围。写实风格，电影级极简照明，80%写实+20%戏剧性风格化。
```

### 灵尤 (characters, ★★★★, P3)

#### 1. 

**English：**
```
Portrait of a ferocious divine beast, front view from chest up. Creature stands 4-5 meters tall with pure ivory-white fur (#F5F5F5) approximately 20cm long, but constantly disheveled and wind-tossed in chaotic patterns. Face completely hairless with pure black skin (#1A1A1A), sharp aggressive features with narrower snout and tighter jawline than typical beast. Eyes bloodshot with constricted predator pupils radiating fury. Two long pointed ears erect on head, tensed and alert. Neck mane approximately 30cm long exploding outward like a lion's mane rather than hanging down. Expression of barely contained violence and explosive energy. Muscles visible under fur on neck and shoulders. Dark neutral background. Photorealistic creature design, dramatic hard lighting emphasizing aggressive features and chaotic fur texture. Shot with 85mm equivalent lens.
```

**中文：**
```
凶猛神兽正面半身像。生物高4-5米，全身覆盖约20厘米长的纯象牙白色毛发（#F5F5F5），但始终凌乱飞散呈混乱状态。面部完全无毛，纯黑色皮肤（#1A1A1A），尖锐的攻击性面部特征，鼻梁较窄，颌线更紧绷。眼睛充血，瞳孔收缩呈猎食者凝视，散发怒火。头顶两只长尖耳直立，紧张警觉。颈部约30厘米鬃毛向外炸开如狮鬃而非自然垂落。表情呈勉强压制的暴力和爆发性能量。颈肩部肌肉在毛发下清晰可见。深色中性背景。写实生物设计风格，强硬戏剧性照明强调攻击性特征和凌乱毛发质感。等效85mm镜头。
```

#### 2. 

**English：**
```
Three-quarter view portrait of a ferocious divine beast, from chest up. Creature with pure ivory-white disheveled fur (#F5F5F5) approximately 20cm long flying in chaotic directions. Head turned aggressively showing sharp black-skinned face (#1A1A1A) with constricted predator pupils and bloodshot eyes. Jawline angular and tight, mouth slightly open revealing tension. One erect ear pointing forward, second ear angled sideways in alert position. Neck mane exploding outward in wild directions. Shoulder muscles bulging under fur, body coiled in spring-loaded posture ready to launch. Expression of seething rage barely held in check. Dark neutral background. Photorealistic creature design, hard side lighting creating sharp shadows on aggressive facial features. Shot with 85mm equivalent lens.
```

**中文：**
```
凶猛神兽四分之三侧面半身像。全身纯象牙白色凌乱毛发（#F5F5F5）约20厘米长向各方向飞散。头部攻击性地转向，展示尖锐的黑色皮肤面部（#1A1A1A），收缩的猎食者瞳孔和充血眼白。颌线棱角分明紧绷，嘴部微张显示紧张感。一只耳朵指向前方，另一只侧向警戒。颈部鬃毛向各方向狂野炸开。肩部肌肉在毛发下隆起，身体蜷缩呈弹簧蓄力姿态随时准备弹射。表情为勉强压制的沸腾怒火。深色中性背景。写实生物设计风格，硬侧光在攻击性面部特征上形成锐利阴影。等效85mm镜头。
```

#### 3. 

**English：**
```
Pure side profile portrait of a ferocious divine beast, from chest up. Creature with pure ivory-white disheveled fur (#F5F5F5) approximately 20cm long layered in chaotic windswept patterns. Side view reveals aggressive silhouette: erect ear on top angled forward, sloped powerful forehead, sharp black-skinned face (#1A1A1A) with angular snout, strong jaw muscles clenched tight, thick chaotic neck mane exploding backward. Visible muscle definition on neck and shoulder through fur. Eye in profile shows constricted pupil and bloodshot intensity. Body posture leaning forward in predatory crouch. Dark neutral background. Photorealistic creature design, rim lighting on chaotic fur edge creating spiky bright outline. Shot with 85mm equivalent lens.
```

**中文：**
```
凶猛神兽纯正侧面半身像。全身纯象牙白色凌乱毛发（#F5F5F5）约20厘米长呈混乱风吹层叠。侧面展示攻击性轮廓剪影：头顶耳朵前倾直立，有力的前额斜面，尖锐的黑色皮肤面部（#1A1A1A）棱角分明的口鼻部，强壮的颌部肌肉紧咬，厚重凌乱颈部鬃毛向后炸开。颈肩部肌肉线条在毛发中清晰可见。侧面眼睛展示收缩瞳孔和充血的凶悍。身体姿态前倾呈捕食者蹲伏状。深色中性背景。写实生物设计风格，轮廓光在凌乱毛发边缘形成尖刺状明亮轮廓。等效85mm镜头。
```

#### 4. 

**English：**
```
Full body front view of a ferocious divine beast standing on all fours in aggressive posture. Creature stands 4-5 meters tall at shoulder height, with pure ivory-white disheveled fur (#F5F5F5) approximately 20cm long flying in all directions. Four powerful muscular legs with dark black claws (#0D0D0D), muscles clearly visible under fur. Face completely hairless with pure black skin (#1A1A1A), bloodshot predator eyes with constricted pupils. Two erect ears, neck mane exploding outward. Body coiled in spring-loaded crouch, front legs planted wide, back arched with visible spine and shoulder muscle ridges. Overall silhouette resembles a coiled white storm about to explode. Short fur-covered tail raised in aggression. Dark neutral background. Photorealistic creature design, full-body hard lighting emphasizing muscle definition and chaotic fur texture. Shot with 35mm equivalent lens to capture full aggressive posture.
```

**中文：**
```
凶猛神兽全身正面像，四足呈攻击性姿态站立。肩高4-5米，全身覆盖约20厘米长的纯象牙白色凌乱毛发（#F5F5F5）向各方向飞散。四条有力的肌肉腿，深黑色爪甲（#0D0D0D），肌肉在毛发下清晰可见。面部完全无毛呈纯黑色皮肤（#1A1A1A），充血的猎食者眼睛瞳孔收缩。两只耳朵直立，颈部鬃毛向外炸开。身体蜷缩呈弹簧蓄力蹲伏姿态，前肢宽展稳固，背部弓起，脊柱和肩部肌肉脊线清晰可见。整体轮廓如一场即将爆发的蜷缩白色风暴。短尾被毛覆盖攻击性上扬。深色中性背景。写实生物设计风格，全身硬光照明强调肌肉线条和凌乱毛发质感。等效35mm镜头以捕捉完整攻击姿态。
```

#### 5. 

**English：**
```
Young ferocious divine beast crouching by a large stone cauldron with roaring bonfire in a hidden mountain valley at 3000+ meters altitude. Creature approximately 4 meters tall (slightly smaller than full adult), pure ivory-white disheveled fur (#F5F5F5) approximately 20cm long, hairless pure black face (#1A1A1A) with aggressive youthful energy. Eyes bright with violent vitality, not yet hardened into pure rage. Neck mane chaotically spread but still youthfully fluffy. Body tense, mid-motion of lunging toward food, displaying competitive aggression. Firelight from below casts warm golden reflections (#C9A032) on chaotic white fur, creating fragmented highlights jumping across tangled strands. Snow-covered ground, crude grass shelter. Photorealistic, cinematic warm firelight, 80% realism + 20% supernatural stylization.
```

**中文：**
```
年轻凶猛神兽蹲伏于隐谷篝火石锅旁，海拔3000米以上的隐蔽山谷。生物约4米高（略小于完全成年体型），纯象牙白色凌乱毛发（#F5F5F5）约20厘米长，无毛纯黑面部（#1A1A1A）带有攻击性的年轻活力。眼睛明亮充满暴烈活力，尚未硬化为纯粹怒火。颈部鬃毛混乱散开但仍有幼兽的蓬松感。身体紧绷，正扑向食物的中间动作，展示竞争性攻击行为。篝火从下方照射在凌乱白毛上投射暖金色反光（#C9A032），在纠结毛发中形成跳跃的碎光高光。地面积雪，简陋草棚。写实风格，电影级暖色火光，80%写实+20%超自然风格化。
```

#### 6. 

**English：**
```
Fully mature ferocious divine beast standing restlessly on the highest peak of Fenglang Mountain Range beside its massive calm father (partially visible). Creature 4-5 meters tall with pure ivory-white fur (#F5F5F5) blown by fierce mountain wind into streaming white banners. Hairless pure black face (#1A1A1A) with eyes burning with suppressed fury, muscles visibly tensed under fur. Body in half-risen crouch, agitated posture radiating restless energy. Neck mane blown backward by wind in wild streamers. Ears forward-pointed in alert predatory focus toward distant human world below. Entire body vibrating with barely contained explosive energy. Cold grey daylight (#B0B0B0), cloud sea below, distant ant-like human figures barely visible on mountain paths. Atmosphere of a caged predator observing from above against cold indifferent sky. Photorealistic, cinematic cold natural light, 80% realism + 20% supernatural stylization.
```

**中文：**
```
完全成年的凶猛神兽不安地站立于凤廊山脉最高峰顶，身旁是其庞大沉静的父亲（部分可见）。生物高4-5米，纯象牙白色毛发（#F5F5F5）被猛烈山风吹成飘动的白色旗帜。无毛纯黑面部（#1A1A1A），眼中燃烧着被压抑的怒火，肌肉在毛发下明显紧绷。身体呈半起身蹲伏姿态，散发出躁动不安的能量。颈部鬃毛被风向后吹成狂野的飘带。双耳前指朝向远处下方人间，呈警觉捕食性专注。整个身体因勉强压制的爆发能量而微颤。冷灰色日光（#B0B0B0），下方云海，远处蚂蚁般的人类身影在山路上依稀可见。笼中猛兽从高处俯瞰的氛围。写实风格，电影级冷色自然光，80%写实+20%超自然风格化。
```

#### 7. 

**English：**
```
Ferocious divine beast in full destructive rampage charging through a burning city gate at night. Creature 4-5 meters tall, originally pure ivory-white fur now stained with blood and dust turning grey-brown (#6B5B4F) with patches of original white (#F5F5F5) visible underneath. Hairless pure black face (#1A1A1A) splattered with blood, eyes now empty of emotion — hollow killing void replacing former rage. Neck mane matted and blood-soaked. Charging in straight line through shattered wooden gate, soldiers and horse debris flying to both sides. Fur streaming backward in motion like a dirty white comet tail. Ground cracking under massive claws. Burning buildings cast orange-red firelight (#CC4400) on blood-stained fur creating hellish appearance. Smoke and dust obscure full form, creating terrifying glimpses. Photorealistic, cinematic war scene lighting, 80% realism + 20% supernatural stylization.
```

**中文：**
```
凶猛神兽全速破坏性冲锋穿过燃烧的夜间城门。生物高4-5米，原本纯象牙白色毛发现被血污和尘土染成灰褐色（#6B5B4F），下层仍可见原始白色（#F5F5F5）斑块。无毛纯黑面部（#1A1A1A）溅满鲜血，眼神现已空无情感——空洞的杀戮虚空取代了先前的怒火。颈部鬃毛结块被血浸透。沿直线冲锋穿过碎裂的木制城门，士兵和战马碎片向两侧飞溅。毛发在运动中向后飞散如一条肮脏的白色彗星尾迹。地面在巨爪下开裂。燃烧建筑投射橙红色火光（#CC4400）在血染毛发上，形成地狱般的外观。烟尘遮蔽完整形体，形成恐怖的碎片化影像。写实风格，电影级战争场景照明，80%写实+20%超自然风格化。
```

### 白巨 (characters, ★★★★, P3)

#### 1. 

**English：**
```
Portrait of a massive divine beast patriarch, front view from chest up. Creature stands 5-6 meters tall, with pure ivory-white fur (#F5F5F5) approximately 20cm long covering entire body. Face completely hairless with pure black skin (#1A1A1A), simplified beast facial features with deeply compassionate eyes reflecting faint starlight. Two long pointed ears stand erect atop the head like antlers. Thick white mane around neck approximately 30cm long forms natural collar. Expression conveys ancient wisdom and profound melancholy. Dark neutral background. Photorealistic creature design, cinematic lighting with soft side light emphasizing fur volume and facial contrast. Shot with 85mm equivalent lens, shallow depth of field.
```

**中文：**
```
巨型神兽族长正面半身像。生物高5-6米，全身覆盖约20厘米长的纯象牙白色毛发（#F5F5F5）。面部完全无毛，露出纯黑色皮肤（#1A1A1A），简化的兽类面部结构，双眼深邃悲悯，映射微弱星光。头顶两只长尖耳朵如鹿角般直立。颈部约30厘米长的白色鬃毛形成天然项圈。表情传达古老智慧与深沉忧伤。深色中性背景。写实生物设计风格，电影级侧光照明，强调毛发体积感与面部黑白反差。等效85mm镜头，浅景深。
```

#### 2. 

**English：**
```
Three-quarter view portrait of a massive divine beast patriarch, from chest up. Creature with pure ivory-white fur (#F5F5F5) approximately 20cm long, face completely hairless with pure black skin (#1A1A1A). Head slightly turned showing the sculptural profile of the black face against white fur backdrop. One long pointed ear visible in full, second ear partially visible behind. Deep wise eyes catching light, revealing star-like reflections in pupils. Thick neck mane flowing downward. Expression of solemn contemplation. Dark neutral background. Photorealistic creature design, Rembrandt lighting creating dramatic shadow on far side of face. Shot with 85mm equivalent lens.
```

**中文：**
```
巨型神兽族长四分之三侧面半身像。全身纯象牙白色毛发（#F5F5F5）约20厘米长，面部完全无毛呈纯黑色皮肤（#1A1A1A）。头部微转，展示黑色面部在白色毛发背景下的雕塑感轮廓。一只长尖耳完整可见，另一只部分遮挡。深邃智慧的眼睛捕捉光线，瞳孔中映射星辰般的反光。厚重颈部鬃毛向下流淌。表情庄严沉思。深色中性背景。写实生物设计风格，伦勃朗式布光在面部远侧形成戏剧性阴影。等效85mm镜头。
```

#### 3. 

**English：**
```
Pure side profile portrait of a massive divine beast patriarch, from chest up. Creature with pure ivory-white fur (#F5F5F5) approximately 20cm long flowing in layers. Side view reveals the beast's noble silhouette: long erect ear on top, sloping forehead, prominent black-skinned face (#1A1A1A) with simplified features, strong jawline, thick white neck mane cascading down. The contrast between the black facial plane and surrounding white fur creates a striking graphic silhouette. Eye visible in profile shows depth and ancient sorrow. Dark neutral background. Photorealistic creature design, edge lighting creating bright rim on fur outline. Shot with 85mm equivalent lens.
```

**中文：**
```
巨型神兽族长纯正侧面半身像。全身纯象牙白色毛发（#F5F5F5）约20厘米长层叠垂落。侧面视角展示神兽高贵的轮廓剪影：头顶长耳直立，额头微倾，突出的黑色皮肤面部（#1A1A1A）五官简化，颌线有力，厚重白色颈部鬃毛向下倾泻。黑色面部平面与周围白毛形成鲜明的图形化轮廓。侧面可见的眼睛展示深邃与远古悲伤。深色中性背景。写实生物设计风格，边缘光在毛发轮廓上形成明亮轮廓光。等效85mm镜头。
```

#### 4. 

**English：**
```
Full body front view of a massive divine beast patriarch standing on all fours. Creature stands 5-6 meters tall at shoulder height, with pure ivory-white fur (#F5F5F5) approximately 20cm long covering entire massive body. Four thick pillar-like legs with dark grey-black claws (#3A3A3A). Face completely hairless with pure black skin (#1A1A1A), two long pointed ears erect on top. Thick white neck mane approximately 30cm long. Short fur-covered tail. Body proportions heavy and mountain-like, front legs slightly taller than rear creating a sloped posture of ancient authority. Overall silhouette resembles a living snow mountain. Dark neutral background. Photorealistic creature design, full-body even lighting to show complete anatomical structure. Shot with 35mm equivalent lens to capture full scale.
```

**中文：**
```
巨型神兽族长全身正面像，四足站立。肩高5-6米，全身覆盖约20厘米长的纯象牙白色毛发（#F5F5F5）。四条粗壮如石柱的腿，深灰黑色爪甲（#3A3A3A）。面部完全无毛呈纯黑色皮肤（#1A1A1A），头顶两只长尖耳直立。颈部约30厘米长的厚重白色鬃毛。短尾被毛覆盖。体型厚重如山丘，前肢略高于后肢形成远古权威的坡形姿态。整体轮廓如一座活的雪山。深色中性背景。写实生物设计风格，全身均匀照明展示完整解剖结构。等效35mm镜头以捕捉完整比例。
```

#### 5. 

**English：**
```
Massive divine beast patriarch seated centrally by a large stone cauldron with roaring bonfire in a hidden mountain valley at 3000+ meters altitude. Creature 5-6 meters tall with pure ivory-white fur (#F5F5F5) approximately 20cm long, hairless pure black face (#1A1A1A) with wise compassionate eyes. Firelight from below casts warm golden-amber reflections (#C9A032) on white fur, creating dramatic chiaroscuro on the black face. Two long erect ears silhouetted against dark sky. Seated in stable patriarch posture at apex of triangular composition. Thick neck mane catches firelight. Atmosphere of primal wilderness domesticity. Snow-covered ground, crude grass shelter visible. Photorealistic, cinematic warm firelight, 80% realism + 20% supernatural stylization.
```

**中文：**
```
巨型神兽族长端坐于隐谷篝火石锅旁，海拔3000米以上的隐蔽山谷。生物高5-6米，全身纯象牙白色毛发（#F5F5F5）约20厘米长，无毛纯黑面部（#1A1A1A），眼神智慧而悲悯。篝火从下方照射在白毛上投射暖金琥珀色反光（#C9A032），在黑色面部形成戏剧性明暗对比。两只长耳在暗色天空中形成剪影。以稳定的族长姿态端坐于三角构图顶点。厚重颈部鬃毛捕捉火光。原始荒野中家居般的氛围。地面积雪，可见简陋草棚。写实风格，电影级暖色火光照明，80%写实+20%超自然风格化。
```

#### 6. 

**English：**
```
Massive divine beast patriarch sitting alone on snow-covered mountain peak under vast starry night sky. Creature 5-6 meters tall with pure ivory-white fur (#F5F5F5) now rendered in cold silver-blue moonlight (#B8C4D0), creating ethereal silver-grey appearance. Hairless pure black face (#1A1A1A) nearly merges with darkness, only the deep eyes visible — reflecting countless stars like windows to the cosmos. Two long erect ears reach toward the star field above. Beside him, a tiny human figure (Zhu Weiyong) sits chained with iron shackles, creating extreme scale contrast. Atmosphere of cosmic loneliness and philosophical stillness. Moonlight cascades across snow like scattered diamonds. Photorealistic, cinematic moonlit scene, desaturated silver-blue palette, 80% realism + 20% supernatural stylization.
```

**中文：**
```
巨型神兽族长独坐于积雪山巅，头顶浩瀚星空。生物高5-6米，纯象牙白色毛发（#F5F5F5）在冷银蓝月光（#B8C4D0）下呈空灵的银灰色调。无毛纯黑面部（#1A1A1A）几乎融入黑暗，仅深邃双眼可见——映射无数星辰如通向宇宙的窗口。两只长耳直指头顶星空。身旁一个渺小的人类身影（朱围庸）被铁链锁住坐着，形成极端的比例反差。宇宙级的孤独感与哲学思辨的宁静氛围。月光如碎钻般倾泻在雪地上。写实风格，电影级月光场景，去饱和的银蓝色调，80%写实+20%超自然风格化。
```

#### 7. 

**English：**
```
Massive divine beast patriarch standing motionless on the highest peak of Fenglang Mountain Range, overlooking vast landscape below. Creature 5-6 meters tall with pure ivory-white fur (#F5F5F5) blown by mountain wind, fur rippling like white banners. Hairless pure black face (#1A1A1A) in natural daylight appears as pure ink. Eyes gaze downward at distant human world with transcendent compassion. Two long erect ears alert to all directions. Standing firm as an ancient stone monument, posture of eternal vigil. Beside him, a slightly smaller aggressive beast (Lingyu) crouches restlessly. Cloud sea below, distant human settlements barely visible. Fur reflects neutral daylight grey-white (#D4D0C8). Atmosphere of detached observation spanning millennia. Photorealistic, cinematic natural daylight, 80% realism + 20% supernatural stylization.
```

**中文：**
```
巨型神兽族长屹立于凤廊山脉最高峰顶，俯瞰下方广袤大地。生物高5-6米，纯象牙白色毛发（#F5F5F5）被山风吹拂，毛发如白色旗帜般波动。无毛纯黑面部（#1A1A1A）在自然日光下呈纯墨色。双眼向下凝视远处人间，超然而悲悯。两只长耳警觉地朝向各方。如远古石碑般坚定不动的屹立姿态，永恒守望之势。身旁一只略小的暴烈神兽（灵尤）不安地蹲伏。下方云海，远处人类聚落依稀可见。毛发反射中性日光灰白色（#D4D0C8）。跨越千年的超然观察氛围。写实风格，电影级自然日光，80%写实+20%超自然风格化。
```

### 老吴 (characters, ★★★★, P3)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese man in his early 60s, short grey-white hair thinning at the forehead, small round eyes with clear bright irises showing warmth and hidden sharpness, thick bushy grey-white eyebrows, wide square honest face with full cheeks, broad bulbous nose with reddened tip, thick lips with a natural gentle expression, deeply tanned dark brown skin with age spots and weathering from outdoor labor, wearing a simple faded brown cotton work shirt, neutral kindly expression with alert intelligence behind the warmth, white neutral background, soft front lighting with warm tone emphasizing the healthy tanned skin, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头中国男性的正面半身肖像，花白短发前额处略显稀疏，圆形偏小的眼睛虹膜清亮透出温暖和隐藏的锐利，花白浓眉略显杂乱，宽阔方正忠厚的面孔面颊饱满，蒜头鼻鼻翼偏宽鼻尖微红，厚唇带自然温和的表情，因长年户外劳作而深度日晒的深褐色皮肤有老人斑和风化痕迹，穿简素褪色棕色棉布工作衬衫，中性和蔼的表情但温暖背后有警觉的智慧，白色中性背景，柔和暖调正面光强调健康的古铜肤色，35mm胶片颗粒感，中高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a Chinese man in his early 60s, short grey-white thinning hair, small round eyes with bright observant gaze, thick grey-white eyebrows, square face with full cheeks and honest expression, broad nose with reddened tip, thick lips, deeply tanned weathered skin with age spots, stocky build visible at shoulders with muscular forearms, wearing a simple faded brown cotton work shirt, expression of quiet contemplation with right hand raised near chin in habitual stroking gesture, white neutral background, warm side lighting from camera-left emphasizing the tanned skin texture and facial creases, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头中国男性的四分之三侧面半身肖像，花白稀疏短发，圆形偏小的眼睛有明亮观察性的目光，花白浓眉，方脸面颊饱满忠厚表情，蒜头鼻鼻尖微红，厚唇，深度日晒的古铜色风化皮肤有老人斑，肩部可见敦实体型前臂肌肉结实，穿简素褪色棕色棉布工作衬衫，安静沉思的表情右手抬至下巴处呈习惯性捻须动作，白色中性背景，左侧暖调侧光强调古铜肤色纹理和面部皱纹，35mm胶片颗粒感，中高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, pure profile bust portrait of a Chinese man in his early 60s, short grey-white hair thinning at crown, prominent broad nose in profile with bulbous tip, thick lips, square jaw with rounded chin, deeply tanned weathered skin showing creases and age spots, stocky neck, wearing a simple faded brown cotton work shirt, calm composed expression, white neutral background, rim lighting from behind outlining the honest sturdy profile, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头中国男性的纯正侧面半身肖像，花白短发头顶处稀疏，侧面可见突出的蒜头鼻宽阔鼻翼，厚唇，方下颌圆钝下巴，深度日晒的古铜色风化皮肤可见皱纹和老人斑，粗壮颈部，穿简素褪色棕色棉布工作衬衫，平静沉着表情，白色中性背景，背后轮廓光勾勒出忠厚结实的侧面轮廓，35mm胶片颗粒感，中高对比度
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a Chinese man in his early 60s, short grey-white thinning hair, clear bright eyes on a square honest face, stocky compact build with broad shoulders and muscular forearms showing bronze tan, medium-short height, standing with feet shoulder-width apart and arms naturally at sides, wearing a faded brown cotton work shirt with sleeves rolled up exposing tanned forearms, dark work trousers, simple cloth shoes, calloused thick hands, posture solid and grounded suggesting physical strength belying his age, white neutral background, warm even lighting, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头中国男性的全身正面肖像，花白稀疏短发，方正忠厚的面孔上眼神清亮，敦实紧凑的体型宽肩膀前臂肌肉结实呈古铜色日晒，中等偏矮身高，双脚与肩同宽双臂自然垂于身侧站立，穿褪色棕色棉布工作衬衫袖子卷起露出晒黑的前臂，深色工装裤，简素布鞋，粗糙厚实的手掌布满老茧，姿态稳固扎实暗示其体力超出年龄所限，白色中性背景，暖调均匀光，35mm胶片颗粒感，中高对比度
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 60s with rejuvenated vitality, short grey-white hair under a straw hat, deeply tanned bronze skin glowing with health, muscular forearms with visible veins, wearing a rough cotton work shirt stained with mud and sweat with sleeves rolled up, dark work trousers tucked into simple boots, a trowel and hammer hanging from a makeshift tool belt, calloused hands showing recent hard labor, face beaming with pride and satisfaction with bright clear eyes, stocky powerful stance suggesting physical vigor, plain dark background, warm golden side lighting suggesting mountain afternoon sun, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头焕发活力的中国男性的全身定妆参考，花白短发上戴草帽，深度日晒的古铜色皮肤透出健康光泽，前臂肌肉结实血管可见，穿粗棉布工作衬衫沾着泥土和汗渍袖子卷起，深色工装裤塞入简素靴子，临时工具带上挂着泥刀和锤子，布满老茧的双手显示近期重体力劳动，面部洋溢骄傲和满足的神情眼神清亮，敦实有力的站姿暗示超越年龄的体力，素色深色背景，暖金色侧光暗示山间午后阳光，35mm胶片颗粒感，中高对比度
```

#### 6. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 60s dressed as a mountain-dwelling retiree, short grey-white hair neatly kept, clear bright eyes with a hint of worried alertness beneath outward calm, wearing a dark grey cotton jacket over a lighter inner shirt, dark simple trousers, plain cloth shoes, a small notebook tucked in jacket pocket barely visible, deeply tanned healthy skin, standing in a relaxed but subtly watchful posture with hands in jacket pockets, plain dark background, natural mixed lighting — warm fill with cool edge suggesting overcast mountain day, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头山居退休者装扮的中国男性全身定妆参考，花白短发整齐，清亮眼神在表面的平静下隐含忧虑的警觉，穿深灰色棉布夹克内衬浅色衬衫，深色简素裤子，平底布鞋，夹克口袋中微微露出一本小笔记本，深度日晒的健康肤色，以放松但暗含警惕的姿态站立双手插在夹克口袋中，素色深色背景，自然混合光——暖色补光配冷色边缘光暗示阴天山间日光，35mm胶片颗粒感，中等对比度
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 60s disguised as a migrant laborer, hair cut shorter than usual, a fake grey beard pasted on chin and jaw altering his appearance to look more rustic and simple, wearing worn rough-cloth work clothes more tattered than his usual attire, simple rope belt, old cloth shoes, carrying a battered cooking utensil suggesting a cook's identity, face deliberately slack with dull harmless expression but eyes betraying sharp alertness on closer inspection, stocky build slightly hunched to appear more subservient, plain dark background, flat overhead lighting typical of indoor work spaces, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头中国男性伪装成外来打工者的全身定妆参考，头发剪得比平时更短，下巴和两腮贴假灰色胡须使外貌看起来更土气更木讷，穿比日常更破旧的粗布工作衣服，简易绳带做腰带，旧布鞋，手提一只破旧的炊事用具暗示厨子身份，面部刻意松弛呈呆滞无害的表情但近看眼中暴露锐利的警觉，敦实体型微微弓背显得更加卑微顺从，素色深色背景，室内工作空间式的平顶光，35mm胶片颗粒感，中等对比度
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 60s as a resistance strategist, face showing deepened wrinkles and increased weariness around eyes compared to earlier stages, grey-white hair slightly disheveled, wearing plain dark cotton civilian clothes with a simple crude vest that could serve as makeshift protection, seated in a wooden chair with a ceramic tea cup held in both calloused hands at chest level, expression grave and contemplative with deep-set intelligent eyes scanning as if assessing a situation, the overall impression is a dependable elder whose body is beginning to show signs of decline, plain dark background, warm interior lighting from camera-right suggesting oil lamp or hearth, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头中国男性作为抵抗军谋士的全身定妆参考，面部皱纹比前期更深眼周疲态加重，花白短发略显凌乱，穿朴素深色棉布平民服装外加一件可充当简易防护的粗制马甲，坐在木椅上双手布满老茧捧着陶瓷茶杯于胸前，表情严肃沉思深陷的睿智眼神如同在审视局势，整体印象是一位可靠的长者但身体开始显出衰退迹象，素色深色背景，右侧暖色室内光暗示油灯或炉火，35mm胶片颗粒感，中高对比度
```

#### 9. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 60s in severe physical and mental decline, face gaunt and sallow with loose sagging skin that was once taut and tanned, eyes vacant and unfocused with milky dullness replacing former brightness, grey-white hair unkempt and matted, wearing torn ragged clothes — shirt ripped at sleeves, trousers shredded below the knee, barefoot with dirty cracked feet, a cloth belt tied around his waist with a trailing end as if used by someone to lead him, body hunched and frail with all former stocky strength dissolved, arms thin and hanging limply, expression blank and absent as if the mind has departed the body, plain dark background, cold desaturated flat lighting draining all warmth from the scene, 35mm film grain, high contrast emphasizing the gauntness
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头中国男性处于严重身心衰退状态的全身定妆参考，面容枯槁蜡黄曾经紧实黝黑的皮肤现在松弛下垂，眼神空洞失焦曾经的清亮被乳白色的混浊取代，花白短发蓬乱打结，穿撕裂破烂的衣服——衬衫袖口撕裂裤子膝盖以下碎烂，赤脚脚底肮脏龟裂，腰间系一条布腰带尾端拖在身后如同被人牵引的痕迹，身体佝偻虚弱此前所有的敦实力量已消散，手臂枯瘦无力垂下，表情空白茫然如同灵魂已离开身体，素色深色背景，冷色去饱和度的平光抽干画面所有暖意，35mm胶片颗粒感，高对比度强调枯槁感
```

### 胡酹 (characters, ★★★★, P3)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a young Chinese man with an imposing muscular build, short spiky black hair standing upright like steel needles, thick dark eyebrows angled slightly upward giving a naturally defiant look, large round eyes with bright black irises full of vitality and barely contained energy, flat broad nose with round fleshy tip, thick lips with corners naturally turned upward in a perpetual cocky half-grin, square jaw wide and powerful, dark tanned skin rough but youthful and healthy with an energetic sheen, massive shoulders and thick neck straining against a simple dark cotton shirt with rolled-up sleeves exposing muscular forearms, expression radiating brash confidence and restless energy, white neutral background, warm front lighting emphasizing the healthy dark skin and muscular definition, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名中国年轻男性的正面半身肖像，身形高大健硕极具压迫感，黑色短发如钢针般向上竖立，粗黑浓眉微微上挑天生一副不服的面相，圆大眼睛明亮的黑色虹膜充满活力和几乎压制不住的能量，塌鼻梁偏宽鼻尖圆钝厚实，厚唇嘴角自然上翘呈永久性的得意半笑，方正下颌宽阔有力，深色日晒粗糙但年轻健康的皮肤带有活力光泽，宽厚肩膀和粗壮脖颈将简素深色棉布衬衫撑满袖子卷起露出肌肉线条分明的前臂，表情散发出张扬的自信和躁动的能量，白色中性背景，暖调正面光强调健康黝黑的皮肤和肌肉线条，35mm胶片颗粒感，中高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a young Chinese man with imposing muscular build, short spiky black hair, thick upward-angled dark eyebrows, large round eyes with an eager gleam directed slightly off-camera as if spotting something interesting, flat broad nose, thick lips curved in an excited grin showing teeth, square powerful jaw, dark tanned rough youthful skin, massive shoulders and thick biceps visible through a simple dark cotton shirt straining at the seams, right fist raised and clenched at chest level in an unconscious gesture of excitement, expression showing barely contained enthusiasm and physical readiness, white neutral background, warm side lighting from camera-left highlighting the muscular definition and the eager animated expression, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名中国年轻男性的四分之三侧面半身肖像，身形高大健硕极具压迫感，黑色短发竖立，粗黑浓眉上挑，圆大眼睛带着热切的光芒微微偏离镜头如同发现了什么有趣的事物，塌鼻偏宽，厚唇弯曲成兴奋的咧嘴笑露出牙齿，方正有力的下颌，深色日晒粗糙但年轻的皮肤，宽厚肩膀和粗壮上臂将简素深色棉布衬衫撑到接缝处，右拳抬起攥紧在胸前呈无意识的兴奋姿态，表情显示几乎压不住的热情和肢体准备感，白色中性背景，左侧暖调侧光突出肌肉线条和热切生动的表情，35mm胶片颗粒感，中高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, pure profile bust portrait of a young Chinese man with imposing muscular build, short spiky black hair bristling upward, thick dark eyebrow visible in profile creating a strong aggressive brow line, large round eye with intense forward gaze, flat nose with broad nostril visible in silhouette, thick lips with upturned corner, square jaw jutting forward with powerful chin, thick muscular neck connecting to massive trapezius and shoulder muscles straining beneath a simple dark cotton shirt, dark tanned rough youthful skin, overall silhouette suggesting coiled physical power and restless energy, white neutral background, rim lighting from behind outlining the powerful muscular profile and spiky hair silhouette, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名中国年轻男性的纯正侧面半身肖像，身形高大健硕极具压迫感，黑色短发如刺般向上竖立，侧面可见粗黑浓眉形成强烈的攻击性眉骨线，圆大眼睛目光直视前方充满力度，塌鼻侧影可见宽阔鼻翼，厚唇嘴角上翘，方正下颌前突有力的下巴，粗壮颈部连接简素深色棉布衬衫下撑满的巨大斜方肌和肩部肌肉，深色日晒粗糙年轻的皮肤，整体侧影暗示蓄势待发的体力和躁动的能量，白色中性背景，背后轮廓光勾勒有力的肌肉轮廓和竖发剪影，35mm胶片颗粒感，中高对比度
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a young Chinese man with imposing muscular build, tall and broad-shouldered towering presence, short spiky black hair, large round expressive eyes on a square-jawed face with thick upturned lips in a cocky grin, dark tanned rough youthful skin, wearing a simple dark cotton short jacket with sleeves rolled up past the elbows exposing thick muscular forearms, a cloth sash tied around the waist, dark loose trousers, simple cloth shoes, hands hanging at sides with fingers slightly curled as if ready to clench into fists at any moment, standing with feet wide apart in a grounded aggressive stance, chest pushed forward, the overall impression is of barely contained physical power — like a spring compressed and ready to release, white neutral background, warm even lighting emphasizing the tall muscular frame and energetic presence, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名中国年轻男性的全身正面肖像，身形高大健硕极具压迫感，高个宽肩如塔般存在感，黑色短发竖立，方正面孔上圆大富有表情的眼睛厚唇上翘带得意笑容，深色日晒粗糙年轻的皮肤，穿简素深色棉布短衣袖子卷过肘部露出粗壮肌肉线条分明的前臂，腰间系布腰带，深色宽松裤子，简素布鞋，双手垂于两侧手指微微弯曲如同随时准备攥拳，双脚大开以扎实富有攻击性的站姿站立，胸膛前挺，整体印象是几乎压制不住的体力——如同一根被压缩到极限随时准备释放的弹簧，白色中性背景，暖调均匀光强调高大健硕的身架和充沛的能量感，35mm胶片颗粒感，中高对比度
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, a pale purple irregular luminous orb floating in void, slightly larger than surrounding orbs with the lightest purple hue among them, surface rippling with slow steady powerful energy waves suggesting immense contained strength, edges pulsing with a calm measured rhythm unlike the rapid anxious patterns of other spirit forms, the orb occasionally expands as if taking a deep breath, pale lavender light particles drift slowly around its perimeter, plain dark background, deep purple ambient glow from below, scattered dim light particles in surrounding void, 35mm film grain, low-key lighting, high contrast between the luminous form and surrounding darkness
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一团淡紫色不规则发光球体悬浮于虚空中，比周围球体略大色调在所有灵魂中最淡，表面以缓慢稳定有力的能量波纹起伏暗示巨大的内蕴力量，边缘以平静有节奏的脉动运行不同于其他灵魂形态的急促焦虑模式，球体偶尔如深呼吸般膨胀，淡薰衣草色光粒子在其周围缓慢飘移，素色深色背景，底部深紫色环境光，周围虚空中散落微弱光粒子，35mm胶片颗粒感，低调照明，发光形态与周围黑暗的高对比度
```

#### 6. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young Chinese man who has recently awakened in a powerful body, tall imposing muscular frame with broad shoulders and thick arms, short spiky black hair, large round eyes wide open with undisguised wonder and excitement at the world around him, square jaw with thick lips split in a broad toothy grin of pure joy, dark tanned rough youthful skin, wearing newly provided simple dark clothes — a cotton jacket slightly too tight across the massive chest with sleeves rolled up exposing forearms, dark trousers, cloth shoes, both fists clenched at his sides in unconscious excitement, stance wide and energetic as if about to burst into motion, the overall impression is of a child's wonder trapped in a warrior's body, plain dark background, warm golden lighting suggesting the joy of rebirth, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名刚在强壮肉体中苏醒的中国年轻男性的全身定妆参考，高大健硕的身架宽肩粗臂，黑色短发竖立，圆大眼睛大睁带着毫不掩饰的对周围世界的惊奇和兴奋，方正下颌厚唇咧开露出一排牙齿纯粹喜悦的大笑，深色日晒粗糙年轻的皮肤，穿新提供的简素深色衣物——棉布外套在宽阔胸膛前略显紧绷袖子卷起露出前臂，深色裤子，布鞋，双拳在身侧无意识地攥紧充满兴奋，站姿大开充满能量如同即将爆发出动作，整体印象是孩子的惊奇困在战士的身体里，素色深色背景，暖金色光线暗示重生的喜悦，35mm胶片颗粒感，中等对比度
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young Chinese man as a rising warrior commander, tall imposing muscular frame radiating aggressive confidence, short spiky black hair slightly disheveled from activity, large round eyes blazing with battle fervor and zealous excitement, square jaw set with thick lips pulled back in a fierce battle grin, dark tanned skin with a sheen of sweat, wearing practical warrior attire — a dark open-front short jacket cinched with a wide cloth sash at the waist, leather arm guards on both forearms, dark trousers tucked into boots, a curved saber hanging from the waist sash, right hand gripping the saber handle, left hand raised in a commanding fist, stance wide and forward-leaning as if about to charge, the overall impression is of a wild tiger barely restrained by its own leash, plain dark background, warm fire-toned side lighting from camera-right suggesting battlefield firelight, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名中国年轻男性作为崛起中的武将的全身定妆参考，高大健硕的身架散发攻击性的自信，黑色短发因活动略显凌乱，圆大眼睛燃烧着战斗的狂热和狂热的兴奋，方正下颌紧咬厚唇后拉露出凶悍的战斗笑容，深色日晒的皮肤泛着汗光，穿实用武士装束——深色开襟短衣以宽布腰带束紧，双前臂佩戴皮质臂甲，深色裤子塞入靴中，弯刀悬挂在腰带上，右手握住刀柄，左手抬起攥拳呈指挥姿态，站姿大开前倾如同即将冲锋，整体印象是一只几乎挣脱缰绳的猛虎，素色深色背景，右侧暖火调侧光暗示战场火光，35mm胶片颗粒感，中高对比度
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young Chinese man as a battle-weary general, still tall and imposingly muscular but now showing visible signs of prolonged warfare, short spiky black hair flattened and matted with dust, dark circles under large round eyes that still hold fierce determination but now carry an undercurrent of exhaustion and moral weariness, square jaw clenched tight with thick lips pressed together in a hard line replacing the former battle grin, dark tanned skin now streaked with grime and minor scratches, wearing returned-being army general armor — dark leather chest plate over layered fabric with visible scratches and battle damage, metal arm guards dented, dark military coat draped over one shoulder, heavy boots scuffed and muddied, a worn saber at his side, standing with arms crossed and weight shifted to one leg suggesting fatigue masked by defiance, plain dark background, cold desaturated side lighting with faint warm undertone suggesting dying embers, 35mm film grain, high contrast emphasizing the weariness beneath the warrior exterior
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名中国年轻男性作为疲倦将军的全身定妆参考，仍然高大健硕极具压迫感但如今可见长期征战的痕迹，黑色短发被灰尘压扁打结，圆大眼睛下有黑眼圈目光仍有凶悍的决心但底色是疲惫和道德厌倦，方正下颌紧咬厚唇紧抿成一条硬线取代了此前的战斗笑容，深色日晒皮肤如今布满灰尘和细小划痕，穿还阳者军团将领铠甲——深色皮质胸甲覆在多层布料上可见划痕和战损，金属臂甲凹陷，深色军大衣搭在一侧肩上，厚重靴子磨损沾泥，身侧挂一把磨损弯刀，双臂交叉站立重心偏向一腿暗示疲惫被倔强掩盖，素色深色背景，冷色去饱和度侧光带微弱暖色底调暗示将灭的余烬，35mm胶片颗粒感，高对比度强调战士外表下的倦怠
```

#### 9. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young Chinese man in his final battle charge, tall muscular frame in full warrior armor — dark leather and metal chest plate, arm guards, leg guards, heavy boots, a saber raised high in right hand, mounted on a dark war horse in mid-gallop, face frozen in a fierce battle roar with mouth wide open showing teeth, large round eyes blazing with the last fire of a warrior who knows only one direction — forward, thick eyebrows angled sharply upward, veins visible on neck and temples from the intensity of the scream, short spiky black hair whipping in wind, dark tanned skin flushed red with battle heat, the armor scratched and battered from an entire campaign, the overall impression is of absolute unstoppable forward momentum — a final charge that will meet its end, plain dark background, harsh cold white light from above mixed with warm red underlighting creating a dramatic split tone of glory and doom, 35mm film grain, very high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名中国年轻男性在最后冲锋中的全身定妆参考，高大健硕的身架全副武装——深色皮质和金属胸甲、臂甲、腿甲、厚重靴子，右手高举弯刀，骑在疾驰的深色战马上，面部定格在凶悍的战吼中嘴巴大张露出牙齿，圆大眼睛燃烧着一个只知道一个方向——前方——的战士最后的火焰，粗黑浓眉锐角上扬，颈部和太阳穴因嘶吼的力度而青筋暴起，黑色短发在风中飞舞，深色日晒皮肤因战斗热血而泛红，铠甲经整场战役的刮擦和磨损痕迹累累，整体印象是绝对不可阻挡的向前冲势——一次将迎来终结的最后冲锋，素色深色背景，上方严酷冷白光混合底部暖红光制造戏剧性的荣光与毁灭的分裂色调，35mm胶片颗粒感，极高对比度
```

### 黄亮伟 (characters, ★★★★, P3)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese man in his early 40s with a prosperous merchant appearance, neat black hair with scattered strands of grey at the temples, sparse curved eyebrows giving a gentle non-threatening look, medium almond-shaped eyes with warm dark irises radiating both shrewdness and genuine kindness, round full face with soft features and plump cheeks, round fleshy nose tip, medium lips with naturally upturned corners forming a perpetual pleasant expression, prominent smile lines radiating from eye corners, fair pinkish skin with a healthy ruddy complexion typical of a well-fed businessman, slightly portly build visible at the rounded shoulders beneath a well-tailored dark blue-grey cotton changshan, expression combining warmth and quiet intelligence — the face of someone who builds trust through sincerity, white neutral background, warm front lighting emphasizing the ruddy complexion and kind expression, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40岁出头中国男性的正面半身肖像，殷实商人外貌，整齐黑发太阳穴处散布几缕灰白，稀疏弯弧形眉毛给人温和不具攻击性的感觉，中等杏仁型眼睛温暖的黑色虹膜同时散发精明与真诚的善意，圆润饱满面孔线条柔和两颊饱满，圆润肉鼻头，中等厚度嘴唇嘴角自然上翘形成永久性的和悦表情，眼角处放射状的显著笑纹，偏白微粉的皮肤带健康红润气色典型的吃得好的商人肤质，深蓝灰色合身棉质长衫下可见圆润肩膀的微胖体型，表情融合温暖与安静的智慧——一张通过真诚建立信任的面孔，白色中性背景，暖调正面光强调红润面色和和善表情，35mm胶片颗粒感，中等对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a Chinese man in his early 40s with a prosperous merchant appearance, neat hair with grey at temples, sparse curved eyebrows, warm almond eyes with an attentive kindly gaze directed slightly off-camera, round full face with plump cheeks and prominent smile lines, fair ruddy skin, slightly portly build in a dark well-tailored changshan, right hand raised with fingers loosely together near chin in a habitual weighing-options gesture, expression thoughtful and benevolent with a hint of business acumen in the focused eyes, white neutral background, warm side lighting from camera-left highlighting the round facial contours and the gesture of deliberation, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40岁出头中国男性的四分之三侧面半身肖像，殷实商人外貌，整齐发型太阳穴处有灰白，稀疏弯弧形眉毛，温暖的杏仁型眼睛带着关切和善的目光微微偏离镜头，圆润饱满面孔两颊丰腴眼角笑纹显著，偏白红润皮肤，深色合身长衫下微胖体型，右手抬起手指在下巴附近松拢呈习惯性的权衡姿态，表情深思温厚聚焦的眼神中透出商业精明，白色中性背景，左侧暖调侧光突出圆润面部轮廓和权衡手势，35mm胶片颗粒感，中等对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, pure profile bust portrait of a Chinese man in his early 40s with a prosperous merchant appearance, neat hair with grey at temples, curved eyebrow visible in profile, almond eye with warm forward gaze, round face with soft chin in profile, round fleshy nose, medium lips with upturned corner visible, prominent smile line creating a gentle crescent on the cheek, fair ruddy skin, slightly portly neck and rounded shoulders beneath a dark changshan, posture upright but relaxed suggesting confidence without arrogance, white neutral background, rim lighting from behind outlining the round gentle profile, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40岁出头中国男性的纯正侧面半身肖像，殷实商人外貌，整齐发型太阳穴处有灰白，侧面可见弯弧形眉毛，杏仁型眼睛目光温暖直视前方，侧面圆润面孔柔和下巴，圆润肉鼻头，中等嘴唇可见上翘嘴角，显著的笑纹在面颊上形成温和的弧线，偏白红润皮肤，深色长衫下微胖的颈部和圆润肩膀，姿态挺直但放松暗示自信而非傲慢，白色中性背景，背后轮廓光勾勒圆润温和的侧面轮廓，35mm胶片颗粒感，中等对比度
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a Chinese man in his early 40s with a prosperous merchant appearance, neat black hair with grey at temples, warm kind eyes on a round full face with prominent smile lines, medium height with a slightly portly build — rounded stomach and soft physique of a well-fed businessman but not obese, wearing a well-tailored dark blue-grey cotton changshan reaching below the knees, dark trousers, clean leather shoes, hands clasped loosely in front with fingers interlaced in a relaxed composed pose, posture upright with a slight forward lean of the shoulders suggesting approachability, the overall impression is of a trustworthy prosperous man — not flashy but quietly successful, white neutral background, warm even lighting, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40岁出头中国男性的全身正面肖像，殷实商人外貌，整齐黑发太阳穴处有灰白，圆润饱满面孔上温暖和善的眼睛显著的笑纹，中等身高微胖体型——圆润的腹部和吃得好的商人柔软身形但不至肥胖，穿合身的深蓝灰色棉质长衫及膝，深色裤子，干净皮鞋，双手在身前松拢十指交叉呈从容镇定的姿态，姿态挺直肩部微微前倾暗示亲和力，整体印象是一个值得信赖的殷实商人——不浮夸但静静地成功，白色中性背景，暖调均匀光线，35mm胶片颗粒感，中等对比度
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 40s as a revitalized merchant at the peak of his success, neat black hair with minimal grey, round full face glowing with ruddy health and satisfaction, warm eyes bright with the light of commercial ambition and gratitude, prominent smile lines deepened by a broad genuine smile, wearing an expensive dark blue-grey silk changshan with subtle pattern embroidery, a lighter inner garment visible at the collar, dark formal trousers, polished leather shoes, right hand raised holding a ceramic wine cup at chest level as if proposing a toast, left hand making an expansive open-palm gesture suggesting grand plans being described, posture upright and confident with chest slightly puffed, the overall impression is of a man enjoying the peak of his fortune with the generosity of someone who remembers hardship, plain dark background, warm golden side lighting suggesting a celebratory banquet atmosphere, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40岁出头中国男性作为事业巅峰的复兴商人的全身定妆参考，整齐黑发灰白极少，圆润饱满面孔泛着红润的健康光泽和满足感，温暖的眼睛闪烁商业雄心和感恩之光，显著笑纹被灿烂真诚的笑容加深，穿昂贵的深蓝灰色丝质长衫带有细微花纹刺绣，领口可见浅色内衬，深色正式裤子，擦亮的皮鞋，右手抬起在胸前举着一只陶瓷酒杯如同在敬酒，左手做出展开掌心的大幅手势暗示正在描述宏大计划，姿态挺直自信胸膛微挺，整体印象是一个正在享受财富巅峰的人但带着记住苦难的慷慨，素色深色背景，暖金色侧光暗示庆功宴会氛围，35mm胶片颗粒感，中等对比度
```

#### 6. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 40s as a departing merchant, neat hair with some grey, round face showing a bittersweet expression — eyes warm with trust and gratitude but brow slightly furrowed with reluctance to leave, smile lines still present but the smile itself is restrained and tinged with sadness, wearing a high-quality dark brown travel overcoat over a lighter changshan, dark trousers, sturdy walking shoes, a leather travel bag slung over one shoulder, one hand extended forward as if reaching to shake someone's hand in farewell, the other hand holding the bag strap, posture leaning slightly forward toward the unseen person being bid farewell, the overall impression is of a good man leaving behind everything he trusts without knowing the truth, plain dark background, warm amber lighting from one side creating long shadows suggesting a sunset departure, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40岁出头中国男性作为离别商人的全身定妆参考，整齐发型带有些许灰白，圆润面孔显示苦乐参半的表情——眼神温暖充满信任和感恩但眉头微微皱起带着不舍，笑纹仍在但笑容本身是克制的染着一层悲伤，穿高品质深褐色旅行大衣内搭浅色长衫，深色裤子，结实行走鞋，一个皮质旅行包斜挎肩上，一只手向前伸出如同在与看不见的人握手告别，另一手握着包带，姿态微微向正在告别的看不见的人前倾，整体印象是一个善良的人在毫不知情中离开他信任的一切，素色深色背景，一侧暖琥珀色光线制造长长的阴影暗示日落时分的离别，35mm胶片颗粒感，中等对比度
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 40s transformed from merchant to resistance supporter, hair now showing more grey and slightly less neat than before, round face thinner with deepened wrinkles and weathering from outdoor exposure, eyes still warm but now carrying the weight of disillusionment and fierce resolve, wearing practical dark cotton clothes replacing the fine changshan — a dark jacket with simple fastenings over a plain inner shirt, dark sturdy trousers, muddied work shoes, a cloth money pouch visible at the waist suggesting his role as financial backer, right hand pressed flat on his own chest over the heart in a gesture of solemn pledge, expression grave and determined with jaw set — the face of a man who has discovered a terrible truth and chosen to act, plain dark background, cool-to-neutral lighting with warm undertone suggesting the transition from comfort to hardship, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40岁出头中国男性从商人转变为抵抗军支持者的全身定妆参考，头发如今灰白更多不如以前整齐，圆润面孔变瘦皱纹加深因户外暴露而风化，眼神仍温暖但如今承载着幻灭的重量和坚定的决意，穿实用深色棉布衣物取代了精致长衫——简单扣合的深色外套内搭朴素衬衣，深色结实裤子，沾泥的工鞋，腰间可见布质钱袋暗示他作为资金支持者的角色，右手掌心平贴在心口呈庄重承诺姿态，表情严肃坚决下颌紧咬——一个发现了可怕真相并选择行动的人的面孔，素色深色背景，冷色到中性的光线带暖色底调暗示从安逸到艰难的过渡，35mm胶片颗粒感，中高对比度
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his mid-to-late 40s as a weary but resolute guardian, hair now predominantly grey and slightly unkempt, round face aged with deeper wrinkles and slightly less plump but still retaining the fundamental roundness, eyes carrying a profound sadness beneath unwavering warmth — the look of someone who has made a promise to the dead and intends to keep it, prominent smile lines now serving as evidence of a kinder past, skin roughened and tanned from years of hardship replacing the former fair complexion, wearing simple clean dark cotton clothes — a plain jacket, trousers, cloth shoes — no luxury but maintained with habitual neatness, right hand extended with palm resting gently on an invisible shoulder in his signature gesture of care, a small wrapped bundle tucked under the left arm suggesting provisions prepared for someone's journey, expression combining paternal warmth with quiet grief, plain dark background, soft cool moonlight-toned lighting from above-left suggesting a nighttime farewell scene, 35mm film grain, medium contrast with soft edges
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40多岁后半中国男性作为疲惫但坚定的守护者的全身定妆参考，头发如今以灰白为主略显凌乱，圆润面孔因更深的皱纹和略有消瘦而苍老但仍保留基本的圆润感，眼神在不动摇的温暖之下承载着深沉的悲伤——一个向逝者做出承诺并打算兑现的人的眼神，显著的笑纹如今成为更善良过去的证据，皮肤因多年艰难而变得粗糙晒深取代了此前的白皙肤质，穿简素干净的深色棉布衣物——朴素外套裤子布鞋——没有奢华但保持习惯性的整洁，右手伸出掌心轻轻放在看不见的肩膀上呈标志性的关怀姿态，左臂下夹着一个包裹好的小包袱暗示为某人旅途准备的物资，表情融合父亲般的温暖与安静的哀伤，素色深色背景，上方偏左柔和冷色月光调的光线暗示夜间送别场景，35mm胶片颗粒感，中等对比度边缘柔化
```

### 十八层塔 (props, ★★★★★, P4)

#### 1. 提示词组A：概念艺术（塔体全景） [概念艺术（塔体全景）]

**English：**
```
"Cinematic still, 2.39:1 widescreen, supernatural underworld aesthetic, ultra-detailed lighting, volumetric atmosphere, professional color grading. Massive architectural tower structure, 18-tiered supernatural construct, layers ascending vertically into darkness. Color palette: deep midnight blue-black (#1A1A2E), dusk blue (#3A4A6B), grey-purple accents (#3A3A5C). Rough dark stone texture, natural weathered surface. No direct light source, only ethereal blue-purple soul glow (#6464C8) scattered throughout tower. Lighting is extremely soft, directionless, almost no shadows. Light intensity decreases from bottom (10%) to top (3%), creating oppressive gradient. Souls depicted as irregular wrinkled circular luminous forms floating between tiers. Architectural detail: clear tier divisions every 8-12 meters, thin thread-like dark roots penetrating from above near the 15th layer (approximately 10cm diameter, soil brown tone #6B5D4F), stark contrast against tower stone. Macro foreground detail: close-up stone surface texture, weathering patterns, faint soul-glow reflections. Overall mood: deep underworld, spiritually oppressive, ancient mechanism of karmic processing. Concept art style, design sheet perspective, multiple angle studies. High contrast between structure and ethereal illumination. No visible characters or figures as focal point, architecture is hero element. Octane render, 8K resolution."
```

**中文：**
```
"电影级截图，2.39:1超宽银幕，超自然冥界美学，极致光影细节，体积雾气，专业调色。巨大的塔状超自然建筑结构，18层清晰分级，向上延伸至黑暗。色彩：深夜蓝黑 #1A1A2E、暮蓝 #3A4A6B、灰紫辅色 #3A3A5C。粗糙深色岩石材质，自然风化纹理，无直射光源，仅有弥散的蓝紫灵魂自光 #6464C8。光线极度柔和、无方向性、几乎无硬阴影，下层 10% 亮度向上层 3% 亮度的压抑光线梯度。灵魂表现为不规则皱褶的圆形发光体在层间漂浮。建筑细节：清晰的层级分隔，每层 8-12 米间距，手指粗细的暗色树根自上方穿透第 15 层附近（约 10cm 直径，土棕色 #6B5D4F），与塔体形成强烈视觉对比。前景细节：岩石表面特写、风化纹理、灵魂光反射。整体氛围：深层冥界、灵魂压抑感、业力处理机制。概念艺术风格、设计稿视角、多角度研究。结构与灵光的高对比。无可见人物作为焦点，建筑为主角。Octane 渲染，8K 分辨率。"
```

#### 2. 提示词组B：场景镜头（灵魂上升通道） [场景镜头（灵魂上升通道）]

**English：**
```
"Cinematic still, 2.39:1 widescreen, supernatural underworld aesthetic, ultra-detailed lighting, volumetric atmosphere, professional color grading. Interior vertical perspective through multi-tiered supernatural tower, mid-ascension viewpoint. Multiple translucent glowing spirit forms (irregular circular shapes) at different heights, slowly ascending through stone tiers. Primary spirit in center-mid-ground, others at various distances creating depth. Core color palette: #1A1A2E tower stone, #3A4A6B shadowed recesses, #3A3A5C texture detail. Spirit glow: blue-purple #6464C8, each spirit casts soft diffuse light upward. Lighting: extremely dim, only spirits provide illumination, light intensity ~6-7% overall, increasing slightly upward. Ethereal volumetric fog effect within layers, creating sense of vast deep space. Atmospheric pressure visible in particle distortion around ascending spirit. Tower walls textured, rough stone with subtle weathering. Upper tiers visible but extremely dim, lower tiers fade to near-black. Psychological oppression conveyed through composition and lighting design. Zero bright colors, zero harsh shadows. Camera angle: upward 30-degree tilt to emphasize scale and ascension. Supernatural ambiance, architectural horror undertone. High-end cinematic lighting, professional post-production color science. No characters with names/identifiable features. Octane render, 8K, studio-quality."
```

**中文：**
```
"电影级截图，2.39:1超宽银幕，超自然冥界美学，极致光影细节，体积雾气，专业调色。超自然塔体内部竖向视角，多层楼梯透视，灵魂上升中段透视。多个半透明发光的灵魂形体（不规则圆形）处于不同高度，缓慢向上漂浮通过石层。主灵魂位于中景偏下，其他灵魂处于不同距离创造纵深感。色彩系统：#1A1A2E 塔体石墙，#3A4A6B 暗处，#3A3A5C 纹理细节。灵魂发光：蓝紫 #6464C8，每个灵魂散发柔和无向光向上。光线：极度昏暗，仅灵魂提供光源，总体亮度 ~6-7%，向上略增。层间浮现灵性体积雾，营造深空感。上升灵魂周围可见气流扭曲，表现灵压。塔壁粗糙岩石纹理，细微风化。上层极度昏暗但可见，下层近乎纯黑。心理压抑感通过构图与光影设计呈现。禁用鲜艳色与硬阴影。摄像机角度：向上 30 度倾斜，强调塔体规模与上升感。超自然气韵，建筑恐怖底蕴。高端电影级光影、专业调色科学。无可见人物或可识别特征。Octane 渲染，8K，演播厅级品质。"
```

#### 3. 提示词组C：设计细节（树根与第15层） [设计细节（树根与第15层）]

**English：**
```
"Concept art, detailed design sheet, close-up architectural section. Section through Tier 15 of supernatural tower, tree roots penetrating stone matrix. Large root structures approximately 10cm diameter (finger-thick), soil brown tone #6B5D4F, organic texture contrast against dark tower stone (#1A1A2E, #3A4A6B). Root surface details: bark texture, moisture shimmer, faint lifeforce aura in pale green (#A8C57A) tone. Stone around roots shows fracture patterns, slight displacement, root-stone interaction zones. Multiple root angles penetrating from upper-right, some curved, some straight, creating directional visual flow. Spirit forms (#6464C8) floating near root contact zones, showing interaction disturbance in their glow. Lighting: ultra-dim key light on root details, volumetric highlight on root surfaces showing life-essence, contrast creates visual hierarchy. Background: darker tower stone fading to silhouette. Cross-section technical view with annotations showing dimensional relationships. Material study emphasis. Multiple detail views: root texture close-up, stone fracture pattern, spirit-root interaction proximity. Color accuracy paramount: root brown must be distinctly warm against tower's cool blue-black palette. No atmospheric haze in this technical view, clean detail visibility. Professional architectural rendering quality. Hard surface detail mastery. Octane, 4K technical illustration."
```

**中文：**
```
"概念艺术，详细设计稿，特写建筑截面。超自然塔体第 15 层截面图，树根穿透石体矩阵。大型树根结构约 10cm 直径（手指粗），土棕色 #6B5D4F，有机纹理对比黑暗塔石 #1A1A2E、#3A4A6B。树根表面细节：树皮纹理、湿润光感、淡生命力绿晕 #A8C57A。树根周围石体显示裂隙纹样、轻微位移、根-石交互区。多条树根自上方穿透，有弧形有直线，创造方向视觉流。灵魂形体 #6464C8 漂浮于树根接触区，其光芒显示交互扰动。光线：超微暗关键光照亮根部细节，体积高光显现根表生命本质，对比创造视觉层级。背景：暗塔石向轮廓淡出。截面技术视图配注释，显示尺寸关系。材质研究为重点。多视角细节：树根材质特写、石裂纹样、灵魂-树根接近度。色彩精度至关重要：树根土棕必须与塔石冷色调 #1A1A2E 形成明显暖冷对比。此技术稿无大气晕，清晰细节呈现。专业建筑渲染品质、硬表面细节掌控。Octane，4K 技术插画。"
```

#### 4. 提示词组D：超自然激活视效 [超自然激活视效]

**English：**
```
"Cinematic still, supernatural visual effect sequence, torment activation vfx concept. Spirit form at center surrounded by invisible force field manifestation, outlined by blue-purple particle halo (#6464C8). Torment layer activation shown as ethereal wave propagation outward from spirit position, reality distortion effect in stone surface directly adjacent. Particle effect: swirling blue-purple wisps, some upward trajectory suggesting suffering ascension, some circular vortex patterns suggesting psychological confusion. Stone surface shows subtle warping where torment force projects, faint purple glow overlay (#7B3FF2 evil spirit marking) visible on spirit's form if applicable. Kinetic energy lines radiating from torment epicenter, invisible forces made visible through particle concentration. Multi-layered depth: immediate particle effects close to spirit, medium-distance stone distortion, background layer still ambient darkness. Lighting: spirit glow intensifies slightly during activation, directional uplighting reinforces upward struggle sensation. Color psychology: cold blue-purple for base torment, warmer purple #7B3FF2 for karmic marking manifestation. Supernatural aura around activating layer shows laminar distortion. Visceral, non-physical representation of spiritual pain. High-end VFX concept, cinematic quality. Octane render, particle dynamics simulation, 6K resolution."
```

**中文：**
```
"电影级截图，超自然视效序列，折磨激活视效概念。灵魂形体居中，被无形力场包围，蓝紫粒子光晕 #6464C8 环绕。折磨层激活表现为灵魂位置向外的灵性波纹扩散，相邻岩石表面现实扭曲效果。粒子效果：旋转蓝紫烟雾，部分向上轨迹暗示痛苦上升，部分圆形涡旋暗示心理混乱。折磨力投射的岩石表面显示细微弯曲，恶灵时可见紫色印记光晕 #7B3FF2 浮现于灵魂身上。动能线自折磨中心辐射，无形力通过粒子浓度可视化。多层纵深：灵魂近处粒子效果、中距石体扭曲、背景层仍是冥界暗。光线：灵魂发光在激活时略增强，向上定向补光强化上升挣扎感。色彩心理学：基础折磨用冷蓝紫，业力印记激活用暖紫 #7B3FF2。激活层周围超自然光晕显示层流扭曲。非物理的灵性痛苦表现，视觉直觉冲击。高端视效概念、电影级品质。Octane 渲染、粒子动力学模拟，6K 分辨率。"
```

#### 5. 提示词组E：终极转化时刻（第18层） [终极转化时刻（第18层）]

**English：**
```
"Cinematic still, 2.39:1 widescreen, supernatural transformation sequence culmination. Spirit form at apex (Tier 18) undergoing final metamorphosis, luminosity spike from normal ~6% to emergency brightness ~20%, creating dramatic light surge upward through tower. Purple karmic marking (#7B3FF2) on spirit's form fragmenting, dissolving into particle cascade, simultaneously new ethereal form coalescing from central luminance. Dual-image transition: old spirit form fading as transparent ghost while new nascent spirit emerges at adjacent position, slightly offset vertically. Light intensity around spirit creates blinding glow halo (managed with careful tonemapping, not blown highlights). Particle effects: purple fragments dispersing outward and downward like shattering crystal, new spiritual essence forming upward-spiral pattern in blue-purple #6464C8. Tower stone around apex bathed in unusual brightness, creating dramatic chiaroscuro. Upper tiers above spirit now fully visible due to light surge, revealing emptiness and finality. Metaphysical rebirth concept: old identity erased, new possibility emergent. Emotional tone: transcendence, completion, cyclical return. Camera angle: slight upward tilt emphasizing breaking free from tower structure. Zero harsh colors, maintains cool palette throughout. VFX-heavy moment, maximum supernatural intensity. Octane render, HDR capable, 8K, dramatic post-color-grade."
```

**中文：**
```
"电影级截图，2.39:1超宽银幕，超自然转化序列高潮。灵魂形体位于塔顶（第 18 层）经历终极蜕变，亮度从常态 ~6% 激增至紧急亮度 ~20%，光爆向上贯穿全塔。灵魂身上紫色业力印记 #7B3FF2 碎裂、溶解成粒子级联，同时新灵性形体从中心光芒凝聚。双重影像转换：老灵魂形体淡出如透明幻像，新生灵魂在相邻位置浮现，略有竖向偏移。灵魂周围光晕（可控影调映射，避免溢出高光）。粒子效果：紫色碎片向外向下飞散如同晶体破碎，新灵本质形成向上螺旋纹样蓝紫 #6464C8。塔顶周围岩石沐浴异常亮度，戏剧性明暗对比。顶层上方因光爆而完全可见，显露空虚与终局感。隐喻灵魂重生：旧身份抹除、新可能浮现。情绪色调：超越、完成、循环回归。摄像机角度：轻微向上倾斜强调摆脱塔体束缚的突破感。禁用刺眼色，全程维持冷色调。视效密集时刻、最大超自然强度。Octane 渲染、HDR 支持、8K、戏剧性调色分级。"
```

### 数字人躯体 (props, ★★★★★, P4)

#### 1. 提示词1：空壳期 - 整体状态 [空壳期]

**English：**
```
Digital Human Body · Empty Shell Phase | Full State

A perfectly formed human body lies supine on a cold-lit experimental table,
skin reconstructed with atomic precision, anatomically perfect symmetry.
Eyes open but completely vacant and lifeless, pupils fixed,
like a living being frozen in amber.

Transparent nutritional fluid tube connected to left upper arm,
liquid flowing slowly to sustain the most basic physiological metabolism.
Medical-grade stainless steel electrode leads connected to right hand and left chest,
precisely installed with surgical accuracy, every line perfectly straight.

Skin tone subtly deviates from natural—too perfect, too uniform,
lacking the microscopic imperfections, vascular texture, and subtle pores of real skin.
Under cold white laboratory light (#F5F5DC),
the body appears clinical and fundamentally alien to this world.

Body completely relaxed, zero autonomous muscle tension,
existing in an uncanny state between living person and object.
Background shows advanced life support equipment, screens displaying stable vital parameters.
```

**中文：**
```
数字人躯体·空壳期｜整体状态

一具完美的人形躯体仰卧于冷光实验台，
皮肤以原子级精度重建，解剖学完美对称。
眼睛睁着但完全呆滞无神，瞳孔固定，
仿佛琥珀中被冻结的生命。

左上臂连接透明营养液硅胶管，
液体缓慢流入躯体维持最基础的生理代谢。
右手背和胸部左侧连接医用不锈钢电极导线，
精确医学级安装，每一根都笔直有序。

肤色略显偏离自然——过于完美、过于均匀，
缺乏真实皮肤的微观瑕疵、血管纹理、细微毛孔。
在冷白实验室光（#F5F5DC）的映照下，
躯体显得生冷而不属于这个世界。

身体完全松弛，无任何自主肌肉张力，
呈现一种介于人和物品之间的诡异状态。
背景是先进的生命监测设备，屏幕显示稳定的生理参数。
```

#### 2. 提示词2：空壳期 - 眼睛特写 [空壳期]

**English：**
```
Digital Human Body · Empty Shell Phase | Eyes Close-Up

Extreme close-up: a pair of open eyes,
pupils fixed and motionless, no focal point, no luster.
Eye whites are excessively bright, lacking the subtle vascular texture of real eyes.
Eye muscles surrounding completely relaxed, no wrinkles or expression lines.

Iris color and texture perfect yet lifeless,
like carefully crafted doll eyes rather than living human eyes.
Eyelids neither squinting nor fully open, in a disturbing neutral state.
Light reflection points on tear film remain fixed, unchanging with viewing angle.

Cold white light illuminates the eyes directly,
creating an unsettling sense of lifelessness.
```

**中文：**
```
数字人躯体·空壳期｜眼睛特写

极近距离特写：一双睁开的眼睛，
瞳孔固定不动，没有焦点，没有光泽。
眼白部分过于洁白，缺乏真实眼睛的微妙血管纹理。
眼睛周围肌肉完全松弛，没有任何皱纹或表情线。

虹膜的颜色和纹理完美但死气沉沉，
如同精心制作的人偶眼睛而非活人之眼。
眼睑既不眯起也不完全睁大，处于一种病态的中立状态。
泪膜光反射点的位置固定，不随观看角度改变。

冷白光直照眼睛，
创造出一种令人不适的无生命感。
```

#### 3. 提示词3：空壳期 - 导管与导线细节 [空壳期]

**English：**
```
Digital Human Body · Empty Shell Phase | Medical Interface System

Medium shot: left upper arm and right chest area of the body.

Left arm: transparent silicone nutritional fluid catheter enters through skin,
fluid inside appears clear and colorless,
medical adhesive tape secures the catheter to skin,
liquid drips into the body at a constant, slow rate.

Right hand: 3 thin and precise medical electrode leads emerge from skin surface,
each line perfectly straight and orderly, secured with sterile medical tape.
Left chest (heart region): 2 similar electrode leads,
connected to monitoring equipment displaying physiological parameters.

All leads and tubes exhibit surgical-grade perfect installation—
no redundancy, no looseness, no sign of disorder.
Background shows medical-grade stainless steel and transparent plastic equipment,
emanating the cold metallic luster of a laboratory.
```

**中文：**
```
数字人躯体·空壳期｜医疗接入系统

中景镜头：躯体的左上臂和右侧胸部区域。

左上臂：透明硅胶营养液导管从肌肤进入，
导管内的液体呈清澈无色，
医用贴膜将导管固定在皮肤上，
液体以恒定的缓慢速率滴入躯体。

右手背：3根细且精确的医用电极导线从皮肤表面引出，
每根导线都笔直有序，用无菌医用胶带固定。
胸部左侧（心脏区域）：2根类似的电极导线，
连接到一台显示生理参数的监测设备。

所有导线和管道都呈现医学级的完美安装——
无冗余、无松散、无任何混乱的迹象。
背景是医用级不锈钢和透明塑料的设备，
散发出实验室的冷金属光泽。
```

#### 4. 提示词4：注魂期 - 眼睛苏醒（状态转变对比） [注魂期]

**English：**
```
Digital Human Body · State Transformation | Eye Awakening Comparison

Comparative dual-frame composition:

【Left - Empty Shell Phase】
Eyes open but completely vacant, pupils fixed,
like frozen amber, no light of life.

【Right - Soul-Infused Phase】
Same eyes, pupils now vivid and focused,
subtle vascular texture and reality emerge in eye whites,
tiny muscle contractions around eyes,
fine wrinkles of a living person appear at eye corners.
Pupil dilation/constriction shows optical response capability,
eyes now possess an indescribable "light"—
this is consciousness, self-awareness, the awakening of soul.

Tear film reflection points now change with light and viewing angles,
completely consistent with real human eye optics.
Eyes are no longer dead objects, but windows opening to an inner world.

Color contrast: Left cold white lifeless vs. Right warm and vibrant
```

**中文：**
```
数字人躯体·状态转变｜眼睛苏醒对比

对比式双画面构图：

【左侧 - 空壳期】
眼睛睁着但完全空洞，瞳孔固定，
仿佛冻结的琥珀，没有生命的光。

【右侧 - 注魂期】
同一双眼睛，瞳孔变得灵动而有焦点，
眼白中出现微妙的血管纹理和真实感，
眼睛周围肌肉有细微的收缩，
眼角处出现了活人才有的细纹。
瞳孔扩张/收缩显示光学反应能力，
眼神中出现了一种无法言说的"光"——
这是意识、自我认知、灵魂的觉醒。

泪膜反射点现在随光线和视线角度变化，
完全符合真实人眼的光学特性。
眼睛不再是死物，而是一扇通向内在世界的窗口。

色彩对比：左侧冷白无光 vs. 右侧温暖有生机
```

#### 5. 提示词5：注魂期 - 整体复苏 [注魂期]

**English：**
```
Digital Human Body · Soul-Infused Phase | Complete Awakening

A body sits up from the experimental table,
eyes visibly transformed—from vacant to focused.
Skin color recovered natural warmth,
subtle vascular texture and pore details emerge,
cheeks and lips regained delicate color.

Body is no longer the perfect medical model,
but a living, breathing person:
subtle asymmetries, fine wrinkles, the warmth of life.

Hands naturally rest on legs, fingers show gentle curl and relaxation,
displaying recovered muscle tone.
Head can turn, eyes track light and movement.
Breathing is natural and rhythmic, chest rises and falls with life.

Facial expressions are no longer fixed—
mouth corners show subtle relaxation, eye corners display fine wrinkles,
displaying a conscious being processing the world around them.

Though still under the laboratory's cold light,
this body is no longer an object,
but an independent individual with consciousness, self, and soul.
```

**中文：**
```
数字人躯体·注魂期｜完全复苏

一具躯体从实验台坐起，
眼神明显改变了——从空洞变成焦点明确。
肤色恢复了自然的温暖，
细微的血管纹理、毛孔纹理，
面颊和嘴唇恢复了轻微的血色。

身体不再是医学模型的完美，
而是一个活生生的人：
有微妙的不对称、有细微皱纹、有生命的温度。

双手自然放在腿上，手指有轻微的蜷曲放松，
显示肌肉张力已经恢复。
头可以转向，眼睛能追踪光线和运动。
呼吸是自然而有节奏的，胸腔起伏有生命感。

面部表情不再固定——
嘴角有轻微的松弛感、眼角有细纹的变化，
显示着一个意识正在处理世界的活人。

虽然仍在实验室的冷光中，
但这个躯体已经不再是物品，
而是一个有意识、有自我、有灵魂的独立个体。
```

#### 6. 提示词6：注魂期 - 肤质与微观变化 [注魂期]

**English：**
```
Digital Human Body · Soul-Infused Phase | Skin Texture Details (Macro View)

Close details of body's arms and face.

Skin transformation from "excessive perfection" to "natural reality":
visible pores distributed according to natural human texture,
subtle wrinkles appear at eye corners, mouth corners, forehead,
suggesting a body that has lived and experienced.

Vascular texture faintly visible at wrists, temples, neck,
suggesting active blood circulation.

Natural and uneven color distribution on facial skin:
cheekbones show slight rosy tone,
temples display subtle blue blood vessels,
lips recovered delicate pink color.

Skin surface reflection transformed from "medical-grade mirror finish" to "natural glow of living human skin,"
reflecting sebum layer and subtle surface irregularity.

Every detail tells the story:
this is no longer a perfect creation,
but a truly living being.
```

**中文：**
```
数字人躯体·注魂期｜肤质细节（宏观视角）

躯体的手臂和脸部的细节特写。

皮肤从 "过度完美" 转变为 "自然真实"：
可见的毛孔分布遵循人体自然纹理，
微妙的皱纹出现在眼角、嘴角、额头，
显示这是一个活过、经历过的身体。

血管纹理在手腕、太阳穴、脖子处隐约可见，
提示活跃的血液循环。

面部肌肤的血色分布自然而不均匀：
颧骨处略显红润，
太阳穴处有微妙的青色血管，
嘴唇恢复了淡淡的粉红色。

皮肤表面反光从 "医用级镜面" 变成 "活人肌肤的自然光泽"，
反映出皮脂膜和细微的表面不平度。

每一处细节都在诉说：
这不再是一个完美的造物，
而是一个真实活着的生命。
```

#### 7. 提示词7：实验室环境 - 空壳期背景 [实验室环境]

**English：**
```
Digital Human Body · Environment | Underground Laboratory (Empty Shell Phase)

A sealed underground laboratory, the heart of Dadda Kingdom's secret research.

Space design:
Cold white fluorescent lights (#F5F5DC color temperature) powerfully illuminate the entire space,
creating an atmosphere of sterility, rationality, and transcendence.
Walls use medical-grade white or light gray paint,
reflecting cold light, reinforcing the laboratory's objectivity.

Equipment layout:
Body lies on the central experimental life-support table,
tabletop is mix of medical-grade stainless steel and transparent acrylic,
displaying professional medical laboratory appearance.

Surrounding advanced life monitoring equipment:
screens display heart rate, brain waves, body temperature, nutritional fluid flow rate and other parameters,
numbers and waveforms jump on screens,
yet these data only reflect the physiological state of an "empty shell."

Pipe and equipment arrangement precise yet organized,
every connection meets medical-grade installation standards.

Overall atmosphere:
austere, rational, filled with scientific spirit,
yet carrying an ineffable uncanniness and disturbing sensation.
This is not a hospital (too warm, too humane),
but a pure experimental forbidden zone pursuing technological breakthrough.
```

**中文：**
```
数字人躯体·环境｜地下实验室（空壳期）

密闭的地下实验室，是定达国都秘密研发的中心。

空间设计：
冷白色荧光灯（#F5F5DC色温）强力照亮整个空间，
创造出一种无菌、理性、超越常规的气氛。
墙壁采用医用级白色或浅灰色涂料，
反射冷光，强化实验室的客观性。

设备布局：
躯体躺在中央的实验生命维持台，
台面是医用不锈钢和透明有机玻璃混合，
显示出专业医学实验室的外观。

周围是数台高端生命监测设备：
屏幕显示心率、脑波、体温、营养液流速等参数，
数字和波形在屏幕上跳动，
但这些数据只反映一个 "空壳" 的生理状态。

管道与设备的布置精确而无序，
每一个连接都符合医学级安装标准。

整体氛围：
冷峻、理性、充满科学精神，
却又带有一种不可名状的诡异和令人不安的气息。
这里不是医院（太温暖、太人道），
而是一个纯粹追求技术突破的实验禁地。
```

#### 8. 提示词8：实验室环境 - 注魂期后的变化 [实验室环境]

**English：**
```
Digital Human Body · Environment | Underground Laboratory (After Soul Infusion)

Same laboratory, but atmosphere has fundamentally changed.

Body still on life-support table, but no longer a lifeless object—
body position has shifted (perhaps sitting more upright),
eyes have focal point (this transforms the entire room's psychological impact).

Cold white light still illuminates the laboratory,
but now this light reflects off a **living** person's face,
not an "object."

Life monitoring equipment screens now display different patterns:
heart rate becomes fluctuating (reflecting emotion and thought),
brain waves show complete conscious activity patterns,
data no longer flat "maintenance mode,"
but complex signals "in activity."

Space still austere and rational,
but this rationality no longer targets "dead objects,"
but surrounds an **independent life** in scientific observation.

Overall effect:
from "anatomy laboratory" transforms to "consciousness laboratory";
from "object inspection" transforms to "life observation";
from "cold engineering" transforms to "science with ethical weight."
```

**中文：**
```
数字人躯体·环境｜地下实验室（注魂期后）

同一个实验室，但氛围已然改变。

躯体仍在生命维持台上，但不再是一个无生命的对象——
身体的位置改变了（可能更向上坐起），
眼神有了焦点（这改变了整个房间的心理感受）。

冷白光仍然照亮实验室，
但现在这光线映照在一个 **活着的** 人脸上，
而不是一个 "物品"。

生命监测设备的屏幕现在显示不同的模式：
心率变得有波动（反映情感和思考），
脑波显示完整的意识活动模式，
数据不再是单调的 "维持模式"，
而是 "活动中" 的复杂信号。

空间仍然冷峻、理性，
但这种理性不再是针对 "死物"，
而是围绕一个 **独立生命** 的科学观察。

整体效果：
从 "解剖学实验室" 转变为 "意识实验室"；
从 "物品检查" 转变为 "生命观测"；
从 "冷漠的工程" 转变为 "带有伦理重量的科学"。
```

### 泉水 (props, ★★★★★, P4)

#### 1. 

**English：**
```
"Cinematic still, 2.39:1 widescreen aspect ratio, color graded, professional cinematography, high production value"
```

**中文：**
```
"电影级静帧，2.39:1 超宽银幕宽高比，色彩分级处理，专业摄影级质感，高制作水准"
```

#### 2. 提示词 1：泉水概念艺术（整体场景） [泉水概念艺术（整体场景）]

**English：**
```
Cinematic still, 2.39:1 widescreen aspect ratio, color graded, professional cinematography, high production value.

Concept art of a mystical natural spring pool nestled deep in mountains, approximately 2.5-3.0 meters in diameter and 0.5 meters deep. Crystal-clear water with ethereal royal blue self-glow (#4169E1) emanating soft upward-scattering light, creating ripple light patterns on surrounding rocks and foliage. Dappled sunlight filters through dense banyan tree canopy overhead. Pool surrounded by moss-covered rocks (#4A6741 moss-green coloring), wild grass, and small flowers. Clear cold stream approximately 1.0 meter wide flows into the pool from mountain source. Natural stone banks, weathered brown (#2C1810), no artificial modification. Atmosphere: misty mountain valley, humid air, serene and sacred. Soft light casting gentle shadows. Photography: 35mm equivalent focal length, shallow depth of field, warm color grading with blue highlights on water.
```

**中文：**
```
电影级静帧，2.39:1 超宽银幕宽高比，色彩分级处理，专业摄影级质感，高制作水准。

深山之中的神秘天然泉水池概念艺术，直径约 2.5-3.0 米，深度约 0.5 米。晶莹清澈的水体散发着缥缈的皇家蓝色（#4169E1）自发光，柔和的光线向上散射，在周围岩石与植被上投射波纹光斑。密集的榕树树冠从上方漏下斑驳的阳光。池周围分布苔藓覆盖的岩石（深绿色苔藓 #4A6741），野草与小花点缀。清冷的山泉溪流宽约 1.0 米，从山源汇入池塘。天然岩石池壁，多年侵蚀呈焦褐色（#2C1810），无人工修饰。氛围：深山幽谷，湿润空气，宁静而神圣。柔和光线投射温柔阴影。摄影：35mm 等效焦距，浅景深，温暖色调分级，水体蓝光高光处理。
```

#### 3. 提示词 2：泉水场景（角色近景互动） [泉水场景（角色近景互动）]

**English：**
```
Cinematic still, 2.39:1 widescreen aspect ratio, color graded, professional cinematography, high production value.

Close-up scene of a character kneeling beside the mystical spring pool, reaching down to collect water in a ceramic vessel. Crystal-clear spring water with soft royal blue self-glow (#4169E1) illuminating the character's face and hands with gentle light patterns. Ripple light scattering across the character's features and surrounding moss-covered stones. Massive banyan tree roots visible in background, filtered sunlight creating dappled shadows. Atmospheric mist rising slightly from the water. Water surface showing gentle ripples, perfectly transparent bottom with visible dark-green moss-covered rocks (#4A6741). Character's expression conveys reverence and gratitude toward the sacred water. Intimate composition emphasizing connection between character and supernatural spring. Color palette: cool blues from water glow balanced against warm earth tones of rocks and foliage. 50mm lens equivalent, shallow depth of field, cinematic color grading.
```

**中文：**
```
电影级静帧，2.39:1 超宽银幕宽高比，色彩分级处理，专业摄影级质感，高制作水准。

一名角色半蹲在神秘泉水池旁，低身伸手用陶瓷容器取水的近景场景。晶莹清澈的泉水散发柔和皇家蓝色自发光（#4169E1），温柔的光线照亮角色的面部与双手，投射出波纹光斑图案。波纹光线散射到角色五官与周围苔藓覆盖的石头上。背景可见巨大的榕树根系，透过树叶的阳光形成斑驳阴影。空气中轻微的水雾上升。水面呈现轻微波纹，池底清晰可见，深绿色苔藓覆盖的岩石（#4A6741）清晰可辨。角色表情传达对圣水的敬畏与感恩。构图强调人物与超自然泉水的连接。色调：泉水冷蓝自发光与岩石及植被暖色调的平衡。50mm 等效焦距，浅景深，电影级色彩分级。
```

#### 4. 提示词 3：泉水设计元素表（多角度设计稿） [泉水设计元素表（多角度设计稿）]

**English：**
```
Cinematic still, 2.39:1 widescreen aspect ratio, color graded, professional cinematography, high production value.

Design sheet: multiple angles and closeups of mystical spring water for visual effects reference. Top angle: overhead view of circular pool, 2.5-3.0m diameter, crystal-clear water with soft royal blue self-glow (#4169E1) radiating upward, visible ripple patterns and light scattering. Side angle: profile view showing pool depth approximately 0.5 meters, natural stone banks (#2C1810 brown), clear stream inlet approximately 1.0m wide, water surface reflections and subsurface visibility. Close-up: water texture detail showing perfect clarity, subtle ripple light patterns (波纹光斑) scattering upward from water surface. Bottom detail: moss-covered rocks (#4A6741 deep moss-green) on pool floor, water transparency showing complete visibility. Light study: soft blue self-glow (#4169E1) emanating 50cm above water surface, projecting ripple patterns on surrounding rocks and foliage, no harsh shadows. Reference: style guide for consistent visual treatment, CG modeling specifications, texture and lighting parameters for production.
```

**中文：**
```
电影级静帧，2.39:1 超宽银幕宽高比，色彩分级处理，专业摄影级质感，高制作水准。

泉水设计表：视觉效果参考用的多角度与特写图。俯视角：圆形池塘俯瞰图，直径 2.5-3.0 米，晶莹清澈的水体散发柔和皇家蓝色自发光（#4169E1）向上辐射，清晰可见波纹图案与光线散射。侧视角：池塘深度约 0.5 米的侧面图，天然岩石池壁（焦褐色 #2C1810），清冷溪流进水口宽约 1.0 米，水面反射与水下清晰可见。特写：水体质感细节呈现完美清澈，轻微的波纹光斑（波纹光斑）从水面向上散射。底部细节：池底苔藓覆盖的岩石（深苔绿色 #4A6741），水体透明度完全可见池底。光学研究：柔和蓝色自发光（#4169E1）向上辐射约 50cm，在周围岩石与植被上投射波纹图案，无生硬阴影。参考：视觉一致性风格指南，CG 建模规格说明，生产级材质与光照参数。
```

#### 5. 提示词 4：泉水超自然发光效应（激活状态） [泉水超自然发光效应（激活状态）]

**English：**
```
Cinematic still, 2.39:1 widescreen aspect ratio, color graded, professional cinematography, high production value.

VFX reference: mystical spring water in activation state during healing process. Crystal-clear water with intensified soft royal blue self-glow (#4169E1) radiating upward in gentle, natural light scatter. Ripple light patterns (波纹光斑) flowing across water surface and projecting onto surrounding rocks, character faces, and foliage. Glow intensity: low to medium, soft and non-glaring, maintaining ethereal quality. Light projection: approximately 50cm vertical range above water surface, creating natural dappled light patterns on shore surfaces. Water surface: maintains perfect clarity and transparency, showing subtle wave ripples synchronized with light scatter. No additional visual effects, no magical symbols or particle systems—the water's inherent supernatural nature is expressed purely through its self-glow and light projection. Lighting: natural cinematic lighting with emphasis on water's ethereal blue luminescence as primary light source in dark environments. Reference for: shader parameters, light intensity values, bloom and glow settings, ripple animation patterns.
```

**中文：**
```
电影级静帧，2.39:1 超宽银幕宽高比，色彩分级处理，专业摄影级质感，高制作水准。

视觉效果参考：泉水在治疗过程中的激活状态。晶莹清澈的水体散发加强的柔和皇家蓝色自发光（#4169E1），温柔地向上辐射自然光线散射。波纹光斑（波纹光斑）在水面流动并投射到周围岩石、角色面部与植被上。发光强度：低至中等，柔和而不刺眼，保持缥缈气质。光线投影：约 50cm 垂直范围向上辐射，在岸边表面形成自然斑驳光斑图案。水面：保持完美清澈透明，呈现与光线散射同步的轻微波纹。无额外视觉效果，无魔法符号或粒子系统——泉水的超自然本质完全通过自发光与光线投影表达。光照：自然电影级光照，强调水体缥缈蓝色发光作为暗环境中的主要光源。参考用于：着色器参数、光强度数值、泛光与发光设置、波纹动画参数。
```

#### 6. 提示词 5：泉水治疗汤药场景（老吴准备汤药） [泉水治疗汤药场景（老吴准备汤药）]

**English：**
```
Cinematic still, 2.39:1 widescreen aspect ratio, color graded, professional cinematography, high production value.

Scene: elderly caretaker preparing healing herbal broth using spring water. Character heating spring water collected in ceramic vessel over open fire, adding medicinal herbs and ingredients. Spring water retains its crystalline clarity and soft royal blue self-glow (#4169E1) even when being heated—subtle luminescence visible through steam and mist. Surrounding environment: rustic cooking setup in mountain setting, natural stone surfaces, traditional pottery. Warm firelight contrasts with cool blue glow of water. Character's weathered hands visible, showing care and reverence in preparation. Background: mountain wilderness, natural foliage. Lighting: interplay between warm firelight and cool ethereal blue water glow, creating dramatic cinematic contrast. Composition emphasizes the sacred nature of water and its healing purpose. Color grading: warm earth tones offset by supernatural blue highlights.
```

**中文：**
```
电影级静帧，2.39:1 超宽银幕宽高比，色彩分级处理，专业摄影级质感，高制作水准。

场景：老年照看者用泉水准备治愈草药汤的过程。角色将收集的泉水装在陶瓷容器中在篝火上加热，加入草药与医疗成分。泉水即使在加热过程中也保持晶莹透明与柔和皇家蓝色自发光（#4169E1）——蒸汽与雾气中可见微妙的发光。周围环境：山区自然烹饪设置，岩石表面，传统陶土容器。温暖的火光与冷蓝的水体发光形成对比。角色布满沧桑的双手可见，体现在准备过程中的关怀与敬畏。背景：山区荒野，自然植被。光照：温暖火光与缥缈蓝色水体发光的相互作用，形成戏剧化电影对比。构图强调水的神圣本质与其治愈目的。色彩分级：温暖的土色调与超自然蓝色高光的平衡。
```

### 美女榕 (props, ★★★★★, P4)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, golden hour lighting.
Ancient banyan tree with massive 3-meter trunk, deeply furrowed bark in dark saddlebrown (#2C1810),
crown spread 20m across with moss-green canopy (#4A6741) filtering dappled sunlight.
Intricate root system fully exposed across earth mound, roots intertwined and sculptural,
arranged in subtle female silhouette lying in repose—delicate "leg roots" extending into
clear mountain stream below. Fine fingerlike root (~10cm diameter) near water's edge
glowing with ethereal dark purple luminescence (#5B3A6B), subtle energy pulse visible.
Surrounding landscape: wildflower meadow, grass, flowing spring water creating gentle ripples.
Tree exudes sacred, otherworldly presence. Atmospheric haze from afternoon light.
No human figures. Cinematic depth of field. Shot from ground level,
emphasizing tree's monumental scale and organic root geometry. Professional nature cinematography.
```

**中文：**
```
电影级截图，2.39:1超宽银幕，黄金时刻光线。
巨大古榕树干约3米直径，树皮深褶皱呈焦褐色（#2C1810），枝冠蔓延20米，
苔绿叶片（#4A6741）形成天然遮荫，阳光透过叶幕形成斑驳光影。
根系完全裸露于隆起的土堤上，盘旋交织成复杂的雕塑状根网，排列呈仰卧女性轮廓—
两条细长"腿根"伸入山溪清水中。指根（直径约10厘米）位于水边，
散发幽幽暗紫色光晕（#5B3A6B），能量脉动可见。
周边环境：野花草地、溪流、浅浪涟漪。树体呈现神圣、超自然气质。
下午光线造成的大气雾气。无人物。电影级景深效果。
从地面视角拍摄，强调树体的宏大尺度与根系的有机几何美感。专业自然摄影风格。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, mystical lighting, dusk atmosphere.
Ancient banyan tree root system actively alive with supernatural energy.
Fingerlike root glowing intensely with dark purple luminescence (#5B3A6B),
radiant aura expanding 2-3m radius around gateway root.
Energy pulse flowing along major root network—visible as flowing violet light trails
tracing root geometry from fingertip root upward through main root system.
Tree trunk trembling subtly (amplitude ~15cm), branches swaying gently, leaves rippling.
Entire root system appears to breathe—roots contracting and releasing rhythmically.
Translucent ethereal silhouette (spirit/soul) mid-compression, coneshaped,
entering the small root portal, surrounded by protective purple aura.
Water surface showing subtle ripples and reflection of purple glow.
Atmosphere: mystical, sacred, inter-dimensional gateway activation moment.
Professional VFX cinematography, supernatural realism, no oversaturation.
```

**中文：**
```
电影级截图，2.39:1超宽银幕，神秘光线，黄昏氛围。
古榕根系充满生命的超自然能量。指根闪耀着强烈的暗紫色光晕（#5B3A6B），
发光光圈向外扩展约2-3米半径。能量脉流沿着整个根系网络流动，
呈现为紫色光痕轨迹，从指根开始沿主根网向上蔓延。
树干微微振颤（振幅约15厘米），枝条轻轻摇晃，叶片随之波动。
整个根系呈现呼吸感—根须有节奏地蜷缩与放松。
半透明的灵体轮廓正在压缩中，锥形状，进入细小的根系通道口，
被保护性的紫色光晕环绕。水面显示细微涟漪与紫光倒影。
氛围：神秘、神圣、次元通道激活的瞬间。
专业VFX电影风格，超自然写实，无过度饱和色彩。
```

#### 3. 

**English：**
```
Production design reference sheet, technical illustration style, multiple angles.
Ancient banyan root system architectural reference. Show three angles:
[Top View] Complete root network plan, highlighting female silhouette geometry,
noting trunk position, fingerlike gateway root location, major root paths, water interface.
[Isometric 3D] Root structure showing intertwined root topology, depth variation,
surface texture (smooth wood in gateway area, rough weathered bark in older roots).
[Close-up Detail] Gateway root (10cm diameter, ~10cm long) cross-section and surface detail,
showing internal wood fiber color (#6B4423 reddish-brown), smooth exterior surface,
base connection to major root network, scale indication with measurement marks.
Include color palette swatches: #4A6741 (moss-green), #2C1810 (dark brown bark),
#6B4423 (wood interior), #5B3A6B (energy purple), with material notes.
Cinematic lighting on reference, clean technical drafting aesthetic.
```

**中文：**
```
制作设计参考稿，技术插画风格，多角度展示。
古榕根系建筑学参考。展示三个视角：
[俯视图] 完整根系平面图，突出女性轮廓几何结构，标注树干位置、指根网关位置、
主根走向、水面交界线。
[等轴测3D图] 根系结构展示，互绕的根系拓扑结构、深度变化、表面纹理
（网关区域光滑木质，老根呈粗糙风化树皮）。
[特写细节] 指根（直径10厘米，长度约10厘米）截面图与表面纹理，
显示内部木质纤维色调（#6B4423红褐色），光滑的外表面，
与主根的连接处，带测量标线的尺度参考。
包含色彩样本条：#4A6741（苔绿）、#2C1810（深褐树皮）、#6B4423（木质内部）、
#5B3A6B（能量紫），附材质标注。
参考稿附电影级光线，技术绘图美学。
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, dramatic low-key lighting, moment of catastrophe.
Ancient banyan tree undergoing violent trembling, extreme motion blur on foliage and root system.
Tree trunk violently swaying with amplitude ~40cm, multiple branches visibly cracking and breaking,
cascading debris falling like rain. Root system contorted—main roots twisted, lifted off ground,
fingerlike gateway root completely severed, showing rough wooden break surface (#6B4423).
All supernatural purple luminescence extinguished completely—no glow, no aura, darkness returns.
Energy channels shattered, root network paralyzed in chaotic sprawl.
Entire mountain valley echoing with violence—soil displaced, wildflowers crushed,
stream water turbulent, mist and dust cloud engulfing lower roots.
Female silhouette completely distorted, broken, no longer graceful—roots contorted in anguish.
Atmosphere: apocalyptic, catastrophic loss, death of gateway.
Cinematic devastation, high dynamic range, professional disaster cinematography.
```

**中文：**
```
电影级截图，2.39:1超宽银幕，戏剧性低调光线，灾难时刻。
古榕树体剧烈振颤，叶片与根系呈现极端动感模糊。树干大幅摇晃
（振幅约40厘米），多条枝条可见折断，碎屑如雨坠落。根系扭曲—
主根折绞、离地隆起，指根完全断裂，露出粗糙的木质断面（#6B4423）。
所有超自然紫光彻底熄灭—无发光、无光晕、黑暗笼罩。
能量通道粉碎，根系网络陷入混乱瘫痪状。整个山谷回荡着暴力声响—
土壤翻飞、野花碾碎、溪水湍急、雾气与尘埃包裹下半部根系。
女性轮廓完全扭曲破碎，不再优雅—根须呈现痛苦姿态。
氛围：末世感、灾难性丧失、通道之死。电影级摧毁场景，高动态范围，
专业灾难摄影风格。
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, melancholic late afternoon light, autumn mood.
Ancient banyan tree in aftermath of severance, completely motionless and devastated.
Trunk standing but lifeless, branches drooping heavily downward, foliage darkened
from lush moss-green (#4A6741) to muted olive-brown, leaves visibly withering.
Root system permanently contorted—female silhouette completely distorted and broken,
no restoration possible. Fingerlike gateway root torn away, only raw wood stub remains.
Major roots twisted, coiled, unnatural angles, lifeless sprawl. All purple luminescence
completely vanished, no supernatural aura—stark return to ordinary botanical form.
Surrounding environment showing early decay—wildflowers drooping, grass browning,
stream water losing clarity. Entire landscape atmosphere: desolation, abandonment,
severed connection to otherworld, permanent loss. Moss and lichen color fading to grays.
Cinematic despair, professional nature photography in post-apocalyptic tone.
```

**中文：**
```
电影级截图，2.39:1超宽银幕，忧伤的午后光线，深秋氛围。
古榕在断根事件后，完全静止与荒凉。树干挺立但无生命感，枝条沉重下垂，
叶片从郁葱的苔绿色（#4A6741）褪变为沉闷的橄榄褐，叶片可见凋零。
根系永久扭曲—女性轮廓完全歪斜破碎，无法恢复。指根被撕断，仅余粗糙的木质断裁。
主根折绞、蜷缩、呈现不自然的角度、无生命的散铺。所有紫色超自然光晕彻底消失，
无任何灵气光环—赤裸回到普通植物形态。周边环境展现早期衰败—野花垂头、
草地褐化、溪水失清。整个地景氛围：荒凉、遗弃、与灵界的连接永久断开、不可逆的丧失。
苔藓与地衣褪色成灰。电影级绝望感，后启示录氛围的专业自然摄影。
```

#### 6. 

**English：**
```
Production design before/after comparison reference, split-screen technical illustration.
Left side [Before - Intact]: Ancient banyan root system in full supernatural glory,
massive trunk, lush canopy, root network arranged as elegant female silhouette,
fingerlike gateway root intact and glowing with dark purple aura, energy flowing.
Annotation notes: "Functional portal, complete silhouette, active supernatural energy,
tree height stable 25-30m, root network extending 200m underground."
Right side [After - Severed]: Same tree devastated by severance, trunk darkened and drooping,
root system contorted and broken, female form distorted beyond recognition,
gateway root torn away with raw wooden stub, all luminescence extinguished,
landscape withering around tree. Annotation notes: "Portal permanently closed,
silhouette destroyed, energy channels shattered, tree in perpetual decline,
connection to underworld severed irrevocably."
Include side-by-side detail insets: [Gateway root intact vs. broken], [Root geometry
intact vs. contorted], [Light state: active vs. extinct]. Color palette shifts from
vibrant (#4A6741 moss-green, #5B3A6B purple) to muted (#8B7355 dull brown, no purple).
Technical production reference, clean drafting aesthetic.
```

**中文：**
```
制作设计对比参考稿，分割屏技术插画。
左侧【之前-完好状态】：古榕根系处于完全超自然荣光状态，巨大树干、郁葱冠幅、
根系排列成优雅女性轮廓、指根完好闪烁暗紫光晕、能量流动。标注说明：
"功能性传送门，轮廓完整，超自然能量活跃，树高稳定25-30米，根系向下延伸200米"。
右侧【之后-断根状态】：同一棵树遭断裂破坏，树干暗沉下垂，根系扭曲破碎，
女性轮廓变得无法辨认，指根被撕断仅余粗糙木质，所有光晕完全熄灭，
周边景观随之衰败。标注说明："传送门永久关闭，轮廓彻底摧毁，能量通道粉碎，
树陷入永久衰落，与阴间的连接永远断开"。包含并排细节插图：
【指根完好vs.破断】、【根系几何完好vs.扭曲】、【光照状态：激活vs.熄灭】。
色彩调板从饱和色（#4A6741苔绿、#5B3A6B紫）转变为沉闷色（#8B7355暗褐、无紫）。
技术制作参考稿，清爽绘图美学。
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen, moonlit night scene, mystical color grading.
Ancient banyan tree illuminated by soft moonlight from above, casting long shadows across root landscape.
Fingerlike gateway root in extreme supernatural prominence—glowing intensely with dark purple
luminescence (#5B3A6B), appearing almost like an ethereal torch in the darkness.
Purple energy pulses rhythmically, creating luminous pathways along major root network.
Moon reflection on stream water mingles with purple glow, creating violet shimmer patterns.
Tree silhouette stark and monumental against night sky, gnarled roots casting intricate shadow
network on ground. Wildflowers visible in dim moonlight, creating ethereal meadow atmosphere.
Spiritual energy highly visible in darkness—every pulse of purple light accentuates the
tree's role as cosmic gateway. Whispers of wind through leaves. Cinematic night cinematography,
supernatural mysticism, high contrast, professional fantasy VFX.
```

**中文：**
```
电影级截图，2.39:1超宽银幕，月夜场景，神秘色彩分级。
古榕被柔和月光从上照亮，根系地景投出长影。指根在超自然光效中极为突出—
闪烁强烈的暗紫色光晕（#5B3A6B），在黑暗中仿佛灵火般发光。
紫色能量有节奏地脉动，沿主根网络形成发光通路。月光在溪水上的倒影与紫光交融，
创造紫色闪烁纹理。树体剪影在夜空衬托下显得宏伟有力，纹理根须在地面投出
复杂影网。野花在月光中隐约可见，营造超越尘世的草地氛围。灵性能量在黑暗中
极为可见—紫光每次脉动都强调树作为宇宙通道的角色。风吹过叶片的细微声响。
电影级夜景摄影，超自然神秘主义，高对比度，专业幻想VFX。
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen, supernatural intensity, chaotic ethereal moment.
Ancient banyan root system overwhelmed by multiple spirit passages simultaneously.
Fingerlike gateway root blazing with intense dark purple luminescence (#5B3A6B) at near-maximum
brightness, creating a beacon-like column of light. Multiple ethereal spirit silhouettes
in various compression stages—some entering, some ascending through roots, some emerging—
creating a traffic of souls. Root system vibrating intensely (frequency 6-8Hz, amplitude 20-25cm),
responding to multiple souls. Energy pulses cascading rapidly, appearing as flowing violet torrents
through root channels. Tree trunk swaying visibly, branches turbulent. Entire root network
radiating supernatural vitality. Ground around tree distorted by energy flux, wildflowers
shimmering with secondary violet glow. Stream water turbulent with reflected purple light.
Atmosphere: cosmic traffic hub, interdimensional throughway at capacity, sacred urgency.
Professional VFX cinematography, high supernatural intensity, no oversaturation.
```

**中文：**
```
电影级截图，2.39:1超宽银幕，超自然强度，混乱的灵界时刻。
古榕根系同时被多个灵体穿行所压倒。指根以接近最大亮度闪耀着强烈的暗紫色光晕
（#5B3A6B），形成灯塔般的光柱。多个灵体轮廓处于不同压缩阶段—部分进入、部分在根系中
上升、部分正在浮现—形成灵魂交通。根系强烈振颤（频率6-8赫兹，振幅20-25厘米），
响应多个灵体。能量脉冲快速连贯，呈现为紫色激流流经根系通道。树干明显摇晃，
枝条湍急。整个根系网络放射超自然生命力。树周地面因能量通量而扭曲，野花闪烁
次生紫光。溪水因反射的紫光而湍急。氛围：宇宙交通枢纽、次元走廊满负荷运作、神圣的紧迫感。
专业VFX电影风格，超自然强度高，无过度饱和。
```

#### 9. 

**English：**
```
Cinematic still, 2.39:1 widescreen, spring season color grading, renewal atmosphere.
Ancient banyan tree in spring, fresh new foliage emerging in bright moss-green (#4A6741),
tender leaves catching afternoon sunlight. Root system exposed across earth mound, roots
freshly washed by spring rains, displaying natural wood colors more vividly—warm saddle-brown
bark (#6B4423), intricate root geometry clearly visible. Gateway finger root glowing softly
with dark purple luminescence, energy pulsing gently. Spring wildflowers blooming around tree
base in yellows, whites, purples—natural meadow vitality. Stream water abundant and clear,
reflecting sky and tree above, minor ripples from root contact. Moss and lichen on roots
displaying bright green vitality. Entire scene radiates life, renewal, natural abundance,
spiritual awakening. Cinematic spring cinematography, soft warm lighting, vibrant but harmonious
color palette, professional nature photography.
```

**中文：**
```
电影级截图，2.39:1超宽银幕，春季色彩分级，更新活力氛围。
古榕在春季，新叶以鲜亮的苔绿色（#4A6741）萌发，嫩叶捕捉午后阳光。
根系裸露于隆起土堤，刚被春雨冲洗的根须展现出更生动的天然木质色彩—
温暖的鞍褐树皮（#6B4423），复杂的根系几何清晰可见。网关指根柔和地闪烁着暗紫色光晕，
能量温和脉动。春季野花在树底绽放，黄、白、紫色—天然草地的生机。
溪水丰沛且清澈，映照天空与树木，根系接触处产生轻微涟漪。根系上的苔藓与地衣
显出鲜绿生命力。整个场景散发生命、更新、自然丰盈、灵性觉醒。电影级春季摄影，
柔和温暖光线，饱和但和谐的色彩调板，专业自然摄影。
```

#### 10. 

**English：**
```
Cinematic still, 2.39:1 widescreen, autumn season color grading, melancholic poetic mood.
Ancient banyan tree in full autumn, foliage shifted from moss-green to warm yellow-green,
golden highlights catching late afternoon sunlight creating rich warm tones. Root system
showing aged character—bark deeply weathered in dark saddle-brown (#2C1810), exposed wood
displaying rust-red tones (#8B4513) from oxidation. Gateway finger root glowing intensely
with dark purple luminescence (#5B3A6B), creating striking color contrast against warm autumn
palette. Root network arranged as elegant female silhouette more prominent in season's light.
Autumn wildflowers fading—remaining blooms in deep purples and oranges. Stream water clearer
in autumn light, minimal debris. Fallen leaves scattered across root landscape, creating
natural pattern. Cinematic autumn cinematography, golden hour lighting, warm-cool color contrast,
melancholic but beautiful supernatural mood. Professional nature cinematography with poetic sensibility.
```

**中文：**
```
电影级截图，2.39:1超宽银幕，秋季色彩分级，忧伤诗意氛围。
古榕在金秋，叶片从苔绿转变为温暖的黄绿色，金色亮点捕捉午后阳光
创造丰富温暖色调。根系显现陈年感—树皮深度风化呈暗鞍褐色（#2C1810），
裸露木质因氧化显现锈红色调（#8B4513）。网关指根强烈闪烁着暗紫色光晕（#5B3A6B），
在温暖秋季调板中形成夺目的色彩对比。根系排列成的优雅女性轮廓在季节光线下更突出。
秋季野花凋零—残留花朵呈深紫与橙色。溪水在秋光下更清澈，落叶甚少。
枯叶散落在根系地景上，形成天然图案。电影级秋季摄影，黄金时刻光线，
温暖与冷调色彩对比，忧伤却优美的超自然氛围。具有诗意敏感度的专业自然摄影。
```

### 上神界 (locations, ★★★★, P4)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, celestial temple interior of supreme deity,
towering sacred columns extending infinitely into divine depths,
dark gold atmosphere #DAA520 with warm off-white light #FFF8DC,
no shadows or soft ethereal glows, geometric perfectly-spaced pillars,
vast incomprehensible space defying mortal perspective,
metallic floor with intricate sacred patterns emitting golden radiance,
transcendent and supremely sacred atmosphere, no white elements,
impossible architecture, otherworldly supernatural aesthetics,
professional cinematic production quality
```

**中文：**
```
电影截帧，2.39:1 宽屏幅，至高存在的天界神殿内部，
耸立的圣光柱廊无限延伸至神圣深处，
暗金色氛围 #DAA520 伴以暖白色光线 #FFF8DC，
无阴影或柔和光晕，几何排列完美的柱体，
违反凡间透视的广阔不可理解的空间，
金属地面刻有神圣纹理散发金色光芒，
超越凡俗与至高神圣的气质，禁用纯白色，
不可思议的建筑结构，超自然美学，
专业电影制作质感
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, supreme celestial being in dialogue with mortal,
divine presence manifesting in temples of sacred architecture,
dark gold #DAA520 and warm white #FFF8DC intertwining in divine light,
geometric patterns on ground floor creating fractal sacred geometry,
pillars emitting sacred white radiance witnessing the encounter,
overwhelming spiritual pressure and cosmic hierarchy visualization,
transcendent color palette, ethereal yet oppressive atmosphere,
impossible spatial perspective conveying supernatural dimensions,
no pure white elements, cinematic masterpiece quality
```

**中文：**
```
电影截帧，2.39:1 宽屏幅，至高存在与凡人进行神圣对话，
神圣显现于殿堂的神圣建筑空间内，
暗金色 #DAA520 与暖白 #FFF8DC 的神圣光线交织，
地面几何纹理形成分形的神圣几何图案，
柱廊散发暖白光芒见证这次对话，
精神压力与宇宙等级制度的极致可视化，
超越凡俗的色彩调板，既空灵又压抑的氛围，
展现超自然多维度的不可思议空间透视，
禁用纯白色，电影级艺术大作质感
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, climactic moment in celestial temple,
reality bending and dimensions collapsing around decisive point,
transitional light from dark gold #DAA520 to transcendent brilliance or void,
sacred pillars fading or multiplying infinitely in response to cosmic decision,
figure silhouetted against overwhelming divine light or consuming darkness,
existential transformation and destiny crystallization visualization,
surreal geometry warping and reconstructing space itself,
no white elements, supernatural horror-sublime aesthetics,
professional cinematic production of cosmic transcendence
```

**中文：**
```
电影截帧，2.39:1 宽屏幅，天界殿堂的命运抉择关键时刻，
现实扭曲与维度在决策点周围坍塌，
光线从暗金 #DAA520 转化为超越的光芒或吞没的虚空，
圣光柱廊消退或无限增殖以应对宇宙决定，
身影映衬在压倒性的神圣光芒或吞没的黑暗前，
存在论的变革与命运结晶化的可视化，
超现实几何扭曲与重构空间本身，
禁用白色，超自然的恐怖-至美美学，
专业电影级宇宙超越制作质感
```

### 凤廊山脉 (locations, ★★★★, P4)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, expansive mountain range at dawn,
layered fog drifting through valleys, peak silhouettes against twilight blue sky,
moss-covered dark green vegetation, exposed rocky outcrops in burnt sienna brown,
no white snow visible, moody atmospheric lighting, cold color grading,
distant unknown creatures implied by environmental details,
sense of vast untamed wilderness, isolation and mystery,
8K ultra detailed landscape photography, cinematic composition
```

**中文：**
```
电影截图，2.39:1超宽屏，晨曦时分辽阔山脉全景，
分层雾霭在谷地中漂浮流动，山峰剪影映衬暮蓝天空，
苔绿色厚重植被覆盖，焦褐色裸露岩壁与碎石坡，
无积雪，冷色调光线投射，压抑沉静的光影，
环境细节暗示古老生灵存在，
广袤荒凉之地，隔绝与神秘交织，
8K超细节风景摄影级质感，电影级构图
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, narrow mountain path clinging to cliff edge,
outer side drops off into abyss, inner side sheer vertical rock wall,
frozen pathway, thin layer of ice and snow partially obscuring ground,
moss-green and burnt brown color palette dominating,
sharp angular rock formations with threatening edges,
misty atmosphere obscures distance, creating claustrophobic tension,
first-person or low angle perspective emphasizing precariousness,
extreme danger and isolation, no safety, cinematic horror-suspense tone
```

**中文：**
```
电影截图，2.39:1超宽屏，山腰狭窄山路，外侧悬崖深坠，
内侧山壁垂直陡峭，裸露岩石，
路面冻结，冰雪薄层与碎石，
苔绿与焦褐色调压倒性主导，尖锐棱角的岩石威胁，
雾霭浓厚遮挡远景，制造幽闭紧张感，
第一人称或低角度视角强化危险感，
极端危险与孤立无援，无任何保护，电影惊悚氛围
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, deep mountain valley or cave hidden deep in range,
two vertical cliff walls looming, shadows and darkness dominate,
scattered massive boulders creating labyrinthine passages,
thick moss covering every surface in moss-green, dampness visible,
gnarled ancient trees with exposed twisted roots, skeletal and haunting,
subtle evidence of large creature inhabitation: scratches, fur, tracks,
twilight blue shadows mixed with darkness, cinematic mystery and dread,
sense of being watched, primal and forbidden sacred space
```

**中文：**
```
电影截图，2.39:1超宽屏，山脉最深处隐蔽山谷或洞穴，
两侧山壁近乎垂直逼仄，影子与暗沉主导，
散落巨石形成迷宫般通道，
厚重苔藓覆盖苔绿色，湿润感明显，
古老扭曲树木，根系裸露，骸骨般诡异，
大型生灵驻居迹象：爪痕、毛发、足迹、啃食痕迹，
暮蓝阴影混合漆黑，电影级神秘与恐惧感，
被凝视感，原始禁忌之地
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, mountain range at deep night in extreme winter,
thick snow blanketing landscape, frozen world, temperature dropping visual cues,
moonlight blocked by heavy clouds, near total darkness with subtle twilight blue,
exposed rock formations jutting through snow in burnt brown tones,
frozen waterfall, ice formations sharp as blades,
survival horror atmosphere, isolation at extremity, cosmic insignificance,
claustrophobic cold, danger from elements and unseen threats,
no white pure color—all tinted in cool blues and earth browns, ultra cinematic
```

**中文：**
```
电影截图，2.39:1超宽屏，深冬极夜山脉，
厚重积雪覆盖，冻结世界，极低温视觉暗示，
月光被厚云遮挡，近乎漆黑仅存微弱暮蓝，
焦褐色岩壁刺穿积雪，
冰冻瀑布、刀片状冰晶，
生存恐怖氛围，极致孤立无援，宇宙级渺小感，
冷冻幽闭感，元素与未知威胁，
无纯白色，全部冷蓝与大地褐色色调，电影级呈现
```

### 十八层塔 (locations, ★★★★, P4)

#### 1. 提示词1：十八层塔全景 [十八层塔全景]

**English：**
```
Cinematic still, 2.39:1 widescreen, a translucent spirit ascending through a towering pagoda of stacked platforms within the underworld. The pagoda interior features 18 levels with shrinking circular platforms in blue-purple tones. Lower levels glow with dusk blue (#3A4A6B) and dark purple (#5B3A6B), while upper levels transition toward warm amber light, creating a gradient from despair to hope. The spirit emits a faint self-luminous aura reflecting its incompleteness. Stone surfaces show cracks and decay in lower tiers, with organic crystal structures visible in upper levels. Layered shadows and light refraction create depth. The atmosphere is oppressive yet transcendent, with volumetric lighting rays piercing through the darkness above. High contrast between warm and cool tones. Intricate architectural geometry. Ultra-detailed, cinematic lighting, moody atmosphere, supernatural horror mixed with redemptive hope. Rendered in a style reminiscent of contemporary dark fantasy illustration.
```

**中文：**
```
电影截帧，2.39:1宽银幕，一个半透明的灵魂在阴间内部的高塔中攀爬，塔身由18层递减的圆形平台堆叠而成。下层平台笼罩在暮蓝色（#3A4A6B）与暗紫色（#5B3A6B）的光线中，上层平台逐渐过渡为温暖的琥珀色光芒，形成从绝望到希望的色彩梯度。灵魂发出微弱的自发光晕，反映其"魄"的不完整状态。石质表面在下层显示裂纹与衰败迹象，在上层出现有机的晶体结构。分层阴影与光线折射营造空间深度感。大气压抑而超越，容积式光线从上方黑暗中穿透而下。冷暖色调形成高对比。复杂的建筑几何结构。超细致、电影级光影、压抑诡异的氛围，混合救赎的希望感。渲染风格参考当代暗黑奇幻插画。
```

#### 2. 提示词1：十八层塔全景 [十八层塔全景]

**English：**
```
Cinematic still, 2.39:1 widescreen, extreme close-up of a spirit's anguished face inside a cavernous pagoda base. The lowest levels are shrouded in dusk blue and chocolate brown tones. Scattered stones and dripping dark purple liquid create a sense of decay. The spirit's self-luminous aura barely illuminates the surrounding stone surface, revealing fractures and corrosion. A faint spiral staircase ascends into absolute darkness above. The atmosphere is suffocating, with soft moans echoing in the void. High humidity, oppressive humidity, despair materialized. Ultra-detailed, hyper-realistic, cinematic horror, volumetric fog.
```

**中文：**
```
电影截帧，2.39:1宽银幕，灵魂扭曲的脸部特写，位于塔底内部洞穴中。最低层笼罩在暮蓝与焦褐色中。散落的石块与渗漏的暗紫色液体表现衰败感。灵魂微弱的自发光晕仅能照亮周围石面的裂纹与腐蚀。螺旋阶梯模糊地向上延伸至绝对黑暗。干呕声、哭泣声在虚空中回响。压抑的湿度、绝望物质化。超细致、超现实、电影级恐怖感、体积雾气。
```

#### 3. 提示词1：十八层塔全景 [十八层塔全景]

**English：**
```
Cinematic still, 2.39:1 widescreen, a circular platform within the pagoda where multiple translucent spirits gather, their self-luminous auras creating a constellation of soft dusk-blue and dark purple lights. The spirits are positioned around the platform, their forms barely visible but their glowing halos creating a sense of connection and shared resonance. The platform is stable and expansive, with subtle glowing runes etched into the stone surface. A low, harmonious humming sound fills the space. The atmosphere shifts from oppression to a fragile sense of hope and kinship. Volumetric lighting, ethereal glow, dark fantasy, intricate details.
```

**中文：**
```
电影截帧，2.39:1宽银幕，塔内的圆形平台上，多个半透明的灵魂聚集，它们的自发光晕形成由暮蓝与暗紫色组成的星座。灵魂形体模糊，但发光晕形成一种连接与共鸣的感受。平台稳定宽敞，石面刻有细微的发光符号。低沉和谐的嗡鸣音充满空间。氛围从压抑转为脆弱的希望与同伴感。体积光效、幽灵般的辉光、暗黑奇幻、细节繁复。
```

#### 4. 提示词1：十八层塔全景 [十八层塔全景]

**English：**
```
Cinematic still, 2.39:1 widescreen, the pinnacle of the pagoda—a perfectly geometric, minimal platform composed of translucent purple crystal glowing from within. A single spirit stands on this precarious platform, illuminated by brilliant warm light descending from above, creating a stark contrast against the dark void below where the entire pagoda structure is visible as layers of diminishing circles. The spirit's form is almost silhouetted against the overwhelming light source. Pure, crystalline, transcendent atmosphere. Spiritual redemption, threshold of transformation, awe-inspiring scale. Ultra-detailed, cinematic masterpiece, ethereal horror-beauty.
```

**中文：**
```
电影截帧，2.39:1宽银幕，塔的顶端——一个由半透明紫色晶体组成的最小化、完美几何的平台，内部自发光。单个灵魂站在危险的平台上，被从上方投射的炽烈温暖光线照亮，与下方黑暗虚空形成极端对比，下方能看到整个塔的结构，层层递减的圆形。灵魂的形体几乎被压倒性的光源淹没成剪影。纯净、晶莹、超越感的氛围。灵魂救赎、转变的临界点、令人敬畏的宏大感。超细致、电影级杰作、幽灵般的恐怖之美。
```

#### 5. 提示词1：十八层塔全景 [十八层塔全景]

**English：**
```
Cinematic still, 2.39:1 widescreen, a spirit at the edge of a precarious platform, the narrowest tier of the lower pagoda. The platform is surrounded by a faint purple energy barrier marking the boundary between existence and void. The spirit looks down at the layers below, shrouded in darkness, then up at the impenetrable blackness above. Its self-luminous aura is weak, struggling against the overwhelming darkness. The atmosphere is one of absolute despair, the final moment before surrendering or pushing forward. Dusk blue and dark purple dominate. Volumetric shadow, claustrophobic infinite space, existential dread.
```

**中文：**
```
电影截帧，2.39:1宽银幕，灵魂站在下塔区最狭窄的平台边缘，周围是标记存在与虚空边界的微弱紫色能量墙。灵魂向下看，黑暗中的层级；向上看，无法穿透的黑暗。其自发光晕微弱，在压倒性黑暗中挣扎。绝对绝望的氛围，放弃与坚持的最后时刻。暮蓝与暗紫主导。体积阴影、幽闭的无限空间、存在性恐惧。
```

#### 6. 提示词1：十八层塔全景 [十八层塔全景]

**English：**
```
Cinematic still, 2.39:1 widescreen, a spirit on the pinnacle platform, bathed in transcendent warm-golden light that seems to come from another dimension. The spirit's form is becoming translucent, almost merging with the light itself. Below, the entire pagoda is visible, layers upon layers in deep indigo and midnight blue, now appearing small and distant. The spirit extends its hand toward the light source above, or turns to look back at the platform where another guardian spirit waits. The moment of choice: ascension or eternal service. Redemptive light, transformative hope, bittersweet eternity.
```

**中文：**
```
电影截帧，2.39:1宽银幕，灵魂站在塔顶平台，沐浴在超越的温暖金色光线中，光线仿佛来自另一个维度。灵魂形体逐渐透明，几乎与光线融合。下方，整个塔清晰可见，层层叠叠的靛蓝与午夜蓝，现在显得渺小而遥远。灵魂向上方光源伸出手，或转身看向平台上等待的守护灵魂。选择的时刻：上升还是永恒服役。救赎的光、转变的希望、甘苦参半的永恒。
```

### 大蒜 (props, ★★★★, P4)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, professional color grading, dramatic lighting. Close-up of fresh garlic bulb with papery white skin and brown dried layers, natural organic texture, studio lighting with subtle shadows emphasizing the natural ridges and organic form. Shallow depth of field, warm natural light. Hyper-realistic botanical illustration style.
```

**中文：**
```
电影质感剧照，2.39:1 宽幅画面，专业调色，戏剧化光影。新鲜大蒜球茎特写，纸质白色外皮与褐色干皮层清晰可见，天然有机粗糙质感，工作室照明突出自然褶皱与有机形态的细节阴影。浅景深，温暖自然光线。超写实植物插画风格。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, dramatic horror lighting, sickly atmosphere. A figure experiencing supernatural soul-body separation, nauseated greenish-purple (#6B4F6B) mist seeping from skin pores across the entire body. The surrounding 1-meter area shifts toward a sickly green color temperature. Medium-intensity supernatural rejection effect. The figure's body language conveys extreme distress and disorientation. Film noir lighting with color-graded sickly pallor. Professional cinematic composition.
```

**中文：**
```
电影质感剧照，2.39:1 宽幅画面，戏剧化恐怖光影，病态氛围。一个身影经历灵魂与肉体分离的超自然反应，病态绿紫色（#6B4F6B）雾气从全身皮肤毛孔中渗出。周围1米范围内色温向病态绿色转变。中等强度的超自然排斥反应视觉效果。身体语言表达极度痛苦与混乱。黑色电影风格光影与病态色调调色。专业电影构图。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, military aesthetic, warm practical lighting. Garlic integrated into military rations - fresh bulbs arranged with dried provisions, canvas bags, field equipment. Natural lighting emphasizing the stark contrast between the organic garlic and utilitarian military supplies. Gritty, authentic wartime aesthetic without romanticization.
```

**中文：**
```
电影质感剧照，2.39:1 宽幅画面，军事美学，温暖实用光线。大蒜融入军用配给——新鲜蒜球与干粮、帆布袋、野战装备并排。自然光线突出有机大蒜与实用军事物资的强烈对比。粗粝、真实的战时美学，无浪漫化处理。
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, supernatural warfare aesthetic, ominous lighting. The invisible spiritual suppression field created by garlic distribution and black cloth formation working in conjunction - represented through atmospheric color shifts, subtle greenish haze suggesting the suppression field. Soldiers positioned strategically, garlic visible in their rations. Supernatural tension without overt magical effects.
```

**中文：**
```
电影质感剧照，2.39:1 宽幅画面，超自然战争美学，不祥光线。大蒜分布与黑布阵结合创造的无形灵性压制场——通过大气色温变化、淡绿色薄雾表现压制场的存在。士兵战术位置布置，配给中的大蒜清晰可见。超自然紧张感，无明显魔法效果。
```

### 水晶棒 (props, ★★★★, P4)

#### 1. 提示词1：概念设计稿 - 棒身正视图 [概念设计稿]

**English：**
```
Cinematic still, 2.39:1 widescreen, professional fantasy art.
Crystal rod, approximately 25 centimeters long, transparent crystalline material,
ancient lamp-like fixture with glass-like transparent sides. Luminous warm-white
glow (#FFF8DC) radiating from interior against dark gold (#DAA520) background.
Self-luminescent without external light source. Mystical divine energy, heavenly
artifact aesthetic. Smooth polished surface, high refraction, multi-layered internal
light rays. Subtle glow pulsation. Isolated on neutral background. Ultra-detailed,
8k cinematic rendering.
```

**中文：**
```
电影级画面，2.39:1宽荧幕比例，专业奇幻艺术风格。
水晶棒，约25厘米长，全透明水晶材质，四周如古时灯具般的透明玻璃设计。内部发出暖白色
(#FFF8DC) 柔和光晕，衬托在深暗金色 (#DAA520) 背景中。自发光特性，无需外部光源。
神秘的天界元神能量，超自然圣物美学。表面光滑无瑕，高折射率，内部多层次光线流动。
细微脉动式闪烁。中性背景隔离显示。超精细细节，8k级电影级渲染。
```

#### 2. 提示词2：场景设定稿 - 山洞中的水晶棒 [场景设定稿]

**English：**
```
Cinematic still, 2.39:1 widescreen, professional fantasy art.
Crystal rod lying on ancient stone pedestal deep within dark mountain cave near
Shaolin temple. Rod glows with warm-white (#FFF8DC) and dark gold (#DAA520)
luminescence, being the sole light source in pitch-black surroundings. Transparent
crystalline structure visible through glow. Cave walls of rough dark stone create
dramatic contrast with the artifact's supernatural radiance. Mystical, sacred
atmosphere. Divine heavenly energy emanating. Detailed cave texture, atmospheric
lighting from rod only. 8k cinematic rendering, ultra-detailed, dramatic shadows.
```

**中文：**
```
电影级画面，2.39:1宽荧幕比例，专业奇幻艺术风格。
水晶棒放置在少林寺附近深山洞穴内的古老石制祭坛上。棒身发出暖白色 (#FFF8DC) 与深暗金色
(#DAA520) 的复合光晕，是黑暗环境中唯一的自然光源。透明水晶结构在光晕中清晰可见。
周围粗糙黝黑的山洞石壁与圣物的超自然光辉形成戏剧性对比。神秘、神圣的氛围笼罩。
天界元神能量溢出。详细山洞质感，仅由棒身提供光照。8k级电影级渲染，超精细细节，
戏剧性阴影。
```

#### 3. 提示词3：激活状态稿 - 元神转移光束 [激活状态稿]

**English：**
```
Cinematic still, 2.39:1 widescreen, professional fantasy art.
Crystal rod emitting intense bright beam of divine light during soul transfer activation.
Beam color: warm-white (#F5F5DC) + dark gold (#DAA520), extremely high intensity,
focused and powerful, shooting straight from rod into digital human figure's head.
Rod interior glowing at maximum brightness, pure-white (#F5F5DC) with golden undertones,
pulsing with celestial energy. Light beam illuminates surrounding area dramatically.
Mystical aura, supernatural phenomenon. Crystal structure radiating intense holy light.
8k cinematic rendering, ultra-detailed, dramatic god-ray lighting effects, ethereal
energy visualization.
```

**中文：**
```
电影级画面，2.39:1宽荧幕比例，专业奇幻艺术风格。
水晶棒在元神转移启动时发射强烈的神圣光束。光束颜色：暖白色 (#F5F5DC) + 深暗金色
(#DAA520)，极高强度，聚焦而有力，笔直射向数字人物头部。棒身内部光芒达到最大亮度，
纯白色 (#F5F5DC) 并带微金色调，脉动着天界能量。光束戏剧性照亮周围环境。
神秘的超自然现象。水晶结构辐射出强烈圣光。8k级电影级渲染，超精细细节，
戏剧性圣光射线效果，以太能量可视化。
```

#### 4. 提示词4：数据显示细节 - 元神计数与倒计时面板 [数据显示细节]

**English：**
```
Cinematic still, 2.39:1 widescreen, professional fantasy art.
Close-up detail of crystal rod's display panel showing mystical numerical readouts.
Upper panel: "Souls Stored: 13/18" in glowing ethereal font. Lower panel:
"Divine Recall Countdown: 247 years, 154 days remaining" in similar luminous text.
Numbers rendered in warm-white (#FFF8DC) and subtle gold accents. Display surfaces
embedded within transparent crystal, glowing from within. Holographic-like mystical
interface. Ancient civilization aesthetic meets supernatural technology. Ultra-detailed,
8k cinematic rendering, mystical glow, divine energy emanating.
```

**中文：**
```
电影级画面，2.39:1宽荧幕比例，专业奇幻艺术风格。
水晶棒显示面板的近距离细节特写，展示神秘数字读数。上部面板："已装载元神：13/18"，
用闪烁的以太字体显示。下部面板："神灵召回倒计时：247年154天"，类似的发光文字。
数字以暖白色 (#FFF8DC) 和微妙金色调渲染。显示面板嵌入透明晶体内部，内部发光。
全息般的神秘界面。古文明美学与超自然科技的融合。超精细细节，8k级电影级渲染，
神秘光晕，天界能量溢出。
```

#### 5. 提示词5：收藏摆件稿 - 完整形态展示 [收藏摆件稿]

**English：**
```
Cinematic still, 2.39:1 widescreen, professional fantasy product photography.
Crystal rod displayed on fine art pedestal, rotated to show all angles of the artifact.
Transparent crystalline form approximately 25 centimeters in length, glowing with
warm-white (#FFF8DC) and dark gold (#DAA520) internal luminescence. Multi-layered
light refraction visible throughout crystal structure. Ancient lamp-like design with
transparent glass-like sides. Mystical divine object, heavenly artifact. Studio lighting
with dramatic shadows emphasizing three-dimensional crystal geometry. Museum-quality
presentation, ultra-detailed, 8k rendering, supernatural aesthetic, ethereal glow.
```

**中文：**
```
电影级画面，2.39:1宽荧幕比例，专业艺术品摄影风格。
水晶棒放置在精致艺术展示台上，多角度展示圣物全貌。透明水晶形态约25厘米长，
内部发出暖白色 (#FFF8DC) 与深暗金色 (#DAA520) 的复合光晕。多层次光线折射贯穿整个
晶体结构。古朴灯具造型，四周透明玻璃质感。神秘的神灵圣物，天界秘宝。
工作室光线搭配戏剧性阴影，强调晶体的三维几何之美。博物馆级呈现，超精细细节，
8k级渲染，超自然美学，以太光晕。
```

### 永安镇 (locations, ★★★★, P4)

#### 1. 

**English：**
```
A bustling coastal town in midday sunlight. The central market square overflows with wooden stalls and vendors selling fresh fish, vegetables, and textiles. Buildings in warm mustard-brown #8B7355 line the unpaved streets with traditional roofing. People move through the scene in various directions—fishermen, merchants, locals—creating a sense of everyday vitality. Fishing boats are moored along the dock to the south, with nets spread on stone platforms. An inn stands to the east with smoke rising from its chimney. The light is clear and warm, casting sharp shadows beneath market awnings. No pure white—earth-tones and golden-brown dominate. The atmosphere is lively, crowded, and safe.
```

**中文：**
```
一个沿海小镇的正午阳光下。镇中心的市集广场被木板摊位密布，卖鱼的、菜贩、布匹商在此聚集。建筑物呈温暖的枯草黄#8B7355，沿着泥土街道排列，传统的瓦顶或茅顶。人影往来穿梭——渔民、商人、镇民——带来日常生活的活力与热闹。南侧码头渔船停靠，渔网铺散在石墩上。东侧客栈烟囱冒起炊烟。光线清晰温暖，在市集棚布下投出锐利的阴影。禁用纯白——土黄色和枯草黄主导整个画面。整体氛围热闹拥挤而安全。
```

#### 2. 

**English：**
```
Evening descends on a peaceful coastal town. Long shadows of market stalls stretch across the plaza. Buildings silhouetted against a sky transitioning from orange to deep blue. Oil lamps and candles are lit in homes and the inn, casting warm yellow glows through windows. A few figures move slowly—merchants closing stalls, families heading home. The sea is calm and still, reflecting the fading daylight. The atmosphere shifts from daytime chaos to evening calm, tinged with contentment and the peace of normalcy.
```

**中文：**
```
傍晚降临一个宁静的沿海小镇。市集摊位投出长长的阴影。建筑物在从橙色渐变为深蓝的天空映衬下呈现剪影。油灯和蜡烛在家宅和客栈中点亮，透过窗户投出温暖的黄色光晕。一些人影缓慢移动——商人收摊、家族返家。海面平静，反射着暮光。氛围从白日的混乱转为傍晚的宁静，带有满足感和日常生活的温暖。
```

#### 3. 

**English：**
```
The same coastal town, but the atmosphere has shifted. The market is still busy, but the energy feels rushed and anxious. Faces are more serious, conversations more hurried. The sky carries a greyish tint, and the light feels harder, less forgiving. The warm mustard-brown #8B7355 now appears duller, almost sickly. People are bundling goods, boarding windows, moving with purpose. Strangers—news-bringers—stand among the crowd. The inn is crowded with unfamiliar faces. Guards at the city gate stand alert. The sense of safety has eroded; tension hangs in the air like humidity before a storm.
```

**中文：**
```
同一个沿海小镇，但氛围已经改变。市集仍然繁忙，但能量变得仓促和焦虑。人脸更加凝重，对话更加急促。天空呈现灰蒙的色调，光线变得更加生硬、更加无情。温暖的枯草黄#8B7355现在显得更加浑浊，几乎病态。人们在捆绑货物、封窗户、有目的地移动。陌生人——带来信息的人——站在人群中。客栈被陌生面孔充满。城门口的守卫显得更加警觉。安全感已经侵蚀；紧张感像风暴前的湿度一样笼罩在空气中。
```

#### 4. 

**English：**
```
Night in the anxious town. Fewer lights than before. The color palette has shifted toward darker, cooler tones—darker brown #2C1810 creeping into shadows. Oil lamps flicker uncertainly. Huddled groups of townspeople whisper urgently in doorways and narrow streets. The sea is dark and restless, its sound ominous. The sky is overcast, blocking starlight. Windows are shuttered or boarded. The inn still glows, filled with anxious murmuring from inside. The city gate looms dark and imposing. The feeling is of a town holding its breath, waiting for something inevitable and terrible.
```

**中文：**
```
焦虑小镇的夜晚。灯火比之前更少。色调调色板已经转向更暗、更冷的色调——焦褐#2C1810渗入阴影中。油灯闪烁不定。成群的镇民在门口和窄街里紧急低语。大海是暗色且不安的，它的声音显得不祥。天空阴沉，挡住了星光。窗户被关闭或封板。客栈仍在发光，内部充满焦虑的低语声。城门在黑暗中显得沉重而令人压抑。感觉是一个小镇屏住呼吸，等待着某种不可避免而可怕的事情。
```

#### 5. 

**English：**
```
Dawn breaks on evacuation day. The market square, once bustling with commerce, is now a staging ground. Hundreds of townspeople are gathered in orderly lines, carrying bundles of possessions. Temporary torches and oil lamps illuminate the pre-dawn darkness, their light reflecting the serious determination on faces. The city gate stands open, a threshold to safety and loss. The buildings in their faded mustard-brown #8B7355 seem hollow now, their warmth replaced by darker tones of brown #2C1810. Carts and pack animals are laden with supplies. Children are quiet, held close to their parents. The sea in the distance promises escape. The atmosphere is solemn, purposeful, heartbreaking—a people leaving home to survive.
```

**中文：**
```
撤离日的破晓。曾经繁忙的市集广场现在是集结点。数百名镇民被组织成有序的队伍，背负着包裹和行李。临时的火把和油灯照亮黎明前的黑暗，光线反映在脸上是严肃的决心。城门敞开，通往安全和失落的门槛。建筑物保留着褪色的枯草黄#8B7355，但温暖已被焦褐#2C1810的深色取代。马车和驮畜被装满了物资。儿童保持安静，紧贴在父母身边。远处的海洋承诺逃脱。整体氛围是庄严的、目的明确的、令人心碎的——一个民族为了活着而离开家园。
```

#### 6. 

**English：**
```
The town after evacuation is complete. The market square is empty—abandoned stalls overturned, goods scattered and spoiling. The inn stands silent, its windows dark. The docks are eerily quiet, boats rocking gently with no one to tend them. Buildings stand hollow, their doors open to the wind. The sun casts long, melancholy shadows. The color palette is dominated by faded brown tones and dark #2C1810 shadows. The sea in the distance is indifferent, its sound mournful. There are no people, no movement, no life. Only the wind and the slow decay of a civilization abandoned. The sky is grey and oppressive. This is what loss looks like—emptiness, stillness, and the fading echoes of a life that once was.
```

**中文：**
```
撤离完成后的小镇。市集广场空荡荡的——摊位被推倒，商品散乱腐烂。客栈沉寂，窗户漆黑。码头诡异地安静，渔船摇晃却无人照料。建筑物空洞地伫立，门被吹开。太阳投出长长的、忧伤的阴影。色调由褪色的棕色和焦褐#2C1810的深色阴影主导。远处的海洋冷漠而哀悼。没有人，没有活动，没有生命。只有风和被遗弃文明的缓慢衰落。天空灰蒙而压抑。这就是失落的样子——空洞、寂静、以及逐渐消逝的昔日生活的回声。
```

#### 7. 

**English：**
```
The final moment—a long line of refugees winds through the southern gate, moving away from the town. Families, the elderly, children—all moving with steady, determined steps. The town behind them grows smaller in the frame. The light is that of late afternoon, golden but mournful. The dark brown tones #2C1810 of the town fade into distance. Ahead lies the unknown—the sea, the road, survival. This is the price of safety—the abandonment of home, the severing of roots. The image captures both the hope of escape and the tragedy of departure. Everyone looks back once, unable to fully let go, but moving forward out of necessity.
```

**中文：**
```
最后的时刻——难民的长队蜿蜒通过南城门，远离小镇。家族、老年人、儿童——都以稳定而坚定的步伐移动。身后的小镇在画面中越来越小。光线是晚午的金色，但充满哀伤。小镇的焦褐色#2C1810色调在距离中褪去。前方是未知——大海、道路、生存。这就是安全的代价——抛弃家园、切断根基。这个画面捕捉了逃脱的希望和离别的悲剧。每个人都回头看一次，无法完全放手，但出于必要向前迈进。
```

### 电磁枪 (props, ★★★★, P4)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, 35mm film grain,
color graded with cool-toned shadows and desaturated mid-tones,
professional film production quality, depth-of-field cinematography.

Subject: Electromagnetic gun resting on a military workbench,
angled to showcase the weapon's utilitarian design.
The gun features no traditional barrel—instead, a recessed circular
electromagnetic projection mechanism at the muzzle end.
Gun body constructed of matte gunmetal and military dark green composite materials
with visible cooling fins along the mid-section.
Worn rubber grip with visible wear marks and maintenance scratches.
Overall length approximately 1.1-1.3 meters.
No neon, holographics, or cyberpunk elements.

Lighting: Harsh directional light emphasizing metal texture and wear patterns.
Cool bluish-white ambient light from overhead military facility lighting.
Shallow depth-of-field with weapon in sharp focus, background soft and industrial.

Composition: Top-down angled shot, weapon positioned diagonally across frame.
Environment: Minimalist military armory workbench, metal tools and spare parts scattered nearby.
Color palette: Dark greens (#2B3A2E), gunmetal grays (#4A4A4A), subtle rust undertones.
Film stock: Kodak Vision3 250D, 35mm, warm tungsten exposure with cool post-grade.
```

**中文：**
```
电影静帧，2.39:1 宽银幕，35毫米胶片颗粒感，
冷色调暗部与饱和度降低的中间调色分级，
专业电影制作品质，浅景深电影摄影。

主体：电磁枪静放在军事工作台上，
角度展示了武器的实用主义设计。
枪支无传统枪管——取而代之的是枪口处的内凹圆形电磁投射机制。
枪身由哑光枪铁黑与军用深绿复合材料构成，
中段可见规则的散热片。
握把采用粗糙橡胶材质，显示清晰的磨损痕迹与维护擦痕。
总长约1.1-1.3米。
严禁霓虹色、全息投影或赛博朋克元素。

灯光：苛刻的方向光突出金属纹理与磨损图案。
冷蓝白色环境光来自军事设施的顶部照明。
浅景深，武器锐利聚焦，背景柔和工业感。

构图：俯视角斜向拍摄，武器沿对角线穿过画面。
环境：极简主义军事兵器库工作台，周围散落金属工具与备件。
色调：深绿色（#2B3A2E）、枪铁灰（#4A4A4A）、微妙的锈色底蕴。
胶片：柯达Vision3 250D，35毫米，温暖钨光曝光配合冷色后期分级。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, 35mm film grain,
color graded with cool-toned shadows and desaturated mid-tones,
professional film production quality, depth-of-field cinematography.

Subject: Soldier in military tactical gear aiming and firing an electromagnetic gun
in an urban combat environment (22nd century coastal town setting).
At the moment of firing, a blue-white electromagnetic pulse erupts from the weapon's muzzle,
creating an intense arc of energy (#E0E8FF lightning-type color).
The light trajectory visible from gun muzzle to a distant target,
instantaneous electric arc with crackling energy tendrils.

Gun design: Utilitarian military-grade weapon with worn matte finish,
dark green and gunmetal color scheme, visible cooling fins, no sleek consumer aesthetics.

Soldier: Professional, composed demeanor. Weapon held with shoulder support,
showing controlled stance. No visible emotion—just tactical efficiency.

Environment: Urban ruins or damaged structures of near-future Chinese coastal town,
worn concrete, metal scaffolding, industrial decay.
Overcast sky, cool ambient lighting.
Dust and debris particles illuminated by the electromagnetic pulse.

Visual effects:
- Muzzle flash: Intense blue-white electromagnetic discharge,
  crackling electrical arcs radiating outward
- Light trail: Visible energy beam connecting gun to impact zone,
  bright #E0E8FF glow fading quickly
- Environmental reaction: Air shimmer around the beam,
  nearby loose objects slightly disturbed by electromagnetic field
- Explosive electromagnetic field: Static discharge visible in immediate surroundings

Composition: Mid-ground soldier in sharp focus, aiming downrange.
Foreground slightly out of focus with tactical obstacles.
Background blurred urban sprawl and damaged buildings.

Color palette: Military darks (greens, grays, blacks) with cold blue cast.
Muzzle flare dominates the lighting, casting harsh blue shadows.
Film stock: Kodak Vision3 500T, tungsten, slight underexposure for dramatic contrast.
```

**中文：**
```
电影静帧，2.39:1 宽银幕，35毫米胶片颗粒感，
冷色调暗部与饱和度降低的中间调色分级，
专业电影制作品质，浅景深电影摄影。

主体：士兵穿着军事战术装备，在城市战斗环境中瞄准并发射电磁枪
（22世纪中国沿海城镇背景）。
发射瞬间，蓝白色电磁脉冲从武器枪口喷出，
产生强烈的能量弧光（#E0E8FF闪电类颜色）。
光线轨迹从枪口延伸到远处目标，
瞬间电弧伴随噼啪放电的能量触须。

枪支设计：实用军工级武器，哑光磨损表面，
深绿与枪铁黑配色方案，可见散热片，无光滑消费品美感。

士兵：专业、沉着的气质。枪支肩部托举，
显示受控的射击姿态。无情感波动——仅有战术效率感。

环境：近未来中国沿海城镇的城市废墟或受损建筑，
磨损混凝土、金属脚架、工业衰败感。
阴霾天空，冷色环境光。
灰尘与碎片被电磁脉冲照亮。

视觉效果：
- 枪口闪光：强烈的蓝白色电磁放电，
  噼啪的电弧向外辐射
- 光线轨迹：清晰可见的能量光柱连接枪口到命中区域，
  明亮的#E0E8FF光线快速衰退
- 环境反应：光柱周围空气闪烁扭曲，
  附近的松散物体被电磁场轻微扰动
- 电磁脉冲爆裂：周围立即可见静电放电痕迹

构图：中景距离的士兵处于清晰焦点，瞄准前方。
前景因战术障碍物略微失焦。
背景模糊的城市蔓延与受损建筑群。

色调：军事深色（绿色、灰色、黑色）配以冷蓝色调。
枪口闪光主导光线，投射苛刻的蓝色阴影。
胶片：柯达Vision3 500T，钨光，轻微欠曝以增强戏剧对比度。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, 35mm film grain,
color graded with cool-toned shadows and desaturated mid-tones,
professional film production quality, depth-of-field cinematography.

Subject: Immediate aftermath of electromagnetic gun impact on a human target.
Target's body in the middle of collapse, limbs going rigid with blue-white
electrical current streaks visible across skin and clothing.
Eyes wide in the final moment before consciousness loss—no pain expression,
rather a look of sudden vertigo and disorientation.
Body surrounded by faint blue-white electrical corona discharge,
static crackling visible in surrounding air particles.

The struck individual shows no external injury—only the evidence of electrical phenomenon:
slight scorch marks on fabric edges, hair slightly electrified and standing,
the electromagnetic field's residual glow dissipating around the body.

Environment: Urban setting, mid-action.
Other figures in background reacting to the strike—some diving for cover,
others maintaining weapons position.
Dust and debris in air illuminated by residual electromagnetic field glow.

Lighting: Harsh blue-white primary light from the electromagnetic impact,
casting stark contrasts and shadows.
Ambient cool light from overcast sky and urban structures.

Visual effects:
- Body electrical patterns: Blue-white (#E0E8FF) electrical streaks
  across clothing and exposed skin
- Electromagnetic corona: Faint blue glow surrounding the falling body,
  static charge particles visible
- Field disturbance: Nearby loose fabric, hair, particles suspended or disturbed
  by electromagnetic field
- No impact trauma: No visible wounds, blood, or traditional ballistic injury

Composition: Center-frame target in sharp focus during the collapse moment.
Other figures blurred in background. Foreground slightly out of focus.

Color palette: Cold blues and grays dominating.
Residual glow of #E0E8FF around the stricken figure.
Urban dusty environment with desaturated tones.

Film stock: Kodak Vision3 500T, high-contrast, sharp grain to emphasize
the moment of electrical discharge.
```

**中文：**
```
电影静帧，2.39:1 宽银幕，35毫米胶片颗粒感，
冷色调暗部与饱和度降低的中间调色分级，
专业电影制作品质，浅景深电影摄影。

主体：电磁枪命中人类目标的立即后果。
目标的身体处于坍塌过程中，四肢变得僵硬，
可见蓝白色电流纹路穿过皮肤与衣物。
眼睛在意识丧失前的最后时刻睁大——无疼痛表情，
而是突然眩晕与失方向感的表情。
身体周围可见微弱的蓝白色电晕放电，
静电噼啪声在周围空气粒子中可见。

被击中的个体无外部伤口——仅有电磁现象的证据：
织物边缘略微焦黑，头发轻微通电竖立，
电磁场的残留光晕在身体周围消散。

环境：城市场景，战斗中期。
背景中的其他人物对打击做出反应——有些跳跃寻求掩护，
其他保持武器射击位置。
空气中的灰尘与碎片被电磁场残留光晕照亮。

灯光：来自电磁冲击的苛刻蓝白色主光源，
投射极端对比与阴影。
来自阴霾天空与城市结构的环境冷光。

视觉效果：
- 身体电流图案：蓝白色（#E0E8FF）电流纹路
  穿过衣物与裸露皮肤
- 电磁电晕：围绕坍塌身体的微弱蓝光，
  静电荷粒子可见
- 场地扰动：附近的松散织物、头发、粒子被电磁场悬浮或扰动
- 无冲击创伤：无可见伤口、血液或传统弹道伤害

构图：画面中心的目标在坍塌时刻清晰聚焦。
其他人物在背景中模糊。前景略微失焦。

色调：冷蓝与灰色占主导。
#E0E8FF的残留光晕围绕被击中的人物。
城市尘埃环境，色调饱和度降低。

胶片：柯达Vision3 500T，高对比度，锐利颗粒感
以强调电磁放电时刻。
```

### 老吴山间小屋 (locations, ★★★★, P4)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen.
Morning light in a rural mountain cottage.
Golden sunlight streams through window frames onto clay-daubed walls and worn wooden furniture.
A simple fire burns in the center of a humble room—rafters of straw and branches visible in shadow.
Dust particles glow in the shaft of light.
Weathered clay brick texture on walls (#8B7355).
Worn wooden table and chairs in dark brown (#6B4423).
Moss-green (#4A6741) creeps along the base of walls and window edges.
The atmosphere is warm, protective, rustic.
A ceramic pot sits by the fire.
No white (#FFFFFF) colors allowed.
Cinematic color grading.
Film grain texture.
Soft, golden hour lighting.
```

**中文：**
```
电影级画面，2.39:1超宽银幕。
山间土屋的晨间时刻。
金色的晨光透过窗框投入，洒落在泥垛子墙体和古旧木制家具上。
简陋的火焰在房间中央燃烧——芦苇和树枝搭建的椽子在阴影中隐约可见。
灰尘粒子在光线中闪闪发光。
泥垛子墙体纹理呈枯草黄色（#8B7355）。
磨损的木制桌椅呈鞍褐色（#6B4423）。
苔绿色（#4A6741）的青苔爬满墙基和窗沿。
氛围温暖、庇护感、田园朴素。
陶瓷罐靠近火焰。
禁用纯白色（#FFFFFF）。
电影级调色。
胶片颗粒质感。
柔和的金色时刻光线。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen.
Midday in a mountain cottage courtyard.
Harsh sunlight floods the unpaved earth yard. Workers move through the space—hauling water, tending a simple vegetable garden, hanging laundry.
Weathered clay brick cottage in background with moss and age marks visible.
A small stream (#3A5F7F) flows beyond the fence, surrounded by wildflowers and tall grass.
Color palette: earth yellows (#8B7355), deep browns (#6B4423), moss green (#4A6741).
No white.
Strong contrast between sun-lit areas and deep shadows cast by the cottage.
Film grain, documentary-like clarity.
Warm but harsh midday light.
Sense of labor, continuity, humble domestic life.
```

**中文：**
```
电影级画面，2.39:1超宽银幕。
山间小屋的日中时刻。
刺眼的阳光充斥着未铺装的黄土院子。劳作者在空间中移动——挑水、打理简陋菜地、悬挂衣物。
背景中风化的泥垛子小屋，青苔和岁月痕迹清晰可见。
小院外，溪流（#3A5F7F）蜿蜒流动，周围环绕野花和高草。
色彩布局：土黄色（#8B7355）、深褐色（#6B4423）、苔绿色（#4A6741）。
禁用纯白。
小屋投射的深影与阳光区域形成强烈对比。
胶片颗粒，纪录感清晰度。
温暖但刺眼的日中光线。
劳作、延续、朴素家务生活的感受。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen.
Late afternoon in the cottage courtyard.
Orange-golden sunlight rakes across the scene at a low angle, creating long shadows.
Two figures sit by the cottage wall or near the stream, in intimate conversation or comfortable silence.
The light wraps around their faces and bodies, suggesting deep connection.
Behind them, the cottage is bathed in warm amber. Moss and weathered clay (#8B7355 #6B4423) glow.
Wildflowers near the stream catch the light (#4A6741 greenery surrounding).
The small stream reflects the golden hour light.
No white tones.
Film photography aesthetic.
Golden hour color temperature.
Emotional, romantic, bittersweet undertone.
Depth of field suggests intimacy.
```

**中文：**
```
电影级画面，2.39:1超宽银幕。
午后斜阳时刻，小屋院子。
橙金色的阳光以低角度斜射，投出长长的影子。
两个身影坐在小屋墙边或溪流旁，亲密对话或舒适的沉默。
光线缠绕着他们的脸庞和身体，暗示深刻的连接。
身后，小屋沐浴在温暖琥珀色中。青苔和风化泥垛（#8B7355 #6B4423）闪闪发光。
溪边的野花捕捉到光线（#4A6741绿色环绕）。
小溪反射金色时刻的光线。
无纯白色调。
胶片摄影美学。
金色时刻色温。
情感、浪漫、苦涩底色。
景深强调亲密感。
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen.
Dusk over the mountain cottage.
Warm reddish-orange light floods the scene.
The kitchen area of the cottage shows smoke/steam rising—preparation of an evening meal.
The cottage walls glow in deep warm tones (#8B7355 becoming more amber and red).
Shadows deepen. The stream reflects the red sky.
A figure tends to the fire or stirs a pot, backlit by the sunset.
Moss and weathered textures catch the golden-red light (#4A6741 turning bronze).
No white.
The cottage feels alive, inhabited, full of anticipation.
Color grading: warm, saturated, melancholic.
Film stock quality.
Sense of time—the day ending, but warmth still present.
```

**中文：**
```
电影级画面，2.39:1超宽银幕。
山间小屋的黄昏时刻。
温暖的红橙色光线充斥画面。
小屋厨房区域显示炊烟/蒸汽升起——晚餐准备中。
小屋墙体在深暖色调中闪耀（#8B7355 变成琥珀和红色）。
影子加深。溪流映红了天空。
身影背对着落日，忙着生火或搅动锅。
青苔和风化纹理在金红光线中闪闪发光（#4A6741 转为古铜色）。
禁用纯白。
小屋显得有生命、被居住、充满期待。
调色：温暖、饱和、忧郁。
胶片质感。
时间感——日落，但温暖依然。
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen.
Night inside the cottage, candlelit and firelit.
The only light sources are a fire in the center of the room and oil lamps or candles.
Two figures sit near the fire, their faces and bodies illuminated by orange flames and shadow.
The walls recede into deep darkness, visible only where firelight catches the clay texture.
The interior is intimate, warm, secret.
Moss-green (#4A6741) barely visible in the deepest shadows.
Deep browns (#6B4423) dominate the shadows.
The earthy yellows (#8B7355) glow where fire reaches.
No white—only orange, brown, shadow.
Grain and contrast emphasize the candlelit atmosphere.
Flickering light creates a sense of movement and impermanence.
Emotional weight. Privacy. Vulnerability.
```

**中文：**
```
电影级画面，2.39:1超宽银幕。
夜间小屋内部，烛光和火光照亮。
唯一的光源是房间中央的火焰和油灯或蜡烛。
两个身影坐在火焰旁，脸庞和身体被橙色火焰和阴影照亮。
墙体深陷于黑暗中，仅在火光触及的泥垛纹理处可见。
内部亲密、温暖、秘密。
苔绿色（#4A6741）在最深的阴影中几乎不可见。
深褐色（#6B4423）主导阴影区。
土黄色（#8B7355）在火光触及处闪耀。
无纯白——仅有橙、褐、阴影。
颗粒和对比强调烛光氛围。
闪烁的光线创造运动感和无常感。
情感厚重感。隐私。脆弱。
```

#### 6. 

**English：**
```
Cinematic still, 2.39:1 widescreen.
Interior of the cottage during the period of coldness and distance.
The fire has diminished to embers or gone out entirely.
Gray ash accumulates in the fireplace. The room is dimly lit, almost dark.
Walls appear drained of color—yellows (#8B7355) become murky gray-brown.
Shadows are thick and oppressive.
A figure stands alone, or two figures are separated, facing away from each other.
Mold and dampness seem to creep up the walls.
The moss-green (#4A6741) appears sickly, not vibrant.
No white—only gray, ash, shadow.
The emotional tone is somber, suffocating, cold.
Film grain is heavy.
Color temperature is cool.
Sense of abandonment and decay.
```

**中文：**
```
电影级画面，2.39:1超宽银幕。
冷淡与疏离期的小屋内部。
火焰已减至余烬或完全熄灭。
灶火处堆积灰烬。房间昏暗，几乎黑暗。
墙体显得褪色——土黄色（#8B7355）变成浑浊的灰褐色。
影子厚重、压抑。
一个身影独自站立，或两个身影分离、背向彼此。
霉菌和潮湿似乎爬上墙体。
苔绿色（#4A6741）显得病态，不鲜活。
无纯白——仅有灰、灰烬、阴影。
情感基调是阴沉、窒息、寒冷。
胶片颗粒沉重。
色温冷调。
被遗弃和衰败的感受。
```

#### 7. 

**English：**
```
Cinematic still, 2.39:1 widescreen.
The cottage after a rainstorm, at early morning light.
The air is clear, washed clean. Sunlight is pure and crystalline.
Water drips from eaves. The courtyard is wet and glistening.
A figure begins to sweep, to organize, to tend the fire anew.
The walls, cleaned by rain, reveal their true colors—warm earth yellows (#8B7355) and rich browns (#6B4423) are vibrant again.
Moss glows bright green (#4A6741).
The stream is full and clear, reflecting the sky.
Hope and renewal are palpable.
Light is soft but clear—not harsh, not dim.
Color is saturated and rich, but not oversaturated.
Emotional tone: redemption, second chance, tender.
Film aesthetic: clean, renewed, honest.
```

**中文：**
```
电影级画面，2.39:1超宽银幕。
雨后的小屋，清晨阳光时刻。
空气澄澈，被洗净。阳光纯净而晶亮。
水从屋檐滴落。院子湿润闪闪发光。
身影开始扫地、整理、重新生火。
被雨水洗净的墙体，露出真实色彩——温暖的土黄（#8B7355）和丰富的褐色（#6B4423）重新鲜活。
青苔闪闪发绿（#4A6741）。
溪流充足而清澈，映照蓝天。
希望和复兴触手可及。
光线柔和但清晰——既不刺眼，也不昏暗。
色彩饱和而丰富，但不过饱和。
情感基调：救赎、重生、温柔。
胶片美学：洁净、重生、诚实。
```

#### 8. 

**English：**
```
Cinematic still, 2.39:1 widescreen.
Distant view of the cottage from the path leading away.
A figure stands at a distance, turning back one last time to look at the small dwelling.
The cottage recedes into the landscape—surrounded by mountain forest, the small stream in foreground.
The light is ambiguous—could be dawn or dusk, neither fully day nor night.
Colors are muted but resonant: earth tones (#8B7355), shadow browns (#6B4423), and fading moss greens (#4A6741).
The stream flows eternally, indifferent to human departure.
The cottage walls still show signs of habitation—smoke, light in a window—but the figure is leaving.
The emotional tone is bittersweet, haunting, final.
No white.
Film grain and soft focus create a dreamlike quality.
Sense of time continuing beyond this moment.
The image is a memory, not a present moment.
```

**中文：**
```
电影级画面，2.39:1超宽银幕。
从离开的路上远望小屋。
一个身影站在远处，最后一次回身凝视这个小小居所。
小屋在风景中渐行渐远——被山林环绕，小溪在前景中流淌。
光线模糊——既可能是晨曦，也可能是暮色，既非完全白昼，亦非完全夜晚。
色彩柔和却有力：土色系（#8B7355）、阴影褐色（#6B4423）、褪去的苔绿（#4A6741）。
溪流永恒流动，漠然于人的离别。
小屋墙体仍显示生活迹象——炊烟、窗中灯火——但身影正在离去。
情感基调：苦涩、幽幻、最终。
禁用纯白。
胶片颗粒和柔焦创造梦幻质感。
时间继续流逝的感受。
画面是记忆，不是现在。
```

### 黑布阵 (props, ★★★★, P4)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, concept art. A colossal black fabric array stretches for kilometers across the battlefield, rising like an insurmountable city wall. The thick, coarse-woven military-grade cloth (#1A1A1A deep black) is elevated by sturdy wooden supports. Behind it, thousands of armored soldiers stand in dense formation, completely obscured from view. Dust swirls at the base of the array. The fabric surface shows weathering, grime, and battlefield wear. Dust particles dance in warm golden afternoon light. Cinematic depth of field, volumetric lighting, earth-tone color palette with burnt orange from distant campfires. No character faces visible.
```

**中文：**
```
电影级静帧，2.39:1 超宽银幕比例，概念艺术风格。一道延绵数公里的巨大黑色布幔拔地而起，如同无法逾越的城墙耸立在战场之上。厚重的粗织军用级黑布（#1A1A1A 深沉黑色）由坚固的木质支撑柱维持竖立。布幔后方集结着数千名铠甲士兵，密集编队，完全隐蔽于视线之外。布幔底部扬起战场尘埃。织物表面显露战场使用痕迹、污垢与磨损。暖金色午后光线中，尘埃粒子舞动。电影级景深，体积光效应，土黄色与焦橙色的战场色调。无人物面部特写。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, scene photography. The massive black cloth array (#1A1A1A) advances across an open battlefield in synchronized motion with the marching army. Thousands of soldiers in ancient military armor march directly behind the opaque fabric barrier, completely concealed. The fabric ripples gently in wind, revealing its coarse texture and weathered surface. The earth beneath shows footprint trails. Sky above transitions from afternoon gold to dusk tones. Distant campfire glow illuminates the cloth's edge with warm orange rim-light. Volumetric dust and smoke swirl. Cinematic color grading: burnt sienna, charcoal, ochre, flame orange. No faces. Military historical epic atmosphere.
```

**中文：**
```
电影级静帧，2.39:1 超宽银幕，场景摄影。巨大的黑色布幔阵列（#1A1A1A）跨越开阔战场，与身后军队同步前进。数千名穿着古代甲胄的士兵密集编队行进，紧贴布幔后方，完全隐蔽于黑色屏障之后。布幔在风中温和摇晃，显现粗织纹理与战场磨损痕迹。地面呈现清晰的踩踏足迹路线。天空从午后金色过渡至黄昏色调。远处营火光线照亮布幔边缘，形成暖橙色的轮廓光。体积光、尘埃与烟雾弥漫。电影级色调分级：焦棕、炭黑、土黄、火橙。无人物面部。古代战争史诗质感。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen. The black cloth array (#1A1A1A, coarse military textile) forms an absolute visual barrier between two opposing forces. The fabric is impenetrably opaque, its weathered surface catching dim firelight. In the foreground (enemy side), soldiers and warriors are disoriented, unable to pierce the veil. Behind the array, the faint silhouettes of massed troops can barely be suggested by the vibrations in the cloth. The ground is scarred with battle marks. Color palette: deep black fabric, charcoal shadows, burnt orange firelight, earth dust (#8B7355). Epic military historical drama. Cinematic depth, volumetric atmosphere. No character identification.
```

**中文：**
```
电影级静帧，2.39:1 超宽银幕。黑色布幔阵列（#1A1A1A，粗织军用纺织品）在两支对立军队之间形成绝对的视觉屏障。织物完全不透光，风化的表面在昏暗火光中泛起光芒。前景处（敌方），士兵们被阻挡，无法穿透这道布幔。布幔后方，密集部队的身影只能通过布料的微微晃动暗示。地面被战场痕迹刻画。色调：深黑色布料、炭灰色阴影、焦橙色火光、土黄色尘埃（#8B7355）。古代战争史诗氛围。电影级景深与体积光效。无人物身份信息。
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, macro detail shot. Close-up of the black cloth array's surface texture. The coarse-woven military-grade fabric (#1A1A1A) shows intricate weaving patterns, weathering, dust accumulation, and thread fraying at edges. Battlefield grime has settled into the weave. Candlelight and firelight create subtle shadows across the texture, emphasizing the cloth's thickness and weight. Warm earth-tone accents (#8B7355) visible in dust pockets. No synthetic or plastic appearance. Purely natural, heavy-duty textile feeling. Historical military material authenticity.
```

**中文：**
```
电影级静帧，2.39:1 超宽银幕，微距细节特写。黑色布幔表面纹理近景。粗织军用级黑布（#1A1A1A）展现出精细的织造纹理、风化迹象、尘埃积累与边缘线缆毛边。战场污垢已沉积在织物内部。烛火与火光在纹理表面投射微妙阴影，强调布料的厚实感与沉重感。暖土黄色细节（#8B7355）在尘埃凹陷处可见。完全无合成或塑料感。纯粹的天然厚重纺织品质感。历史军事材料真实性。
```

### 于崇宝 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a rugged Chinese martial artist man aged 40-50, short black hair tousled and unkempt suggesting constant vigilance, small dark intense eyes with piercing gaze and subtle purple-dark glow emanating from the eye sockets, thick sculpted eyebrows with high peaks suggesting stubbornness, lean angular face with prominent cheekbones and sharp jawline showing no softness, deeply tanned bronze skin with visible scar textures and outdoor-weathered appearance, thin lips set in neutral or slightly stern expression, muscular neck and broad shoulders visible, wearing dark traditional long robe with simple thick fabric, completely stoic and composed expression with otherworldly spiritual awareness visible in eyes, white neutral background, strong directional side lighting emphasizing the sharp facial planes and the mysterious purple glow within the eyes, 35mm film grain, high contrast highlighting the warrior aesthetic and spiritual intensity
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40-50岁粗粝武士气质男性的正面半身肖像，黑色短发蓬乱不齐显示时刻的警觉，圆形眼睛深色瞳孔锐利穿透且眼眶深处隐约泛出暗紫色的灵性光芒，粗厚的雕塑感眉毛眉峰高挑暗示倔强气质，棱角分明的面孔颧骨突出下颌线条锋利不见温柔，深度日晒的古铜色皮肤可见细微刀疤纹理和风化痕迹，薄唇呈中立或略显严肃的表情，肌肉发达的颈部和宽厚肩膀隐约可见，穿深色传统长衫布料厚实简素，完全沉着冷静的表情眼中闪烁着灵性觉知的光，白色中性背景，强方向性的侧光强调锋利的面部线条和眼眶内神秘的紫光，35mm胶片颗粒感，高对比度突出武士美学和灵性强度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a rugged martial artist man aged 40-50, short tousled black hair, intense small dark eyes with deep purple spiritual glow visible in the eye sockets, angular sculpted face with prominent nose and sharp jawline, deeply tanned bronze weathered skin with scar textures, thick muscular neck, broad powerful shoulders, wearing dark traditional long robe, stoic contemplative expression with spiritual intensity, hands partially visible with calloused fingers, white neutral background, warm side lighting from camera-left emphasizing the mystical purple glow in eyes and the sharp angular planes of the face, subtle energy shimmer around the figure suggesting spiritual power, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40-50岁粗粝武士气质男性的四分之三侧面半身肖像，黑色短发蓬乱，圆形眼睛深色瞳孔强烈眼眶深处可见深紫色灵性光芒，棱角分明雕塑感的面孔鼻梁高直下颌线条锋利，深度日晒的古铜色风化皮肤有刀疤纹理，粗厚肌肉颈部，宽厚有力的肩膀，穿深色传统长衫，沉着冷静而充满灵性强度的表情，手部部分可见布满老茧的手指，白色中性背景，左侧暖调侧光强调眼眶内的神秘紫光和面部锋利的棱角平面，身体周围有微妙的能量波动暗示灵性力量，35mm胶片颗粒感，高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a rugged martial artist man aged 40-50 at peak spiritual power, short tousled black hair slightly raised backward from spiritual energy flow, intense dark eyes absolutely blazing with deep purple light consuming entire eye sockets and radiating outward, deeply tanned bronze skin now seemingly glowing from within with faint metallic shimmer, extremely muscular physique at maximum tension every muscle fiber visible and shimmering, wearing dark traditional long robe with battle-worn appearance worn wrinkles and dust adding to authority, full spiritual protective gear on forearms and wrists glowing faintly with purple light, firmly holding a crystal rod that radiates intense purple glow, hand and wrist connected to the rod with visible energy tendrils, standing in absolute commanding posture tall and perfectly vertical, the entire figure seeming to be enveloped in spiritual energy, face showing absolute authority and spiritual mastery, plain dark background, dramatic intense lighting from multiple directions creating luminous effect emphasizing the purple glow, strong rim lighting on edges creating angelic supernatural halo effect around the figure, 35mm film grain with visible luminosity, cinematic supernatural warrior aesthetic
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40-50岁粗粝武士气质男性达到灵性力量巅峰的全身定妆参考，黑色短发因灵性能量流动而略显向后竖起，强烈的深色眼神现在完全被深紫色光芒占据眼眶并向外辐射，深度日晒的古铜色皮肤现在仿佛从内部发光伴有淡淡的金属光泽，肌肉在最高张力下完全绷起每一根肌肉纤维都可见且闪烁，穿深色传统长衫呈现战役后的破旧状态磨损皱褶和尘埃反而增添权威感，前臂和手腕处的完整灵性防护装备隐约泛起紫光，紧握着散发强烈紫光的水晶棒，手腕与棒体相连可见清晰的能量触须，以绝对指挥性的姿态站立笔直高大完全竖直，整个身体仿佛被灵性能量裹着，面部显示绝对的权威和灵性掌控，素色深色背景，来自多方向的戏剧强光制造发光效果强调紫光，强烈的轮廓光在边缘制造天使般的超自然光晕效果围绕整个身体，35mm胶片颗粒感可见发光效果，电影级超自然武士美学
```

### 于永智 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a young Chinese man in his early 30s, thin tall scholarly build with narrow shoulders, long pale face with high cheekbones and sharp jawline, wearing large black-framed glasses that dominates the composition and conceals the eyes behind reflective lenses, short dark hair neatly combed back against the head, pale sickly complexion from prolonged indoor laboratory work, deep-set dark eyes barely visible through the thick glasses lenses, thin lips with almost no expression, wearing a clean pristine white laboratory coat buttoned formally, hands folded or resting on a surface, expression coldly professional and detached, white neutral background, cold harsh LED laboratory lighting from overhead creating strong shadows under eyes and cheekbones, 35mm film grain, high contrast emphasizing the geometric severity of features and glasses
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头年轻中国男性的正面半身肖像，瘦高书生体型肩膀狭窄，长脸颧骨略高下颌线条棱角分明，戴着占据构图主体的大黑框眼镜镜片反光遮挡眼神，深色短发整洁贴头皮向后梳，长期室内实验室工作导致的苍白病态肤色，眼窝深陷黑眼圈明显眼神几乎被厚眼镜镜片遮挡，薄唇几乎无表情，穿整洁笔挺的白色实验服正式扣合，双手交叠或搭在表面，表情冷漠专业疏离，白色中性背景，头顶冷白色LED实验室灯光强烈投射在眼下和颧骨形成深重阴影，35mm胶片颗粒感，高对比度强调面部线条的几何感和眼镜的压倒性存在
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a young Chinese man in his early 30s with scholarly thin build, long pale face with sharp jawline in profile, large black-framed glasses prominent in the composition showing the thick frame and reflective lenses, small dark eyes visible only partially through the glasses, thin lips showing no emotion, pale laboratory-worker complexion, short dark hair neatly kept, wearing white laboratory coat, right hand raised to push glasses in characteristic gesture suggesting continuous thought, contemplative distant expression, white background, cold LED laboratory lighting creating rim light on the far side of face emphasizing the glasses frame and cheekbone structure, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头年轻中国男性的四分之三侧面半身肖像，书生气的瘦削体型，长脸苍白下颌棱角分明侧面显著，大黑框眼镜在构图中突出显示粗重的镜框和反光镜片，小眼睛仅部分透过眼镜可见，薄唇无任何情绪表达，实验室工作者苍白的肤色，深色短发整洁，穿白色实验服，右手抬起推眼镜呈习惯性思考动作，远距离沉思的表情，白色背景，冷白LED实验室光从远侧打出轮廓光强调眼镜框架和颧骨线条，35mm胶片颗粒感，高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a young Chinese man in his early 30s in laboratory work environment, thin scholarly build in profile slightly bent over workstation, wearing pristine white laboratory coat with pocket containing pen and small notebook, black-framed glasses reflecting fluorescent light obliterating the eyes behind, short dark hair neatly combed, pale indoor-worker complexion, hands poised over keyboard or data display with intense focus, expression coldly professional showing no emotion through reflected glasses, surrounded by laboratory equipment and bright screens showing data and code, plain dark background, harsh cold fluorescent LED overhead lighting creating sharp shadows and bright reflections on glasses, 35mm film grain, very high contrast emphasizing clinical coldness and technological environment
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁出头年轻中国男性在实验室工作环境中的全身定妆参考，侧面瘦削书生体型微微俯身在工作台前，穿笔挺的白色实验服口袋中插着笔和小记录本，黑框眼镜反射荧光灯光完全遮挡眼神后方，深色短发整洁贴头皮，长期室内工作的苍白肤色，双手悬停在键盘或数据屏幕上显出强烈专注，表情通过反光眼镜冷漠专业无任何情感波动，周围环绕实验室设备和亮屏显示数据和代码，素色深色背景，头顶刺眼的冷白荧光LED灯光形成锐利阴影和眼镜上的亮反射，35mm胶片颗粒感，极高对比度强调临床的冷漠感和技术环境的压迫性
```

### 于永龙 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a 30-year-old Chinese male engineer, short black hair neatly styled, prominent sharp facial features with defined cheekbones and jawline, round bright eyes filled with keen intelligence and passionate intensity, straight nose, thin lips set in determined expression, deeply tanned bronze skin from outdoor engineering work, wearing a dark blue or grey cotton work jacket with sleeves rolled up exposing tanned muscular forearms with visible work calluses and oil stains, slight forward lean of shoulders suggesting engaged readiness, white neutral background, warm studio lighting from front and side emphasizing the bronze skin tone and facial definition, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁中国男性工程师的正面半身肖像，黑色短发整洁有型，棱角分明的脸型高颧骨尖锐下颌线条清晰，圆形明亮的眼睛充满聪慧与工程热情强度，挺直鼻梁，薄唇呈坚定表情，因工程工作长期在户外而深度日晒的古铜色皮肤，身着深蓝或灰色棉布工作夹克袖子卷起露出晒黑的结实前臂可见老茧和油渍，肩膀微微前倾显示随时待命的投入姿态，白色中性背景，前侧暖调工作室光强调古铜肤色和面部线条清晰度，35mm胶片颗粒感，中高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a 30-year-old Chinese male engineer, black short hair, sharp facial features radiating youthful intensity, bright intelligent eyes conveying passionate determination, medium height (170-175cm) with lean athletic build, muscular shoulders and arms showing bronze tan from outdoor work, standing with slight forward lean of torso and feet shoulder-width apart suggesting ready-to-act posture, wearing dark blue or grey cotton work jacket with visible tool belt across hips, grey work trousers, sturdy construction boots, work gloves hanging from belt, hands showing visible oil stains and work calluses indicating active fieldwork, white neutral background, warm even lighting emphasizing the tanned musculature and sharp facial definition, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁中国男性工程师的全身正面肖像，黑色短发，棱角分明的脸型散发年轻的强度感，明亮聪慧的眼睛传达充满工程热情的坚定，中等身高（170-175厘米）精瘦运动型体型，肩膀宽阔前臂肌肉分明呈因工作而日晒的古铜色，身体微微前倾脚距肩宽的站立姿态暗示随时可投入行动的准备状态，穿深蓝或灰色棉布工作夹克腰间系工具腰包，灰色工装裤，坚实施工靴，工作手套悬挂在腰带上，双手可见明显油渍和老茧暗示积极的实地工作，白色中性背景，暖调均匀光强调日晒的肌肉线条和面部清晰度，35mm胶片颗粒感，中高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body reference of a 30-year-old Chinese male engineer at the moment of brilliant breakthrough after intense struggle, black hair tousled and damp from sweat and laser focus, eyes showing profound exhaustion yet radiating sudden crystal-clear clarity and unshakeable determination as if inner lights have ignited, deeply tanned bronze skin appearing slightly pale from extreme fatigue but entire face glowing with profound realization and understanding, lean muscular body visibly weary yet poised with dynamic renewed purpose, wearing heavily soiled and torn work jacket with sleeves completely rolled up exposing sweat-drenched bronze forearms with prominent muscle definition, work trousers heavily stained with oil and dust, boots caked with construction site material, posture still characteristically forward-leaning but now with electric kinetic energy as if breakthrough moment is crystallizing, hands positioned in explosive discovery gesture (raised in sudden realization or firmly grasping critical component with white-knuckled intensity), face transformed from previous anxiety and doubt to radiant clear resolve and purpose, plain dark background, dramatic directional lighting from upper-left creating strong sculptural shadows with warm earth tones #8B7355 dominated in shadow areas, lighting dramatically shifts from cool steel blues to warm golden ambers suggesting exact moment of breakthrough insight, 35mm film grain heavily applied for documentary authenticity, high dramatic contrast emphasizing the profound spiritual and physical transformation
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名30岁中国男性工程师经历艰苦奋斗后突破时刻的全身定妆参考，黑色头发蓬乱被汗浸湿表明激烈专注，眼睛虽然显示极度疲惫但突然闪现清晰无比的顿悟和不可撼动的坚定，仿佛内心灯火瞬间全部点亮，深度日晒的古铜色皮肤因极限疲劳略显苍白但整个面部在灵魂领悟中绽放光芒，精瘦结实的身体显示明显的疲劳但以焕然重生的动态目标精准摆正，穿着污渍破旧到极致的工作夹克袖子完全卷起露出被汗湿透的古铜色前臂肌肉清晰分明，工装裤上油渍和尘土污渍密集覆盖，靴子上沾满工地材料层叠，身体姿态保持标志性的前倾但现在带着突破时刻的电击般的动态能量，手部摆出爆发性发现时刻的手势（高举显示瞬间恍然大悟或用尽全力握住关键部件），面部从前期的焦虑和疑虑彻底蜕变为清晰炽热的决心和使命感，素色深色背景，戏剧性的左上方定向强光创造雕塑感强影，枯草黄#8B7355暖土色主导阴影区域，光线从冷硬的钢蓝色戏剧性转向温暖金色的琥珀色预示突破顿悟的确切时刻，35mm胶片颗粒感重度应用表现记录片般的真实性，高戏剧对比度强调深刻的精神与肉体蜕变
```

### 元刚智刚 (characters, ★★★, P5)

#### 1. 

**English：**
```
A sterile laboratory illuminated by cold white LED lights uniformly. Glass walls and precision equipment surround the space. On the left stands Yuan Gang, a young male with a fresh, clean face, innocent and harmless gaze like a blank sheet of paper, wearing a simple white scientific uniform, appearing pure and sterile overall. On the right hovers Zhi Gang, same body but completely different aura, sharp and confident eyes, body surrounded by soft blue-white energy halos and subtle ripples, wearing dark gray tactical gear, appearing lethal and powerful. The two form a stark contrast, symbolizing the fusion of technology and the supernatural, 80% photorealism + 20% fantasy elements.
```

**中文：**
```
一个无菌实验室，冷白LED灯光均匀照射。玻璃墙壁与精密设备围绕空间。左侧站着元刚，年轻男性，清爽清新面容，天真无害的眼神如白纸般空白，穿着简洁的白色科研制服，整体显得纯净与无菌。右侧漂浮着智刚，同样的身体但气质完全不同，眼神锐利自信，身体周围环绕蓝白色的柔和能量光晕与微妙的波纹，穿着深灰色战术装，显得致命而有力。两者形成鲜明对比，象征科技与超自然的融合，80%写实主义+20%魔幻元素。
```

#### 2. 

**English：**
```
Two head close-ups side by side, in comparison. On the left is Yuan Gang's head, a young and handsome male face, skin excessively smooth and uniform (displaying artificial characteristics), eyes crystal clear and transparent like jade, pupil edges sharp and defined, gaze blank yet full of curiosity, lips pale pink, the entire face under cold white lighting appearing slightly blue-white (normal medical lighting effect), without any blemishes or traces, appearing sterile and perfect. On the right is Zhi Gang's head, same facial structure but expression completely different, eyes sharp and profound, pupils concentrated, gaze like a knife blade sharp, possibly flashing subtle blue or amber micro-light, facial lines appearing determined due to focus, mouth corners slightly tense, the entire head surrounded by subtle blue-white halos, appearing dangerous yet reliable. Both heads should display the refinement and perfection of artificial beings, but through differences in gaze and aura convey completely different character qualities.
```

**中文：**
```
两个头部特写，并排对比。左侧是元刚的头部，年轻清秀的男性面容，皮肤过度光滑与均匀（显示人造特征），眼睛清澈透彻如琉璃，瞳孔边缘清晰，眼神空白而充满好奇，嘴唇淡红色，整个面部在冷白灯光下显得有点青白（正常的医学照明效果），无任何瑕疵或痕迹，显得无菌而完美。右侧是智刚的头部，同样的面部结构但神情截然不同，眼睛锐利深邃，瞳孔集中，眼神如刀锋般专注，可能闪现微妙的蓝色或琥珀色微光，面部线条因专注而显得坚定，嘴角略微紧绷，整个头部被微妙的蓝白色光晕环绕，显得危险而可靠。两个头部都应该显示出人造体的精致与完美，但通过眼神与气质的差异传递完全不同的人物质感。
```

#### 3. 

**English：**
```
A digital human creation laboratory, sci-fi style sealed clean room. Cold white LED daylight lights illuminate every corner uniformly, color temperature approximately 6000K, medical-level lighting environment. Floor and walls use pure white and light gray matte materials. At the center is an open-air life support platform, surrounded by precision scanning equipment (exterior like medical imaging devices), energy monitoring instruments, data display screens, and dozens of pipes and power lines. The ceiling shows visible industrial-style grid and ventilation systems. Large glass observation windows reveal external control rooms. The entire space appears sterile, cool-toned, filled with scientific and futuristic aesthetics. At the center, young male Yuan Gang just opens his eyes, lying on the life support platform, wearing a simple white medical gown, skin smooth as mirror, eyes clear yet full of confusion and curiosity. The ceiling's blue-white energy indicator lights flicker subtly. This is a crucial moment of artificial life birth, filled with both miraculous and technological coldness.
```

**中文：**
```
数字人造体实验室，科幻风格的密封无尘室。冷白色的LED日光灯均匀照射每个角落，色温约6000K，医学级别的照明环境。地面与墙体采用纯白与浅灰的磨砂材料。中心是一个开放式的生命维持平台，周围环绕精密的扫描设备（外形如医学成像设备）、能量监测仪表、数据显示屏与数十根管道与电源线。天花板是可见的工业风格网格与通风系统。大型玻璃观察窗显示外部监控室。整个空间显得无菌、冷调、充满科学与未来感。中央，年轻男性的元刚刚刚睁开眼睛，躺在生命维持平台上，穿着简单的白色医疗衣，皮肤光滑如镜，眼神清澈但充满困惑与好奇。天花板的蓝白色能量指示灯微妙地闪烁。这是一个人工生命诞生的关键时刻，既充满奇迹感，又充满了科技冷感。
```

#### 4. 

**English：**
```
The same digital human creation laboratory, but now filled with supernatural energy. Cold white LED lights still present, but the entire space is veiled by subtle blue-white energy halos. At the center, Zhi Gang hovers in mid-air, his body approximately 50 centimeters above the ground, surrounded by bright blue-white light circles beneath his feet, the circles spreading outward into subtle energy ripples. Visible energy streamlines flow around his body, like ripples in water, distorting surrounding light. He wears dark gray tactical gear, his eyes sharp as blades, eyes flashing with ice-blue or amber micro-light. His body is surrounded by soft yet powerful blue-white light membranes, displaying activated supernatural energy. The surrounding precision equipment shows subtle swaying traces from energy impacts, monitoring screens flickering with abnormal data. This is a perfect fusion of science and the supernatural, full of power and danger.
```

**中文：**
```
同一个数字人造体实验室，但现在充满了超自然的能量。冷白LED灯光仍在，但整个空间被微妙的蓝白色能量光晕所笼罩。中央，智刚悬浮在空中，身体距地面约50厘米，脚下环绕明亮的蓝白色光圈，光圈向外扩散成微妙的能量波纹。他的身体周围可见肉眼可辨的能量流线，如水中的涟漪，扭曲周围的光线。他穿着深灰色的战术装，眼神锐利如刀，眼睛中闪现冰蓝色或琥珀色的微光。他的身体被柔和但有力的蓝白色光膜包围，显示出被激发的超自然能量。周围的精密设备显示出被能量冲击而微妙晃动的痕迹，监测屏幕闪烁着异常的数据。这是科学与超自然的完美融合，充满力量与危险。
```

#### 5. 

**English：**
```
Digital human creation laboratory, cold white lighting intense and uneven, light distortion caused by energy release. On the left, Yuan Gang is forced backward, eyes full of fear and confusion, body appearing fragile and helpless. On the right, Zhi Gang hovers in mid-air, body surrounded by intense blue-white energy shields and halos, both hands possibly gathering blue-white energy spheres, about to release shock waves. Surrounding air visibility changes, light shows irregular refraction, as if the entire space is overwhelmed by the energy field. Floor and walls show cracks or swaying from shock waves. This moment symbolizes transformation from innocence to awakening, from powerlessness to strength. Scene filled with cold scientific laboratory atmosphere and supernatural battle tension.
```

**中文：**
```
数字人造体实验室，冷白灯光强烈而不均匀，因为能量的释放而产生光线扭曲。左侧，元刚被迫退后，眼神充满恐惧与困惑，身体显得脆弱与无助。右侧，智刚悬浮在空中，身体周围环绕强烈的蓝白色能量护盾与光晕，双手可能汇聚着蓝白色的能量球，即将释放冲击波。周围的空气可见性改变，光线呈现不规则折射，仿佛整个空间都被能量场压倒。地面与墙体因冲击波而产生裂纹或晃动。这一刻象征着从天真到觉醒、从无力到强大的转变。场景充满了科学实验室的冷调与超自然战斗的紧张感。
```

#### 6. 

**English：**
```
Viewing from the control room outside the laboratory, looking through large glass windows. Intense cold white LED lights illuminate the entire interior space, displaying details of all equipment and platforms. At the center, Yuan Gang or Zhi Gang (or both) are visible. Inside the control room, Wu Qisi or other researchers operate panels, screens displaying various data and energy waveforms. This perspective emphasizes the scientific nature of artificial beings and the laboratory's medical atmosphere. The glass may show reflections or fingerprints, displaying realism. Light from the laboratory interior projects out, creating subtle shadows in the control room. This is a visual representation of the power dynamics of observation and being observed, creation and being created.
```

**中文：**
```
从实验室外部的观察室看向内部，透过大玻璃窗。冷白LED灯光强烈地照亮了整个内部空间，显示出所有的设备与平台的细节。中央，元刚或智刚（或两者）可见。观察室内，吴启思或其他科研人员在操作面板，屏幕上显示出各种数据与能量波形。这个视角强调了人造体的科学性与实验室的医学感。玻璃上可能有反光或指纹，显示真实感。灯光从实验室内透出，在观察室内产生微妙的阴影。这是一个观察与被观察、创造与被创造的权力动态的视觉呈现。
```

### 分割带 (props, ★★★, P5)

#### 1. 提示词 1：激发与蓄力场景 [激发与蓄力场景]

**English：**
```
Cinematic still, 2.39:1 widescreen, 8K quality. A supernatural being with primordial spirit energy holds a glowing division strip wrapped around its wrist, carefully unwrapping the elastic bands. The strip shimmers with dark gold (#DAA520) and warm white (#FFF8DC) hues, with translucent spiritual light emanating from its surface. Left hand pinches the strip between thumb and forefinger, right hand hooks and begins to pull, creating tension. Surrounding air distorts with spiritual energy, faint glow trails forming around the strip. Cinematic lighting emphasizes the taut form and luminous texture. Heavenly/celestial realm aesthetic, supernatural energy visualization, photorealistic rendering with ethereal light effects, professional cinematography, no character faces visible, focus on the prop mechanics and spiritual luminescence.
```

**中文：**
```
电影级影像，2.39:1宽银幕，8K品质。元神状态的超自然存在握着缠绕于手腕的分割带，小心地展开弹性织物。灵能条纹闪烁着暗金色（#DAA520）和暖白色（#FFF8DC），表面散发半透明灵气光晕。左手拇指与食指夹住分割带两端，右手食指勾住并开始拉动，形成张力。周围空气因灵能扭曲，淡淡的光迹在分割带周围形成。电影质感光照强调了紧绷的形态与发光质感。天界/元神美学，超自然能量可视化，写实渲染配合灵气光效，专业电影质感，不显示角色面部，聚焦于道具机制与灵能发光。
```

#### 2. 提示词 2：飞行切割与瞬间爆发 [飞行切割与瞬间爆发]

**English：**
```
Cinematic still, 2.39:1 widescreen, 8K quality. A supernatural energy strip flies through space at extreme velocity, captured mid-action as it cuts through a large translucent spherical object, cleanly dividing it into two distinct halves. The division strip glows brilliantly with dark gold (#DAA520) and warm white (#FFF8DC) luminescence, trailing flowing light energy patterns. The cut surface of the divided sphere gleams with residual spiritual energy, fine details of the pristine division visible. Surrounding environment erupts with ethereal light bursts and energy dispersal at the moment of separation. Heavenly realm aesthetic, supernatural physics, dynamic motion blur, cinematic depth of field, professional lighting design, focus on the cutting mechanics and luminous energy effects, no character visible, celestial atmosphere.
```

**中文：**
```
电影级影像，2.39:1宽银幕，8K品质。超自然灵能飞带以极速穿过空间，在切割大型半透明球形物体的瞬间被捕捉，将其完整分割为两个独立的半球。分割带绽放暗金色（#DAA520）和暖白色（#FFF8DC）的强烈光芒，拖曳着流动的灵能光迹纹理。被分割球体的切割面闪烁着残余灵能，可见完美分割的细节质感。周围环境在分割瞬间爆发以太光团与能量散逸。天界美学，超自然物理规则，动态运动模糊，电影景深效果，专业灯光设计，聚焦于切割机制与发光能量效应，无角色出现，天界氛围营造。
```

#### 3. 提示词 3：手腕佩戴与静息状态 [手腕佩戴与静息状态]

**English：**
```
Cinematic still, 2.39:1 widescreen, 8K quality. Close-up detail of a supernatural division strip coiled loosely around a wrist, rendered in dark gold (#DAA520) and warm white (#FFF8DC) tones. The fabric appears ethereal and translucent, with subtle luminescence pulsing beneath the surface. Spiritual energy faintly glows along the edges, creating a soft halo effect. Surrounding aura indicates celestial/heavenly realm origin. Photorealistic texture with supernatural light properties, intricate weaving details visible, cinematic macro photography style, heavenly aesthetic, no character face shown, emphasis on prop material and ethereal quality, professional rendering.
```

**中文：**
```
电影级影像，2.39:1宽银幕，8K品质。超自然分割带松散缠绕于手腕上的特写细节，暗金色（#DAA520）和暖白色（#FFF8DC）色调呈现。织物显现出以太般的轻透质感，表面下方灵能微弱脉冲闪烁。灵气沿着边缘淡淡发光，形成柔和的光晕效果。周围灵气提示天界/元神来源。写实纹理配合超自然光学特性，可见细致的编织细节，电影微距摄影风格，天界美学，不显示角色面部，强调道具材质与以太品质，专业渲染水准。
```

### 卢卫寿 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese man in his early 50s, short black hair with hints of grey at temples, oily complexion with visible shine on forehead and cheeks indicating a lifetime in restaurant business, round face with full cheeks and honest expression, small alert eyes with sharp calculating gaze revealing merchant intelligence, warm friendly smile with laugh lines around eyes, slightly stocky build with rounded shoulders visible, wearing a clean white or beige restaurant apron over a simple long robe or shirt, set against a plain dark background, warm soft lighting emphasizing the oily skin tone and the contrast between warmth and shrewdness in expression, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50岁出头中国男性的正面半身肖像，短黑发两鬓略显花白，油腻的面容额头和脸颊可见明显油光暗示终身从事餐饮业，圆脸面颊饱满忠厚的表情，小而有神的眼睛精明的目光透露出商人的聪慧，温暖友善的笑容眼角有笑纹，略显敦实的体型肩膀略圆，穿洁白或米色的餐馆围裙套在简洁的长衫或衬衫外，纯暗色背景，暖调柔光强调油腻的肤色和表情中温暖与精明的对比，35mm胶片颗粒感，中高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a Chinese man in his early 50s, short black hair with grey streaks, round face with full cheeks, small eyes with keen merchant's gaze, oily skin with characteristic shine, warm gentle expression with smile lines, wearing clean white restaurant apron over simple robe, right hand raised in a welcoming gesture typical of restaurant proprietor, white neutral background, warm side lighting from camera-left emphasizing oily skin texture, soft shadows under eyes suggesting age and experience, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50岁出头中国男性的四分之三侧面半身肖像，短黑发略有花白，圆脸面颊饱满，小眼睛有敏锐的生意人目光，油腻的皮肤特有的光泽，温暖和蔼的表情有笑纹，穿洁白的餐馆围裙套在简洁长衫外，右手呈出迎接的手势是餐馆老板的典型肢体语言，白色中性背景，左侧暖调侧光强调油腻肤色纹理，眼底柔和阴影暗示年龄和阅历，35mm胶片颗粒感，中等对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a Chinese man in his early 50s, medium build with slight roundness indicating comfortable lifestyle, short black hair with grey streaks, round honest face with warm smile, small sharp eyes showing merchant intelligence, oily complexion, standing upright with natural confident posture, wearing a clean white or beige restaurant apron secured at waist and chest, underneath a simple long robe or light-colored shirt, simple cloth shoes, hands held naturally at sides or gesturing in welcoming manner, overall appearance of a successful restaurant proprietor radiating warmth and reliability, plain dark background, warm even lighting, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50岁出头中国男性的全身正面肖像，中等身材略显圆润显示舒适的生活，短黑发略有花白，圆脸忠厚温暖的笑容，小眼睛有商人的精明，油腻的面容，笔直自信的站姿，穿洁白或米色的餐馆围裙系于腰间和胸前，内穿简洁的长衫或浅色衬衫，简素布鞋，双手自然垂于身侧或做出欢迎手势，整体形象是一位成功的餐馆老板散发温暖和可靠感，素色深色背景，暖调均匀光，35mm胶片颗粒感，中高对比度
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, scene from a traditional Chinese restaurant interior, a middle-aged Chinese man in his early 50s with oily complexion and sharp intelligent eyes stands behind a wooden counter or in the dining hall, wearing a pristine white apron over a simple long robe, smiling warmly and welcoming at approaching guests or family members, his expression radiating both merchant shrewdness and genuine hospitality, round full-cheeked face glowing with the health of someone comfortable and successful, hands gesturing in friendly greeting or holding a serving tray, the restaurant background shows wooden furniture and warm interior lighting suggesting evening hours, color palette warm earthy tones with #8B7355 predominant, soft shadows, realistic portrait style capturing the essence of a content successful proprietor
```

**中文：**
```
电影感静帧，2.39:1宽银幕，传统华人餐馆内部场景，一位50岁出头油腻面容眼神精明的中国男性站在木质柜台或餐厅中，穿洁白的围裙套在简洁的长衫外，笑容满面地向靠近的客人或家人问好，表情既透出商人的精明又展现真挚的热情待客，圆脸面颊饱满闪耀着舒适成功人生的光彩，双手做出友善的欢迎手势或拿着托盘，餐馆背景可见木质家具和暖色室内灯光暗示夜间时段，色调为温暖的大地色调以#8B7355为主，柔和阴影，写实肖像风格捕捉一位满足的成功餐馆老板的本质
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, interior or institutional setting, the same Chinese man from earlier stages now appears drastically changed, oily skin has turned sallow and grey losing all healthy luster, round face now slack and expressionless, eyes vacant and unfocused with milky dullness replacing the previous sharp intelligence, hair unkempt, wearing soiled rumpled apron and robe, posture hunched and mechanical, standing or moving with sluggish unnatural movements as if controlled by an external force, hands hanging limply or being directed by unseen puppet strings, expression completely blank with no trace of the former warmth or shrewdness, background institutional or dimly lit interior, color palette shifts to sickly grey-yellow and dark purple tones (#5B3A6B), cold harsh lighting draining all warmth, overall atmosphere deeply unsettling suggesting possession or complete loss of will
```

**中文：**
```
电影感静帧，2.39:1宽银幕，室内或机构场景，与前期形象判若两人的同一位男性现在显得骇人改变，油腻的皮肤已变为病态的蜡黄失去所有健康光泽，圆脸现在松弛麻木无表情，眼神空洞失焦乳白色的混浊取代曾经的精明锐利，头发蓬乱，穿沾污的褶皱围裙和长衫，佝偻的身体和机械的姿态，以缓慢不自然的动作站立或移动仿佛被外力操纵，双手无力下垂或被看不见的提线操控，表情完全空白曾经的温暖和精明痕迹全无，背景是机构或昏暗室内，色调转变为病态的灰黄和暗紫（#5B3A6B），冷色刺眼的光线抽干所有暖意，整体氛围诡异不安暗示被附身或意志完全丧失
```

### 卢静 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a young Chinese woman in her 20s, long glossy black hair carefully arranged, round youthful face with bright sparkling eyes full of curiosity and mischief, smooth fair skin with a natural healthy glow, wearing a clean well-maintained tunic in warm earth tones (beige-brown palette #8B7355), delicate features reflecting a merchant's daughter upbringing, slight confident smile suggesting enthusiasm and joy, expression radiating innocence and wonder at the world, white neutral background, soft warm front lighting emphasizing youthful radiance, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名20多岁年轻中国女性的正面半身肖像，乌黑长发精心梳理，圆润年轻的脸庞上眼睛明亮闪闪发光充满好奇与调皮，光滑白皙的皮肤呈现天然健康的光泽，穿着整洁打理精致的上衣色调为温暖的米色褐色（#8B7355），精致的五官反映商人之女的优越身份，嘴角带着自信微笑暗示热情与欢乐，整体表情洋溢对世界的纯真与惊喜，白色中性背景，柔和暖调正面光强调年轻的容光焕发，35mm胶片颗粒感，中高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of the same young woman now showing signs of hardship and motherhood, long black hair less maintained but still retaining dignity, face showing exhaustion and deep love intertwined with sorrow, eyes with protective maternal intensity, wearing simple faded brown clothes worn from travel and care-giving, one hand cradling a child unseen but implied by her posture, standing with protective stance, pale skin from indoor care duties contrasting with worn fabric, expression grave and devoted, plain dark background emphasizing isolation and hardship, dramatic lighting with shadows suggesting emotional weight, 35mm film grain, high contrast emphasizing maternal determination
```

**中文：**
```
电影感静帧，2.39:1宽银幕，同一位年轻女性的全身正面肖像，此时已显露苦难与母性的痕迹。长黑发未精心打理但保留尊严，脸庞显露疲惫与深情的交织，眼神闪烁母爱的保护性强度，穿着简朴褪色的棕色衣着沾着旅行与照顾的痕迹，一只手环抱不可见但由姿态暗示的孩子，身体语言显露保护的立场，苍白的肌肤因长期室内照顾与日晒的棕褐色衣着形成对比，表情严肃而献身，素色深色背景强调孤立与艰难，戏剧性光影投出阴影暗示情感的重压，35mm胶片颗粒感，高对比度强调母亲的决心
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a young woman transformed into a widow, face showing deep exhaustion but unwavering resolve, eyes no longer bright but clear with purpose, long black hair pulled back simply, wearing worn working clothes or travel-stained garments in faded browns and grays, one hand holding a whip or tool of necessity, other hand firmly gripping a child's hand or reaching forward, standing with mother's fierce protective stance, skin weathered but not broken, expression mixing maternal tenderness with steel-like determination, background transitioning from dark to warm edge light suggesting hope ahead, 35mm film grain, dramatic contrast between vulnerability and strength
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一位年轻女性蜕变为寡妇后的全身正面肖像。脸庞显露深度疲惫但不屈的意志，眼神不再明亮但充满目的的清晰，长黑发简单束起，穿着褪色的棕色灰色工作装或旅行沾染的衣物，一只手握着鞭子或生存的工具，另一只手紧紧握住孩子的手或向前伸出，母亲的凶悍保护姿态明显，皮肤经历风霜但未被摧毁，表情混合母性的温柔与钢铁般的决心，背景从深色逐渐过渡到暖色边缘光暗示前方的希望，35mm胶片颗粒感，脆弱与力量的戏剧性对比
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, scene of a young couple exploring new lands together, young woman with radiant expression pointing at something in the distance or examining local scenery with wonder, resembling "a young wild horse freshly let out of cage, looking here and there" — her eyes wide with discovery, head turning with curiosity, body leaning forward with eagerness. Warm golden natural lighting, rich earth-tone color palette with blues and greens suggesting new environments, intimate moments showing affection and mutual trust. New marriage setting with adventure and romance in early married life. 80% realism, 20% subtle fantasy suggesting boundless possibilities and youthful optimism. Traditional folk era background. Cinematic 35mm grain.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，年轻夫妻共同探索新世界的场景。年轻女性容光焕发的表情指向远处或观察当地景物时满是惊喜，"像一匹刚出笼的野马，东瞧瞧，西看看"——眼睛睁得很大充满发现的喜悦，头部随好奇而转动，身体因热情而向前倾。温暖的金色自然光，丰富的枯草黄褐色色调配合蓝色绿色暗示新的环境，充满亲昵与相互信任的亲密时刻。新婚家庭的设定背景充满冒险与浪漫。80%写实+20%幻想氛围暗示无限可能与青年的乐观。民间时代背景。电影感35mm胶片颗粒。
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, somber intimate scene of a young woman crouched or sitting beside a sickbed in a humble dwelling. Face showing deep love and profound exhaustion intertwined, hand holding the ill man's hand, sometimes calling out his name. Candlelight or dim natural light casting long shadows, simple worn furnishings, atmosphere heavy with illness and impending loss. Woman's expression pure anguish and tender devotion, her body language protective and completely devoted. Worn fabric suggesting poverty and hardship. 80% realism with 20% supernatural emphasis on human love and maternal sacrifice. Dramatic lighting emphasizing the weight of caregiving, intimate tragic quality. Cinematic 35mm grain.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，年轻女性蹲坐在简陋居所病床边的沉重亲密场景。脸庞显露深深的爱与深重的疲惫的交织，手紧握病人的手，有时大声呼喊他的名字。烛光或昏暗的自然光投射长影，简陋的家具，弥漫着疾病与死亡临近的沉重气氛。女性的表情纯粹是痛苦与温柔的献身，身体语言显露保护欲与完全的投入。破旧的布料暗示贫困与艰辛。80%写实+20%超自然风格强调人类的爱与母亲的牺牲。戏剧性的光影强调照顾的沉重，亲密的悲剧感。电影感35mm胶片颗粒。
```

#### 6. 

**English：**
```
Cinematic still, 2.39:1 widescreen, dramatic nighttime escape scene. A young widow standing or moving with fierce maternal determination, face resolute and sharp, raising a whip or tool of survival with intensity, one hand firmly gripping the hand of a young child beside her, eyes blazing with protective fire. Traveling through rough terrain at night, dark sky overhead, figures silhouetted against fading twilight or moonlight. Worn travel-stained clothes, every movement purposeful and powerful. In the distance, faint silhouettes of hope (settlement or other survivors). 80% realism with 20% supernatural emphasizing maternal ferocity and unbreakable survival will. Epic intense quality showing a mother's determination to save her child. Cinematic 35mm grain, dramatic high contrast.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，戏剧化的夜间逃亡场景。年轻寡妇站立或移动时充满凶悍的母性决心，脸庞坚决而锐利，高举鞭子或生存工具时充满强度，一只手紧紧握住身旁年幼孩子的手，眼神闪烁保护的火焰。在夜间崎岖地形上移动，暗沉的天空笼罩，人物轮廓在暮色或月光中清晰。衣着褪色沾上旅行痕迹，每个动作都充满目的与力量。远方隐约可见希望的身影（定居地或其他幸存者）。80%写实+20%超自然风格强调母亲的凶悍与不可摧毁的生存意志。具有史诗感、紧张感强，展现母亲为了孩子不可阻挡的决心。电影感35mm胶片颗粒，戏剧性高对比度。
```

### 县城破庙 (locations, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, abandoned ruined temple exterior with collapsed roof sections and decaying wooden beams, destitute beggars gathered in shadowed areas, broken stone steps and debris scattered, dappled sunlight through gaps revealing poverty and despair, muted earth tones with deep shadows, hopelessness embodied in architecture, desperate atmosphere, low camera angle emphasizing human suffering, gritty documentary-like realism.
```

**中文：**
```
电影镜头，2.39:1宽幅，屋顶坍塌与腐烂木梁的废弃破庙外景，乞丐们聚集在暗处，碎石阶梯与废墟散落，斑驳日光透过缝隙揭示贫困与绝望，沉静土褐配深影，建筑体现的无望感，绝望气氛，低机位强化人类苦难，粗粒纪录感写实。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, dramatic interior of derelict temple hall, well-dressed figure in center surrounded by wretched beggars, stark contrast between authority and desperation, dim candlelight or sparse daylight, expressions of hope and despair intermingled, composition emphasizing power imbalance, muted and sickly color palette, tension of manipulation, moral corruption embodied, shadows masking true intentions.
```

**中文：**
```
电影镜头，2.39:1宽幅，破败庙堂内部戏剧性时刻，衣着体面的身影居中被衣衫褴褛乞丐包围，权威与绝望的刺眼对比，昏暗烛光或稀疏日光，希望与绝望交织的表情，构图强化权力失衡，沉静与病态色调，操纵的张力，道德腐烂的体现，阴影掩盖真实意图。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, extreme low-key lighting in temple interior, barely visible human figures in suffocating darkness, architectural decay surrounding shadowy forms, single candle or faint light source creating isolated pools of visibility, overwhelming sense of helplessness and dread, monochromatic near-black color palette, suffocating composition, existential darkness, moral abyss visualized, cinematic horror of human condition.
```

**中文：**
```
电影镜头，2.39:1宽幅，庙堂内部极度低调光线，人形在窒息般黑暗中几乎不可见，建筑衰败环绕阴影身形，单烛或微弱光源投出孤立光圈，绝对无助与恐惧淹没，单色近黑色调，窒息构图，存在主义黑暗，道德深渊的可视化，人类处境的电影式恐怖。
```

### 向天志 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a 35-year-old Chinese man with angular refined features, deep-set intense dark eyes with sharp intelligent gaze suggesting profound power and control, high prominent cheekbones, sculpted jaw line, straight tall nose, thin lips with subtle upward curve hinting at authority, clear pale skin with healthy complexion, short neatly combed dark hair, wearing an elegant deep blue official robe with dark gold embroidery and pale gold insignia of state power on chest, dark gold ornate belt, subtle jade pendant at chest, expression grave and composed showing absolute command, white neutral background, cool professional front lighting emphasizing facial structure and piercing gaze, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名35岁中国男性的正面半身肖像，棱角分明的精致五官、深邃狭长的眼睛黑色瞳孔闪烁着锐利的智慧和权力感、高颧骨突出、下颌线条锐利精致、笔挺高鼻梁、薄唇微微上扬暗示权力和威严、肤色冷调偏白健康润泽、深色短发梳理整洁，穿着剪裁得体的深蓝色国主官服胸前绣有暗金纹样和淡金色的国家权力徽章、系深色金色华美腰带、佩戴精致玉佩于胸前，表情严肃沉稳透出绝对的权力掌控感，白色中性背景，冷调专业正面光强调面部结构和穿透性目光，35mm胶片颗粒感，高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a 35-year-old Chinese man with sharp angular features, deep-set eyes with penetrating gaze, high cheekbones, sculpted jaw, straight prominent nose, thin lips, clear pale skin, short dark hair neatly styled, expression of serious contemplation with subtle authority, wearing an elegant deep blue official robe with dark gold embroidery and gold insignia, dark gold belt, jade pendant, right hand raised near chin in a gesture of power and thought, white neutral background, cool professional side lighting from camera-left emphasizing the sharp facial angles and intelligent expression, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名35岁中国男性的四分之三侧面半身肖像，棱角分明的精致五官、深邃眼睛透出穿透性的目光、高颧骨、精致的下颌线条、笔挺的鼻梁、薄唇、冷调苍白的皮肤、整洁梳理的深色短发，表情严肃沉思透出隐隐的权力气质，身着剪裁得体的深蓝色官服胸前绣有暗金纹样和金色徽章、深金色华美腰带、胸前玉佩，右手抬起放于下巴处呈权力与思考的手势，白色中性背景，左侧冷调专业侧光强调锐角面部结构和聪慧的眼神，35mm胶片颗粒感，高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a 35-year-old Chinese man with lean sculpted build and commanding presence, sharp angular face with penetrating eyes, short dark hair, tall upright posture radiating authority and control, wearing an elegant deep blue official robe with dark gold embroidered patterns and state insignia on chest, elaborate dark gold belt at waist, jade pendant hanging at chest, hands positioned authoritatively at sides or resting on robe, feet shoulder-width apart in a stance of absolute power, expression of cold composure, white neutral background, cool even professional lighting, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名35岁中国男性的全身正面肖像，身材修长精壮和令人畏惧的权力气场、棱角分明的精致面孔和穿透性眼神、深色短发、笔直挺立的身姿透出权力和掌控感，身着剪裁得体的深蓝色国主官服胸前绣有暗金纹样和国家权力徽章、腰间精致华美的深金色腰带、胸前悬挂玉佩，双手自然垂于身侧或搭在衣摆上呈权力姿态、双脚与肩同宽站立呈绝对权力的站姿，表情冷静沉稳，白色中性背景，冷调均匀专业光，35mm胶片颗粒感，高对比度
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a 35-year-old Chinese man as a sovereign ruler in his prime of power, face showing sharp angular features with intense penetrating dark eyes radiating control and intelligence, short dark hair neatly groomed, wearing an exquisitely tailored deep blue official robe with intricate dark gold embroidered patterns across the chest and sleeves, bright gold state insignia prominently displayed on chest, elaborate dark gold ornamental belt cinching the waist with precision, jade pendant and formal ceremonial accessories at chest, posture rigidly upright with shoulders squared, hands either at sides in commanding pose or raised in authoritative gesture, skin tone cool pale complexion suggesting refined noble lineage, expression grave and composed radiating unquestionable authority, plain dark background, cool professional front lighting with subtle golden highlights on embroidery emphasizing regal bearing, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名35岁中国男性权力顶峰时期国主的全身定妆参考，面容棱角分明眼神锐利穿透如刀刃透出掌控和睿智、深色短发梳理整洁，身着精心剪裁的深蓝色官服胸前和袖口绣有复杂精细的暗金纹样、胸口显眼的明亮金色国家权力徽章、腰间精致华美的深金色腰带紧紧束腰显得有力、胸前玉佩和正式仪式配饰，身体笔直挺立肩膀水平，双手垂于身侧呈掌控姿态或抬起呈权力手势，肤色冷调苍白显示精英贵族身份，表情严肃沉稳透出不可侵犯的权力气质，素色深色背景，冷调专业正面光在绣纹处有细微金色高光强调雍容高贵的气质，35mm胶片颗粒感，高对比度
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a 35-year-old Chinese man showing signs of power fatigue and withdrawal, face showing the same angular structure but eyes now displaying visible weariness and loss of sharp focus, subtle lines of fatigue around eyes and mouth, short dark hair beginning to appear slightly unkempt, wearing the same deep blue official robe but now showing visible wrinkles and creases suggesting carelessness, embroidery beginning to appear dull and lacking lustre, gold belt still present but appearing less bright, jade pendant less frequently worn or displayed, posture showing subtle forward lean or slumping as if bearing invisible weight, hands often resting passively or fidgeting with robe fabric, skin tone beginning to show dullness losing the pale radiance, expression increasingly vacant and distracted with eyes not fully focused on surroundings, plain dark background, mixed cool and warm lighting beginning to shift toward shadow, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名35岁中国男性显现权力疲劳和权力衰落迹象的全身定妆参考，面容结构依旧但眼神显出明显的疲惫和焦点散乱、眼周和嘴角出现疲惫纹理、深色短发开始显得略微凌乱，穿着同样的深蓝色官服但现在显出明显的皱褶和褶皱暗示对仪容的漠不关心、绣纹开始显得黯淡失去光泽、金色腰带仍在但显得不够明亮、玉佩较少佩戴或展示，身体姿态显出微妙的前倾或下沉仿佛在承受无形的重量、双手常常被动地搭放或在衣摆上无谓地转动，肤色开始显出暗沉失去苍白的光泽感，表情逐渐空洞和心不在焉眼神无法完全聚焦在周围事物，素色深色背景，混合的冷暖光开始向阴影转变，35mm胶片颗粒感，中高对比度
```

#### 6. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a 35-year-old Chinese man completely hollowed out by power loss and political marginalization, face showing same angular bone structure but now hollow and gaunt, eyes completely vacant and unfocused with milky dull iris replacing former penetrating gaze, subtle sagging of facial muscles, dark hair appearing disheveled and uncared for, wearing the deep blue official robe now visibly tattered and worn with prominent wrinkles and creases throughout, embroidery faded and tarnished showing no lustre, gold belt dull and corroded as if touched by verdigris, jade pendant completely absent or discarded, posture collapsed with shoulders sagging and body leaning forward or backward without control, hands hanging limply at sides or fidgeting weakly with torn fabric, skin tone sallow and grey showing complete loss of vitality and lustre, expression utterly blank and empty as if the soul has departed the body, eyes staring into nothing with no comprehension of surroundings, plain dark background, cold desaturated murky lighting draining all color and warmth from the frame, 35mm film grain, high contrast emphasizing gauntness and decay
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名35岁中国男性因权力完全丧失和政治边缘化而彻底虚空的全身定妆参考，面容骨骼结构依旧但现在显得凹陷和消瘦、眼神完全空洞和失焦曾经穿透的目光被乳白色混浊取代、面部肌肉微妙的下垂，深色短发显得蓬乱和无人打理，穿着深蓝色官服现在明显褴褛破损皱褶遍布衣身、绣纹褪色发暗完全失去光泽、金色腰带失去光泽并开始显出铜绿色的侵蚀、玉佩完全缺失或被丢弃，身体姿态完全坍塌肩膀下沉身体向前或向后倾斜失去控制、双手无力地垂于身侧或虚弱地在破衣上转动，肤色苍黄和灰白显示完全失去生命力和光泽感，表情彻底空白和虚空仿佛灵魂已离开身体、眼神呆滞地看向虚空无法理解周围发生的任何事，素色深色背景，冷色去饱和阴沉的光线吸干画面所有色彩和暖意，35mm胶片颗粒感，高对比度强调消瘦感和衰败感
```

### 吴启思 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese man in his late 60s, unruly grey-white hair with strands standing on end suggesting obsessive focus, high cheekbones with deeply etched wrinkles indicating decades of concentrated thinking, prominent clear intelligent eyes behind round-framed glasses with scratched lenses, direct penetrating gaze with sharpness and clarity despite advanced age, thin lips often pressed in contemplation, pale unhealthy skin tone from prolonged indoor laboratory work with age spots, wearing a worn faded beige cotton lab coat stained with chemical residue and ink marks, dark undershirt visible at collar, gaunt neck suggesting ascetic lifestyle dedicated to research, neutral composed expression mixed with hidden intensity, white neutral background, cool bright white laboratory lighting casting sharp shadows under cheekbones emphasizing scholarly intensity, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头中国男性的正面半身肖像，蓬乱杂乱的花白头发如同站起来般暗示执着的专注，高耸的颧骨有深刻的皱纹显示数十年专注思考的印记，圆框眼镜后的眼睛清亮有神有穿透力，直接锐利的目光即使年迈仍显年轻人的智慧，薄唇常处于沉思状态，因长期实验室室内工作而苍白不健康的肤色有老人斑，穿褪色磨损的米色棉布实验服上有化学试剂和墨迹痕迹，深色衬衫在领口处露出，瘦长的颈部暗示献身于研究的禁欲生活，表情中性沉着但隐含强烈的内在能量，白色中性背景，冷亮的实验室白色灯光在颧骨下投出锐利的阴影强调学者的内在强度，35mm胶片颗粒感，高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a Chinese man in his late 60s, unkempt grey-white hair, gaunt profile with prominent cheekbones and sharp jaw line, thin lips often pressed in concentration, large intelligent eyes visible even in three-quarter view showing depth and contemplation, high nose bridge, pale unhealthy complexion, wearing a worn beige lab coat with visible stains and chemical marks, thin frame suggesting years of neglecting physical health for intellectual pursuit, expression suggesting internal calculation and thought process, white neutral background, cool white laboratory-style lighting from camera-left creating rim lighting on the back of his head emphasizing the scholar's isolation and intensity, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头中国男性的四分之三侧面半身肖像，蓬乱的花白头发，瘦削的侧面轮廓高耸的颧骨和锐利的下颌线条，薄唇处于浓缩的状态，即使侧面仍可见大而聪慧的眼睛显示深度和沉思，高挺的鼻梁，苍白不健康的肤色，穿褪色磨损的米色实验服上有明显的染迹和化学痕迹，瘦削的身体框架显示多年为了智力追求而忽视身体健康，表情暗示内部计算和思考过程，白色中性背景，来自相机左侧的冷白实验室式灯光在头后部投出轮廓光强调学者的孤立感和强度，35mm胶片颗粒感，高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his late 60s as a reclusive researcher, unruly grey-white hair, gaunt concentrated expression, large intelligent eyes behind round glasses with scratched lenses showing years of use, pale unhealthy skin from years of indoor laboratory work, wearing a heavily stained and worn beige lab coat with ink marks, chemical residue stains, burn marks at the sleeves indicating direct contact with experimental equipment, dark cotton undershirt barely visible at neckline, old worn black sneakers, standing in a slight forward-leaning posture with arms relaxed at sides but fingers positioned in a gesturing state ready to demonstrate concepts, multiple pens and data cables visible in lab coat pocket, standing in profile or three-quarter view suggesting movement, plain dark background, cool bright white laboratory lighting from above and front creating sharp shadows emphasizing facial features and the worn texture of the lab coat, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名60岁出头中国男性隐世研究者全身定妆参考，蓬乱的花白头发，瘦削专注的表情，圆框眼镜后的大眼睛显示清晰智慧镜片磨损显示多年使用痕迹，因多年室内实验室工作而苍白不健康的肤色，穿磨损严重的米色实验服上有墨迹、化学试剂残留污迹、袖口处的烧伤痕迹显示与实验设备的直接接触，深色棉布衬衫几乎看不到只在颈口露出，旧磨损的黑色运动鞋，身体略微前倾站立双臂放松垂于身侧但手指处于随时可以做出解释性手势的准备状态，多支笔和数据线在实验服口袋中隐约可见，站立姿态为侧面或四分之三侧面暗示处于运动的研究者状态，素色深色背景，来自上方和前方的冷亮白色实验室灯光投出锐利的阴影强调面部特征和实验服的磨损纹理，35mm胶片颗粒感，高对比度
```

### 吴启思实验室 (locations, ★★★, P5)

#### 1. 提示词1：实验室全景 [实验室全景]

**English：**
```
Cinematic still, 2.39:1 widescreen, underground laboratory interior,
cold white LED lighting #F5F5F5, dark brown wooden door frame #2C1810,
medical monitoring equipment with deep blue indicator lights #3A4A6B,
digital humanoid lying supine on examination table, left arm with
nutrient IV tube, right chest with ECG leads, eyes open but vacant,
sterile scientific atmosphere, precise medical instruments surrounding,
high-end research facility aesthetic, cinematic depth of field,
professional medical photography style
```

**中文：**
```
电影质感画幅，2.39:1宽银幕，地下实验室内景，冷白色LED实验室灯光 #F5F5F5，
焦褐色木质门框 #2C1810，医疗监测设备暮蓝色指示灯 #3A4A6B，
数字人躺卧在检查台上，左臂营养液导管，右胸心电导线，
眼睛睁着但呆滞无光，无菌科学氛围，精密医疗仪器环绕，
高端研究设施美学，电影级景深，专业医学摄影风格
```

#### 2. 提示词2：灵魂觉醒特写 [灵魂觉醒特写]

**English：**
```
Cinematic close-up, 2.39:1 widescreen, humanoid face awakening moment,
eyes transitioning from vacant to conscious, slight breath mist on lips,
ECG lead attachments visible on chest, cold sterile lighting from above,
medical monitoring equipment blurred in background, deep blue LED glow,
profound moment of consciousness emergence, dramatic cinematic lighting,
shallow depth of field focusing on eyes, tension and wonder atmosphere
```

**中文：**
```
电影特写画面，2.39:1宽银幕，数字人脸部觉醒时刻，
眼睛从呆滞逐渐有了意识焦点，嘴角微弱呼气，
胸膛心电导线清晰可见，冷白无菌灯光从上方照下，
医疗监测设备虚化背景，暮蓝LED光晕，
意识苏醒的深刻时刻，戏剧化电影光线，
浅景深聚焦眼睛，紧张与奇迹的氛围
```

#### 3. 提示词3：设备细节与液体流动 [设备细节与液体流动]

**English：**
```
Cinematic macro shot, 2.39:1 widescreen, nutrient IV tube with liquid dripping,
close-up of medical apparatus connection, cold blue and white lighting,
sterile laboratory aesthetic, metal and plastic materials, precision medical
technology, scientific beauty composition, dramatic side lighting, shallow
depth of field, detail-focused cinematography, tension and precision atmosphere
```

**中文：**
```
电影微距镜头，2.39:1宽银幕，营养液导管液体滴入特写，
医疗装置连接口细节，冷蓝与冷白光线交织，
无菌实验室美学，金属与塑料材质质感，
精密医疗技术，科学美构图，戏剧化侧光照明，
浅景深，细节聚焦摄影学，紧张与精密的氛围
```

### 吴婶 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese woman in her 50s, curly permed short hair with grey highlights, warm smile with visible laugh lines on face, slightly plump but energetic appearance suggesting vitality and strength, round honest face with kind eyes, wearing comfortable cotton clothing in warm beige-brown tones (#8B7355 predominant) and a practical apron, standing in front of a plain dark background, realistic style with warmth and human kindness in expression, professional headshot, soft studio lighting with warm tone, emphasizing kind observant eyes and gentle demeanor, 80% realism with 20% subtle warmth suggesting inner light, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一位50多岁中国女性的正面半身肖像，花白烫卷短发，脸上笑纹明显、嘴角带着温暖微笑，体型微胖但精神矍铄显露活力和力量，圆润忠厚的面孔温和的眼神，身穿舒适的棉衣（以枯草黄#8B7355为主色调的暖调）和实用围裙。纯深色背景，画风以写实为主（80%写实+20%内在光辉的温暖感）。专业人物定妆照，柔和棚光暖调，突出其温暖敏锐的观察眼神与和善气质。35mm胶片颗粒感，中高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a Chinese woman in her 50s, curly permed short grey-white hair, warm smile with laugh lines, slightly plump sturdy build suggesting physical strength and resilience, standing with feet shoulder-width apart and natural posture, wearing comfortable faded beige-brown cotton clothes (#8B7355) with a practical apron, hands naturally at sides showing the marks of daily labor, honest kind expression with alert intelligent eyes, white neutral background, warm even front lighting emphasizing the healthy rosy complexion and warm demeanor, 80% realism with 20% subtle supernatural warmth suggesting inner strength, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一位50多岁中国女性的全身正面肖像，花白烫卷短发，脸上笑纹明显嘴角微笑温暖，体型微胖坚实暗示物理力量和韧性，双脚与肩同宽自然站立姿态，穿舒适的褪色枯草黄棕色棉衣（#8B7355为主色调）配实用围裙，双手自然垂于身侧显示日常劳作的痕迹，忠厚亲切的表情透出警觉的睿智眼神，白色中性背景，暖调均匀正面光强调健康的红润肤色和温暖气质。80%写实+20%超自然温暖风格强调内在力量，35mm胶片颗粒感，中高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, cozy scene by a natural spring in rural Chinese countryside, simple dwelling with a middle-aged woman with curly grey-white permed hair and warm smile tending to daily chores or welcoming a guest, micro-plump but energetic build, wearing comfortable cotton clothes in warm beige-brown tones (#8B7355) and a practical apron, soft natural daylight creating warm shadows, beige and brown color palette emphasizing rural comfort and home, spring water visible in background, signs of mysterious phenomenon beginning to appear - subtle supernatural elements in water reflection or mist, woman's observant expression showing early awareness of the unusual, 80% realism with 20% subtle fantasy atmosphere suggesting hidden mysteries, time period: traditional folk era, intimate and lived-in spaces full of care and detail, plain dark background, warm intimate lighting
```

**中文：**
```
电影感静帧，2.39:1宽银幕，乡间泉水旁的温暖场景。简朴的居所，吴婶（花白烫卷短发、笑纹明显、温暖微笑），微胖但精神矍铄的身影忙碌于日常家务或招待来客。身穿舒适的棉衣（以枯草黄#8B7355为主的温暖色调）和实用围裙。柔和的自然光创造温暖阴影，以枯草黄、褐色为主的温暖色调强调乡村舒适感和家的温度。泉水清晰可见，隐约显现异象迹象——水面反光或雾气中有超自然元素微妙呈现，女性表情中显示出对异常的早期察觉。80%写实+20%幻想氛围，暗示隐藏的神秘。民间时代背景，居家与生活感浓厚，素色深色背景，温暖亲切的光线
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, harsh journey through mountain passes and barren landscapes, a middle-aged woman with curly grey-white hair now barefoot and in tattered worn clothes, steadily pulling a rope tied around the waist of a confused elderly man behind her who follows with difficulty, steep rocky terrain, twilight or overcast moody lighting casting long shadows and creating drama, wind-swept worn appearance reflecting weeks of relentless hardship, clothing in faded greyish-brown tones torn and threadbare at knees and hems, feet bare and marked by the harsh terrain, yet her eyes remain resolute and forward-looking with unwavering determination, set jaw showing inner strength, in distance faint silhouettes of hope (settlement or figures ahead offering refuge), 80% realism with 20% supernatural emphasis on human resilience and spiritual fortitude, dramatic epic quality showing triumph of love and will over circumstance and physical limitation, plain dark background, cool dramatic lighting emphasizing struggle and transcendent spirit
```

**中文：**
```
电影感静帧，2.39:1宽银幕，穿越山脉与荒野的艰难逃亡场景。一位花白烫卷短发的中年妇女现已赤足、衣衫褴褛，坚定地牵着腰带，引领身后精神涣散、步履蹒跚地跟随的老年男子。陡峭的山石地形，夕阳或阴沉天光投射长影营造戏剧感。经历数周不懈逃亡的沧桑与疲惫写在容貌上，衣物褪为灰褐色调膝盖处和衣摆撕裂破烂，赤脚被崎岖地形标记，但眼神坚定向前目光不移充满不屈的决心，紧收的下颌显示内在力量。远方隐约可见希望的身影（定居点或前方提供庇护的人）。80%写实+20%超自然风格强调人的坚韧与精神力量。具有史诗感，表现爱的力量和意志战胜困难与体能极限的壮阔气象。素色深色背景，冷色戏剧光线强调困苦与超越精神的对比
```

### 和寻灵 (characters, ★★★, P5)

#### 1. 

**English：**
```
High-quality ancient-fantasy digital art. Pure energy divine spirit design. He Xunling, Supreme Deity governing the human realm.
Form: Colossal luminous energy entity with absolutely no concrete human body features, only vague humanoid silhouette dissolving into light.
Color: Composed of dark gold (#DAA520) and warm white (#FFF8DC) soft yet intense golden radiance, absolutely no pure white (#FFFFFF).
Optics: Omnidirectional 360-degree uniform golden light source, completely no shadows, gentle outward-expanding halo gradually fading into infinite void.
Texture: Pure energy form, non-corporeal, subtle light pulsation like heartbeat suggesting continuous cosmic force flow.
Details: Body may be surrounded by multiple halos, light symbols, or geometric patterns representing the weaving of universal law and power hierarchy.
Background: Celestial void, omnidirectional golden light filling the entire environment, creating dreamlike and transcendent atmosphere, background subdued to highlight subject.
Mood: Absolute authority, transcendent calm, eternal stability, awe-inspiring and inescapable presence.
Style: 80% realistic + 20% supernatural (can increase to 30-40% supernatural to emphasize divine non-corporeality).
Viewpoint: Front-facing overlooking or level perspective, emphasizing majestic and overwhelming presence with absolute power.
Special Effects: Light may have color spectrum edges (gold→yellow→warm-white) suggesting multidimensionality; light particle scattering increases energy feel.
```

**中文：**
```
高质量古幻艺术，纯能量神灵体设计。和寻灵，至高上神，掌管人界的神灵。
形态：巨大发光的能量体，完全没有具体的人类身体特征，只有模糊的人形轮廓消融于光中。
色彩：主色为暗金 (#DAA520) 与暖白 (#FFF8DC) 组成的柔和强烈的金色光芒，绝对禁用纯白 (#FFFFFF)。
光学：无方向的均匀360度金色光源，完全无阴影，柔和的向外扩散的光晕逐渐消散于虚空无限延伸。
质感：纯能量形态，非物质体，微妙的光脉动如心跳一般暗示宇宙力量的持续流动。
细节：周身可能环绕多重光环或光符号、几何图案，代表宇宙法则的编织与权力等级。
背景：虚空天界，无方向的金光洒满整个环境，显得梦幻而超越，背景应被压低突出主体。
气质：绝对权威、超然冷静、永恒稳固、令人敬畏而无可反抗。
风格：80% 写实 + 20% 超自然（可酌情提升至30-40% 超自然以强调神灵的非物质性）。
视角：正面俯视或平视，强调其宏大而压倒性的存在感与绝对权力。
特效：光可能有彩色光谱边缘（金→黄→暖白），暗示多维度；光粒子散射增加能量感。
```

#### 2. 

**English：**
```
High-quality ancient-fantasy digital art, supernatural optical design. Judgment dialogue scene between He Xunling and Song Xiaoxian.
He Xunling Form: Colossal pure energy luminous entity at 45-degree profile angle, light intensified and focused, suggesting direct power projection and absolute authority.
Color Scheme: Dark gold (#DAA520) as primary 60%, warm white (#FFF8DC) as highlights and halo 30%, deep gold (#B8860B) at power focus point 10%.
Optical Effect: Shadow-free uniform golden light as foundation, light concentrates into more focused beam when projecting power, deep gold intensified, creating strong visual suppression.
Song Xiaoxian Contrast: Diminished human form overwhelmed by He Xunling's colossal overwhelming luminescence, emphasizing absolute power disparity and inescapable destiny.
Spatial Composition: He Xunling dominates upper half and central focus of frame, Song Xiaoxian positioned below at edge, reinforcing divine hierarchy and absolute authority.
Background: Celestial void with omnidirectional golden light lines interwoven, visible energy undulation, creating interdimensional visual folding effect.
Interactive Visual: He Xunling's light may project downward forming beam pointing to Song Xiaoxian, hinting at sacred judgment and unidirectional energy flow.
Mood: Majesty combined with subtle acknowledgment of listening, but absolute authority never wavered, calm yet dignified.
Style: 80% realistic + 25-35% supernatural (emphasizing optics, multidimensional effects, and power projection visualization).
Viewpoint: 45-degree profile angle, emphasizing dialogue tension and absolute suppression between He Xunling and Song Xiaoxian.
Special Effects: Visible light ripples and energy pulsation; space may subtly distort due to light beams; Song Xiaoxian may be surrounded by light as if "baptized".
```

**中文：**
```
高质量古幻艺术，超自然光学设计。和寻灵与宋小仙的裁决对话场景。
和寻灵形态：巨大的纯能量发光体，侧面45度角显示，光芒聚焦强化，暗示权力的直接投射与绝对权威。
颜色方案：暗金 (#DAA520) 主体占60%，暖白 (#FFF8DC) 高亮与光晕占30%，深金 (#B8860B) 权力聚焦处占10%。
光学效果：无阴影的均匀金光为基础，权力投射时光芒聚集成更集中的束，深金色加强，形成强烈视觉压制。
宋小仙对比：渺小的人类形态被和寻灵的巨大压倒性光芒所笼罩，显示绝对的权力差异与命运的不可抗拒。
空间感：和寻灵占据画面的上半部分和中心焦点，宋小仙在下方边缘位置，强化上神的权力等级与绝对地位。
背景：天界虚空，无方向的金色光线交织成网，可见能量波动，产生超越维度的视觉折叠感。
互动视觉：和寻灵的光可能向下投射形成光束指向宋小仙，暗示神圣的裁决与能量的单向流动。
气质：威严中不失某种对倾听的微妙认可，但绝不动摇权力的绝对性，冷静而不失庄严。
风格：80% 写实 + 25-35% 超自然（侧重光学、多维效应与权力投射的视觉呈现）。
视角：侧面45度角，突出对话中和寻灵与宋小仙的权力张力与绝对压制感。
特效：可见光的波澜与能量脉动；空间可能因光束而微微扭曲；宋小仙周身可能被光所笼罩如"洗礼"。
```

#### 3. 

**English：**
```
Epic ancient-fantasy scene, absolute display of divine power. Divine Realm Judgment Scene, final arbitration of universal order.
Main Subject: He Xunling, Supreme Deity, manifests as a colossal luminous energy entity dominating the entire visual space absolutely and undeniably.
Color Tone: Sacred golden light composed of dark gold (#DAA520) and warm white (#FFF8DC), filling and overwhelming entire space, all other colors subdued.
Optical Character: Omnidirectional uniform light source, completely no shadows, rays expanding in all directions extending to infinity, creating "everything is in light" sensation.
Space Setting: Void-like celestial realm with no concrete terrain, architecture or material dimension, only the weaving of energy and light, transcending physical dimension.
Sacred Symbols: Abstract light symbols, geometric patterns or halos float in the air, representing the operation of universal law and hierarchy of power.
Power Display: Luminescence may concentrate into focused beam of force, color deepens to deep gold (#B8860B), manifesting absolute power release and projection.
Atmosphere: Solemn and majestic, transcending the mundane, brimming with absolute authority and inescapable destiny, awe-inspiring yet powerless.
Contrast Elements: May include minute human figures (such as Song Xiaoxian or other petitioners) to reinforce He Xunling's monumentality and suppressive absolute power.
Visual Focus: He Xunling positioned at center or highest point of frame, all light and attention converge upon its form, forming absolute visual center.
Special Effects: Luminescence may have subtle pulsation like heartbeat suggesting continuous cosmic force; light particle scattering effect possible; space may have energy undulation.
Other Elements: If Zhi Xundao appears, luminescence forms harmonious yet independent visual composition with He Xunling, power symmetry of dual stars.
Style: 80% realistic + 30-40% supernatural (emphasizing deity's non-corporeality, transcendence and absolute power display).
Composition: Monumental and symmetrical, emphasizing absolute authority and perfect balance and irreversibility of universal order.
Viewpoint: High-angle bird's eye view or panorama, emphasizing macro-level sense of order and absolute power suppression.
```

**中文：**
```
史诗级古幻场景，神灵权力的绝对展现。神界裁决场景，宇宙秩序的最终仲裁。
主体：和寻灵，至高上神，以巨大的能量光体形态显现，占据整个视觉空间的绝对主导，无可置疑。
色彩基调：暗金 (#DAA520) 与暖白 (#FFF8DC) 组成的神圣金光，填充并压倒整个空间，所有其他色彩都应被压低。
光学特性：无方向的均匀光源，完全无阴影，光线向四面八方扩散延伸至无限，创造"一切都在光中"的感觉。
空间设置：虚无的天界，没有具体的地形、建筑或物质维度，只有能量与光的织造，超越物理维度。
神圣符号：可见抽象的光符号、几何图案或光环在空中浮动，代表宇宙法则的运行与权力的等级制。
权力展示：光芒可能聚焦成集中的力量束，颜色加深至深金 (#B8860B)，表现权力的绝对释放与投射。
氛围：庄严肃穆、超越世俗、充满绝对权威感与宿命的压制，令人敬畏而无可奈何。
对比元素：可能包括渺小的人类身影（如宋小仙或其他请愿者），用于强化和寻灵的宏大与绝对权力的压制性。
视觉焦点：和寻灵位于画面中心或最高点，所有光线与注意力都汇聚汇集于其身，形成绝对的视觉中心。
特效：光芒可能有微妙的脉动如心跳，暗示持续的宇宙力量；可能有光粒子的散射效果；空间可能有能量波澜。
其他元素：智寻道若出现，光芒与和寻灵形成和谐但独立的视觉构图，双星的权力对称。
风格：80% 写实 + 30-40% 超自然（强调神灵的非物质性、超越性与权力的绝对展现）。
构图：宏大而对称，强调绝对权威与宇宙秩序的完美平衡与不可逆转。
视角：高角度俯视或全景，强调宏观的秩序感与绝对的权力压制。
```

### 城主府 (locations, ★★★, P5)

#### 1. 提示词 1 - 权力指挥中心 [权力指挥中心]

**English：**
```
Cinematic still, 2.39:1 widescreen, war room of a 700,000-strong fortress city's command center. A massive wooden conference table dominates the chamber, surrounded by military maps and defense schematics on the walls. A military commander stands over a detailed sand table showing city fortifications and enemy positions. Officers confer urgently in lamplight. Flags bearing city insignia hang from the vaulted ceiling. The atmosphere bristles with tension and decision-making. Color palette: burnt sienna #2C1810 for stone walls, dried grass yellow #8B7355 for wood furnishings, amber lamplight, deep shadows. Hyper-detailed period military architecture, cinematic war room atmosphere, volumetric smoke and intensity.
```

**中文：**
```
电影截图，2.39:1 宽幅，70万人口堡垒城市的指挥中心战争室。巨大的木质会议桌主导整个厅堂，四周墙面铺满军事地图与防御图纸。军事将领站在详细的沙盘前，展示城市防御与敌军位置。官员们在灯光下急促商议。城市纹章旗帜悬挂在拱形天花上。氛围充满张力与决策的紧急感。色彩：焦褐#2C1810（石墙），枯草黄#8B7355（木制家具），琥珀灯火，深邃阴影。超精细古代军事建筑，电影级战争室氛围，体积烟雾与强度。
```

#### 2. 提示词 2 - 办公权力与战争负担 [办公权力与战争负担]

**English：**
```
Cinematic still, 2.39:1 widescreen, interior of the city magistrate's office during wartime. A 52-year-old commander sits heavily at his wooden desk, surrounded by scrolls and military reports. Lamplight casts deep shadows across his weathered face, revealing exhaustion and burden. Maps and city administrative documents cover the walls. Windows reveal distant fortifications. The atmosphere is one of crushing responsibility and mounting pressure. Color palette: burnt sienna #2C1810 stonework, dried grass yellow #8B7355 wood, amber lamplight, deep midnight blue #3A4A6B in shadows. Hyper-detailed period office, cinematic portrait of burden, intricate period details and atmospheric tension.
```

**中文：**
```
电影截图，2.39:1 宽幅，战时城市市长办公室内景。52岁的指挥官沉重地坐在木制办公桌前，周围堆满军事奏折与报告。灯光在他风化的脸庞投出深邃阴影，显露疲惫与负担。墙面覆盖地图与城市行政文件。窗户显示远处的防御工事。气氛充满压倒性的责任与加重的压力。色彩：焦褐#2C1810（石墙），枯草黄#8B7355（木制），琥珀灯火，深午夜蓝#3A4A6B（阴影）。超精细古代办公室，电影级负担的肖像，精细的古代细节与氛围张力。
```

#### 3. 提示词 3 - 厨房的混乱与渗透 [厨房的混乱与渗透]

**English：**
```
Cinematic still, 2.39:1 widescreen, chaos and heat of the magistrate's residence kitchen during wartime preparations. Multiple large braziers blaze with intense flames. Servants bustle frantically, preparing vast quantities of food. Smoke rises thick and dark. In the shadows between the chaos, a cloaked figure moves silently, unnoticed—a threat hidden in plain sight. Preparation vats, stored provisions, and cooking implements surround the scene. The heat and noise create perfect cover for infiltration. Color palette: deep crimson #8B1A1A from firelight, dried grass yellow #8B7355, smoky grays, dark silhouettes. Hyper-detailed period kitchen, psychological thriller atmosphere, smoke and movement, cinematic danger.
```

**中文：**
```
电影截图，2.39:1 宽幅，战时市长府邸厨房的混乱与炽热。多个大灶火焰燃烧得炽烈。仆从们忙碌奔走，准备大量食物。浓重的烟雾升腾而起。混乱中的暗处，一个蒙面身影无声移动，未被察觉——威胁隐没于众目睽睽。食材准备盆、储存的供给、烹饪器具环绕四周。热度与噪音为渗透者创造完美掩护。色彩：灶火映出的深红#8B1A1A，枯草黄#8B7355，烟雾灰，黑色剪影。超精细古代厨房，心理惊悚氛围，烟雾与移动，电影级危险感。
```

#### 4. 提示词 4 - 权力崩溃与防线瓦解 [权力崩溃与防线瓦解]

**English：**
```
Cinematic still, 2.39:1 widescreen, the command center descends into chaos as the magistrate collapses. Officers shout conflicting orders. Lamplight flickers uncertainly. Maps and sand tables that moments ago guided victory now seem useless. Through the windows, watch fires on the distant city walls begin to dim. The double walls and 10-meter moat beyond seem suddenly vulnerable. A void of leadership spreads through the chamber like darkness. The city's fate pivots on this moment of failure. Color palette: burnt sienna #2C1810 fades to ashen gray, amber lamplight becomes sickly and unstable, deep blue #3A4A6B encroaches. Hyper-detailed period military structure, cinematic collapse and desperation, atmospheric disintegration.
```

**中文：**
```
电影截图，2.39:1 宽幅，当市长倒下时，指挥中心陷入混乱。官员们喊出相互矛盾的命令。灯火闪烁不定。刚才指引胜利的地图与沙盘如今显得无用。透过窗户，远方城墙上的烽火开始暗淡。双层城墙与10米宽的护城壕沟突然显得脆弱无比。权力真空如黑暗般在厅堂蔓延。城市的命运在这次失败的时刻转折。色彩：焦褐#2C1810褪为灰烬，琥珀灯火变得病态与不稳，深蓝#3A4A6B入侵。超精细古代军事结构，电影级崩溃与绝望，氛围瓦解。
```

### 天德城城墙 (locations, ★★★, P5)

#### 1. 提示词 1 - 平时戒备 [平时戒备]

**English：**
```
Cinematic still, 2.39:1 widescreen, overhead shot of ancient city walls surrounding a fortress town of 100,000 residents. Golden hour sunlight bathes weathered brick and clay ramparts. Watchtowers stand at regular intervals, torches unlit. Soldiers patrol in measured rhythm. Empty battlements await. Color palette: burnt sienna #2C1810 for bricks, twilight blue #3A4A6B accents, deep amber for distant torch brackets. Hyper-detailed medieval defensive architecture, cinematic lighting, volumetric atmosphere.
```

**中文：**
```
电影截图，2.39:1 宽幅，俯视古城城墙俯瞰，10万人口的堡垒城市四周。金色时刻日光洒满风化的砖块与夯土城墙。瞭望塔间隔有序，火盆未燃。士兵按规律巡逻。空荡的垛口等待。色彩：焦褐#2C1810（砖块），暮蓝#3A4A6B（阴影），深琥珀（远处火盆架）。超精细中世纪防御建筑，电影级光线，体积雾气。
```

#### 2. 提示词 2 - 战备与火焰 [战备与火焰]

**English：**
```
Cinematic still, 2.39:1 widescreen, night scene of fully-lit city walls engulfed in firelight. Every brazier burns bright, casting amber and orange flames across weathered stone. Archers silhouetted on watchtowers. Defenders gripping spears and shields in battle formation. Dark maroon flickers from fire #8B1A1A. Smoke rises into starlit sky. Intense military readiness. Hyper-detailed medieval fortification, dramatic chiaroscuro lighting, cinematic tension.
```

**中文：**
```
电影截图，2.39:1 宽幅，夜幕城墙全被火光吞没的场景。每个火盆都熊熊燃烧，琥珀与橙黄火焰洒遍风化石墙。弓箭手在瞭望塔顶剪影。防卫者持矛盾牌严阵以待。暗红#8B1A1A火光闪烁。烟雾升入星空。强烈军事备战感。超精细中世纪堡垒，戏剧性明暗对比，电影级张力。
```

#### 3. 提示词 3 - 攻城战突破 [攻城战突破]

**English：**
```
Cinematic still, 2.39:1 widescreen, chaos and destruction as enemy forces assault city gates. Massive wooden gates splinter under battering ram strikes. Arrows and spears fill the air in deadly salvo. Defenders desperately counterattack from ramparts. Fire blazes uncontrolled, spreading across battlements. Dark crimson smoke mingles with orange flames. Multiple explosions of impact. Thousands of soldiers engaged in brutal siege warfare. Hyper-detailed medieval combat, ultra-dramatic lighting, smoke and embers particles.
```

**中文：**
```
电影截图，2.39:1 宽幅，敌军突击城门时的混乱与破坏。巨大木质城门在攻城锤撞击下崩裂。箭矢与长枪满天飞舞。防卫者从城墙顶部绝望反击。火焰失控蔓延，烧燃城墙垛口。深红烟雾与橙黄火焰交织。多处撞击爆发。数千士兵陷入残酷攻城战。超精细中世纪战斗，超戏剧化光线，烟雾与飞灰粒子。
```

### 小小顶 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, close-up front-facing portrait of a 12-year-old Chinese boy with extreme fear expression.
Large round eyes with dilated pupils taking up most of the iris, pupils dark and dominant #000000, whites of eyes bloodshot red with visible tear membranes, eyebrows high and tense, forehead wrinkled, mouth slightly open trembling.
Round baby-fat face, pale complexion with slight reddening on cheeks from crying, dark tousled short hair.
Features show complete terror and helplessness, eyes searching for safety that cannot be found.
Wearing a torn dark blue-gray school uniform shirt with dust and dirt marks.
Muted color palette dominated by #2c3e50 (school uniform) and #d4a5a5 (pale skin), dusty brown #8B7355 in background.
Plain dark background. Film grain texture, hard lighting emphasizing facial contours and the intensity of fear.
Style: 85% realism, 15% expressionist distortion emphasizing emotional extremity.
No distracting elements, extreme close-up focus on the terror-stricken face.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名12岁中国男孩极度恐惧表情的近距特写。
大而圆的眼睛瞳孔放大占据虹膜大部分，瞳孔深黑#000000为主，眼白充血泛红能看到泪膜，眉毛高高上扬紧绷，额头皱纹密集，嘴巴微张颤抖。
圆脸有婴儿肥，肤色苍白但因哭泣脸颊微红，黑色蓬乱短发。
面部特征显示彻底的恐惧与无助，眼睛在寻求找不到的安全。
穿着破损的深蓝灰色校服上衣有灰尘和污垢痕迹。
色彩以#2c3e50（校服）和#d4a5a5（苍白肤色）为主，背景枯草黄#8B7355。
纯黑色背景。胶片颗粒纹理，硬光强调面部轮廓和恐惧的强度。
风格：85%写实，15%表现主义扭曲强调情感的极端。
无分散注意力的元素，极致特写聚焦在恐惧扭曲的脸。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view close-up portrait of a 12-year-old Chinese boy in profound grief.
Eyes downcast with abundant tears streaming down cheeks, lower eyelids swollen from prolonged crying, eyes partially closed, eye corners turned downward.
Expression shows deep loss and longing, lips pressed together or slightly parted trembling.
Small hands visible near face, possibly clasping together or touching face seeking comfort.
Dark tousled short hair framing face, complexion warm beige-brown with reddened nose and swollen eyes.
Wearing faded casual shirt suggesting temporary shelter or refugee clothing.
Tears reflect light creating a glistening effect on cheeks.
Color palette: muted warm browns #8B7355, pale skin #d4a5a5, dark grays #4a4a4a.
Plain dark background. Film grain texture, soft golden sidelight creating long shadows emphasizing solitude and sorrow.
Style: 85% realism, 20% soft impressionist blur for dreamlike grief quality.
Intimate composition with minimal environmental detail.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名12岁中国男孩深深悲伤的四分之三视角近距特写。
眼睛低垂，大量泪水从脸颊流下，下眼睑因长时间哭泣而浮肿，眼睛半闭，眼角下弯。
表情显示深深的失落与思念，嘴唇紧闭或微张颤抖。
小手在脸旁可见，可能紧握或触摸脸寻求安慰。
黑色蓬乱短发框住脸部，肤色暖棕色，鼻子发红眼周浮肿。
穿褪色便装衬衫暗示临时庇护所或难民衣物。
泪滴反射光线在脸颊产生闪烁的湿润效果。
色彩：暗沉暖棕色#8B7355，苍白肤色#d4a5a5，深灰#4a4a4a。
纯黑色背景。胶片颗粒纹理，柔和金色侧光投出长影强调孤独与悲伤。
风格：85%写实，20%柔和印象派模糊营造梦幻悲伤感。
亲密构图，最少的环境细节。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, close-up portrait of 12-year-old boy in sudden awakening shock.
Eyes snapped open wide with startled expression, pupils dilated, whites of eyes showing more than normal, eyebrows shot up.
Face showing momentary panic before conscious awareness returns, mouth open as if mid-gasp or cry.
Dark tousled hair disheveled from sleep, face flushed and glistening with sweat.
Body position suggesting he has just jolted upright in bed or seat.
Expression captures the millisecond between nightmare and reality - the terror is raw and unfiltered.
Muted color palette with sweat-glistened skin creating slight highlights.
Plain dark background. Film grain, dramatic lighting with sharp contrast emphasizing the shock state.
Style: 85% realism, 15% expressionist tension in facial muscles.
Composition focuses on the moment of terror-to-awareness transition.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，12岁男孩突然惊醒的近距特写。
眼睛倏然睁得很大惊恐表情，瞳孔扩大，眼白比正常状态显露更多，眉毛向上射起。
脸部显示短暂的惊恐在意识回归前，嘴巴张开如同吸气或尖叫中。
黑色蓬乱头发因睡眠而凌乱，脸部潮红、闪烁着汗液。
身体位置暗示他刚从床或座位上猛然坐起。
表情捕捉了噩梦与现实之间的毫秒——恐惧是原始而未被过滤的。
暗沉色彩配上汗液闪烁的肌肤产生细微的高光。
纯黑色背景。胶片颗粒，戏剧性光影与锐利对比强调惊骇状态。
风格：85%写实，15%表现主义面部肌肉紧张。
构图聚焦于恐惧到觉醒的过渡时刻。
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, medium shot of a small 12-year-old boy crouching behind his mother's back in emergency shelter.
Only his large frightened eyes visible above his mother's shoulder, peering out with extreme wariness, the rest of his face hidden.
Small trembling hands clutching desperately at mother's clothing, pulling the fabric with white-knuckled grip.
Mother's figure partially visible showing protective stance, shoulders slightly hunched shielding the child.
Boy wearing torn dusty dark blue school uniform, mother in worn neutral-colored clothing.
Color palette: muted grays #4a4a4a, dusty browns #8B7355, minimal highlights, desaturated.
Plain dark background emphasizing the isolation and fear. Dramatic lighting from single source creating stark shadows.
Film grain, slight tension in composition. Emotion: terror, complete dependency, seeking shelter in an unsafe world.
Style: 80% realism, 20% expressionist shadow work emphasizing danger and claustrophobia.
Composition: tight framing, the boy appearing impossibly small and vulnerable.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一个12岁的小男孩蜷缩躲在母亲身后临时庇护所中的中景。
只有他的大而惊恐的眼睛在母亲肩膀上方可见，带着极度的谨慎向外观察，脸的其余部分隐藏。
小手颤抖地绝望地抓住母亲衣物，用指节发白的力度拉扯衣料。
母亲身形部分可见显示保护性姿态，肩膀略微驼背护住孩子。
男孩穿着破烂满灰尘的深蓝校服，母亲穿着破旧中性色衣物。
色彩：暗沉灰色#4a4a4a、枯草黄#8B7355、最少高光、去饱和。
纯黑色背景强调孤立与恐惧。戏剧性光影来自单一光源投出硬影。
胶片颗粒，构图中的细微紧张。情感：恐惧、彻底的依赖、在危险世界中寻求庇护。
风格：80%写实，20%表现主义影子工作强调危险和幽闭感。
构图：紧凑框架，男孩显得难以想象地微小与脆弱。
```

### 智寻道 (characters, ★★★, P5)

#### 1. 

**English：**
```
A supreme divine deity of the Beast Realm, appearing as an ethereal humanoid figure
composed of flowing energy and divine light. The character has a dark blue (#3A4A6B)
luminous form with intricate lightning patterns crackling across the surface in
electric purple (#7B68EE). Faint golden accents (#DAA520) highlight areas of power.
Translucent dragon and qilin silhouettes hover around the figure in soft blue-white
light. The eyes glow with dark blue luminescence, suggesting ancient wisdom and
absolute authority. The entire figure radiates warm white (#FFF8DC) divine radiance.
Standing in a commanding pose with one hand raised, energy tendrils flowing from
fingertips. The atmosphere shows subtle space distortion around the figure, indicating
reality-bending power. Overall aesthetic is 80% realism with 70% supernatural elements,
inspired by Eastern mythology and cosmic divinity. The figure should convey supreme
authority and mystique without appearing threatening or chaotic. The energy flow appears
controlled and precise, not scattered or chaotic. Detailed, cinematic quality, cosmic
lighting, high resolution.
```

**中文：**
```
兽界至高神灵，呈现为流动的能量与神圣光芒构成的人形体态。主体为暗蓝色发光形态
（#3A4A6B），表面覆盖精致的闪电纹路，呈现电紫色（#7B68EE）。暗金色（#DAA520）
点缀权力区域。透明的龙与麒麟虚影在柔和蓝白色光芒中环绕。眼眸发出暗蓝色光芒，
暗示古老的智慧与绝对的权威。整个身体散发暖白色（#FFF8DC）的神圣光晕。呈现权
力展示姿态，单手抬起，能量从指尖流出。周围空间显示微妙的扭曲效果，暗示因果干
预的力量。整体美学为80%现实主义与70%超自然融合，灵感来自东方神话与宇宙神圣
性。应传达至高权威与神秘感，但不显得威胁或混乱。能量流动显得精准而非散乱。精
致、电影质感、宇宙光线、高分辨率。
```

#### 2. 

**English：**
```
The same divine Beast Realm deity in a contemplative, observing stance. The figure
stands vertically, shoulders relaxed but still commanding presence. The dark blue
luminescence (#3A4A6B) is more subdued and collected compared to the previous pose,
with lightning effects reduced to faint, occasional flickers. Golden accents (#DAA520)
are minimal, visible only on subtle ornamental patterns near the head and chest. The
primary dragon totem is visible as a ghostly outline surrounding the figure rather
than multiple vivid manifestations. Eyes glow softly, showing observation rather than
active power-wielding. Warm white radiance (#FFF8DC) creates a gentle halo rather
than intense light. The figure appears "approachable yet absolutely unapproachable" -
composed and reserved. Aura is contained within 200-300cm radius. The background
should be neutral, perhaps showing a hint of a divine realm or cosmic space. Aesthetic
is 80% realism with 50% supernatural, emphasizing the contemplative mood. Still-frame
composition, solemn atmosphere, professional quality, high resolution.
```

**中文：**
```
同一位兽界至高神灵处于沉思观察的姿态。身体垂直站立，肩膀放松但仍保持压迫力。
暗蓝色发光（#3A4A6B）相比之前更加收敛，闪电效果减少为微弱的偶尔闪烁。暗金色
点缀（#DAA520）最少化，仅在头部和胸口处显现细微纹饰。主龙图腾显现为环绕身体
的幽灵般轮廓，而非多个生动的虚影。眼眸柔和发光，显示观察而非主动展示能力。暖
白色光晕（#FFF8DC）形成温和的光环而非强烈光芒。整体显得"可接近却绝对不可冒
犯"，沉着而内敛。气场收敛在200-300cm范围内。背景应为中立，可略微显示神界或
宇宙空间的暗示。美学为80%现实主义与50%超自然融合，强调沉思的气氛。静帧构图、
庄严氛围、专业质感、高分辨率。
```

#### 3. 

**English：**
```
A grand divine negotiation chamber in the Heavenly Realm. The setting features towering
marble-like pillars with golden (#DAA520) celestial engravings running along their
surfaces. The floor is inlaid with intricate cosmic patterns, glowing softly in blues
and golds. The ceiling opens to reveal a cosmic vista with stars and distant nebulae.
Two supreme deities stand opposite each other - one (Zhi Xun Dao, Beast Realm deity)
manifests in dark blue luminescence with crackling lightning and ghostly dragon/qilin
silhouettes, while the other (He Xun Ling, Human Realm deity) radiates in warm golden
tones. Between them stands a third figure (Song Xiaoxian) - a human elevated to divine
status, wearing a fusion of human and celestial attire, looking somewhat overwhelmed yet
determined. The air between them shimmers with divine energy, and reality itself seems
to bend slightly. Golden light descends from above, illuminating the sacred moment. The
atmosphere is tense but orderly, suggesting cosmic law and divine judgment. Dark neutral
background behind the figures. Cinematic, detailed, atmospheric lighting, ethereal,
high-end concept art quality, 4K resolution.
```

**中文：**
```
神界宏大的谈判大厅场景。设定特色包括高耸的大理石般柱子，上面刻有黄金色（#DAA520）
天界纹饰。地面铺有精致的宇宙纹样，散发柔和的蓝金色光芒。天花板打开露出宇宙景象，
显示星辰与远处的星云。两位至高神灵对峙 - 一位（兽界神灵智寻道）以暗蓝色发光与闪
烁的闪电和幽灵般的龙麒麟虚影显现，另一位（人界神灵和寻灵）散发温暖的黄金色调。
两者之间站着第三位人物（宋小仙）- 一位被提升至神圣地位的人类，穿着人类与天界服
饰的融合风格，看起来既感到不安又坚定。他们之间的空气闪烁着神圣能量，现实本身似乎
微妙地弯曲。金色光线从上方降下，照亮这神圣的时刻。气氛紧张但有序，暗示宇宙法则与
神圣判决。人物背后为暗色中立背景。电影质感、细致、大气光线、缥缈、高端概念艺术质
量、4K分辨率。
```

### 曹元艺 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a middle-aged Asian spy posing as a refined city official named Li Honglong, age 35-45, square face with ordinary features softened by careful makeup showing warmth and accessibility, complexion warm tan brown (#B8956A) looking well-groomed and maintained, styled light brown hair with subtle highlights in professional style, small rounded eyes with clear bright irises appearing warm and trustworthy but containing hidden sharpness and observation intelligence, wearing impeccably tailored dark navy suit (#1C3A47) with crisp white shirt and subtle silk tie, wearing subtle gold watch (#D4AF37) and refined accessories suggesting authority, posture upright and confident with shoulders relaxed displaying power and control, expression warm and calculated with a careful polished smile maintaining emotional distance, white neutral background, soft professional front lighting with warm tone emphasizing the groomed tan skin, medium film grain, medium-high contrast creating the appearance of a high-ranking sophisticated official
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名35-45岁冒充精致城市官员李红龙的中年亚洲间谍的正面半身肖像，方脸五官普通但通过精心化妆被柔和处理显得温暖亲和，肤色精致棕色(#B8956A)显示悉心打理和保养，经过造型的浅棕色头发带细微挑染显示专业护理，圆形偏小的眼睛虹膜清亮呈现温暖可信但暗含锐利的观察智慧，穿着剪裁完美的深色海军蓝西装(#1C3A47)搭洁白衬衫和精致丝质领带，佩戴精致金色腕表(#D4AF37)和显示权力的优雅配饰，姿态挺立自信肩膀放松展示权力与掌控，面部表情温暖精心计算带着细致打磨的微笑保持情感距离，白色中性背景，柔和专业的暖调正面光强调修饰得当的棕色肤色，中等胶片颗粒感，中高对比度呈现高阶官员的精致形象
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a middle-aged Asian man named Cao Yuanyi, the true identity of the spy, age 35-45, square face with ordinary unmemorable features, complexion muted ochre-yellow (#8B7355) showing the wear and weathering of undercover operations, short dark brown hair in simple practical style with no special styling, small round eyes with black irises showing deep clarity and sharp vigilance containing hidden danger despite the forgettable appearance, subtle scar visible on the inside of left wrist, wearing simple grey or dark green jacket in neutral everyday clothing that blends into background, expression controlled and alert with minimal unnecessary emotion, posture slightly tensed with feet shoulder-width apart ready for quick movement, hands positioned for rapid action, white neutral background, cool-toned side lighting from camera-left creating dramatic shadows emphasizing the depth of the eyes and the tension beneath the surface, heavy film grain with desaturated colors creating a spy-thriller aesthetic, high contrast emphasizing the psychological intensity
```

**中文：**
```
电影感静帧，2.39:1宽银幕，间谍真实身份曹元艺的35-45岁中年亚洲男性的四分之三侧面半身肖像，方脸五官平凡易被遗忘，肤色枯草黄(#8B7355)显示长期卧底操作的消耗与风化，短暗棕色头发简洁实用无特殊打理，圆形偏小的黑色虹膜眼睛显出深邃清晰和尖锐的警觉尽管外貌易被遗忘但眼神透露隐藏的危险，左腕内侧可见淡色疤痕，穿简素的灰色或深绿色夹克中性日常服装易融入人群背景，表情受控且警觉最少化不必要的情感显露，姿态略显紧绷双脚与肩同宽准备快速行动，双手位置可随时爆发，白色中性背景，冷调的侧光从左侧营造戏剧性阴影强调眼神的深度和表面下的紧张，重胶片颗粒感配去饱和色彩营造谍报悬疑美学，高对比度强调心理强度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, intense confrontation scene showing Cao Yuanyi/Li Honglong during the moment of identity exposure (ch54-ch55), character caught between two identities in extreme danger, visual breakdown of psychological fragmentation: the refined Li Honglong appearance is visibly cracking — makeup smudged and streaked, suit disheveled with torn seams, the careful calculated smile replaced by cold lethal alertness, hair disheveled, one sleeve torn exposing muscular forearms with visible tension; his true nature as a trained spy fully exposed: eyes sharp and dangerous with predatory focus, body tense in tactical stance ready for action, one hand positioned for combat or escape, muscles coiled under torn clothing showing military training marks; background: dimly lit official office or dark shadowed alley, shadows dominating the composition; color palette: cold blue (#5A7D8C) and dark green (#2D5D3E) and muted purple (#5B3A6B) tones create noir atmosphere; stark dramatic overhead lighting casts severe shadows across the face emphasizing the psychological transition between two selves showing the cracks in the mask; film grain heavy, high contrast, desaturated and cold color temperature creating intense psychological pressure; composition uses split or mirrored imagery suggesting the dual nature and fragmentation of identity; extreme tension and danger and the moment of truth when deception ends
```

**中文：**
```
电影感静帧，2.39:1宽银幕，高度紧张的对峙场景展现曹元艺/李红龙在身份暴露的危急时刻(ch54-ch55)，角色被困在两个身份之间处于极端危险，心理碎片化的视觉呈现：精致的李红龙形象明显崩裂——化妆污迹模糊，西装凌乱有撕裂，精心计算的微笑被冷酷致命的警觉取代，头发凌乱，一只袖口撕裂露出紧绷的肌肉手臂；他作为训练有素间谍的真实本质完全暴露：眼神锐利危险含有掠食性的聚焦，身体进入战术姿态准备行动，一只手位置可随时发起战斗或逃脱，肌肉在撕裂衣物下蓄势显示军事训练痕迹；背景：昏暗的官方办公室或阴影重的黑暗小巷，阴影主导画面构图；色调：冷蓝(#5A7D8C)、深绿(#2D5D3E)和柔和紫色(#5B3A6B)营造黑色电影氛围；刺激的头顶戏剧性照明在面部投射严酷阴影强调两个自我间的心理转变显露面具的裂隙；重胶片颗粒感，高对比度，去饱和冷色温营造极端心理压力；构图使用分屏或镜像意象暗示双重身份和自我的碎片化；极端的紧张、危险和欺骗终结的真相大白时刻
```

### 朱围庸住处 (locations, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, inconspicuous traditional merchant residence interior, simple wooden furniture arranged for strategic meetings, dim oil lamp lighting creating pools of shadow, austere yet functional aesthetic, tea service and scattered documents on table, man in dark robes seated centrally, contemplative authority, muted color palette, shallow depth of field, tension beneath stillness, interior power center atmosphere.
```

**中文：**
```
电影镜头，2.39:1宽幅，不起眼的传统商人住宅内景，简洁木质家具布置为战略会议形式，昏暗油灯光线投出影子池，朴素而功能性美学，茶具与散落文件覆盖案台，深衣人物居中而坐，沉思的权威感，沉静色调，浅景深，静止下的张力，内部权力中枢氛围。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, intimate interior scene with two figures in tense discussion, sparse wooden room with close walls emphasizing claustrophobia, candlelight casting dramatic shadows across their faces, documents and maps scattered indicating strategic planning, muted earth tones and deep browns, oppressive atmosphere, high stakes conversation, detail-oriented lighting, cinematic tension.
```

**中文：**
```
电影镜头，2.39:1宽幅，两个身影在紧张讨论中的亲密内景，稀疏木质房间与近距离墙壁强化幽闭感，烛光投出戏剧性面部阴影，文件与地图散落暗示战略规划，沉静土褐与深褐色调，压抑氛围，高风险对话，细节照明，电影式张力。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, darkened courtyard enclosed by high walls, narrow passage between buildings, minimal moonlight creating silhouettes, texture of aged brick and weathered wood, sense of hidden escape route, mysterious shadows, cool gray and black tones, architectural geometry, atmospheric perspective, tension of secrecy.
```

**中文：**
```
电影镜头，2.39:1宽幅，被高墙围困的黑暗庭院，建筑间的狭窄通道，月光最小化投出剪影，陈旧砖石与风化木的纹理，隐蔽逃脱通道的感觉，神秘阴影，冷调灰黑色，建筑几何感，大气透视，秘密的张力。
```

### 江新成 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese man in his early 50s, short neatly groomed grey-white hair, deep-set dark eyes with sharp penetrating gaze radiating cold authority, arched eyebrows, high-bridged aquiline nose, thin lips set in a hard line, square jaw, pale complexion from lack of outdoor labor, wearing a deep red or dark teal official robe with embroidered insignia on chest, gold-trimmed collar and sleeves, official belt with jade pendant, posture rigid and imposing, neutral expression with no warmth, plain dark background, dramatic side lighting from camera-left emphasizing the severe bone structure and power radiating from the eyes, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50岁出头中国男性的正面半身肖像，花白短发梳理得体，深眼窝中的深色眼睛锐利如刀散发冷漠权威，高挺眉毛，高挺鼻梁呈鹰钩鼻，薄唇紧抿成硬直线，方脸，苍白肤色显示少见日光，穿深红或深青官袍胸前绣有官阶纹章，金色镶边领口和袖口，佩戴官带配玉佩，身体僵硬端正散发压迫感，面无表情毫无温度，素色深色背景，戏剧性左侧侧光强调严肃的骨骼结构和眼睛散发的权力感，35mm胶片颗粒感，高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a Chinese man in his early 50s with commanding official presence, short grey-white well-groomed hair, deep-set penetrating eyes, square stern face, tall stature 178-180cm with broad shoulders and composed military-like posture, wearing complete official robes in deep red or dark teal with full insignia on chest, ornate gold-trimmed collar and sleeves, wide official belt with symbols of authority, hands at sides with fingers slightly curled showing tension and readiness, standing with feet shoulder-width apart and spine perfectly straight, pale complexion and austere demeanor, plain dark background, warm even golden lighting across the body emphasizing the formal dignified silhouette, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50岁出头中国男性具有官员威严的全身正面肖像，花白短发梳理考究，深眼窝的深色眼睛锐利穿透，方脸严肃，高身材178-180cm宽肩膀呈军人般的端正姿态，穿深红或深青完整官袍胸前有完整的官阶纹章，华丽的金色镶边领口和袖口，宽大官带佩戴权力象征，双手自然垂于身侧手指微微蜷曲显示紧张和准备状态，双脚与肩同宽脊背完全笔直，苍白肤色和严肃气质，素色深色背景，温暖均匀的金色光线照亮身体强化正式尊贵的轮廓，35mm胶片颗粒感，中高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 50s as a powerful city mayor in his prime, sharp alert eyes scanning with authority, taut facial muscles showing command and decisiveness, dressed in pristine deep red official robes with ornate gold-embroidered dragon insignia on chest, traditional collar and sleeves trimmed in gold, wearing a wide official belt with jade pendant and decorative symbols, standing in a commanding stance with perfect posture and shoulders squared, within an official government hall with maps and strategic documents visible on tables behind him, pale aristocratic complexion, expression of complete control and cold authority, hands positioned to suggest active command, warm golden interior lighting emphasizing the formal power dynamic, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50岁出头中国男性作为权力巅峰时期城市市长的全身定妆参考，眼神警觉而带有权威的扫视，面部肌肉紧张显示掌控和果决，穿着崭新的深红官袍胸前绣有华丽的金色龙纹官阶纹章，传统的金色镶边领口和袖口，佩戴宽大的官带配玉佩和权力象征饰物，以掌控的姿态站立脊背完美笔直肩膀张开，身处官府大厅内背后可见战略地图和文件，贵族苍白肤色，完全掌控和冷漠权威的表情，双手位置暗示主动下达命令，温暖的金色室内光强化正式的权力动态，35mm胶片颗粒感，高对比度
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body costume reference of a Chinese man in his early 50s now possessed and hollowed out, same official robes but worn unnaturally — sleeves pulled too tight, belt fastened wrong, fabric crumpled in odd places, eyes wide and vacant with unfocused pupils and slightly milky white appearance, mouth hanging slightly open with slack jaw, head tilted at unnatural angle, neck muscles visibly tense and contorted, body posture awkward and disjointed as if limbs are being puppeteered, hands held at strange angles with fingers unnaturally splayed or clenched, facial muscles completely slack creating a mask-like expression, sickly pallid skin, standing in dim government hall with cold desaturated blue-grey lighting casting harsh shadows, eerie unnatural quality to every pose and gesture, 35mm film grain, high contrast emphasizing the disturbing wrongness
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50岁出头中国男性被占领后空洞化的全身定妆参考，穿着同样的官袍但穿着不当——袖子拉得过紧、腰带系错位置、布料在奇怪的地方皱起，眼睛睁大空洞的瞳孔失去焦点略显乳白色浑浊，嘴巴微微张开下颌松弛，头部倾向不自然的角度，颈部肌肉明显紧张扭曲，身体姿态尴尬不协调好像四肢被木偶线操控，双手持奇异角度手指不自然地张开或紧握，面部肌肉完全松弛呈现面具般的表情，病态苍白的皮肤，站立在昏暗的官府大厅内被冷色去饱和的蓝灰光强烈投射形成刺眼阴影，每个姿态和手势都散发诡异的非人质感，35mm胶片颗粒感，高对比度强调令人不安的违和感
```

### 泡泡 (props, ★★★, P5)

#### 1. 提示词组 1 - 泡泡创生过程 [泡泡创生过程]

**English：**
```
Cinematic still, 2.39:1 widescreen. A massive translucent sphere materializes from divine breath, expanding outward with prismatic iridescence. Surface shimmers with soft rainbow gradients (violet, blue, green, yellow, orange) flowing across its curved membrane. Core radiates with ethereal golden luminescence (#DAA520), creating delicate flowing patterns within the semi-transparent sphere. Pure white (#F5F5DC) and cornsilk (#FFF8DC) color palette dominates. The bubble contains wisps of divine mist swirling gently. Background fades to warm celestial glow. Supernatural luminosity, heavenly realm atmosphere, high-intensity divine aura.
```

**中文：**
```
电影级静帧，2.39:1超宽屏。一枚巨大的半透明球体从神圣呼吸中凝聚而出，向外扩张。表面呈现柔和的彩虹色渐变（紫、蓝、绿、黄、橙）流动于曲面。核心散发缥缈的金色荧光（#DAA520），在半透明膜质内形成细微流纹。纯白色（#F5F5DC）与玉米绸黄（#FFF8DC）主导色调。泡泡内轻雾缓缓旋动。背景呈暖色天界光晕。超自然高亮度，天界仙境氛围，元神显现强度。
```

#### 2. 提示词组 2 - 泡泡包裹目标 [泡泡包裹目标]

**English：**
```
Cinematic still, 2.39:1 widescreen. A colossal divine bubble envelops a massive armored warrior and enormous beast within its shimmering membrane. The sphere's surface refracts light into perfect rainbow patterns. Interior slightly hazy with divine energy wisps. The enclosed figures distorted slightly by the curved surface. Membrane surface glows with soft luminescence, showing cracks of brilliant white light. Golden ethereal threads (#DAA520) pulse through the sphere like divine veins. Cornsilk highlights (#FFF8DC) outline the form. Supernatural intensity, heavenly realm effect, magical enclosure aesthetic, cinematic lighting.
```

**中文：**
```
电影级静帧，2.39:1超宽屏。一枚巨大的神圣泡泡包裹着装甲骑士与庞大灵兽。球体表面完美折射彩虹色光线。内部充满神圣灵气雾气，被困身影因弧形膜质而略显扭曲。膜质散发柔和荧光，闪烁白色裂纹光芒。金色幽灵纹线（#DAA520）如神圣血管般脉动其中。玉米绸黄（#FFF8DC）勾勒轮廓。超自然高强度，天界元神显现，魔法囚禁感，电影级光影。
```

#### 3. 提示词组 3 - 泡泡破裂瞬间 [泡泡破裂瞬间]

**English：**
```
Cinematic still, 2.39:1 widescreen. A massive bubble ruptures violently, white light exploding outward. Cracks radiate from the puncture point with brilliant luminescence. Golden divine energy (#DAA520) explosively disperses as shimmering mist. Fragments of ethereal membrane scattered throughout. Cornsilk light (#FFF8DC) pulses from the rupture. Supernatural energy wave radiating outward. Chaotic, dramatic moment captured mid-destruction. Heavenly realm visual effects, ultra high luminosity, explosive supernatural power display.
```

**中文：**
```
电影级静帧，2.39:1超宽屏。巨大泡泡剧烈破裂，白光炸裂向外。裂纹从刺穿点放射，闪耀夺目。金色神圣灵气（#DAA520）爆炸性散开成闪烁雾气。破碎的缥缈膜质碎片四散。玉米绸黄（#FFF8DC）从破口脉冲。超自然能量波向外扩散。捕捉破裂的剧烈瞬间。天界视效，超高亮度，爆炸性超自然力量呈现。
```

### 温伯封 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a distinguished 60+ year-old Chinese businessman with sharp penetrating gaze and composed authoritative expression. He has sleek white or salt-and-pepper hair combed back, small deep-set eyes with bright intelligent irises showing wisdom and subtle menace, high prominent cheekbones, sharp jawline with tightly closed lips, deeply lined face showing the weight of power and scheming, lean muscular neck visible above a fine silk robe or tailored western suit in dark sophisticated colors. One hand rests on an ornate wooden cane suggesting both age and authority. His skin shows the pallor of indoor commercial life — not weathered but meticulously maintained. Set against a plain dark background. Soft front lighting emphasizing the penetrating gaze. Professional headshot style, radiating intelligence, power, and calculated ruthlessness. 35mm film quality, medium-high contrast.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一位60多岁尊贵的华人商业巨头的正面半身肖像，眼神锐利穿透有威权的平静表情。花白或黑白参杂头发向后梳贴，小而深陷的眼睛虹膜明亮智慧闪现细微的威胁感，高耸颧骨，锐利下颌线紧闭嘴唇，面容深刻显示权力与权谋的重量。瘦削有力的颈部露在精致丝绸长袍或裁剪得体的深色西装之上。一只手轻轻搭在精致木制拐杖上既暗示年龄也象征权力。皮肤呈现室内商业生活的苍白——不粗糙但精心维护。纯暗色背景。柔和正面光强调穿透的眼神。专业肖像风格，散发智慧、权力和有计算的冷酷。35mm胶片质感，中高对比度。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a distinguished 60+ year-old Chinese businessman, sharp profile view emphasizing the high cheekbones and sharp jawline, white or salt-and-pepper hair combed neatly, intelligent penetrating eyes gazing into distance as if assessing power dynamics, thin lips tightly closed in a composed expression, lean neck emerging from fine dark silk robe or tailored suit, one hand raised near chin in a contemplative gesture suggesting scheming, ornate cane visible at the frame edge, dark sophisticated color palette, plain dark background, warm side lighting from left emphasizing the sharp facial features and power-laden expression, 35mm film grain, medium-high contrast.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一位60多岁尊贵的华人商业巨头的四分之三侧面半身肖像，锐利的侧面轮廓强调高耸颧骨和锐利下颌线，花白或黑白参杂头发整齐梳理，智慧穿透的眼神望向远方如同在评估权力格局，薄唇紧闭呈沉着表情，瘦削颈部露在精致深色丝绸长袍或裁剪得体西装之上，一只手抬至下巴处呈沉思姿态暗示权谋思考，精致拐杖的尖端可见于画框边缘，深色高贵配色，素色深色背景，左侧暖色侧光强调锐利面部轮廓和充满权力的表情，35mm胶片颗粒感，中高对比度。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a distinguished 60+ year-old Chinese businessman in commanding posture, standing upright with shoulders back and chest forward, white or salt-and-pepper hair neatly combed, sharp penetrating gaze looking directly forward, high cheekbones and sharp jawline, wearing an elegant dark silk robe or perfectly tailored western suit in sophisticated earth tones (#8B7355), one hand resting on an ornate wooden cane, the other hand at his side or making a subtle dismissive gesture, lean muscular physique visible, expensive shoes completing the ensemble, plain dark background, warm even lighting emphasizing the power and refinement, 35mm film grain, medium-high contrast, radiating absolute control and decades of accumulated wealth and influence.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一位60多岁尊贵的华人商业巨头的全身正面肖像，挺立站姿肩膀向后挺胸，花白或黑白参杂头发整齐梳理，锐利穿透的眼神直视前方，高耸颧骨和锐利下颌线，穿着优雅深色丝绸长袍或完美裁剪的西装呈高贵大地色调（#8B7355），一只手轻搭在精致木制拐杖上另一只手自然垂于身侧或做出细微的挥手姿态，瘦削有力的体型清晰可见，昂贵皮鞋完成整体形象，素色深色背景，暖调均匀光强调权力与精致，35mm胶片颗粒感，中高对比度，散发绝对的控制力和数十年积累的财富与影响力。
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, interior scene of an upscale boardroom or banquet hall. A distinguished 60+ year-old Chinese businessman stands or sits at the head of an antique-laden table, surrounded by ancient artifacts, fine furniture, and candlelit ambiance. He wears an elegant dark silk robe or tailored western suit in warm earth tones (#8B7355). His expression is composed and authoritative with sharp penetrating eyes commanding respect. One hand rests on an ornate cane, the other gestures with controlled authority. Behind him, symbols of wealth and power — scrolls, ceramics, bronze vessels. The lighting is warm and golden, suggesting commercial prosperity and refined taste. The background shows signs of meticulous interior design reflecting decades of accumulated wealth. His posture is perfectly upright. The mood is one of quiet dominance and controlled power. Around him other business figures show subtle signs of deference.
```

**中文：**
```
【场景：高档董事会或宴会厅】电影感静帧，2.39:1宽银幕，一位60多岁的尊贵华人商业巨头站立或坐在堆满古董的长桌首座，四周环绕古代艺术品、精美家具、烛火照明。穿着优雅深色丝绸长袍或裁剪得体的西装呈暖调大地色（#8B7355）。表情沉着威权眼神锐利令人敬畏，一只手轻握精致拐杖另一只手做出控制有度的权力手势。身后是财富权力的象征——书卷、瓷器、青铜器。光线温暖金色暗示商业繁荣和品味雅致。背景显示精心设计的室内装潢体现数十年的财富积累。姿态完全挺立。氛围是无言的主宰和掌控的权力。周围商人显示细微的尊敬信号。
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, interior of the same boardroom or office, but now vacant and eerie. The same businessman stands in the same location, still upright and still wearing the same fine suit and holding the cane, but his expression is completely vacant and lifeless. His eyes are glassy and unfocused, pupils dilated and empty of intelligence. His face is blank and emotionless showing no sign of the previous authority or cunning. His movements are stiff and mechanical — the way he holds the cane shows no grace, just function. The luxurious surroundings remain unchanged, but he stands among them like a puppet among his own possessions. The lighting is cold and desaturated with dark purples and grays (#5B3A6B) replacing the warm gold. The mood is deeply eerie and tragic — a powerful man reduced to an empty walking shell. His body remains but his essence has been consumed.
```

**中文：**
```
【场景：同一高档董事会/办公室，但气氛诡异空洞】电影感静帧，2.39:1宽银幕，同一位商业巨头站在同一位置，仍然挺立仍然穿着精致西装手握拐杖，但表情彻底空洞无神。眼睛呈玻璃状失焦瞳孔散大没有智慧的光芒。面部空白冷漠完全看不到之前的权力或狡诈。动作生硬机械——他握拐杖的方式没有优雅只有机械功能。奢华陈设保持不变，但他站在自己的产业中像一具傀儡。光线冷色去饱和深紫和灰色（#5B3A6B）取代了温暖的金色。氛围诡异悲剧——曾经强大的权力者沦为空壳行尸走肉。身体仍在但灵魂已被吞噬。
```

### 温伯封府邸 (locations, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, traditional East Asian manor estate entrance, ornate wooden gates with brass fixtures, stone-paved courtyard with guards in formation, soft golden afternoon light casting long shadows across red-painted doors, wealthy merchant family residence, meticulous landscape design, dusty courtyard atmosphere, historical architecture, subtle power and control aesthetic, shallow depth of field, warm color grading.
```

**中文：**
```
电影镜头，2.39:1宽幅，传统东亚庄园府邸大门，精美木质大门配黄铜装饰，石板铺装院落，守卫列队肃立，金色午间光线投出长影横跨红漆大门，富商家族宅邸，精心设计的园林景观，院落尘埃飘浮感，历史建筑风格，微妙的权力与控制美学，浅景深，暖调色彩分级。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, traditional Asian dining hall interior, ornate wooden furniture and carved details, soft candlelight and oil lamps creating dramatic shadows, two figures in tense confrontation across a laden table, rich dishes and wine vessels, amber and deep brown color palette, oppressive intimate atmosphere, high tension moment, classical architecture, detail-rich textures, cinematic depth.
```

**中文：**
```
电影镜头，2.39:1宽幅，传统东亚饭厅内景，精美木质家具与雕刻细节，烛火与油灯投出戏剧性阴影，两个身影隔着装满菜肴的案台紧张对峙，精致食物与酒盏，琥珀与深褐色调，压抑的亲密感与高度紧张，古典建筑风格，纹理丰富，电影感深度。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, traditional manor courtyard garden, wooden pavilion with latticed windows, mature trees casting filtered dappled light, stone pathway and garden elements, servants moving in background, peaceful yet watchful atmosphere, warm brown and golden tones, shallow depth of field, subtle unease beneath tranquility, architectural elegance, afternoon light quality.
```

**中文：**
```
电影镜头，2.39:1宽幅，传统府邸后花园，木制亭台与格子窗，成熟树木投出斑驳光影，石板小径与园林元素，仆人在背景移动，宁静却警惕的氛围，温暖的褐色与金色调，浅景深，平静下暗含不安，建筑优雅感，午间光质。
```

### 灵闽 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a divine beast named Lingmin of the Ling clan.
Upper body frontal view showcasing Lingmin's characteristic gentle and soft features in stark contrast to his massive scale.
Pure white long fur #F5F5F5, smooth and well-groomed with luxurious fluffy texture, approximately 20cm length, glowing with inner warmth under natural light.
Pure black hairless face #1A1A1A with gentle, curious, slightly shy expression.
Warm and trusting eyes filled with wisdom and understanding, conveying kindness without threat.
Soft, graceful body lines that communicate approachability and tenderness despite the 5-6 meter massive stature.
No aggressive elements — only innocence, intelligence and compassion in the gaze.
Cinematic color grading with warm golden tones and soft film grain, emphasizing the divine yet intimate quality.
Natural directional lighting from above-left, creating luminous highlights on white fur while maintaining the purity of the black face.
Muted earthy background tones with hints of deep green suggesting mountain or forest habitat.
Aspect ratio 2.39:1 widescreen format, emphasizing the scale and presence while maintaining gentleness through composition.
Medium-high contrast, photorealistic with subtle supernatural luminosity.
Clear visual contrast to brother Lingyu's wildness — where Lingyu is fierce, Lingmin is serene.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，灵族神兽灵闽的正面半身肖像。
正面半身视角，展现灵闽特有的温柔与柔和特征，与其巨大的体量形成对比。
纯白长毛 #F5F5F5，光滑顺畅，蓬松柔软的质感，约20厘米长度，在自然光下呈现温暖光泽。
纯黑无毛面部 #1A1A1A，温柔好奇、略带羞怯的表情。
温和信任的眼眸充满智慧与理解，传达善良而非威胁。
柔和优雅的身体线条传达易接近与温柔，与5-6米的巨大身躯形成对比。
无任何侵略性元素——表情中只有纯真、智慧与同情。
电影级色彩分级，暖金色调，柔和胶片颗粒，强调神圣与亲密的矛盾统一。
自然方向光来自左上方，在白毛上产生发光高光，同时维持黑脸的纯净。
柔和的土褐色背景，深绿色暗示山地或森林栖息地。
宽屏 2.39:1 aspect ratio，强调体量与存在感同时通过构图维持温和气质。
中高对比度，摄影写实风格配合细微的超自然发光。
与兄长灵尤的凶悍形成清晰视觉对比——灵尤暴戾则灵闽温和。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body frontal portrait of Lingmin, a divine beast of the Ling clan.
Standing upright with subtle body lean suggesting approachability and gentleness, feet planted shoulder-width apart.
Massive 5-6 meter tall figure but with soft, graceful proportions and welcoming posture contrasting typical threatening giant stereotypes.
Pure white long fur #F5F5F5 covering entire body, approximately 20cm in length, smooth and flowing with a gentle luminous quality.
Pure black hairless face #1A1A1A with warm, kind, slightly shy expression and clear intelligent gaze.
Front limbs positioned in non-threatening stance, suggesting readiness to help and protect rather than dominate.
Rear legs planted firmly and confidently, conveying quiet strength and stability without aggression.
Overall silhouette: gentle giant, sacred yet deeply approachable, strength tempered by compassion.
Cinematic lighting from above with warm golden tones, causing the white fur to luminously glow while maintaining the purity and mystery of the black face.
Muted color palette: soft earth tones, deep forest greens, warm light, creating a nature-harmony atmosphere.
No darkened tones or shadows that would suggest danger — lighting is consistently warm and inviting.
Film grain texture throughout, soft focus depth of field isolating Lingmin from background.
Plain dark background, keeping focus entirely on the character's form and spirit.
Aspect ratio 2.39:1 widescreen, allowing the full scale of the divine beast to be appreciated while emphasizing gentle presence.
High production value, cinematic quality, sense of hope and warmth radiating from the figure.
Expression should convey: wisdom, kindness, trust, and an openness to genuine connection across species boundaries.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，灵族神兽灵闽的全身正面肖像。
挺立姿态，身体微微倾斜表示易接近与温柔，双脚与肩同宽站立。
巨大的5-6米身躯但线条柔和优雅，姿态开放友善，打破传统威胁性巨人刻板印象。
纯白长毛 #F5F5F5 覆盖全身，约20厘米长度，光滑流畅，呈现温暖发光质感。
纯黑无毛面部 #1A1A1A，温和善良、略带羞怯的表情，眼神清澈聪慧。
前肢处于非威胁姿态，暗示准备帮助与保护而非支配的意愿。
后肢稳固自信地植入地面，传达静默力量与稳定性但不显侵略性。
整体轮廓：温和的巨人，既神圣又极易接近，力量被同情所温柔化。
电影级上方光线呈暖金色调，使白毛发出光芒般的光泽，同时维持黑脸的纯净与神秘。
柔和色彩调色板：柔软的土褐色、深森林绿、温暖光线，营造人与自然和谐的氛围。
无暗沉或阴影色调暗示危险——光线始终温暖邀请。
整体呈现胶片颗粒质感，柔和焦点深度从背景中隔离出灵闽。
素色深色背景，将焦点完全集中在角色的形体与精神上。
宽屏 2.39:1 aspect ratio，允许欣赏神兽的完整体量同时强调温和的存在。
高制作价值，电影质感，希望与温暖从人物身上辐射而出。
表情应该传达：智慧、善良、信任、以及跨越物种边界进行真诚连接的开放性。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, intimate scene showing the connection between Lingmin, a massive white divine beast, and Zhu Weiyong in a transformative moment of trust and understanding.
Foreground: Lingmin's enormous white-furred form #F5F5F5 with pure black face #1A1A1A, positioned with gentle body language suggesting non-threat and approachability.
Lingmin's eyes conveying warmth, intelligence, and compassion — this is the visual heart of the scene.
Zhu Weiyong positioned in relation to Lingmin, their shared space demonstrating the breakdown of predator-prey boundaries.
Lighting: Warm golden light suggesting hope and transformation, creating luminous highlights on Lingmin's white fur while maintaining the mystique of the black face.
Background: Transitional environment — elements of confinement shifting toward natural landscape, symbolizing the movement from captivity toward freedom.
Color palette: Warm golds and ambers in foreground dominated by Lingmin, cooler grays and muted greens in background, creating emotional contrast.
Atmosphere: Breakthrough moment — fear transforming into hope, trust being established in real time, two beings transcending their natural roles.
Film grain quality throughout, cinematic composition emphasizing the emotional rather than physical dominance.
Aspect ratio 2.39:1 maintaining the sense of scale while centering on the profound connection between two beings.
High production value, emotional resonance of hope, redemption, and the possibility of understanding across species boundaries.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，展现灵闽与朱围庸在信任与理解的转变性时刻中建立连接的场景。
前景：灵闽的巨大白色毛发身躯 #F5F5F5 配纯黑面部 #1A1A1A，姿态温柔友善暗示非威胁性与易接近。
灵闽的眼眸传达温暖、聪慧与同情——这是场景的视觉中心。
朱围庸与灵闽相互关联的位置，他们共享的空间展现捕食者与猎物界限的消解。
光线：温暖的金色光暗示希望与转变，在灵闽白毛上产生发光高光同时维持黑脸的神秘感。
背景：过渡性环境——囚禁的元素逐渐转向自然景观，象征从束缚向自由的运动。
色彩：前景以灵闽为主的暖金色与琥珀色，背景冷灰色与柔和绿色，产生情绪对比。
氛围：突破时刻——恐惧转化为希望，信任在实时建立，两个生物超越自然角色。
整体胶片颗粒质感，电影构图强调情绪而非物理力量的统治。
宽屏 2.39:1 维持体量感同时聚焦于两个生物间的深刻连接。
高制作价值，希望、救赎与跨越物种理解可能性的情绪共鸣。
```

### 灵魂收集容器 (props, ★★★, P5)

#### 1. 提示词组 1：容器外观与静止状态 [容器外观与静止状态]

**English：**
```
Cinematic still, 2.39:1 widescreen, close-up of an ancient supernatural soul collection container held in steady hands, dark purple-black metallic material with rough natural texture, spherical form slightly smaller than closed fists, semi-translucent interior revealing faintly flickering blue-violet spiritual essences, mystical cold aura with ethereal mist surrounding the artifact, soft purple luminescence glowing from within, ornate ceremonial design, desaturated color grading, cinematic lighting with subtle rim light, mystical atmosphere, hyper-detailed texture, professional fantasy concept art.
```

**中文：**
```
电影截图，2.39:1 宽屏，超特写镜头，古老的超自然灵魂收集容器被稳稳握在双手中，暗紫色黑色金属材质，粗糙天然纹理，球形外形略小于双拳合握大小，半透明内部呈现微弱闪烁的蓝紫色灵魂光芒，神秘寒冷气息，周围缭绕着虚幻雾气，容器内部散发柔和紫色发光，神圣仪式设计，去饱和色调处理，电影级光影与微妙的边缘光，神秘压抑的氛围，超细节质感纹理，专业级奇幻概念艺术。
```

#### 2. 提示词组 2：战斗中的高强度闪烁状态 [战斗中的高强度闪烁状态]

**English：**
```
Cinematic still, 2.39:1 widescreen, dynamic shot of soul collection container rapidly flickering with intense blue-violet light, held by a ceremonial guard in dark robes, container overflowing with dozens of brilliant spiritual essences creating chaotic luminescent patterns, pulsing energy waves emanating outward, mystical purple glow filling entire frame, battle aftermath ambiance, cold supernatural energy, intricate light refractions within semi-transparent vessel, war casualties evident in the multiplying soul lights, ominous and awe-inspiring atmosphere, professional military fantasy, cinematic depth of field, dramatic high-contrast lighting.
```

**中文：**
```
电影截图，2.39:1 宽屏，动感场景，灵魂收集容器内蓝紫光芒密集闪烁不停，由身穿深色长袍的庄严守卫紧紧握持，容器内数十个璀璨的灵魂光点形成混乱的发光图案，脉冲能量波向外扩散，蓝紫色神秘光芒充满整个画面，战斗余烬的氛围，冷冷的超自然能量，半透明器皿内复杂的光线折射，阵亡士兵的灵魂在增加的光点中显现，压抑而令人敬畏的氛围，专业级军事奇幻风格，电影景深效果，戏剧性的高对比光影。
```

### 皇宫 (locations, ★★★, P5)

#### 1. 提示词1：朝会厅权力对峙 [朝会厅权力对峙]

**English：**
```
Cinematic wide shot, 2.39:1 widescreen, grand imperial throne room interior,
emperor seated on golden throne at center-top, officials arranged in hierarchical
rows below, dark gold pillars #DAA520 supporting vaulted ceiling, deep red walls
#8B1A1A, theatrical lighting from above creating dramatic shadows beneath figures,
brown wooden beams #2C1810, marble or polished wood flooring, astronomical ceiling
frescoes, atmosphere of authority and political intrigue, cinematic composition
emphasizing power dynamics and vertical hierarchy
```

**中文：**
```
电影宽景镜头，2.39:1宽银幕，宏大帝国朝会厅内景，
皇帝坐于金色龙椅中央高位，文武百官按等级序列排列，
暗金色 #DAA520 宫殿柱支撑穹顶，暗红色 #8B1A1A 宫墙，
从上方戏剧化光线投射形成人物脚下深邃阴影，
焦褐木梁 #2C1810，大理石或抛光木地板，
穹顶天文图案壁画，权威与政治阴谋的氛围，
电影构图强调权力动态与纵向等级制
```

#### 2. 提示词2：私密接见室的阴谋 [私密接见室的阴谋]

**English：**
```
Cinematic close interior shot, 2.39:1 widescreen, private imperial chamber,
candlelight illuminating two figures in conspiratorial conversation across
table, warm golden candlelight #DAA520 contrasting with dark wood #2C1810,
ornate furniture and treasures barely visible in shadows, intimate but sinister
atmosphere, shallow depth of field on faces showing ambition and calculation,
whispered dialogue implied, political intrigue tension, dramatic side lighting
```

**中文：**
```
电影近景室内镜头，2.39:1宽银幕，皇帝密室接见，
烛光照亮两道身影在案前密谋，温暖烛火金光 #DAA520
与暗色木质 #2C1810 对比，华丽器物与宝藏隐没于影中，
亲密而诡异的氛围，浅景深聚焦脸部表情显示野心与算计，
低声对话暗示，政治阴谋的紧张，戏剧化侧光照明
```

#### 3. 提示词3：秘密小楼恐怖揭露 [秘密小楼恐怖揭露]

**English：**
```
Cinematic horror reveal, 2.39:1 widescreen, underground secret chamber within
palace, five humanoid figures lined up on examination tables in sterile white
light, metallic equipment and tubes surrounding bodies, cold clinical aesthetic
contrasting with ornate palace architecture partially visible, deep shadows at
edges, psychological tension and forbidden science atmosphere, revealing light
from opened door, moment of horrified discovery, cinematic depth creating
claustrophobic dread
```

**中文：**
```
电影恐怖揭露镜头，2.39:1宽银幕，皇宫地下秘密暗室，
五具数字人躯壳整齐排列在检查台上，冷白无菌灯光，
金属设备与导管环绕躯壳，冷酷临床美学与宫殿华丽建筑
部分可见形成诡异对比，边缘深邃阴影，心理紧张与禁忌科学，
打开门扉的启示光线，恐怖发现时刻，电影景深营造幽闭恐怖感
```

#### 4. 提示词4：灵魂仪式终幕 [灵魂仪式终幕]

**English：**
```
Cinematic finale, 2.39:1 widescreen, grand imperial ritual chamber, ornate
ceremonial space with golden accents #DAA520 and crimson walls #8B1A1A,
mysterious spiritual apparatus or soul-transfer device at center, multiple
figures witnessing ritual under dramatic overhead lighting, ethereal light
effects suggesting supernatural element, tension between scientific and
religious ceremony aesthetics, brown wooden architectural elements #2C1810,
moment of ultimate power transition, cinematic chiaroscuro lighting
```

**中文：**
```
电影终幕镜头，2.39:1宽银幕，宏大帝国灵魂仪式殿厅，
华丽的仪式空间配金色装饰 #DAA520 与深红墙面 #8B1A1A，
神秘的灵魂转移装置或仪器置于中央，多人见证仪式在
头顶戏剧化灯光下，虚幻灵性光效暗示超自然元素，
科学与宗教仪式美学的张力碰撞，焦褐木质建筑 #2C1810，
终极权力转移的时刻，电影级明暗对比光线
```

### 裘万财 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a middle-aged Chinese man in his 40s-50s, slightly plump physique with mixed muscle and fat suggesting both strength and decadence, coarse rough skin with possible scars from violence, face showing arrogant smirk with disdainful eyes, hair plain and unkempt, wearing exaggerated thick gold chain necklace and oversized gold rings, dark gaudy expensive-looking outfit, expression contemptuous and aggressive with sleazy gaze, neutral background, harsh direct lighting emphasizing coarse skin texture and scarring, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40-50岁出头中国中年男性的正面半身肖像，微胖体型肌肉与脂肪混合暗示既有力量又有堕落，粗糙皮肤可能有暴力留下的伤疤，面容傲慢冷笑蔑视的眼神，头发平常不修饰略显蓬乱，戴着夸张粗厚的金色项链和超大金戒指，穿深色俗气奢华的衣着，表情凶悍凌厉目光色厉，中性背景，刺眼直射光强调皮肤的粗糙质感和伤疤，35mm胶片颗粒感，高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a middle-aged Chinese man in his 40s-50s, slightly plump build standing with chest puffed out and feet wide apart, arms held slightly away from body in domineering posture, coarse face with arrogant smirk, wearing exaggerated gold chain necklace and large gold rings over gaudy expensive-looking dark outfit, coarse weathered skin showing possible scars and rough texture, posture exuding swagger and tyrannical presence, plain dark background, warm harsh side lighting emphasizing muscular forearms and powerful stance, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40-50岁出头中国中年男性的全身正面肖像，微胖体型挺胸站立双脚分开，双臂略离身体呈跋扈的姿态，粗糙面容傲慢冷笑，戴着夸张粗厚金色项链和超大金戒指穿着俗气奢华的深色衣着，皮肤粗糙风化可能有伤疤和粗糙质感，姿态散发大摇大摆的气势和专制的压迫感，素色深色背景，暖色刺眼侧光强调前臂肌肉和强势的身体，35mm胶片颗粒感，中高对比度
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body scene of a coarse-featured middle-aged Chinese man walking arrogantly down a dusty town street with swagger, slightly plump physique with muscular forearms, wearing gaudy expensive-looking dark outfit with exaggerated gold chain necklace and large gold rings, face showing contemptuous and aggressive expression with disdainful gaze, locals parting to make way as he passes, traditional rural architecture in background, color palette dominated by earthy #8B7355 tones with warm lighting, harsh shadows suggesting his tyrannical presence, overall mood oppressive and tense, embodying a local town bully in the height of his power
```

**中文：**
```
电影感静帧，2.39:1宽银幕，粗面容的中年中国男子大摇大摆地走在镇上尘土街道，微胖体型前臂肌肉结实，穿着俗气奢华的深色衣着配夸张粗厚金链和超大金戒指，面容傲慢凶悍目光蔑视，行人纷纷让路，背景是传统农村镇街景建筑，色调以#8B7355枯草黄为主的暖光，刺眼阴影凸显其压倒性的专制存在，整体气氛压抑紧张，体现镇恶霸权力巅峰时期
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body scene of the same man now appearing completely vacant and controlled, eyes wide open but utterly vacant and lifeless with completely vacant stare, face gaunt and sallow, walking mechanically with rigid jerky movements either pacing aimlessly back and forth or being used as labor, clothes now disheveled and wrinkled, gold chain and rings still present but forming sharp contrast with his degraded state, expression completely blank and emotionless, background dark and oppressive, color palette shifts to dark purples and grays (#5B3A6B), the overall mood eerie and disturbing, showing a powerful man reduced to a mindless controlled puppet with vacant unfocused eyes
```

**中文：**
```
电影感静帧，2.39:1宽银幕，同一个男子现在显得完全呆滞被控制，眼睛圆睁但彻底空洞无神完全失焦的目光，面容枯槁蜡黄，行走机械生硬要么漫无目的踱步要么被当作苦力使用，衣服皱褶邋遢，金链和金戒指仍在身上但与其衰败沦落的状态形成尖锐对比，表情完全空白冷漠无情绪，背景黑暗压抑，色调转为暗紫和灰色（#5B3A6B），整体氛围诡异恐怖令人不安，曾经的权力者沦为无意识的被控制傀儡眼神完全失焦空洞
```

### 观音庙神水 (props, ★★★, P5)

#### 1. 提示词 1：概念艺术（圣水与容器） [概念艺术（圣水与容器）]

**English：**
```
"Cinematic still, 2.39:1 widescreen, close-up of ancient wooden bucket filled with crystalline spring water glowing with ethereal royal blue luminescence. Water surface ripples with supernatural shimmer. Aged wood barrel in dark brown (#2C1810) with copper bands patinated green, moss-covered texture. Interior divine light softly emanating from water, creating halo effect. Mystical, spiritual atmosphere. Mountain temple setting in background blur. Professional concept art, volumetric lighting, hyperrealistic water physics, cinematic color grading."
```

**中文：**
```
"电影级画面，2.39:1 宽屏幅，古老木桶装满晶莹透澈的山泉水，散发幽灵般的皇家蓝荧光。水面涟漪呈现超自然微光。桶身焦褐色木质（#2C1810）配青铜色环箍泛铜绿，覆盖苔藓纹理。内部神圣之光从水中柔和散发，形成光晕效果。神秘、灵性氛围。背景模糊的山寺场景。专业概念艺术，体积光效，超写实水物理，电影级色彩分级。"
```

#### 2. 提示词 2：场景艺术（仪式时刻） [场景艺术（仪式时刻）]

**English：**
```
"Cinematic still, 2.39:1 widescreen, overhead view of ritual ceremony: wooden bucket with divine water on stone altar, surrounded by candles and incense smoke. Fine mist rising from liquid glowing with soft royal blue (#4169E1). Moss-green shadows (#4A6741) cast by temple stones. Ethereal wisps of spirit energy swirling above water surface. Flickering candlelight creates dancing reflections. Mystical, sacred ambiance. Dark brown wood (#2C1810) contrasts with divine glow. Cinematic lighting, volumetric fog, spiritual atmosphere, color graded fantasy aesthetic."
```

**中文：**
```
"电影级画面，2.39:1 宽屏幅，俯视角度的仪式场景：石祭坛上的装满神水的木桶，被烛火与香烟围绕。液体上升的细雾发出柔和的皇家蓝光（#4169E1）。寺庙石头投射的苔绿色阴影（#4A6741）。灵气涟漪在水面上方盘旋。烛火摇曳光线创造舞动的反射。神秘、神圣的气氛。深褐木色（#2C1810）与神圣光辉形成对比。电影级光照，体积雾效，灵性氛围，奇幻美学色彩分级。"
```

#### 3. 提示词 3：效能呈现（饮用时刻） [效能呈现（饮用时刻）]

**English：**
```
"Cinematic still, 2.39:1 widescreen, intimate scene of mystical water flowing into vessel. Luminous royal blue (#4169E1) glow intensifying as water pours. Soft warm light emanating from liquid, illuminating surrounding environment in green tones (#4A6741). Macro detail of water droplets reflecting divine luminescence. Ethereal mist rising with subtle spiral patterns. Spiritual energy visualization in misty form. Volumetric lighting emphasizes supernatural properties. Cinematic color grading, high-resolution detail, fantasy realism aesthetic."
```

**中文：**
```
"电影级画面，2.39:1 宽屏幅，亲密场景中神秘之水倾入器皿。皇家蓝光（#4169E1）随着水的倒入而增强发光。柔和温暖的光从液体散发，用绿色调（#4A6741）照亮周围环境。水珠微距特写反射神圣荧光。升起的灵气雾气呈现细微螺旋纹。灵能在雾状形式中的可视化。体积光效强调超自然特性。电影级色彩分级，高分辨率细节，奇幻写实美学。"
```

#### 4. 提示词 4：治疗变化（恢复场景） [治疗变化（恢复场景）]

**English：**
```
"Cinematic still, 2.39:1 widescreen, transformative healing moment: divine blue light (#4169E1) emanating from wounded area, spreading warmth and regeneration. Skin texture changing from pale to rosy flush in real-time. Ethereal glow surrounding recovering body. Soft illumination in temple stone chamber, moss-green ambient light (#4A6741). Spiritual energy flowing through visible channels of light. Volumetric mist capturing healing essence. Cinematic composition emphasizing renewal and supernatural restoration. Color graded for fantasy drama."
```

**中文：**
```
"电影级画面，2.39:1 宽屏幅，变革性治疗时刻：神圣蓝光（#4169E1）从伤口区域散发，传播温暖与再生。皮肤质感从苍白实时变为红润。灵性光辉围绕恢复的身体。寺庙石室中的柔和照明，苔绿色环境光（#4A6741）。灵能通过可见的光之通道流动。体积雾气捕捉治疗本质。电影级构图强调更新与超自然恢复。为奇幻剧情调色。"
```

### 郝大川 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese man
in his 40s with an emaciated face showing severe dark circles and hollow cheeks.
Wearing a tattered, worn-out cotton shirt with patched fabric. His whole body
trembles slightly, hands visibly shaking. Expression shows pure terror mixed with
numbness, eyes sunken and unfocused. Thin wisps of hair hang unkempt around his
pale face. Background: plain dark background, studio lighting with side-key light
emphasizing the hollows of his face. Color tone: #8B7355 earthy rust and muted
beige. Sickly pallor, standing against darkness. Photorealistic, melancholic,
haunting portrait. Shot from chest up.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一个40多岁的极度消瘦男性正面半身肖像，面容凹陷，
严重黑眼圈，颧骨凸起。穿着破旧邋遢的棉布衣衫，有多处补丁。整个身体微微颤抖，
双手明显发抖。表情呈现恐惧与麻木的混合状态，眼神空洞无神。头发蓬乱稀疏，苍白
面容。背景：纯深色，摄影棚光线，侧逆光强化脸部凹陷和黑眼圈。色调：枯草黄
#8B7355，沉闷的铁锈色与米色。病态苍白，站在黑暗中。写实风格，忧郁凄凉。
半身照。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body frontal portrait of a skeletal man
in his 40s standing rigidly, entire frame trembling. Extremely thin frame visible
through torn, patched clothing hanging loose on his bones. Severe dark circles
dominate his face, eyes wide with lingering terror. His posture is slightly hunched,
shoulders drawn inward in a defensive position. Bare feet visible, suggesting utter
destitution. His hands hang limply at his sides, fingers slightly curled as if
frozen mid-tremble. Backdrop: plain dark background, minimal shadows to emphasize
isolation. Lighting: cool, clinical, showing every detail of his physical and mental
deterioration. Color: muted earth tones of #8B7355. Full-length shot, standing alone
in void. Photorealistic, haunting, desperate.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一个40多岁的消瘦男性全身正面肖像，僵直地站立，整个
身体颤抖。骨瘦如柴的身体在破旧、多处补丁的衣衫下清晰可见，衣物松散地挂在骨骼
上。严重黑眼圈支配整个脸部，眼睛睁大，充满挥之不去的恐惧。姿态略微驼背，肩膀
内缩成防御姿势。赤足可见，象征彻底沦落。双手无力地垂在身体两侧，手指轻微蜷缩，
仿佛冻结在颤抖的动作中。背景：纯深色，极简阴影以突出孤立感。光线：
冷调、临床感，突出身体与精神崩溃的每一个细节。色调：枯草黄#8B7355的沉闷大地色。
全身照，孤独地站在虚无中。写实风格，令人不安，充满绝望。
```

#### 3. 

**English：**
```
Interior stage set: dimly lit apartment or cabin interior. Furniture arranged to
show tight proximity—郝大川 standing inches behind 小顶, one trembling hand gripping
小顶's shoulder. Shadows cast long across the floor. A doorway visible in the
background, symbolically dark and threatening. Color palette dominated by #8B7355
earth tones mixed with deep shadows. 郝大川's silhouette shows hunched posture,
visible tremor in limbs. Light focused on 小顶's face contrasts with 郝大川's
obscured, fearful expression partially hidden. Stage direction: 郝大川 moves in
small, constrained steps, never more than arm's length away.
```

**中文：**
```
舞台布景：昏暗的室内场景，可以是船舱或破旧房间。家具布置显示紧密的近距离状态——
郝大川站在小顶身后几寸距离，一只发抖的手紧紧抓住小顶的肩膀。长长的影子投射在
地面上。后方可见一扇门，象征黑暗与威胁。色调由枯草黄#8B7355的大地色与深影混合
主导。郝大川的轮廓显示驼背姿态，肢体明显颤抖。灯光集中在小顶的脸上形成对比，
而郝大川表情模糊、恐惧、半隐在黑暗中。舞台指示：郝大川步履小而受限，从不距离
小顶超过一臂之远。
```

#### 4. 

**English：**
```
Interior stage: a bare, decrepit room. Visible details: scattered dust motes in
faint light, spider webs in corners, locked door with chain visible. 郝大川 sits
hunched on the floor or on edge of a cot, rocking slightly. His silhouette barely
visible in the shadows—only his wide, unblinking eyes visible catching sparse light.
A rope prop suggested in background (hanging from above, unused). Stage lighting:
extremely dim, perhaps only a single cold spotlight on his face showing the black
circles and sunken features in cruel detail. Color: blacks, deep grays, with minimal
touches of #8B7355. Sound design: subtle creaking, distant footsteps triggering his
sudden stiffening. Sense of complete isolation and psychological claustrophobia.
```

**中文：**
```
舞台布景：空荡荡、破旧的房间。可见细节：散落的尘埃在微弱光线中漂浮，角落的蜘蛛网，
锁着的门带有铁链。郝大川蜷缩坐在地面或简陋床边，身体微微摇晃。他的轮廓在阴影中
几乎看不见——只有他睁大、呆滞的眼睛在稀疏的光线中闪烁。背景暗示绳索道具（从上方
悬挂，未使用）。舞台灯光：极度昏暗，或许只有一盏冷调聚光灯照在他的脸上，无情地
突出黑眼圈和凹陷的五官。色调：黑色、深灰，极少触及#8B7355。声音设计：微妙的吱呀声，
远处脚步声触发他突然的僵硬。完全孤立感与心理上的幽闭感。
```

#### 5. 

**English：**
```
Stage: completely dark or lit only by a single overhead light source. A rope visible
(hanging from visible ceiling fixture or darkness above). The space is empty except
for 郝大川's body or silhouette. If body is shown: slumped posture beneath the rope,
feet barely touching or suspended. The stage floor is empty and bare—no furniture,
no escape. Color: deep blacks and charcoal, with only the outline of the rope
catching faint light. Atmosphere: absolute silence except for possible audience
breathing. The emptiness of the space represents the emptiness of his mind. Optional:
footsteps approaching (小顶 discovering), then sudden stopping as realization hits.
Lighting change: slow fade to black or cold white spotlight on the rope alone.
```

**中文：**
```
舞台：完全黑暗或仅由单一顶部光源照亮。绳索可见（从可见的天花板支架或上方黑暗悬挂）。
空间除了郝大川的身体或轮廓外空荡荡。如果显示身体：蜷缩的姿态悬挂在绳索下，脚尖
几乎接触地面或悬空。舞台地面空荡赤裸——没有家具，没有逃脱。色调：深黑与炭灰，只有
绳索的轮廓捕捉微弱的光线。氛围：绝对的寂静，除了可能的观众呼吸声。空间的空荡代表他
精神的空荡。可选：脚步声逼近（小顶发现），然后突然停止当意识到发生了什么。灯光变化：
缓慢淡出到黑色或冷白聚光灯仅照在绳索上。
```

### 郭云成 (characters, ★★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese man in his mid 50s to early 60s with a stern military bearing, short neatly combed grey-white hair swept back from forehead, deep-set dark eyes with penetrating gaze showing both command authority and hidden sorrow, sharp high cheekbones with angular jaw, thin lips held in a resolute line, deeply lined face bearing the marks of decades of military service, neatly trimmed grey facial hair, wearing battle-worn military armor with visible scratches and dents in deep green and tan colors with tarnished metal fittings, neck visible above armor showing weathered skin, dignified and composed expression despite visible fatigue, white neutral background, cool side lighting from camera-left emphasizing the lined face and armor details, 35mm film grain, high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50多至60多岁中国男性的正面半身肖像，军人气质严肃，花白短发梳理整洁向后掠，深陷而深褐色的眼睛目光锐利透出指挥官权威和隐藏的悲悯，颧骨高耸下颌线条棱角分明，薄唇保持坚定的直线，脸部布满从军数十年的皱纹，修剪整齐的灰白络腮胡，穿战痕累累的军甲深绿色和卡其色主调可见明显的划痕和凹陷金属部分磨损，甲胄上方露出风化的颈部皮肤，表情尊严沉着但可见明显疲态，白色中性背景，左侧冷色调侧光强调线条脸部和甲胄细节，35mm胶片颗粒感，高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait of a Chinese military general in his mid 50s to early 60s, short neatly combed grey-white hair, high sharp cheekbones and strong angular jaw in profile, deep-set dark eyes staring into the distance with a mixture of determination and weariness, thin lips, weathered deeply lined face, neat grey facial hair, wearing heavy battle-worn military armor in deep green with visible damage and scratches, large armored pauldrons on shoulders, expression of grave contemplation, right hand raised with fingers poised to tap on chest plate in a gesture of deep thought, white neutral background, dramatic cool side lighting from left emphasizing the profile's angular features and armor wear, 35mm film grain, high contrast emphasizing age and authority
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50多至60多岁中国军事将领的四分之三侧面半身肖像，花白短发梳理整齐，侧面可见高耸锐利的颧骨和强硬的棱角下颌，深陷的深褐色眼睛凝视远方混合了坚定与疲惫，薄唇，风化深皱的脸部，修剪整齐的灰白胡须，穿着沉重的战痕累累的军甲深绿色主调可见明显的破损和划痕，肩膀上硕大的甲胄片，表情严肃沉思右手抬起手指姿态如要敲击胸甲的深思动作，白色中性背景，左侧戏剧性冷色调侧光强调侧面的棱角特征和甲胄磨损，35mm胶片颗粒感，高对比度强调年龄感和权威性
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body shot of a Chinese military general in his mid 50s to early 60s standing on fortress wall rampart, short neatly combed grey-white hair, weathered angular face showing deep fatigue and resolve, wearing heavily damaged battle-worn military armor in deep green with fresh scratches, dents and blood splatters from final combat, pauldrons partially shattered, hands gripping stone wall edge with both palms firmly planted, posture perfectly upright and dignified despite exhaustion, gaze directed toward the distant burning city below with expression of grave acceptance and clarity, fortress wall ruins and collapsed sections visible to either side, plain dark neutral background, dramatic warm backlighting from fires and explosions casting long shadows and red-orange rim light across the figure, emotional and tragic atmosphere, 35mm film grain, high contrast emphasizing the heroic tragedy and unwavering resolve
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名50多至60多岁中国军事将领全身站在城堡城墙壕垛之上，花白短发梳理整齐，风化棱角脸部显示深度疲劳和坚定决心，穿着严重破损的战痕累累的军甲深绿色主调可见新鲜的划痕凹陷和血迹来自最后战斗，肩甲部分破碎，双手用力把握石墙边缘两只手掌坚实地按在墙上，身姿完美笔直尽管疲惫，目光投向下方远处燃烧的城市表情显示沉着接纳和清晰的认知，城堡城墙废墟和崩塌的断面在两侧可见，素色深色中性背景，来自火焰和爆炸的戏剧性暖色逆光投射长长的阴影和红橙色轮廓光横跨整个身影，情感悲壮的氛围，35mm胶片颗粒感，高对比度强调英雄式的悲剧和不屈的意志
```

### 丁路 (characters, ★★, P5)

#### 1. 

**English：**
```
A young male tour guide in his 20s with a healthy, sunny disposition.
Sharp features, bright and spirited eyes, warm genuine smile.
Healthy skin with a subtle tan from outdoor work, luminous complexion.
Black short hair, neat and voluminous, shoulders held upright.
Wearing clean tour guide uniform or casual clothing.
Radiating youthfulness, enthusiasm, and trustworthiness.
Color palette: Wheat brown #8B7355 as primary tone.
Front-facing half-body portrait, warm lighting, minimalist background.
```

**中文：**
```
年轻男性导游，20多岁，健康阳光气质。
面容立体，眼神明亮有神，含着爽朗微笑。
皮肤健康有光泽，略带小麦色（户外工作痕迹）。
黑色短发蓬松整洁，肩膀挺拔。
穿着整洁的导游制服或休闲衣物。
整体散发年轻、热情、可信赖的气场。
色彩：枯草黄 #8B7355 为主色调。
正面半身像，光线温暖，背景简洁。
```

#### 2. 

**English：**
```
A young man in his 20s, appearing pallid and exhausted.
Gaunt face, sickly pale complexion, sunken eye sockets.
Eyes deep and hollow, mismatched to age, pupils shifting between unfocused and intense.
Corners of mouth twisted upward in an eerie smile, expression incongruent with context.
Head tilted at an unnatural angle, stiff neck.
Fingernails digging into palms, fingers trembling faintly, traces of cold sweat.
Sallow skin, veins faintly visible, hair clinging to forehead.
Clothing loose and ill-fitting, noticeably emaciated body.
Overall emanating an eerie, oppressive, puppet-like sense of violation.
Color palette: Dark purple #5B3A6B as primary tone, avoid pure white #FFFFFF.
Front-facing half-body portrait, gloomy lighting, mysterious oppressive background.
```

**中文：**
```
年轻男性，20多岁，但显得苍白疲惫。
面容消瘦，肤色病态苍白，眼眶深陷。
眼神深邃得不匹配年龄，空洞而沉重，瞳孔时而涣散。
嘴角诡异上扬，表情与语境不符，散发被操纵感。
头部角度略显不自然，脖子僵硬。
双手指甲掐入手心，手指微颤，冷汗迹象。
皮肤暗沉，血管隐约可见，头发贴着额头。
衣着依旧但显得不合身，身体消瘦。
整体散发诡异、压抑、被吞没的人偶感。
色彩：暗紫 #5B3A6B 为主色调，禁用纯白 #FFFFFF。
正面半身像，光线阴沉，背景神秘压抑。
```

### 五名古代恶灵 (characters, ★★, P5)

#### 1. 

**English：**
```
5 ancient evil spirits group portrait in early beggar possession form: tattered beggar corpses, dark purple eye sockets glowing, pupils radiating outward, eerie upturned mouths, twisted uncoordinated limbs, surrounded by faint dark purple mist, dark oppressive background, 5 figures arranged in diagonal formation, low-key cool lighting, detail focus: torn rags, grime stains, ancient seal script faintly floating on skin, oil painting texture, oppressive eerie atmosphere. Prohibit pure white background.
```

**中文：**
```
5名古代恶灵群像肖像，乞丐附身初期：破败的乞丐躯体，暗紫色眼眶泛光芒，瞳孔呈放射状纹理，嘴角诡异上扬，肢体扭曲不协调，周身缠绕淡薄的暗紫色雾气，背景黑暗压抑，5个人物排列成对角线阵型，光线低沉冷色调，细节刻画：破碎衣衫、污垢斑驳、古篆文纹隐约浮现于皮肤，真实油画质感，压抑诡异氛围。禁用纯白背景。
```

#### 2. 

**English：**
```
Five ancient evil spirits late-stage synchronized state group scene: 5 figures in tattered ancient official robes, dark purple patterns completely covering bodies, 5 arranged in pentagram formation, synchronized turning motion, skulls terrifyingly twisted 360 degrees, elongated curved limbs, skin with cracked porcelain texture, surrounding dark magnetic field, dark purple and crimson energy vortex, temperature visualized as icy blue cold mist encircling, victim souls sucked into center funnel, details: ancient seal script glowing on skin, bone-cracking sound visual effects, 5 shadows merged into giant silhouette, golden fractured patterns flickering on robes. Eerie horror, realistic style.
```

**中文：**
```
五名古代恶灵后期协调态群像场景：5个人物穿着破碎古代官袍，暗紫色纹路完全覆盖躯体，5人排成五角星阵型，同步转身动作，头颅可怕地360度扭转，肢体拉长弯曲，皮肤呈现龟裂瓷器质感，周围形成黑暗磁场，暗紫和暗红能量漩涡，温度视觉化为冰蓝色寒气环绕，被害者灵魂被吸入中心漏斗，细节：古篆文字在肌肤发光、骨裂音效的视觉表现、5个影子重叠成巨大黑影、金色破碎纹饰在官袍上闪烁。诡异恐怖，写实风格。
```

### 仙人掌 (props, ★★, P5)

#### 1. 

**English：**
```
Giant Cactus / Desert Prickly Pear
```

**中文：**
```
仙人掌 / 巨大仙人掌
```

#### 2. 提示词1 - 仙人掌细节特写 [仙人掌细节特写]

**English：**
```
Cinematic still, 2.39:1 widescreen, extreme close-up of giant cactus stem and spines,
natural green #5A7C59 flesh with golden-brown #A0826D needle-like spines densely packed,
rough organic texture with sand grain detail, sharp shadow patterns from spines,
harsh desert sunlight, 35mm film grain, warm muted earth tone color grading,
weathered botanical aesthetic, no artificial gloss
```

**中文：**
```
电影质感，2.39:1宽屏，巨大仙人掌茎秆与刺毛特写，自然绿#5A7C59肉质配金褐#A0826D细长刺，
密集分布，粗糙有机纹理与沙粒细节，刺影投射出锋利的阴影图案，
刺烈的沙漠阳光，35mm胶片颗粒感，温暖黯淡的土色调分级，风化的植物美学，
无人工光泽感
```

#### 3. 提示词2 - 山崖救援场景 [山崖救援场景]

**English：**
```
Cinematic still, 2.39:1 widescreen, wide angle view of giant cactus growing on cliff edge,
character falling against green #5A7C59 plant, torso caught on dense spines, dramatic
depth, rocky cliff face surrounding, golden afternoon light casting long shadows,
35mm film grain, dusty color palette, muted browns and greens, gritty cinematic texture,
tension and survival moment captured
```

**中文：**
```
电影质感，2.39:1宽屏，宽景仰角展现山崖边缘的巨大仙人掌，角色坠落与绿#5A7C59植物相撞，
躯干被密集刺毛钩住，极具纵深感，周环岩壁环绕，金色午后光线投射长阴影，
35mm胶片颗粒感，尘埃色调，黯淡褐绿配色，粗糙电影质感纹理，
紧张与生存时刻的捕捉
```

### 刘振 (characters, ★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of an emaciated homeless man with gaunt hollow face, high sharp cheekbones, sunken eyes with crazed manic gaze, bloodshot whites with dilated pupils showing unhuman intensity and malevolence, wildly unkempt long black hair matted with dirt, patchy unkempt beard, dark weathered skin covered in grime, wounds and bruises, wearing tattered rags and filthy clothes in dark grays and blacks, no shoes or feet wrapped in dirty cloth, the face registers deep derangement but the eyes burn with ancient evil intelligence—a sharp contrast between bodily decay and spiritual malevolence, dark supernatural color palette, dim murky lighting revealing wisps of dark purple spectral energy #5B3A6B swirling around the head and eyes like ghostly aura, 35mm film grain, high contrast emphasizing the horror of possession, atmosphere deeply unsettling and otherworldly
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名瘦削流浪汉的正面半身肖像，消瘦凹陷的脸部高耸的颧骨，深陷的眼窝里闪烁疯狂的癫狂目光，眼白充血瞳孔放大显示非人类的强度和恶意，蓬乱肮脏的长黑发纠缠着污垢，胡须凌乱贴脸，肤色黝黑粗糙布满污垢伤痕淤青，穿着褴褛肮脏的衣物黑灰色调，无鞋或脚缠破布，脸部显示深度的精神错乱但眼睛燃烧着古老恶灵的智慧——身体衰败与灵性恶意的极端对比，深色超自然色系，昏暗诡异的光线显露暗紫色#5B3A6B的幽灵般能量漩涡缠绕头部和眼眶如灵魂光晕，35mm胶片颗粒，高对比度强调附身的恐怖，整体氛围深度诡异与超越现实
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a middle-aged Chinese man appearing as restaurant proprietor but profoundly altered, formerly round face now slack and sagging, oily skin now sallow and pallid with unhealthy greyish tone replacing previous healthy glow, eyes once intelligent and warm now vacant and unfocused with milky dullness completely void of original personality, pupils dilated and unseeing gazing past the viewer, eye sockets surrounded by shadowy dark circles suggesting life force drained, lips lacking warmth no longer forming genuine smile only mechanical grimace, hair neglected and unkempt losing former neatness, wearing soiled rumpled apron and robe showing signs of neglect and deterioration, clean white apron from earlier now grimy, overall bearing completely drained of vitality and presence—a corpse animated by external will, cold harsh sidelight creating deep shadows emphasizing hollowness, dark purple spectral energy #5B3A6B visibly swirling around eyes and temples threatening to overflow, temperature of image feels unnaturally cold, 35mm film grain, extreme high contrast, deeply unsettling atmosphere of possession and violation of selfhood
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名中年中国男性的正面半身肖像外表仍是餐馆老板但形象骇人改变，曾经圆脸现已松弛下垂，油腻皮肤现已蜡黄苍白带不健康的灰色调替代曾经的健康光彩，眼睛曾经聪慧温暖现已空洞失焦乳白色混浊完全失去原有的个性，瞳孔扩张无神目光越过观众, 眼眶周围笼罩阴影深深的黑眼圈暗示生命力被吸干，嘴唇失去温度不再形成真挚笑容只有机械的假笑，头发被忽视蓬乱失去曾经的整洁，穿着沾污的褶皱围裙和长衫显示被忽视和衰败，曾经洁白的围裙现已污垢，整体举止完全失去活力和存在感——一具被外力操纵的尸体，冷色刺眼的侧光创造深阴影强调内部空洞，暗紫色#5B3A6B的灵魂能量明显在眼睛和太阳穴周围漩涡威胁溢出，整个画面的温度感觉不自然冰冷，35mm胶片颗粒，极高对比度，深度不安的附身和自我被侵犯的氛围
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, three-quarter view bust portrait showing profound possession, slack face in profile with sagging cheeks and dull expressionless features, completely vacant unfocused eyes gazing into empty distance showing no awareness, hollow sunken appearance around eyes and temples, unkempt greying hair falling across forehead, sickly pallid complexion with greyish-yellow tone, wearing soiled apron and robe rumpled and unwashed, the complete absence of the original warm merchant proprietor—instead a puppet moving through motions of human existence, cold sidelight creating harsh shadows emphasizing the void within, dark purple supernatural energy #5B3A6B faintly visible around eye socket and temple area like malevolent possession marker, overall impression of a life completely hollowed out, temperature and color palette convey unnatural cold and wrongness, 35mm film grain, high contrast, profoundly disturbing atmosphere
```

**中文：**
```
电影感静帧，2.39:1宽银幕，展现深度附身的四分之三侧面半身肖像，松弛的侧脸下垂的脸颊和呆滞无表情的五官，完全空洞失焦的眼睛凝视空洞的远方显示无觉察，眼睛和太阳穴周围凹陷空心，蓬乱花白的头发垂过额头，病态苍白灰黄色调的面容，穿着沾污的褶皱围裙和长衫脏乱不洁，完全丧失原有的温暖商人老板气质——反而是一具在人类存在的动作中移动的傀儡，冷色侧光创造刺眼阴影强调内部的空洞，暗紫色超自然能量#5B3A6B微弱但可见环绕眼眶和太阳穴如恶意附身的标记，整体印象是一个生命被彻底掏空，温度和色系传达不自然的冷感和错误感，35mm胶片颗粒，高对比度，深度令人不安的氛围
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, scene from an ancient Chinese town street at dusk, a gaunt emaciated homeless vagrant stands or lurks in the shadows of alley or street corner, wearing tattered rags in dark colors nearly blending into darkness, unkempt wildly matted black hair, face hollow and weathered, but the eyes burn with crazed intelligent malevolence—ancient evil spirit inhabiting a broken body, the contrast between the deranged appearance and the penetrating supernatural intelligence in the gaze is deeply unsettling, murky dim lighting from fading twilight, dark purple spectral energy #5B3A6B swirls faintly around the figure suggesting paranormal presence, the air around this figure appears colder and more distorted, color palette dark grays blacks and browns with wisps of dark purple, atmosphere heavy with dread and wrongness suggesting something inhuman observing from within human form, 35mm film grain, high contrast, profoundly eerie and threatening mood
```

**中文：**
```
电影感静帧，2.39:1宽银幕，古代中国镇街道黄昏场景，一名瘦削流浪汉站立或潜伏在小巷或街角的阴影中，穿着褴褛的衣物深色调几乎与黑暗融为一体，蓬乱肮脏的长黑发纠缠，脸部消瘦粗糙，但眼睛燃烧着癫狂的聪慧和恶意——古代恶灵附身在破败的身体内，疯狂的外表与眼神中穿透性的超自然智慧的极端对比深度令人不安，暮色褪去的昏暗诡异光线，暗紫色#5B3A6B的灵魂能量微弱地在人物周围旋涡暗示超自然存在，这个人物周围的空气显得更冷和扭曲，色系深灰黑褐色调缠绕暗紫色，氛围沉重充满恐惧和错误感暗示非人类的东西从人类形态内观察，35mm胶片颗粒，高对比度，深度诡异和威胁的情绪
```

#### 5. 

**English：**
```
Cinematic still, 2.39:1 widescreen, interior scene of restaurant or family setting, the same Chinese man who was once warm and welcoming proprietor now appears drastically altered and possessed, sitting or standing with mechanical unnatural posture, vacant unfocused eyes staring blankly ahead showing complete absence of the original warmth and intelligence, face slack and expressionless, oily skin now sallow and grey losing all healthy luster, wearing soiled rumpled apron and robe once clean now neglected, the entire presence radiates emptiness and wrongness—a puppet being animated by unseen puppet master, hands hanging limply or being directed by invisible strings, cold fluorescent or dim lamplight creating harsh shadows emphasizing the hollow appearance, dark purple spectral energy #5B3A6B faintly visible around eyes and temples threatening to overflow—visual marker of possession, color palette shifts from warm earth tones to sickly grey-yellow and dark purple creating profound unease, temperature of entire scene feels unnaturally cold and draining, 35mm film grain, high contrast, deeply disturbing atmosphere of bodily violation and spiritual erasure
```

**中文：**
```
电影感静帧，2.39:1宽银幕，餐馆或家庭内部场景，曾经温暖好客的老板形象骇人改变且被附身，坐立时显现出机械不自然的姿态，空洞失焦的眼睛呆滞凝视前方完全丧失原有的温暖和聪慧，脸部松弛无表情，油腻皮肤现已蜡黄灰色失去所有健康光泽，穿着沾污褶皱的围裙和长衫曾经洁白现已被忽视，整个存在散发出空洞和错误感——一具被看不见的幕后操纵者操纵的傀儡，双手无力下垂或被隐形提线指挥，冷色荧光或昏暗灯光创造刺眼阴影强调内部空洞，暗紫色#5B3A6B的灵魂能量微弱可见环绕眼睛和太阳穴威胁溢出——附身的视觉标记，色系从温暖的大地色调转变为病态灰黄和暗紫色创造深度不安，整个场景的温度感觉不自然冰冷和耗尽，35mm胶片颗粒，高对比度，深度令人不安的身体被侵犯和灵魂被抹除的氛围
```

### 北岸新码头 (locations, ★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, solitary figure standing on breakwater overlooking vast harbor, modern shipping port infrastructure in background, powerful sea breeze billowing robes, golden sunset light from behind creating silhouette effect, open water horizon stretching infinitely, merchant shipping vessels and cargo facilities visible, contemplative authority and ambition embodied, warm and cool color balance, dramatic backlighting, cinematic composition emphasizing dominance over landscape.
```

**中文：**
```
电影镜头，2.39:1宽幅，孤独身影立于防波堤眺望辽阔港口，现代航运港口基础设施在后景，强劲海风吹拂衣物，金色夕阳逆光投出剪影效果，开放水域地平线无限延伸，商业船队与货物设施清晰可见，沉思的权威与野心体现，暖冷色调平衡，戏剧性背光，电影式构图强调对风景的掌控。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, modern port facility in full operation, clean orderly docks with separated cargo and passenger areas, advanced machinery and equipment clearly visible, multiple vessels in berthing positions, organized workforce moving efficiently, bright natural daylight casting sharp shadows, stone breakwater and wooden pilings, bustling yet systematic atmosphere, warm earth tones and steel grays, architectural precision, prosperity and progress embodied in infrastructure.
```

**中文：**
```
电影镜头，2.39:1宽幅，现代港口设施全面运营，整洁有序码头分离货物与客运区域，先进机械与设备清晰可见，多艘船舶停靠位置，有组织的劳动力高效运动，明亮自然光线投出锐利阴影，石质防波堤与木质桩柱，繁忙而系统的氛围，暖调土褐与冷调钢灰，建筑精确感，基础设施体现的繁荣与进步。
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, dramatic sunset moment at coastal breakwater, architectural structures silhouetted against glowing sky, rough sea waves churning against stone barriers, distant harbor lights beginning to glow, maritime workers' silhouettes in foreground, moody atmospheric perspective, golden and deep blue color palette, wind-swept and dynamic composition, sense of human infrastructure versus nature's power, cinematic drama.
```

**中文：**
```
电影镜头，2.39:1宽幅，沿海防波堤的戏剧性夕阳时刻，建筑结构在发光天空前呈剪影，粗糙海浪冲击石墙，远处港口灯光开始点亮，前景中海港工人剪影，情绪化大气透视，金色与深蓝色调，风吹动态构图，人类基础设施与自然力量的对比，电影式戏剧感。
```

### 天都山脉 (locations, ★★, P5)

#### 1. 

**English：**
```
A catastrophic avalanche descending a towering mountain pass. Massive waves of snow cascade down steep cliffsides, completely engulfing a narrow mountain corridor. The sky rendered in twilight blue, creating sharp contrast with the overwhelming white of the avalanche and surrounding snow. Snow particles suspended in mid-air catch pale golden light, creating a blinding, almost surreal atmosphere. The scale emphasizes human insignificance against natural forces. Jagged rock faces barely visible through the snow deluge. The composition conveys motion, chaos, and absolute finality. Shot from a distant vantage, capturing the apocalyptic scope of the disaster.
```

**中文：**
```
灾难级的雪崩从高耸的山口倾泻而下。大规模的雪流从陡峭的崖壁滚落，彻底吞没狭窄的山道走廊。天空呈暮蓝色，与压倒性的雪白形成锐利对比。悬浮在空中的雪粒捕捉到暖金白的光线，形成致盲般的超现实氛围。整个尺度强调人类在自然力量面前的渺小。锯齿状的岩壁几乎在雪流中隐没。画面传达出运动、混乱与绝对的终局感。从远处视角拍摄，捕捉灾难的末世规模。
```

### 宁国红 (characters, ★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a 40+ year-old Chinese male former ship captain ravaged by trauma, prematurely aged with sunken skeletal features, white or salt-and-pepper disheveled hair lacking luster and appearing unwashed, hollow anguished eyes with dilated pupils fixed on a distant point unseeing, eyes surrounded by pronounced dark circles and visible blood vessels indicating chronic insomnia, eye corners in constant state of slight quivering suggesting post-traumatic stress response, high cheekbones protruding sharply, sunken cheeks, ashen-grey complexion completely drained of blood color showing morbid pallor, thin tense lips perpetually pressed together or slightly open in silent scream, fine involuntary tremor visible throughout face and neck from deep nervous system trauma, wearing tattered worn ship captain's coat or maritime work clothes with faded coloring and possible salt stains or unexplained dark stains, white neutral background, cool dim overhead lighting casting deep shadows emphasizing skeletal face structure and pallid complexion, desaturated color palette dominated by sickly grey #D3D3D3 and bruised blue #4A5568 with traces of faded ochre #8B7355 from past identity, 35mm film grain, high contrast emphasizing the haunting death-in-life quality of his appearance
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40多岁中国男性前船长因创伤摧毁而极度衰老的正面半身肖像，早衰的骨感特征、颧骨凸显、脸颊凹陷、黑白花白或全白凌乱毛躁的头发显然未妥善打理缺乏光泽，眼神空洞绝望，瞳孔散大，目光投向远方但无焦点，眼周有明显深色眼圈与血丝表明长期失眠，眼角持续细微颤动暗示创伤后应激反应，面色病态苍白呈灰白色完全失血色，嘴唇薄而紧张，常年紧抿或微张呈无声尖叫状，整个面部与颈部可见细微不随意的颤抖源于深层神经性创伤，身着破旧陈旧的船长服或海事工作衣物色调褪色可能有盐碱迹或不明污渍，白色中性背景，冷调阴沉的头顶光线投射深影强调骨感面部结构与苍白肤色，色调采用病态灰白#D3D3D3和瘀蓝#4A5568主导以及褪色的枯草黄#8B7355残迹代表已逝身份，35mm胶片颗粒感，高对比度强调他那令人毛骨悚然的"死亡中的活人"气质
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body front-facing portrait of a 40+ year-old Chinese male ship captain consumed by psychological trauma, prematurely aged with emaciated skeletal frame suggesting years of neglect, white or greyed disheveled hair unkempt and lacking any vitality, hollow haunted eyes with constant thousand-yard stare broken occasionally by sudden terrified eye-widening and pupil dilation as traumatic flashbacks involuntarily intrude, deeply sunken cheeks, ashen-grey mortified complexion suggesting living death, entire body visibly trembling with fine continuous involuntary micro-tremors from severe PTSD, standing with slightly hunched posture and turned shoulders suggesting self-protective collapse, wearing tattered faded ship captain's coat or maritime work uniform with visible salt stains, dark mysterious stains, frayed edges and general decay, work boots worn and weathered, hands visible with slight whitening at knuckles from unconsciously gripping fabric or clenching fists, posture suggesting he remains constantly alert with peripheral awareness scanning for exits and threats despite obvious mental collapse, cool dim environmental lighting casting deep shadows, desaturated bluish-grey color palette #4A5568 and sickly #D3D3D3 with faint ochre remains #8B7355, 35mm film grain applied heavily for documentary authenticity conveying the "living corpse" visual metaphor
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40多岁中国男性船长因心理创伤消蚀的全身正面肖像，极度衰老的骨骼瘦弱框架暗示多年的自我放弃，白色或花白凌乱毛躁的头发未加打理失去光泽，眼神空洞呆滞凝视远方但时而因创伤闪回突然睁大眼睛瞳孔极度散大显示突然的惊恐，高度凹陷的面颊，病态苍白的灰色肤色如同死亡般的面容，整个身体可见持续的细微无意识颤抖源于严重的创伤后应激障碍，身体微微佝偻肩膀内扣显示自我保护性的精神崩溃姿态，穿着破旧褪色的船长服或海事工作服，可见盐碱污渍、神秘的深色污渍、破损的边缘和整体的衰败迹象，工作靴磨损风化，双手可见指关节泛白因无意识地紧握衣物或握紧拳头，尽管精神明显崩溃但身体姿态显示持续的警惕性会下意识地扫过周围空间寻找出口与威胁，冷调阴暗的环境光线投射深影，色调采用去饱和的蓝灰色#4A5568和病态灰#D3D3D3以及褪色的枯草黄#8B7355残迹，35mm胶片颗粒感重度应用表现记录片般的真实性诠释"活死人"的视觉隐喻
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, full-body reference of a 40+ year-old Chinese male ship captain mid-traumatic flashback, hollow eyes suddenly wide-open in pure unfiltered terror and recognition, pupils dilated to maximum capacity, eyeballs seeming to stare through the present moment into the horrific past event he witnessed on water, face drained of all color becoming nearly translucent with sickly grey-white pallor, mouth slightly open in silent scream or strangled gasp, entire body seized by involuntary violent trembling intensifying dramatically during flashback, hands convulsively gripping nearby fabric or object with white-knuckled intensity, knuckles pressed so hard they appear bloodless, shoulders raised tensely toward ears in defensive collapse, breathing visible as rapid shallow gasps suggesting acute panic attack, tattered maritime uniform appearing even more disheveled as though the fabric itself is being shaken by inner turmoil, standing or sitting but posture completely rigid with trauma response, background should evoke maritime environment (ship deck, cabin, dock) but rendered in nightmarish distorted way suggesting the perceived reality vs. memory conflict in his mind, cold blue-grey shadows #4A5568 dominating with sickly overlay #D3D3D3, dramatic cross-lighting emphasizing the skeletal face structure and the raw anguish of the moment, no warm tones—pure trauma palette, 35mm film grain heavily applied, extreme contrast emphasizing the moment when past and present collide in his fractured psyche
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名40多岁中国男性船长在创伤闪回时刻的全身定妆参考，眼神突然睁得极大充满纯粹不加过滤的恐惧与认知，瞳孔散大到极限似乎凝视穿透当下时刻洞穿他在水上目睹的恐怖事件，面色完全褪去几近透明的病态灰白苍白，嘴唇微张呈无声尖叫或被掐住的喘息，整个身体被无意识的剧烈颤抖紧紧抓住，在闪回期间颤抖剧烈到戏剧化程度，双手痉挛地紧握周围布料或物体指关节泛白到近乎失血色，指骨按压得如此用力以至于显得无血色，肩膀紧张地向耳朵方向上提呈防御性的崩溃姿态，呼吸可见为快速浅促的喘息暗示急性惊恐发作状态，破旧的海事工作服显得更加凌乱不堪仿佛布料本身被内心动荡震撼，身体站立或坐下但整体姿态完全刚硬僵硬呈创伤反应，背景应呈现海事环境（船甲板、船舱、码头）但以噩梦般扭曲的方式渲染暗示他心中现实感知与记忆冲突，冷调蓝灰色阴影#4A5568主导并覆盖病态灰#D3D3D3，戏剧性的交叉光强调骨感面部结构与时刻的原始痛苦，禁用任何暖色调——纯粹的创伤色板，35mm胶片颗粒感重度应用，极端对比强调过去与现在在他破裂心灵中的碰撞时刻
```

### 宁阁码头 (locations, ★★, P5)

#### 1. 

**English：**
```
A coastal harbor at dusk, wooden vessels moored in a line. Masts rise against a twilight sky. Golden sunset light backlights the scene while the sea ripples in cool tones. Weathered wooden dock with coiled ropes and loading platforms. Figures moving across gangplanks and between stacks of cargo. The atmosphere carries warm khaki tones fading into deep twilight blue. A sense of anticipation and departure fills the composition. Shot from water level, emphasizing the grandeur of the ships and the imminent journey ahead.
```

**中文：**
```
黄昏时的沿海港口，木质船队并排停靠。桅杆耸立于夕阳天空。金色阳光逆光洒向船队，海面波光粼粼泛着暮蓝。风化的木质码头散布着盘绕的绳索和装货平台。人影在舷梯间与货物堆间穿梭。整个画面从温暖的枯草黄逐渐消融为深沉的暮蓝。一种启程的期待与希望弥漫其间。从水平面视角拍摄，强调船队的宏伟与即将远航的命运感。
```

### 封 (characters, ★★, P5)

#### 1. 

**English：**
```
Ancient soul spirit from Zhou Dynasty, oldest inhabitant of the underworld's evil spirit realm,
floating massive orb of spiritual essence with highly defined concentric ring-like texture covering surface,
resembling ancient tree cross-section where each ring represents centuries of accumulation,
color palette: dark purple (#5B3A6B) mixed with bronze-copper tones, emitting profound and serene spiritual aura,
crisp and dense boundaries showcasing millennia of accumulated spiritual power,
background: underworld environment in twilight-blue (#3A4A6B) atmosphere,
supernatural entity, stylized rather than photorealistic, emphasizing visual representation of time,
avoid pure white (#FFFFFF).
```

**中文：**
```
周朝古灵，阴间最老的灵魂体，悬浮的巨大光球形态，
表面覆盖深刻的年轮般纹理如同古树切面，每一圈纹路代表漫长岁月沉淀，
色调为暗紫（#5B3A6B）和古铜色混合，散发深邃而沉静的灵能光晕，
边界清晰凝聚，体现数千年灵力的积累，
阴间环境背景，暮蓝色调（#3A4A6B）的氛围衬托，
超自然存在，非写实风格，强调时间的视觉化呈现，
禁用纯白色。
```

#### 2. 

**English：**
```
Interior of evil spirit realm, dimly lit underworld space with numerous smaller spiritual orbs scattered around,
center: colossal and dense ancient spirit "Feng" with highly visible concentric ring texture under deep purple aura,
resembling a masterpiece carved by time itself,
surrounding lower-tier spirits appear dimmed by its spiritual suppression, creating visual hierarchy centered on Feng,
overall color palette: cool tones dominated by dark purple, twilight-blue, deep gray,
light sourced from the spirits themselves creating supernatural visual effects,
emphasize atmosphere of antiquity, ancient patina, and authority,
avoid pure white and warm color tones.
```

**中文：**
```
恶灵区内部场景，昏暗的阴间空间，众多较小的灵魂光团散布四周，
中央是巨大而凝实的古老灵魂"封"，
表面的年轮纹理在深紫色光晕中清晰可见，仿佛被时间雕琢的艺术品，
周围低等灵魂被其灵力压制而显得暗淡，形成以封为中心的视觉等级差异，
整体色调冷调：暗紫、暮蓝、深灰的主导，
光线来自灵魂体自身，营造超自然的视觉效果，
强调古老、沧桑、威权的氛围，
禁用纯白色和温暖色调。
```

### 小顶天德城住所 (locations, ★★, P5)

#### 1. 提示词 1 - 婚礼热烈 [婚礼热烈]

**English：**
```
Cinematic still, 2.39:1 widescreen, joyful wedding banquet in a newly-renovated residence. Warm amber lamplight illuminates smiling guests raising cups in celebration. Red silk drapery and paper lanterns festoon the reception hall. Freshly whitewashed walls and repaired surfaces gleam. In the background, a newly-painted roof glistens. Floral arrangements frame doorways. Golden hour lighting bathes everything in warmth. Color palette: dried grass yellow #8B7355 walls, warm white #FFF8DC trim, amber lanterns, lush green from garden visible through windows. Hyper-detailed period celebration, cinematic joy and hope, volumetric warm light.
```

**中文：**
```
电影截图，2.39:1 宽幅，新装修住所内的热烈婚宴。温暖琥珀灯光照亮举杯庆祝的宾客们。红丝绸与纸灯笼装饰接待厅。新粉刷的墙面与修复的裂缝闪闪发亮。远处新漆的屋顶熠熠生辉。花卉装饰框映门廊。金色时刻光线将一切笼罩在温暖中。色彩：枯草黄#8B7355（墙面），暖白#FFF8DC（修饰），琥珀灯笼，从窗户可见的翠绿花园。超精细古代庆典，电影级喜悦与希望，体积温暖光线。
```

#### 2. 提示词 2 - 花园的期待与浪漫 [花园的期待与浪漫]

**English：**
```
Cinematic still, 2.39:1 widescreen, romantic evening stroll through a newlyweds' garden. Morning glory flowers climb wooden trellises in shades of purple and pink. Fragrant osmanthus trees bloom nearby, petals drifting in soft breeze. Stone pathway winds through emerald grass. A couple walks hand-in-hand beneath cool moonlight, silhouetted against the twilight. Lantern light spills from windows behind them, casting long shadows. Color palette: deep blue #3A4A6B twilight sky, jade green grass, pink and purple flowers, warm amber light from residence. Hyper-detailed garden landscape, romantic cinema verité, hope and intimacy.
```

**中文：**
```
电影截图，2.39:1 宽幅，新婚夫妇在花园中的浪漫傍晚散步。牵牛花攀爬木棚，紫蓝与粉红盛开。香气四溢的桂花树绽放，花瓣在轻风中飘零。石板小径蜿蜒穿过翠绿草地。一对新人在月光下手牵手，剪影映衬在暮蓝天色前。窗户后的灯光洒出温暖，投出长长的影子。色彩：暮蓝#3A4A6B（天空），翡翠绿（草地），粉紫花朵，住所的琥珀光。超精细花园景观，浪漫电影式写实，希望与亲密。
```

#### 3. 提示词 3 - 新房的转折与恐怖 [新房的转折与恐怖]

**English：**
```
Cinematic still, 2.39:1 widescreen, darkened bedroom in the newlyweds' residence transforms from romantic to ominous. Red silk canopy now casts sinister shadows. Moonlight filters through windows, illuminating disheveled bed and scattered wedding garments. The bride-to-be lies motionless, face twisted in agony. An empty wine cup sits on the table—evidence of betrayal. Decorations that promised happiness now symbolize death. Cold blue #3A4A6B light mingles with dying amber from extinguished lamps. Color palette transitions from warm #FFF8DC to sickly pale. Hyper-detailed period bedroom, psychological horror atmosphere, cinematic tragedy and dread.
```

**中文：**
```
电影截图，2.39:1 宽幅，新房卧室从浪漫转为恐怖。红丝绸蚊帐投出诡异阴影。月光透过窗户，照亮凌乱的床铺与散落的婚礼衣物。新娘痛苦地蜷缩在床上，面容扭曲。桌上的空酒杯是背叛的证据。曾经象征幸福的装饰品如今预示死亡。冷蓝#3A4A6B月光与熄灭灯笼的暗琥珀交织。色彩从暖白#FFF8DC转为病态苍白。超精细古代卧室，心理恐怖氛围，电影级悲剧与恐惧。
```

### 杜金标 (characters, ★★, P5)

#### 1. 

**English：**
```
Chinese male official in his 50s, lean and wiry build, sharp piercing eyes, high cheekbones, gray-white hair neatly combed, serious expression. Wearing formal dark gray official robe with ochre-brown undertone (#8B7355), official belt, traditional official hat. Upright posture, hands clasped behind back. Plain dark background. Style: 80% realistic, 20% stylized fantasy art. Color palette: earthy ochre, dark gray, soft shadows. 35mm film quality, medium-high contrast.
```

**中文：**
```
50多岁的中国男性官员，精瘦身材，锐利的眼神，高颧骨，灰白相间的整洁短发，严肃表情。穿着规矩的深灰色官袍（带枯草黄色调 #8B7355），系着官员腰带，戴着传统官帽。挺直的身姿，双手背在身后。素色深色背景。风格：80%写实，20%风格化。色系：枯草黄、深灰色、柔和阴影。35mm胶片质感，中高对比度。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, middle-aged Chinese official sitting at official desk in a government office, surrounded by scrolls and documents. Lamplight illuminates the formal space. Serious demeanor, sharp eyes focused on administrative duties. Wearing dark gray official robes with ochre-brown undertone (#8B7355) and official hat. Traditional wooden furniture. Plain dark background with warm lamp light accents. 35mm film quality, medium-high contrast.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，中年中国官员坐在官府公务厅堂的办公桌前，周围堆放着公务竹简和文牒。灯光照亮庄重的公务空间。严肃神情，锐利眼神专注于行政事务。穿着深灰色官袍配枯草黄色调（#8B7355）和官帽。传统木制家具。素色深色背景配温暖灯光。35mm胶片质感，中高对比度。
```

### 杨伯礼 (characters, ★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a Chinese boy aged 12, delicate refined features showing noble bloodline, sharp intelligent eyes with arrogant gaze full of contempt, dark brown irises gleaming with unchecked pride, high-bridged nose inherited from father, clear pale skin with youthful sheen, black soft hair neatly cut with bangs framing forehead, elegant composed expression tinged with disdain, wearing luxurious dark gold silk shirt (#DAA520) with purple undertones (#5B3A6B), outer dark gold robe with exquisite embroidery at cuffs and collar, silver ornamental clasps, posture perfectly upright radiating arrogant nobility, plain dark background, warm soft lighting from studio emphasizing fine features and lustrous fabric, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一名12岁中国男孩的正面半身肖像，精致秀气的五官显示贵族血统，锐利聪慧的眼睛充满傲慢的轻蔑目光，深棕色虹膜闪耀着无人能挡的骄傲，高挺的鼻梁继承自父亲，清透苍白的肌肤有少年的光泽，黑色细软头发剪裁整齐额前有齐刘海，优雅沉着的表情带着不屑感，穿着华丽的暗金色（#DAA520）丝绸衣衫带紫色衬里（#5B3A6B），外披暗金色长袍在袖口和领口有精美刺绣，银色装饰扣子，身体笔直挺拔散发傲慢的贵族气质，素暗色背景，来自摄影棚的暖柔光线强调精细五官和面料的光泽感，35mm胶片颗粒感，中高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of the same 12-year-old Chinese boy now with catastrophic acid burn damage to left side of face, skin severely charred and decomposed on left side exposing underlying tissue, left eye area almost completely destroyed with severe tissue damage, left ear burnt to blackened remains, mouth corner pulled upward toward left side by scarring creating grotesque expression, right side of face showing secondary burns with blistering and swelling, hair partially singed and burnt especially on left side, pale shock-white face with patches of deep red and black from burns and blood, eyes showing extreme pain mixed with emergent rage and vengeful desperation, wearing torn dark gold robe stained with blood and caustic liquid residue, medical bandages partially visible, trembling body posture reflecting both agony and furious hatred, plain dark background, harsh cold surgical lighting that cruelly illuminates all damage and wound detail, 35mm film grain, high contrast emphasizing the horrific transformation
```

**中文：**
```
电影感静帧，2.39:1宽银幕，同一位12岁中国男孩的正面半身肖像现在呈现左脸严重的酸液灼伤创伤，左侧皮肤严重焦黑溃烂暴露下层组织，左眼眼窝周围皮肤几乎完全毁损严重的组织损伤，左耳被烧成焦黑的残余物，嘴角被疤痕扯向左上方产生狰狞的表情，右脸也显示二级烧伤有水泡和肿胀，头发部分被烧焦尤其是左侧，苍白的休克白色脸部有来自烧伤和血液的深红色和黑色斑块，眼睛显示极端的痛苦混合着新兴的愤怒和复仇的绝望，穿着被撕破的暗金色长袍上有血液和腐蚀液体残留污迹，可见医疗绷带的一部分，颤抖的身体姿态同时反映了极度的痛苦和愤怒的仇恨，素暗色背景，残酷冷酷的手术白色灯光无情地照亮所有损伤和伤口细节，35mm胶片颗粒感，高对比度强调骇人的转变
```

#### 3. 

**English：**
```
Cinematic still, 2.39:1 widescreen, interior of a noble manor room with warm ambient lighting, a 12-year-old Chinese boy stands in an imperious posture with one hand raised in a commanding gesture toward servants or companions, his expression haughty and disdainful, wearing luxurious dark gold silk clothing (#DAA520) with purple accents (#5B3A6B), pristine appearance with every detail perfectly arranged, sharp intelligent eyes gleaming with unchecked arrogance and contempt, fine features showing noble bloodline, black hair neatly arranged, standing in the center of the composition as if the world revolves around him, servants or furniture in soft focus background, warm golden lighting casting soft shadows, color palette dominated by warm golds and purples from his clothing against darker background furnishings, 35mm film grain, medium contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，贵族宅邸房间内部暖色环境灯光，一位12岁中国男孩以专制姿态站立一只手抬起做出命令手势指向仆人或同伴，表情傲慢轻蔑，穿着华丽的暗金色丝绸服装（#DAA520）带紫色装饰（#5B3A6B），整洁无缺的外表每一个细节都安排完美，锐利聪慧的眼睛闪耀着无人能挡的傲慢和轻蔑，精致的五官显示贵族血统，黑色头发梳理整齐，站在构图的中心仿佛世界围绕他旋转，仆人或家具在软焦背景中，暖色金色灯光投出柔和阴影，色调由他服装中的暖色金色和紫色主导对比背景的深色家具装饰，35mm胶片颗粒感，中等对比度
```

#### 4. 

**English：**
```
Cinematic still, 2.39:1 widescreen, dramatic moment of caustic liquid splashing across the young boy's face, his eyes wide with shock and terror transitioning to beginning pain, mouth open in a scream, left side of face beginning to show charring and tissue damage as corrosive substance makes contact, hands reflexively moving upward to protect face creating desperate motion blur, surrounding environment shows chaos - perhaps a courtyard or indoor space with caustic containers nearby, lighting shifts from warm to cold harsh emergency lighting, steam or smoke rising from the burn site, his once pristine dark gold clothing beginning to show corrosive damage and staining, the moment captures the instant a privileged young life is forever shattered, 35mm film grain, high contrast emphasizing the horror
```

**中文：**
```
电影感静帧，2.39:1宽银幕，戏剧性的腐蚀液体泼洒在少年脸上的瞬间，他的眼睛睁得很大充满震惊和恐惧逐渐转为开始的痛苦，嘴巴张开在尖叫中，左脸开始显示焦黑和组织损伤当腐蚀物质接触时，双手反射性地向上移动试图保护脸部产生绝望的运动模糊，周围环境显示混乱——也许是庭院或室内空间旁边有腐蚀液体容器，灯光从暖色转变为冷色刺眼的紧急灯光，蒸汽或烟雾从烧伤部位升起，他曾经整洁的暗金色衣物开始显示腐蚀伤害和污迹，瞬间捕捉一个特权少年的人生被永久摧毁，35mm胶片颗粒感，高对比度强调恐怖感
```

### 永安镇会议厅 (locations, ★★, P5)

#### 1. 提示词1：众人怀疑到信服的转变 [众人怀疑到信服的转变]

**English：**
```
Cinematic wide assembly hall shot, 2.39:1 widescreen, provincial town government
meeting chamber interior, hundreds of townspeople seated on rough cloth-covered
wooden benches #8B7355, dark brown wooden frames #2C1810, woman standing at
center speaking passionately to crowd, candlelight and oil lamps creating warm
glow, faces of crowd transitioning from smiling dismissal to shocked realization,
dramatic lighting emphasizing emotional transformation, shadows deepening as
evening progresses, cinematic composition of collective revelation moment
```

**中文：**
```
电影大厅宽景镜头，2.39:1宽银幕，小镇政府会议厅内景，
数百镇民坐于粗麻布覆盖的木凳 #8B7355，暗褐木框 #2C1810，
女性站于中心向众人激情陈述，烛火与油灯温暖光晕，
众人脸部从嘲笑不屑到震撼认知的转变，
戏剧化光线强调情感转折，夜幕降临阴影加深，
电影构图呈现集体启蒙时刻的转折
```

#### 2. 提示词2：凌晨紧急会议的沉重 [凌晨紧急会议的沉重]

**English：**
```
Cinematic night meeting shot, 2.39:1 widescreen, emergency assembly chamber
at 1-2 AM, dimly lit by flickering oil lamps and candles, tired and anxious
townspeople seated haphazardly, witness standing to give testimony with grave
expression, wooden chairs and rustic decor #8B7355 and #2C1810, deep shadows
from insufficient lighting creating ominous atmosphere, serious faces of
administration officials, cinematic chiaroscuro emphasizing gravity of decision,
moment of collective despair and acceptance
```

**中文：**
```
电影夜间会议镜头，2.39:1宽银幕，凌晨1-2点紧急集会厅，
油灯与蜡烛摇曳微光照亮，疲惫与焦虑的镇民仓促而坐，
证人站起沉重表情作证，木椅与素朴装饰 #8B7355 与 #2C1810，
灯光不足投出深邃阴影营造不祥氛围，行政官员严肃脸孔，
电影级明暗对比强调决议的沉重，集体绝望与接纳的时刻
```

#### 3. 提示词3：镇长的权力与责任 [镇长的权力与责任]

**English：**
```
Cinematic authority figure portrait, 2.39:1 widescreen, town mayor standing
at podium in dimly lit assembly chamber, oil lamps illuminating his face from
below creating dramatic shadows, wooden architectural elements brown #8B7355
and dark #2C1810, hundreds of townspeople seated before him waiting for decision,
moment of bearing unbearable weight of entire town's fate, resolved expression
mixed with hidden despair, cinematic lighting emphasizing lonely burden of
leadership, chiaroscuro portrait of necessary cruelty
```

**中文：**
```
电影权力人物肖像，2.39:1宽银幕，镇长站于讲演台，
昏暗会议厅内油灯从下方照亮面部投出戏剧化阴影，
木质建筑褐色 #8B7355 与暗色 #2C1810，
数百镇民坐下等候决议，承载全镇命运的沉重时刻，
坚定表情混合隐没的绝望，电影光线强调领导孤独负担，
明暗对比呈现必要残酷的肖像
```

#### 4. 提示词4：全镇撤离决定的关键时刻 [全镇撤离决定的关键时刻]

**English：**
```
Cinematic decision moment, 2.39:1 widescreen, final announcement in provincial
assembly chamber, town official announcing mass evacuation order, townspeople
faces showing crying, protest, resignation mixed together, wooden benches
#8B7355, dark frames #2C1810, oil lamps casting long shadows across room,
collective despair atmosphere, moment when private family survival becomes
impossible and collective evacuation becomes only option, cinematic gravity
and inevitability, faces of parents, children, elderly reflecting hopeless
decision
```

**中文：**
```
电影决议时刻，2.39:1宽银幕，小镇会议厅最终宣言，
官员宣布全镇撤离令，镇民脸部显露哭泣、抗议、
认命的混合情绪，木凳 #8B7355，暗色框 #2C1810，
油灯投出长长阴影跨越厅堂，集体绝望氛围，
从个人家庭逃亡转向全镇集体行动的唯一选择时刻，
电影级的沉重感与必然性，父母、儿童、老人脸部
反映绝望决议的重量
```

### 永安镇客栈 (locations, ★★, P5)

#### 1. 提示词1：二楼走廊的压抑 [二楼走廊的压抑]

**English：**
```
Cinematic hallway shot, 2.39:1 widescreen, dimly lit cheap inn corridor,
low ceiling creating claustrophobic atmosphere, faded brown wooden walls
#8B7355, dark brown doorframes #2C1810, dusty air with minimal lighting,
multiple room doors lining both sides, single weak candlelight source,
deep shadows in corners and between doors, worn wooden floorboards showing
age and wear, sense of danger and isolation, oppressive narrow space,
moody cinematic lighting emphasizing dread
```

**中文：**
```
电影走廊镜头，2.39:1宽银幕，廉价客栈昏暗走廊，
低矮天花板营造幽闭压抑感，褪色褐色木墙 #8B7355，
焦褐木门框 #2C1810，尘埃浓重空气与极弱照明，
两侧多个房门排列，单一微弱烛光光源，
角落与门之间深邃阴影，磨损木地板显露年代感，
危险与孤立感，压抑狭窄空间，
阴郁电影级光线强调恐惧感
```

#### 2. 提示词2：房间内的惊恐时刻 [房间内的惊恐时刻]

**English：**
```
Cinematic close-up, 2.39:1 widescreen, cheap inn room interior at night,
person huddled on worn bed under rough blanket, ears alert listening through
thin wooden wall to adjacent room, faint candlelight casting dancing shadows,
faded brown fabric #8B7355 and dark wood #2C1810, cramped space with minimal
furniture, vulnerable posture contrasting with environment, psychological
tension visible in body language, shallow depth of field on fearful expression,
intimacy of dread and isolation
```

**中文：**
```
电影近景镜头，2.39:1宽银幕，廉价客栈房间夜景，
人物蜷缩在破旧床铺粗糙棉被下，耳朵竖起侧听隔壁薄墙，
微弱烛光投出摇曳阴影，褪色褐布 #8B7355 与暗木 #2C1810，
局促狭窄空间简陋家具，脆弱身姿与环境对比强烈，
心理紧张通过身体语言显现，浅景深聚焦恐惧表情，
恐惧与孤立的亲密感
```

#### 3. 提示词3：薄墙隔断的恐怖 [薄墙隔断的恐怖]

**English：**
```
Cinematic two-room split-screen or parallel composition, 2.39:1 widescreen,
thin wooden partition wall separating two cheap inn rooms, both dimly lit,
silhouettes of two people on opposite sides of wall barely separated,
one listening intently, other moving menacingly, worn brown wood #8B7355,
dark frames #2C1810, sound implications of danger penetrating thin barrier,
psychological thriller aesthetic, claustrophobic composition, suspended
anticipation, hunter and prey separated by paper-thin wall, cinematic tension
```

**中文：**
```
电影分屏或平行构图，2.39:1宽银幕，廉价客栈两间房间
被薄木板隔断分离，两个房间都昏暗照明，
两侧人形剪影几乎紧靠分隔墙，一个专注侧听，
一个威胁般移动，褪色褐木 #8B7355，暗色框 #2C1810，
危险声音穿过薄墙屏障的心理含义，心理惊悚美学，
幽闭压抑的构图，悬念倒计时，猎与被猎仅隔纸墙，
电影级紧张感
```

#### 4. 提示词4：逃离时刻的蹑手蹑脚 [逃离时刻的蹑手蹑脚]

**English：**
```
Cinematic action moment, 2.39:1 widescreen, figure slowly opening door in
complete darkness and silence, hand gripping door handle with tension,
old wooden door creaking slightly, faded brown interior #8B7355, dark
frame #2C1810, hallway darkness beyond partially visible, every motion
deliberate and terrified, slow-motion aesthetic of escape attempt, minimal
lighting suggesting pre-dawn or candlelight, cinematic suspense in mundane
action, footstep about to happen implying extreme danger
```

**中文：**
```
电影动作时刻，2.39:1宽银幕，人物在完全黑暗中缓缓推门，
手握门把手紧张用力，老旧木门微微吱呀，
褪色褐色内室 #8B7355，暗色木框 #2C1810，
走廊黑暗部分可见，每一个动作都刻意与恐惧，
逃离尝试的慢动作美学，极弱光线暗示天将亮或烛光，
日常动作中的电影级悬念，即将踏出暴露位置的极度危险感
```

### 江新成宅邸 (locations, ★★, P5)

#### 1. 提示词 1 - 官邸日常 [官邸日常]

**English：**
```
Cinematic still, 2.39:1 widescreen, interior of traditional official's residence in ancient fortress city. Sunlit front hall with stone floor and hanging scrolls depicting maps and achievements. Ornate wooden pillars support high ceiling. A city magistrate sits at the central desk, reviewing documents in soft golden light. Attendants move quietly through doorways. Color palette: dried grass yellow #8B7355 for walls, deep red #8B1A1A for lacquered pillars, amber for sunlight. Hyper-detailed period architecture, cinematic government building atmosphere, volumetric dust particles.
```

**中文：**
```
电影截图，2.39:1 宽幅，古堡城市官邸内部日常。日光洒满前堂，石板地面与悬挂的地图及功绩册。华美木梁支撑高天花。官员坐在中央案前，在柔和金光下审阅奏折。侍从静静穿梭门廊间。色彩：枯草黄#8B7355（墙面），暗红#8B1A1A（漆柱），琥珀（日光）。超精细古代建筑，电影级官府氛围，体积尘埃粒子。
```

#### 2. 提示词 2 - 夜幕与危机 [夜幕与危机]

**English：**
```
Cinematic still, 2.39:1 widescreen, dark bedroom chamber within official's residence. Moonlight filters through silk curtains, casting diffuse shadows on the bed canopy. Oil lamps glow weakly in corners. The magistrate lies motionless on the bed, eyes suddenly opening with an unsettling intensity. Something ancient and alien stirs within him. Color palette: deep burgundy #8B1A1A from candlelight, twilight blue #3A4A6B from moonlight, dark silhouettes. Hyper-detailed period bedroom, ominous supernatural atmosphere, cinematic dread.
```

**中文：**
```
电影截图，2.39:1 宽幅，官邸内的黑暗卧室。月光透过丝绸窗帘洒下，在床幔上投出扩散的阴影。油灯在角落微弱发光。官员躺在床上，突然睁眼，眼神中闪过诡异的光芒。某种古老而陌生的东西在他体内苏醒。色彩：烛光映出的深红#8B1A1A，月光的暮蓝#3A4A6B，黑色剪影。超精细古代卧室，不祥的超自然氛围，电影级恐怖感。
```

#### 3. 提示词 3 - 侵入与转折 [侵入与转折]

**English：**
```
Cinematic still, 2.39:1 widescreen, shadowy figure moving through the rear garden and kitchen doorway of the official's residence at dusk. Warm amber light spills from the kitchen window, but the intruder remains in darkness. Stone pathway leads deeper into danger. The back yard looms with ominous purpose. Color palette: dried grass yellow #8B7355, dark silhouettes, amber kitchen light, deep shadow blue. Hyper-detailed period architecture, psychological thriller atmosphere, cinematic tension and foreboding.
```

**中文：**
```
电影截图，2.39:1 宽幅，黑暗身影在暮色中穿过官邸后花园与厨房侧门。温暖琥珀光从厨房窗户溅出，但入侵者埋藏在黑暗里。石板路延伸入危险深处。后院笼罩在凶险的意图中。色彩：枯草黄#8B7355，黑色剪影，琥珀厨房光，深蓝阴影。超精细古代建筑，心理惊悚氛围，电影级张力与不祥之感。
```

### 泊岗镇1200居民 (characters, ★★, P5)

#### 1. 

**English：**
```
Bobang Town 1200 possessed residents group portrait close-up perspective: multiple residents of different ages and genders in dense arrangement, all with identical expressions—empty rigid 0-shaped mouths, eyes dilated into deep black pupils, purple-tinted blood vessel networks in eye whites, skin showing sickly grayish-white tone, muscles completely slack as if post-mortem stiffening, multiple faces tightly adjacent in grid arrangement, overall atmosphere silent and terrifying, detail emphasis: vacant eyes, unnatural head tilt angles, dark purple energy lines coiling around necks, cold harsh lighting, no life signs, realistic oil painting style, oppressive despair.
```

**中文：**
```
泊岗镇1200被附身居民群像肖像，密集排列视角：多个不同年龄和性别的镇民脸部特写，表情完全相同——空洞僵硬的零字型嘴，眼睛扩散成深黑色瞳孔，眼白处浮现暗紫色血丝网络，肌肤呈现病态灰白色，肌肉完全松弛，仿佛死后僵直，多张脸紧密相邻排列，整体氛围寂静恐怖，细节强调：失神的眼神、不自然的头颅倾斜角度、暗紫色能量线缠绕在脖颈，灯光冷酷惨白，无任何生命迹象，真实油画风格，压抑绝望。
```

#### 2. 

**English：**
```
Bobang Town collective possession scene: entire town square filled with 1200 soulless puppets arranged in perfect grid formation, spacing completely uniform (1.5m apart), all adopting identical posture—arms hanging down, spine curved unnaturally, heads slightly tilted back, expressions uniformly vacant, skin color uniformly grayish-white, entire town shrouded in cold blue eerie light, oppressive dim sky, distant decaying town buildings, withered plants, dark purple energy lines in air (connecting 1200 people to five spirits) forming spider web structure, 1200 people simultaneously synchronized breathing (white mist rhythm consistent), completely silent, like cellular tissue of giant organism. Details: neck rotation fracture marks, synchronized eye blink wet luster, perfectly uniform footstep sounds. Extremely eerie, oppressive, despairing atmosphere.
```

**中文：**
```
泊岗镇集体附身场景：整个小镇广场被1200个失魂傀儡填满，人物排成完美的网格阵列，间距完全相同（1.5米），所有人采用同一姿势——双臂下垂、脊椎弯曲、头部微后仰、表情一致的空洞，肤色统一的灰白色，整个镇子笼罩在冷蓝色的诡异光线中，天空压抑昏暗，远景是破败的镇子建筑，植物枯萎，空气中弥漫暗紫色的能量线（连接1200人与五灵）形成蜘蛛网状结构，1200个人同时进行统一的呼吸（白雾节奏一致），完全无声，宛如一个巨大有机体的细胞组织。细节：脖颈转向时的骨裂痕迹、眼睛同步眨动时的湿润光泽、整齐划一的脚步声。极度诡异、压抑、绝望的氛围。
```

### 泥垛子建筑 (props, ★★, P5)

#### 1. 

**English：**
```
Rammed-Earth Cottage / Adobe Block Architecture
```

**中文：**
```
泥垛子建筑 / 夯土山居
```

#### 2. 提示词1 - 山地泥垛子建筑外观 [山地泥垛子建筑外观]

**English：**
```
Cinematic still, 2.39:1 widescreen, wide shot of ancient rammed-earth cottage on hillside,
warm brown tones #2C1810 and #6B4423, weathered adobe walls with visible layered texture,
broken windows and wooden door frame, worn tiled roof with moss patches, muted natural palette,
harsh golden hour light casting long shadows, 35mm film grain, gritty rustic aesthetic,
mountain backdrop, isolated lonely dwelling
```

**中文：**
```
电影质感，2.39:1宽屏，山坡古老夯土山居远景，温暖褐色#2C1810与#6B4423色调，
风化的泥土墙壁露出清晰的分层夯筑纹理，破损窗框与木质门框，
磨损瓦顶覆青苔，黯淡自然色调，金色时段光线投射长阴影，
35mm胶片颗粒感，粗糙乡村美学，山景背景，孤立冷清的居所
```

#### 3. 提示词2 - 泥垛子建筑内部空间 [泥垛子建筑内部空间]

**English：**
```
Cinematic still, 2.39:1 widescreen, interior view of rammed-earth cottage living room,
clay and earth walls in brown #6B4423 and tan #8B7765, rough organic texture,
sparse wooden furniture, broken window with scattered light patterns on floor,
dim natural lighting, dusty atmosphere, 35mm film grain, desaturated earth tone palette,
gritty weathered interior space, isolation and solitude mood
```

**中文：**
```
电影质感，2.39:1宽屏，泥垛子山居内厅空间，粘土泥土墙壁呈褐#6B4423与驼褐#8B7765，
粗糙有机纹理，稀疏木质家具，破窗洒落分散光斑于地面，
昏暗自然光线，尘埃氛围，35mm胶片颗粒感，去饱和土色调，
粗糙风化的内部空间，孤独隐居的情绪
```

### 灵王 (characters, ★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a stern Chinese male underworld bureaucratic official. Square jaw, narrow dark eyes gazing downward with condescending authority but lacking true insight, thick straight eyebrows barely moving, tightly pressed thin lips with corners turned slightly down, pale skin with a subtle twilight-blue (#3A4A6B) luminous undertone. Hair combed back immaculately, possibly wearing an ornate dark official's headpiece. Wearing formal dark robes in twilight blue (#3A4A6B) with dark gold (#DAA520) trim along collar and cuffs indicating administrative rank. Expression is cold, procedural, and utterly devoid of warmth. Hands clasped formally in front. Plain dark background with faint blue ambient glow suggesting the underworld realm. 35mm film quality, medium-high contrast, desaturated cool tones.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一位威严刻板的华人男性阴间行政官员正面半身肖像。方正下颌，狭窄深色双眼居高临下地俯视但缺乏真正洞察力，浓黑平直眉毛几乎不动，薄唇紧抿嘴角微微下压，苍白皮肤带有微妙的暮蓝色（#3A4A6B）荧光底色。头发一丝不苟地梳向脑后，可能佩戴精致深色官帽。着暮蓝色（#3A4A6B）深色正式官服，领口袖口饰有暗金色（#DAA520）纹饰标识行政等级。表情冷漠程序化完全没有温度。双手正式交叠于身前。素色深色背景带微弱蓝色环境光暗示阴间领域。35mm胶片质感，中高对比度，去饱和冷色调。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, a stern Chinese male underworld bureaucratic official seated behind a formal dark wooden desk in an underworld administrative chamber. He sits upright with perfect posture, hands clasped on the desk surface, narrow dark eyes looking down at a subordinate with condescending authority. Wearing formal twilight-blue (#3A4A6B) robes with dark gold (#DAA520) trim. The desk is immaculately organized with scrolls and official seals. Cold blue ambient lighting from unseen sources creates deep shadows. The atmosphere is oppressive and procedural. Plain dark background. No warmth in the scene — pure bureaucratic authority. 35mm film quality, desaturated cool palette, medium-high contrast.
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一位威严的华人男性阴间行政官员端坐在阴间行政厅的深色木制公案后。坐姿完美挺直，双手交叠于桌面，狭窄深色双眼居高临下地审视下属。着暮蓝色（#3A4A6B）正式官服配暗金色（#DAA520）纹饰。桌面整洁有序摆放着卷轴和官印。来自不可见光源的冷蓝环境光制造深沉阴影。氛围压抑而程序化。素色深色背景。场景毫无温度——纯粹的官僚权威。35mm胶片质感，去饱和冷色调，中高对比度。
```

### 熊大宝 (characters, ★★, P5)

#### 1. 

**English：**
```
A 20-year-old emaciated male youth, half-body frontal view, plain face filled with terror. Eyes unfocused, dilated pupils, expressionless mouth, pallid complexion lacking blood color. Shoulders hunched inward, sunken chest, showing severe malnutrition. Wearing tattered clothes with irregularly distributed patches, faded fabric, noticeably worn collar and cuffs. Slender trembling fingers, dirt under fingernails. Deep dark circles under eyes, disheveled hair. Overall color palette dominated by dry grass yellow #8B7355, combined with gray-brown shadows, dim lighting, muted background, no pure white elements. Atmosphere oppressive and melancholic, embodying the despair of war trauma.
```

**中文：**
```
一个20岁的瘦弱男青年，正面半身，面容普通但充满惊恐。眼神散焦，瞳孔扩张，嘴角无弧度，面色苍白缺血色。肩膀内缩，胸腔凹陷，显示严重营养不良。身穿破烂衣物，多处补丁不规则分布，布料褪色，领口袖口磨损明显。手指纤细颤抖，指甲有泥土痕迹。眼周有深色黑眼圈，头发蓬乱。整体色调以枯草黄#8B7355为主，配合灰褐阴影，光线昏暗，背景素雅，无纯白元素。氛围压抑沧桑，承载战争创伤的绝望感。
```

#### 2. 

**English：**
```
In the ruins of Qingping Town, a corner of a dilapidated house. The emaciated male youth sits curled on the ground, back leaning against a cracked stone wall, knees drawn up, arms hugging knees. Vacant eyes gazing into the distance, filled with terror and despair. Scattered rubble and dust surround him, haze permeating the air. Light filters through a broken window, casting diagonal dim shadows. Clothing appears dry grass yellow in the shadows, blending with the gray-brown ruins. Overall image dull and dark, no bright colors, no pure white elements. The figure appears extremely fragile, as if about to be consumed by this shattered world.
```

**中文：**
```
清平镇的废墟中，一间残破房屋的角落。瘦弱男青年蜷缩坐在地上，背靠断裂的石墙，膝盖拉起，双臂抱膝。眼神空洞注视远方，充满惊恐与绝望。周围散落残砖碎瓦，烟尘弥漫。光线从破损窗户透入，形成斜暗的光影。衣物在阴影中呈现枯草黄，与灰褐废墟融为一体。整体画面沉闷灰暗，无鲜艳色彩，禁用纯白。人物显得极度脆弱，仿佛即将被这个残破的世界吞噬。
```

### 王轻无 (characters, ★★, P5)

#### 1. 

**English：**
```
An East Asian male officer in his 30s-40s with an honest face and earnest eyes.
Wearing a simple military uniform predominantly in dark gold (#DAA520) with accents of moss green (#5F7A61).
Broad shoulders, upright military posture, blank expression concealing subtle moral hesitation.
Clear eyes with a hint of introspective melancholy, embodying the conflict between professional duty and humanity.
Minimalist background. Lighting from top-left creates contemplative shadows on face.
No pure white. Overall: a conscientious military officer within the system.
```

**中文：**
```
一位30-40岁的东方男性副官，诚实面容、恳切眼神。穿着简朴的军装，
以暗金色为主色调（#DAA520），点缀苔绿色（#5F7A61）细节。
肩膀宽阔，军姿挺直，面无表情中透露细微的道德犹豫。
眼神清晰但含有内敛的忧虑，显示职业军人的沉着与人性的冲突。
背景简洁，避免分散注意力。光线从左上打来，在脸部投射出思考的阴影。
禁用纯白色。整体气质：体制内有良知的军人。
```

#### 2. 

**English：**
```
Interior of General's tent. Wang Qingwu stands to the side with upright posture
but downcast eyes, suggesting obedient yet morally conflicted demeanor. Background
shows military tent interior with dark gold flags and moss green fabric interweaving.
Candlelight illuminates his honest face; moral dilemma flickers in his eyes.
Military maps and battle reports nearby emphasize his adjutant role. Other soldiers
blur in background, highlighting his middle-management position in the hierarchy.
Atmosphere: tense yet restrained.
```

**中文：**
```
杨弘帐篷内部场景。王轻无站在将军帐的一侧，身体挺直但眼神向下微敛，
显示听命但心存疑虑的姿态。背景是军营帐篷的内部，暗金色的军旗与
苔绿色的帐篷布料交织。烛火映照在他诚实的面容上，眼神中隐现道德困境。
身旁摆放着军事地图与战报，显示其副官身份。其他士兵在背景模糊处，
突出王轻无作为权力结构中间层的地位。气氛：紧张但克制。
```

### 红领巾 (props, ★★, P5)

#### 1. 

**English：**
```
Red Neckerchief / Red Armband
```

**中文：**
```
红领巾 / 红色识别标志
```

#### 2. 提示词1 - 红领巾细节特写 [红领巾细节特写]

**English：**
```
Cinematic still, 2.39:1 widescreen, extreme close-up of red cloth neckerchief
tied loosely around neck, dark red #8B1A1A fabric with visible cotton weave,
soft folds and wrinkles, weathered edges, subtle dirt marks and creases,
natural daylight, 35mm film grain, muted earth tone color grading,
rough artisanal texture, isolated against soft blurred background
```

**中文：**
```
电影质感，2.39:1宽屏，红领巾特写镜头，系于脖颈处，暗红#8B1A1A棉布材质，
清晰纺织纹理与布料褶皱，磨损的边缘，细微的污渍与皱褶痕迹，
自然日光照明，35mm胶片颗粒感，黯淡土色调分级，粗糙天然材质质感，
孤立于柔和虚化背景前
```

#### 3. 提示词2 - 通行检查场景 [通行检查场景]

**English：**
```
Cinematic still, 2.39:1 widescreen, character wearing red neckerchief passing through
checkpoint, low-angle view showing fabric detail and knotwork, worn fabric texture,
muted colors, dim outdoor lighting, 35mm film grain, rough weathered aesthetic,
checkpoint gate in soft focus background, tense atmosphere
```

**中文：**
```
电影质感，2.39:1宽屏，角色佩戴红领巾通过检查点场景，低角度展现布料细节与结扣工艺，
磨损的布料质感，黯淡色调，暗弱室外光线，35mm胶片颗粒感，粗糙苍白的美学风格，
背景检查点大门虚化，紧张氛围渲染
```

### 苏伟力 (characters, ★★, P5)

#### 1. 

**English：**
```
A cold and composed man in dark suit, appearing around 40 years old, with deep and emotionless eyes. Ancient evil spirit inhabiting a modern human body; posture is upright and coordinated. Pale complexion suggesting non-human nature. Background filled with fleeting dark purple spiritual light (#5B3A6B) and dark red battle aura (#8B1A1A). Lighting from upper left emphasizes cold majesty. Expressionless face, gaze directed forward, exuding absolute dominance. Black minimalist clothing, no warm color tones.
```

**中文：**
```
身穿深色西装的冷酷男性，年约40岁，眼神深邃而无温度。古代恶灵附身现代人体，肢体姿态挺直而协调。肌肤略显苍白，透出非生人特质。背景为暗紫色灵光闪现（#5B3A6B）与暗红色战气（#8B1A1A）的混杂氛围。光线从左上方打来，强调其冷酷威仪。无面部表情，目光直视前方，给人绝对压迫感。黑色简洁着装，避免任何温暖色彩。
```

#### 2. 

**English：**
```
In a dark hall, the ancient general (do not use real name) stands in dark suit, body slightly turned sideways, one hand pointing forward issuing commands. Blurred silhouettes of evil spirits surround him, flickering in dark purple spiritual light (#5B3A6B). His movements are precise and restrained, reflecting ancient general's tactical wisdom. Dark red battle aura (#8B1A1A) reflects on the ground, intensifying war atmosphere. Background blends ancient palace and modern architecture. Dim background lighting with only purple-red spirit light illuminating the scene. Cold, oppressive, and professional visual effect.
```

**中文：**
```
暗色大厅内，苏伟力(不用真名)穿深色西装站立，身体微微侧身，单手指向前方下达命令。其周围环绕着模糊的恶灵士兵轮廓，在暗紫色灵光（#5B3A6B）中若隐若现。其肢体动作精确而克制，透出古代将领的战术思维。地面倒映出暗红色的战气（#8B1A1A），强化战争氛围。背景为古代宫殿与现代混杂的建筑。远处光线昏暗，仅有紫红色灵光照亮现场。冷调、压抑、专业的视觉效果。
```

### 茶馆 (locations, ★★, P5)

#### 1. 

**English：**
```
A dimly lit teahouse interior in a provincial town. Low wooden tables surrounded by worn cushioned seating. Oil lamps cast amber shadows across the space, barely illuminating corners shrouded in darkness. Weathered wooden walls stained with years of smoke and neglect. Two figures sit in intimate proximity across a low table, steam rising from tea cups. The atmosphere is suffused with muted saddle-brown and deep charcoal tones. Shadows define the edges of the space more than light. A sense of tension and whispered confession permeates the scene. Shot from a side angle, emphasizing the psychological weight of the moment.
```

**中文：**
```
镇上昏暗的茶馆内景。低矮木桌周围排列着破旧的蒲团座椅。油灯投射琥珀色阴影，几乎无法照亮笼罩在黑暗中的角落。风化的木质墙壁因多年烟火和疏于打理而泛起污迹。两个身影在低矮的茶桌前近距离相对而坐，茶杯中升起水蒸气。整个空间充满沉郁的鞍褐色与焦褐色调。阴影比光线更能定义空间的边界。紧张与低语忏悔的心理氛围弥漫全场。从侧面角度拍摄，强调这一时刻的心理重量。
```

### 葛有利 (characters, ★★, P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, front-facing bust portrait of a young Chinese military leader in his late twenties, strong angular face with sharp unwavering eyes full of resolve and authority, sun-tanned weathered skin showing years of outdoor combat and training, short dark hair with possible early grey streaks, muscular fit build visible in shoulders and neck, wearing simple dull brown or dark grey rough cloth military garment typical of resistance forces, no ornate decorations, showing visible wear and battle scars, hands with visible calluses and possible old wounds signifying combat experience, stern mouth with determined expression, warrior bearing evident in posture and gaze, realistic style emphasizing hardened but principled young leader, professional headshot, strong dramatic lighting with cool tones reflecting leadership and resilience, 85% realism with 15% heroic quality suggesting unwavering conviction, 35mm film grain, medium-high contrast
```

**中文：**
```
电影感静帧，2.39:1宽银幕，一位二十八九岁年轻中国军事领导者的正面半身肖像，棱角分明的脸部线条，眼神锐利坚定充满权威感和不可动摇的意志。肤色深沉显示多年户外战斗与训练的痕迹，短发或露额头发型，可能有早期白发。肌肉线条分明的肩膀和颈部显示强健体格。身穿简朴的深褐或深灰色粗布军装，是抵抗军的典型服饰，无华丽装饰，衣着显示战斗痕迹。双手可见明显老茧与旧伤，象征身经百战。嘴角坚毅表情严肃，战士气质在姿态和眼神中充分呈现。写实风格强调硬朗而有原则的年轻领导者形象。专业人物定妆照，强烈戏剧光线采用冷色调反映领导力与坚韧。85%写实+15%英雄气质强调不可动摇的信念。35mm胶片颗粒感，中高对比度
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen, tense diplomatic meeting scene in a mountain stronghold or war council chamber, young resistance leader with sharp eyes and weathered face standing with military bearing, hands at sides or gestures showing quiet confidence and command, surrounded by his own troops visible in background suggesting group authority, facing off with or negotiating with powerful figures representing larger forces, interior space with rustic stone or wooden elements showing mountain resistance hideout, low dramatic lighting casting long shadows, warm brown and grey tones (#8B7355 predominant) mixed with cooler shadow tones, tension visible in focused gazes and measured body language, both figures showing mutual respect despite being from different power camps, moment of crucial decision or alliance-forming, 80% realism with 20% historical drama atmosphere suggesting pivotal moment in larger conflict, cinematic composition emphasizing gravity and consequence, warm interior lighting with cold outdoor shadows visible through windows hinting at larger war beyond
```

**中文：**
```
电影感静帧，2.39:1宽银幕，山区堡垒或战争议事厅内的紧张外交会谈场景。年轻抵抗军首领眼神锐利脸部沧桑，身体挺直显示军人气质，双手自然垂于身侧或做出有力手势传达沉着自信与指挥力。身后可见自己的队伍象征集团权威。与代表更大势力的人物面对或谈判。室内为山区抵抗营的典型布置——粗糙的石墙或木制结构，光线低暗投射长影营造戏剧张力。以枯草黄 #8B7355、深褐与灰色为主的温暖色调混合冷色阴影。专注的眼神与节制有力的身体语言显示紧张气氛，双方都表现出相互尊重尽管来自不同阵营。这是关键的决策与联盟成形时刻。80%写实+20%历史戏剧氛围暗示宏大冲突中的枢纽时刻。电影级构图强调沉重与后果。室内温暖光线，窗外可见冷色户外阴影暗示更大的战争在外
```

### 郑伟玉 (characters, ★★, P5)

#### 1. 

**English：**
```
A young male civilian from Dingda City in his early twenties, with a thin and lean build. Frontal upper-body portrait. His expression shows deep anxiety and apprehension, with flickering eyes and trembling features reflecting the sufferings of war. He wears plain gray cloth garments, simple and worn. His posture is slightly hunched, shoulders tense. Color palette: withered straw yellow (#8B7355) as the primary color, with muted grayish-brown (#A89080) for his clothing, conveying poverty, loss, and the ravages of wartime. Realistic style with somber tone. No pure white (#FFFFFF) in the background.
```

**中文：**
```
定达城的平民青年，20出头，瘦弱中等身材。正面半身像。表情焦虑惶恐，目光闪烁，面容透露出战争带来的苦难与失意。穿着灰布平民服装，简陋破旧，略显贫困。身体语言显现出紧张与不安，双肩微耸，姿态收缩。色彩体系采用枯草黄（#8B7355）作为主色调，辅以沉灰色（#A89080）的衣着，营造出贫困、失意、沧桑的视觉基调。写实风格，沉郁沉闷的氛围。背景禁用纯白（#FFFFFF）。

### B - 场景：战争后期城市困境
```

#### 2. 

**English：**
```
A scene depicting the suffering of ordinary people in Dingda City during the late stages of war. A thin young man in gray cloth garments stands amid the ruins or crowded streets, his anxious expression reflecting despair. The surroundings show signs of war destruction—ruined buildings, sparse crowds, or chaos. The color palette centers on withered straw yellow (#8B7355) and muted browns, creating a sense of devastation and hardship. The young man's body language shows tension and powerlessness. Realistic style with a somber, oppressive atmosphere capturing the desperation of ordinary civilians caught in wartime turmoil.
```

**中文：**
```
战争后期定达城普通民众生存困境的场景。一位身穿灰布平民服装的瘦弱年轻男子站在废墟或拥挤的街道中，焦虑惶恐的表情反映出绝望与无奈。周围环境显现出战争的痕迹——破损的建筑、稀疏的人群或混乱的街景。色彩体系以枯草黄（#8B7355）和沉闷的褐色调为主，营造出战争摧残与苦难的视觉氛围。年轻男子的身体语言展现出紧张与无力感。写实风格，沉郁压抑的氛围，真实捕捉普通民众在战争中的困顿与绝望。

---

## 创作笔记

### 人物意义
- **时代缩影**：郑伟玉以个体身份代表了战争后期普通民众的集体处境
- **视角转换**：从宏观战争叙事转向微观民众困难，提供人文关怀的视角
- **情感代入**：通过这样一个小人物，让读者感受历史对个人的真实冲击

### 设计要点
- **视觉统一**：枯草黄色系贯穿始终，强化"平民、贫困、失意"的身份标签
- **表现力聚焦**：虽然出场仅2章，但通过高度集中的视觉与心理特征确保记忆点
- **故事功能**：作为"众生相"的一个切面，为宏大叙事增添人性温度

### 叙事约束
- 出场严格限定在第67-68章
- 不参与主要冲突，保持边缘化地位
- 重点体现时代困境而非个人传奇

---

*文件创建于：2026-02-23*
*字数等级：★★☆☆☆ | 出场2章 | 格式：8章制*
```

### 郝大川破败小屋 (locations, ★★, P5)

#### 1. 

**English：**
```
A derelict wooden cottage isolated on a barren hillside. Roof severely damaged with gaping holes allowing pale twilight to filter through. Walls cracked and warped, paint peeled to expose rotting timber. Interior sparse and decrepit—a collapsed bed frame, overturned table, cold stone hearth. Floor boards buckled and water-stained. Shadows dominate the space in deep charcoal and burnt umber tones. A figure sits motionless in the corner, dwarfed by decay. Outside, no signs of habitation for miles. The atmosphere is one of profound abandonment and temporal stasis. Shot from exterior angle, emphasizing the cottage's isolation and final desolation.
```

**中文：**
```
荒凉山坡上一栋破败的木质小屋孤立伫立。屋顶严重受损，露出大片漏洞让苍白的黄昏光线透入。墙体开裂翘曲，油漆剥落露出腐烂的木料。室内家具残破——坍塌的床架、翻倒的桌子、冰冷的石质炉膛。地板起翘、布满水渍。焦褐色与暮蓝色的阴影主导整个空间。一个身影蜷缩在角落，被衰落包围。室外数英里内无任何人迹。整个场景散发出深沉的被遗弃感和时间停滞的绝望。从外部角度拍摄，强调小屋的隔离与最终的荒凉。
```

### 铁链 (props, ★★, P5)

#### 1. 

**English：**
```
Iron Chain / Shackle Chain
```

**中文：**
```
铁链 / 囚禁铁链
```

#### 2. 提示词1 - 铁链特写纹理 [铁链特写纹理]

**English：**
```
Cinematic still, 2.39:1 widescreen, extreme close-up of heavy iron chain links,
dark grey #3A3A3A with rust orange #B85C3C patches, rough hammered texture,
deep corrosion marks and pitting, weathered metal surface, harsh directional lighting,
35mm film grain, cold industrial color grading, no reflections, raw metal aesthetic
```

**中文：**
```
电影质感，2.39:1宽屏，重型铁链链节极近景，深灰#3A3A3A色调配锈橙#B85C3C纹理，
粗糙锻造纹理与敲打痕迹，深深的腐蚀凹陷与点蚀，风化的金属表面，
强烈定向光照，35mm胶片颗粒感，冷色工业级分级，无镜面反射，原生金属美学
```

#### 3. 提示词2 - 监禁场景中的铁链 [监禁场景中的铁链]

**English：**
```
Cinematic still, 2.39:1 widescreen, heavy iron chain wrapped around character's wrist
and torso, taut metal links under tension, rust-patched surface, casting dark shadow,
dim dungeon lighting with single light source, 35mm film grain, desaturated color palette,
mood of confinement and despair, weathered texture detail, gritty aesthetic
```

**中文：**
```
电影质感，2.39:1宽屏，沉重铁链缠绕角色腕部与躯干，紧张的金属链节，
锈蚀的表面，投射深色阴影，昏暗牢房光线配单一光源，35mm胶片颗粒感，
去饱和色调，禁锢与绝望的情绪氛围，风化的纹理细节，粗糙原始美学
```

### 集市 (locations, ★★, P5)

#### 1. 

**English：**
```
A crowded village marketplace at midday. Weathered stalls display dried produce and faded cloth beneath patchy canvas coverings. Earth-toned ground scattered with trampled remnants. Dense crowds of figures moving between stalls, creating visual chaos. Dappled sunlight filtering through makeshift awnings casts broken shadows across the scene. Warm dusty atmosphere, faded khaki and ochre tones dominating. A single figure visible for a moment before disappearing into the crowd—the essence of chaos providing concealment. Shot from elevated angle showing the overwhelming density of people and stalls.
```

**中文：**
```
正午时分的村镇集市，拥挤不堪。破旧摊位展示干枯蔬菜和褪色布料，顶部覆盖风化帆布棚。夯实的土地上散落踩踏痕迹。人群密集地在摊位间穿梭，视觉上呈现混乱。斑驳阳光透过简陋遮棚洒下碎裂的影子。温暖的尘埃感氛围，枯草黄和土黄色占主导。一个身影在众人中短暂闪现后消失于人海——混乱成为掩护的本质。从高角度拍摄，强调人群和摊位的压倒性密集感。
```

### 马戈逸 (characters, ★★, P5)

#### 1. 

**English：**
```
Male administrative officer, middle-aged, deeply furrowed brow, practical features, anxious expression.
Wearing dried grass yellow (#8B7355) service uniform, shoulders with dark purple (#5B3A6B) insignia, meticulously organized administrative attire.
Shoulders slightly tense, vigilant gaze, eyes revealing subtle anxiety.
Standing posture is reserved yet orderly, holding documents or records in hand.
Dark gray background emphasizing composed demeanor.
Front-facing half-body portrait, clear details, natural soft lighting.
```

**中文：**
```
行政官员，男性，中年，紧皱眉头，实际面容，忧虑神态。
穿着枯草黄 #8B7355 色系服饰，肩章为暗紫 #5B3A6B，井井有条的行政制服。
肩膀略显紧绷，目光警觉，眼神中透露不安。
站立姿态拘谨而有秩序，手中持有公文或记录册。
背景为深灰色调，突出人物的沉着气质。
正面半身像，细节清晰，光线自然柔和。
```

#### 2. 

**English：**
```
Late war period, makeshift administrative office, wooden desk piled with documents and data sheets.
Administrative officer seated at desk, deeply furrowed brow, focused on documents in hand.
Dim candlelight or oil lamp illumination around, casting shadows of urgency and tension.
Rough walls in background, faint traces of war visible.
Color palette dominated by dried grass yellow (#8B7355) and deep gray, accented with dark purple (#5B3A6B) in details.
Scene conveys the burden of maintaining order and administrative responsibility under prolonged pressure.
```

**中文：**
```
战争后期，简陋的行政处理室，木质办公桌堆满文件和数据表格。
行政官员坐于桌前，紧皱眉头，专注于手中的公文。
周围昏暗的烛光或油灯照明，映射出仓促与紧张的氛围。
背景墙面粗糙，隐隐可见战争留下的痕迹。
色调以枯草黄 #8B7355 和深灰色为主，暗紫 #5B3A6B 点缀于细节。
场景传达出长期压力下的秩序维持与行政职责的重负。
```

### 冯德友 (characters, ★, P5)

#### 1. 

**English：**
```
A weathered male military officer in his 40s-50s, stern facial features carved by time and hardship, upright military posture, dark gold uniform #DAA520 with signs of wear, captured but maintaining dignity, sharp evaluative eyes, clenched jaw, chest-up portrait, government army bearing.
```

**中文：**
```
40-50岁男性军事教官，被多年风霜刻画的严肃面孔，笔直军人姿态，暗金色制服#DAA520显露风霜磨损，被俘却保持尊严，眼神锐利评估，紧咬下颌，胸部以上半身像，政府军队气质。

### B1. 场景：被俘时刻的坚忍
```

#### 2. 

**English：**
```
A military officer in dark gold uniform #DAA520 stands with unyielding posture in a detention area, wind-weathered face calm and defiant, hands gripped with suppressed strength, faded government army banners behind, shadows of captivity, unbroken military dignity despite hardship.
```

**中文：**
```
穿着暗金色制服#DAA520的军事教官在拘禁地带笔直而立，被风霜磨蚀的面容平静而不屈，双拳紧握压抑力量，身后淡褪的政府军队旗帜，囚禁的阴影笼罩，困境中不破的军人尊严。
```

### 刘默雨 (characters, ★, P5)

#### 1. 

**English：**
```
Young male police officer, approximately 30 years old, wearing a crisp dark blue police uniform (#001F3F) with black utility belt equipped with police credentials. Young face with alert eyes full of professional competence. Skin tone carries warm khaki-grass yellow (#8B7355) tone of human world. Police cap on head or short hair visible. Background is a light office or patrol car environment. Shoulders show royal blue (#4169E1) uniform detail and accents. Overall demeanor is capable yet composed, presenting standard young grassroots police image. Expression is professional yet humane, gaze directed forward with slight alertness.
```

**中文：**
```
年轻男性警察，约30岁，穿着笔挺的深蓝色警察制服（#001F3F），黑色腰带配备警用证件。面容年轻而警觉，眼神清晰充满专业感。肌肤带有枯草黄（#8B7355）的温暖人间气息。头戴警帽或裸露短发。背景为淡白的警务办公室或巡逻车环境。肩部可见皇家蓝（#4169E1）的制服配色和细节。整体气质干练而平和，呈现标准基层警察的年轻形象。表情职业而不失人情味，目光直视前方略显警惕。
```

#### 2. 

**English：**
```
Inside a police office, the young officer (do not use real name) in dark blue uniform sits at a desk or stands talking with colleagues. Background shows office fluorescent lighting, file cabinets and police documents visible. Royal blue (#4169E1) on the uniform presents professional cool tones under office lighting. Skin tone displays natural khaki-grass yellow (#8B7355) of human world. Posture is natural and professional, showing everyday work of young police officer. No supernatural elements, pure modern police scene authenticity. Overall bright and practical lighting, embodying daily work environment of grassroots police.
```

**中文：**
```
警务办公室内，刘默雨（不用真名）穿着深蓝制服坐在办公桌前，或与宋小仙同事站立交流。背景是办公室的日光灯照明，档案柜和警务文件可见。制服上的皇家蓝（#4169E1）在办公灯光下呈现出专业的冷色调。其肤色呈现枯草黄（#8B7355）的自然人间气息。姿态自然而职业，显示出年轻警察日常工作的平常感。无超自然元素，纯粹现代警务场景的真实性。整体光线明亮务实，体现基层警务的日常工作环境。
```

### 匿名纸条 (props, ★, P5)

#### 1. 

**English：**
```
Anonymous Note / Handwritten Warning Letter
```

**中文：**
```
匿名纸条 / 警告纸条
```

#### 2. 提示词1 - 匿名纸条特写 [匿名纸条特写]

**English：**
```
Cinematic still, 2.39:1 widescreen, extreme close-up of handwritten anonymous note,
cream colored paper #F5F1E8 with black ink handwriting #1A1A1A, irregular pen pressure,
folded creases visible, rough paper texture, shallow depth of field focusing on text,
dim indoor lighting, 35mm film grain, muted warm color grading, gritty aesthetic,
no fingerprints visible, minimalist composition
```

**中文：**
```
电影质感，2.39:1宽屏，手写匿名纸条极近景，奶油纸色#F5F1E8配黑墨#1A1A1A笔迹，
笔压不均的书写痕迹，可见的折叠褶皱，粗糙纸张质感，浅景深聚焦于文字，
昏暗室内光线，35mm胶片颗粒感，黯淡暖色调分级，粗糙美学，
无可见指纹，极简主义构图
```

#### 3. 提示词2 - 警察发现纸条场景 [警察发现纸条场景]

**English：**
```
Cinematic still, 2.39:1 widescreen, detective officer holding and reading handwritten note,
cream paper #F5F1E8 with dark ink text, hands positioned carefully, tense facial expression,
indoor office or patrol car setting, dim warm lighting, 35mm film grain, desaturated color palette,
muted browns and creams, gritty cinematic texture, mood of discovery and urgency
```

**中文：**
```
电影质感，2.39:1宽屏，执法人员持纸条阅读场景，奶油纸色#F5F1E8配深墨文字，
双手小心翼翼地展开，紧张的面部表情，室内办公室或巡车环境，
昏暗暖光照明，35mm胶片颗粒感，去饱和色调，黯淡褐奶油配色，
粗糙电影质感，发现与紧迫情绪的渲染
```

### 巫方镇 (locations, ★, P5)

#### 1. 

**English：**
```
A military fortress on elevated northern terrain. Fortified walls and watchtowers command the landscape. Cold, hard light from the north casts long, sharp shadows across the compound. Watch towers rise against a twilight blue sky. Armed soldiers move with disciplined precision along defensive positions. The earth is brown and barren, meeting distant horizon. Stone and timber fortifications show signs of weathering from harsh climate. Military standards hang from buildings. The composition emphasizes geometric order, defensive geometry, and the desolate beauty of a frontier stronghold. Atmosphere carries the weight of vigilance and readiness. Shot from elevated vantage, showing the strategic dominance of the position.
```

**中文：**
```
北方高地上的军事堡垒。加固的城墙与瞭望塔俯瞰整个地景。北方的冷硬光线投射出长而锐利的影子跨越整个营地。瞭望塔耸立于暮蓝色的天空。武装士兵沿防线以纪律严明的精准步伐巡行。大地褐色荒凉，延伸至远方地平线。石木结构的防御工事显示出北方恶劣气候的侵蚀痕迹。军旗从建筑悬挂。整个画面强调几何秩序、防御的弧线美学、以及边疆堡垒的荒凉之美。氛围充满警觉与随时准备的沉重感。从高处视角拍摄，展现该位置的战略绝对优势。
```

### 干柿子与肉干 (props, ★, P5)

#### 1. 

**English：**
```
Dried Persimmons and Jerky / Survival Rations
```

**中文：**
```
干柿子与肉干 / 流浪生存粮
```

#### 2. 提示词1 - 干柿子与肉干细节特写 [干柿子与肉干细节特写]

**English：**
```
Cinematic still, 2.39:1 widescreen, extreme close-up of dried persimmons and jerky,
dark red #8B4513 persimmons with white frost coating, brown-red #6B3410 jerky pieces,
rough weathered texture, salt crystals visible on meat surface, laid on rough fabric,
natural soft light casting subtle shadows, 35mm film grain, warm muted earth tones,
raw organic aesthetic, gritty survival mood
```

**中文：**
```
电影质感，2.39:1宽屏，干柿子与肉干极近景特写，暗红#8B4513干柿配白霜覆盖，
褐红#6B3410肉干片段，粗糙风化纹理，肉表盐白结晶清晰可见，
铺于粗糙布料上，自然柔光投射细微阴影，35mm胶片颗粒感，
温暖黯淡的土色调，原生有机美学，粗糙生存情绪
```

#### 3. 提示词2 - 流浪角色携带食物袋场景 [流浪角色携带食物袋场景]

**English：**
```
Cinematic still, 2.39:1 widescreen, character's worn hands holding open cloth bag
with dried food inside, grey-brown #8B7765 fabric worn and stained, dried persimmons
and jerky visible, natural outdoor light, weathered hand texture, desperate hunger mood,
35mm film grain, desaturated muted colors, gritty cinematic texture, poverty and survival
```

**中文：**
```
电影质感，2.39:1宽屏，流浪角色满是风霜的双手打开布食物袋，
灰褐#8B7765布料磨损污垢，干柿子与肉干清晰可见，自然室外光线，
风化的手部纹理，绝望饥饿的情绪，35mm胶片颗粒感，去饱和黯淡色调，
粗糙电影质感，贫穷与生存的渲染
```

### 户政室 (locations, ★, P5)

#### 1. 

**English：**
```
The interior of a government administrative office. Multiple service windows lined in a row, each with a numbered placard. Queue barriers divide the vast, rectangular space with geometric precision. Fluorescent overhead lights cast uniform, shadowless illumination across the scene, creating a sterile, emotionless atmosphere. Colors reduced to institutional grays and burnt umber tones. A line of citizens wait in orderly fashion, rendered with minimal individual character. Walls bare and blank. The composition emphasizes repetition, conformity, and bureaucratic indifference. Everything is measured, cold, and devoid of human warmth. Shot from a standard mid-level perspective, capturing the mechanical nature of the space.
```

**中文：**
```
政府行政办事机构内部。多个办事窗口一字排开，每个窗口配置编号牌。排队栏杆以几何精准度分割这个宽敞的矩形空间。日光灯从天花板均匀投射，造成无阴影的刺眼均匀照度，营造无菌、无感的氛围。颜色极度单调，仅有制度灰与焦褐色系。一队市民按秩序排列等待，每个个体都被刻画得缺乏个性。墙面空白无装饰。整个画面强调重复、一致性与官僚的冷漠。一切都是精确、冰冷、毫无人味的。从标准中等高度视角拍摄，捕捉该空间的机械化本质。
```

### 旅行团群像 (characters, ★, P5)

#### 1. 

**English：**
```
Middle-aged and elderly retiree tour group ensemble portrait close-up: 30-50 diverse aged faces tightly arranged, deep wrinkles, sunburned or mottled complexion, eyes full of love for life and anticipation for travel, upturned smiling mouths, wearing sun hats, reading glasses, masks and travel accessories, warm color tone of dried grass yellow and earthy brown, background showing tourist scenic area or ancient ruins, overall atmosphere joyful warm and harmonious, detail emphasis: wrinkle texture, sun-damage marks, affectionate eyes, intimate proximity of huddling together, realistic oil painting style, rich lifestyle atmosphere.
```

**中文：**
```
中老年退休旅游团群像肖像，30-50人的多样面孔特写密集排列：各种不同的老年和中年脸庞，皱纹深刻、晒黑或肤色斑驳，眼神充满对生活的热爱和旅行的期待，嘴角上扬的笑容，戴着防晒帽、老花镜、口罩等旅行配饰，色调温暖的枯草黄和棕土色，背景显示旅游景区或古迹，整体氛围欢乐温暖、其乐融融，细节强调：皱纹纹理、晒黑痕迹、亲切的眼神、互相靠近的亲密感，真实油画风格，生活气息浓厚。
```

#### 2. 

**English：**
```
Tour group 30-50 people after spiritual essence extraction ensemble portrait, vegetative state close-up: all faces displaying identical lifeless expression—eyes wide open but pupils turbid and vacant, mouths slightly agape in 0-shape, skin sickly grayish-white, lips blackened, hair dull and matted to scalp, eye whites covered with dark red blood vessels, facial muscles completely slack appearing corpse-like, entire group tightly arranged, color tone completely transformed from dried grass yellow to lifeless gray-white and dark purple, oppressive dim background, detail emphasis: vacant staring eyes, rapidly aged wrinkles, blackened lips, completely vitality-drained skin texture, realistic horror style, extremely oppressive and despairing atmosphere.
```

**中文：**
```
旅行团30-50人被夺精气后的群像肖像，植物人状态特写：所有面孔呈现完全相同的死寂表情——眼睛睁得很大但瞳孔浑浊无神、嘴巴微张呈0字型、皮肤病态灰白色、嘴唇发黑、头发失去光泽贴在头皮上、眼白布满暗红色血丝、脸部肌肉完全松弛显得像死人一样，整个群体排列紧密，色调从枯草黄完全转为死寂的灰白和暗紫，背景昏暗压抑，细节强调：瞪大的空洞眼神、快速衰老的皱纹、黑化的嘴唇、完全丧失生命力的肤质，真实恐怖风格，极度压抑绝望的气场。
```

#### 3. 

**English：**
```
Tour group collectively encountering five ancient evil spirits escape scene: 30-50 middle-aged and elderly people fleeing in disarray, pushing each other, collective screaming chaos, background ancient ruins or scenic area entrance in dim light, sky eerily darkening, ground covered with inexplicable dark purple mist spreading, some falling to ground, some mutually supporting attempting escape, some raising arms shielding eyes, all faces showing extreme terror with sweat and tears, clothing beginning to dishevel and slacken, color tone rapidly shifting from warm dried grass yellow to cool tones and dark purple, detail emphasis: clothing scattered from jostling, dust from falls, desperate arms raised skyward, suffocating feeling in crowded mass, encroaching sinister purple mist, extremely horror-filled tense visual impact.
```

**中文：**
```
旅行团集体遭遇五名古代恶灵时的逃离场景：30-50个中老年人四散逃离、互相推搡、集体尖叫的混乱场景，背景是昏暗的古迹或景区入口，天空诡异地变暗，地面出现不可解释的暗紫色雾气蔓延，部分人跌倒在地、部分人互相扶持试图逃脱、部分人举起手臂遮挡眼睛，所有人的脸上都是极度的惊恐、汗水和泪水，衣着开始凌乱松垮，色调急速从温暖的枯草黄转变为冷色调和暗紫色，细节强调：被推搡导致衣着散乱、跌倒时的尘土、伸向高空的绝望双手、聚集的人群中的窒息感、逼近的诡异暗紫雾气，极度恐怖紧张的视觉冲击。
```

#### 4. 

**English：**
```
Tour group gradual recovery scene after drinking sacred spring: 30-50 people slowly awakening, lying on ground or sitting up, skin color gradually transforming from grayish-white to dried grass yellow, eyes progressively brightening from turbidity, some crying, some trembling, some mutually embracing for comfort, surroundings bathed in gentle blue-white healing light (sacred spring's curative radiance), background showing sunrise or moonlight, temperature visualized as warm golden rays, detail emphasis: progressive skin color restoration, eye-focusing process, tears and sweat, mutually supporting hands, clothing still bearing stains but gradually straightened, expression blending gratitude and sorrow from return to life at death's edge, realistic moving style, complex atmosphere interwoven with hope and despair.
```

**中文：**
```
旅行团饮用圣泉后的群体恢复场景：30-50个人缓慢苏醒，躺在地上或坐起身，肤色从灰白逐渐转为枯草黄色，眼神从浑浊逐步清亮，有人哭泣、有人颤抖、有人互相拥抱安慰，周围弥漫着柔和的蓝白光芒（圣泉的治愈光），背景是初升的朝阳或月光，温度视觉化为暖和的金色光线，细节强调：渐进式的肤色恢复、眼睛的聚焦过程、泪水和汗水、互相扶持的双手、衣着虽然仍有污渍但逐渐整理、从死亡边缘回归生命的庆幸和悲伤混合的表情，真实感人风格，希望与绝望交织的复杂气氛。
```

### 白思元 (characters, ★, P5)

#### 1. 

**English：**
```
A county official in middle age with composed demeanor and formal attire. Frontal upper-body portrait. Original appearance shows a bureaucrat's steady bearing, dressed neatly in official robes. Color palette: withered grass yellow (#8B7355) for mortal official status. Calm but distant expression. Represents an ordinary administrator before spiritual possession.
```

**中文：**
```
中年县级官员的正面半身像，气质沉着，衣着规整。原有身份展现出公务员的稳重气象，着装符合官员身份。色彩采用枯草黄（#8B7355）代表人间官员属性。表情平静而疏离。代表被附身前的普通行政官员形象。

---

## 十、场景提示词 - 精神病院场景
```

#### 2. 

**English：**
```
A mentally disturbed patient in a psychiatric hospital ward. The county official's body shows signs of spiritual possession aftermath - disheveled appearance, vacant stare, loss of self-control. Dark purple (#5B3A6B) undertones suggest the supernatural trauma. Hospital setting with clinical furniture and subdued lighting. The character's posture and expression convey complete mental breakdown and loss of identity after possession.
```

**中文：**
```
精神病院病房内的失常患者。县官躯体显现附身后遗症：衣着凌乱、眼神呆滞、失去自制力。暗紫色（#5B3A6B）暗示超自然创伤。医院环保设施、冷调光线。姿态与表情传达精神彻底崩溃与身份丧失。

---

*文件创建于：2026-02-23*
*字数等级：★☆☆☆☆极低 | 格式：8章制结构*
```

### 罗勇 (characters, ★, P5)

#### 1. 

**English：**
```
A male military commander in his 30s, subordinate rank insignia, alert sharp eyes, ordinary sturdy build, khaki yellow uniform #8B7355, dark purple armband #5B3A6B, standing at attention, expression stern and obedient, simple military appearance, chest-up portrait.
```

**中文：**
```
30多岁的男性军事指挥官，低级军衔标记，眼神敏锐警觉，身材普通健壮，枯草黄制服#8B7355，暗紫臂章#5B3A6B，立正姿态，表情严肃服从，简洁军人气质，胸部以上半身像。

### B1. 场景：恶灵营地指令执行
```

#### 2. 

**English：**
```
Inside a shadowy military camp, low-ranking commander receives orders from superiors, dark purple mystical aura #5B3A6B surrounds the tent, khaki yellow lamplight #8B7355, tense obedient expression, standing ready with subordinates around him, gothic military aesthetic.
```

**中文：**
```
昏暗军事营地内，低级指挥官接收上级命令，深紫色诡异光晕#5B3A6B笼罩帐篷，枯草黄灯光#8B7355照亮，紧张服从的表情，身侧围绕下属，哥特军事美学风格。
```

### 葛立 (characters, ★, P5)

#### 1. 

**English：**
```
A middle-aged male soldier in his 40s-50s, stocky and muscular build, weathered rough face tanned from years of duty, wearing plain guard uniform in khaki yellow #8B7355, clear alert eyes in sober state, strong jawline, chest-up portrait, no-nonsense soldier appearance.
```

**中文：**
```
40-50岁中年男性士兵，健壮肌肉身材，长年值勤晒黑的粗糙面孔，穿着简朴的枯草黄守卫制服#8B7355，清醒时眼神专注警惕，强硬下颌线，胸部以上半身像，务实兵卒气质。

### B1. 场景：醉酒值班失控
```

#### 2. 

**English：**
```
A drunk middle-aged guard in khaki yellow uniform #8B7355 sits slouched in a dim facility guard post, wine cup in hand, eyes unfocused and drowsy, mouth loose with excessive words spilling out, sweat-stained simple uniform, lax posture betraying intoxication, dim lighting casting long shadows.
```

**中文：**
```
醉酒的中年守卫穿着枯草黄制服#8B7355坐在昏暗的设施值班室内，手持酒杯，眼神涣散困倦，嘴角松弛言辞泛滥，汗渍侵湿简陋制服，瘫软姿态暴露醉意，昏黄灯光投出长长阴影。
```

### 齐年康 (characters, ★, P5)

#### 1. 

**English：**
```
A middle-aged male, approximately 45-55 years old, with a smooth and worldly appearance. Round or square face, sharp and experienced eyes, faint professional smile at the corners of the mouth. Skin tones yellowish from long-term restaurant environment, lacking luster but appearing warm. Medium build with slight middle-age weight gain, loose waistline, slightly bent posture showing habits of long-term service work. Wearing black vest and white dress shirt service uniform with dark apron. Rough hands, neatly trimmed nails with visible work marks, muscle lines showing long-term labor. Fine crow's feet at eye corners hinting at age and experience. Overall color palette dominated by dry grass yellow #8B7355, combined with dark gray and dark brown shadows. Warm lighting, muted background, no pure white elements. Demeanor smooth and professional, embodying occupational patina and life experience.
```

**中文：**
```
一位中年男性，约45-55岁，面容圆滑世故。方脸或圆脸，眼神精明老练，嘴角带着淡淡的职业微笑。皮肤偏黄，因长期在餐厅环境中而缺乏光泽但显得温暖。身材中等略显微胖，腰线有所松弛，背部微弯显示长期服务工作的习惯。穿着黑色背心与白色衬衫的制服，搭配深色围裙。双手粗糙，指甲整洁但显示工作痕迹，肌肉线条显示长期劳作。眼角有细微鱼尾纹，暗示年龄与阅历。整体色调以枯草黄#8B7355为主，配合深灰、暗棕阴影。光线温暖，背景素雅，无纯白元素。气质圆滑得体，蕴含职业沧桑与人生阅历。
```

#### 2. 

**English：**
```
Warm interior of a restaurant, soft warm-colored lighting casting onto warm brown walls and wooden furniture. A middle-aged waiter Qi Nian-kang dressed in standard uniform of black vest, white dress shirt and dark gray apron, steadily holding a serving tray in his left hand, right hand holding a pen ready to take orders. His body leans slightly forward, displaying professional grace and caution. Eyes make contact with customers while maintaining professional distance, slight professional smile at the corners of mouth. Background shows blurred silhouettes of dining tables, dishes, and other diners. Overall color palette dominated by dry grass yellow #8B7355, warm brown and dark gray, creating an atmosphere of warmth with slight occupational weariness. Every detail of the character—steady hands, graceful posture, smooth expression—demonstrates the professional expertise and life experience of a seasoned waiter.
```

**中文：**
```
温暖的餐厅内部，柔和的暖色灯光洒在暖棕色的墙面与木制家具上。一位中年服务员齐年康身穿黑色背心白衬衫加深灰围裙的标准制服，左手稳稳端着托盘，右手拿笔准备记录订单。他身体微微前倾，表现出职业的灵活与谨慎。眼神与客人有接触但保持得体的距离感，嘴角带着淡淡的职业微笑。背景中可见餐桌、菜肴、其他用餐者的模糊身影。整体色调以枯草黄#8B7355、暖棕色和深灰为主，营造出温暖而略显疲倦的餐饮业氛围。人物的每一个细节——手的稳健、姿态的得体、表情的圆滑——都显示出资深服务员的专业素养与人生阅历。
```

### AA大学 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, university campus corrupted by occupation and secret experimentation, modern academic buildings repurposed as military installation, food hall converted to distribution center with industrial machinery, dormitory rows transformed into barracks with surveillance systems, contaminated learning spaces with blackboards covered and seats removed, hidden entrance to underground laboratory in shadows, descent into deep underground facility with cold scientific lighting, experimental chambers with life support systems, digital human cultivation tanks, sterile laboratories with biomechanical equipment, straw-yellow and dark purple color scheme reflecting corruption of knowledge, cold white and cyan scientific lighting creating inhumane atmosphere, former pride of academia twisted into ethical nightmare, emphasize transformation from intellectual sanctuary to technological horror.
```

**中文：**
```
电影级画面，2.39:1超宽屏，被占领和秘密实验污染的大学校园，现代学术建筑被改作军事设施，食堂被改装为配给中心配备工业机械，宿舍楼变成装有监控系统的军营，被污染的学术空间黑板被覆盖座位被清空，隐藏在阴影中通往地下实验室的入口，下降到深层地下设施中冷色科学照明，配备生命维持系统的实验舱室，数字人培育池，装有生物机械设备的无菌实验室，枯草黄与暗紫色调反映知识的腐蚀，冷白和青色科学光线营造非人类的冷漠，曾经的学术骄傲扭曲成伦理噩梦，强调从知识殿堂到科技恐怖的转变。
```

### 千秋星岗 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Desolate battlefield of Qianqiu Star Hill. Dark red blood stains #8B1A1A marking broken defensive lines. Burned brown earth #2C1810 scattered with weapons and armor debris. Blood-red sunset sky. Vast emptiness, silence of defeat. Cinematically tragic, wartime cemetery.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。千秋星岗荒凉战场。暗红血迹 #8B1A1A 标记断裂防线。焦褐大地 #2C1810 散布兵器与甲胄碎片。血红落日天空。辽阔空旷，战败寂静。电影级悲壮，战争墓地。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Yang Hong standing amid ruins of broken fortifications, surrounded by dark red bloodstains #8B1A1A on burned brown ground #2C1810. Defeated army retreating. Blood-red sunset casts long shadows. Shame and defiance in posture. Moment of first defeat, unforgiving battlefield.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。杨弘站立在破碎防线废墟中，暗红血迹 #8B1A1A 浸染焦褐地面 #2C1810。战败军队撤退。血红落日投出长影。姿态中耻辱与不甘。初战失利之刻，无情战场。
```

### 半山腰秘密仓库 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Secret underground cave storage on mountainside. Moss-green stone walls #4A6741 with burned brown wooden shelves #2C1810. Natural spring water pool crystal clear. Torchlight illuminates organized supplies. Mysterious, sacred, protected atmosphere. Darkness beyond light's reach.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。山腰地下岩洞秘密仓库。苔绿石壁 #4A6741 与焦褐木制架子 #2C1810。天然泉水池晶莹。火把照亮整齐物资。神秘、庄严、受保护的氛围。黑暗笼罩光线外。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Underground spring water flowing into ancient stone basin, surrounded by moss-green walls #4A6741. Burned brown wooden crates #2C1810 stacked carefully. Torches casting dancing shadows. Water reflects amber light. Sacred, hidden sanctuary of survival.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。地下泉水流入古老石盆，苔绿石壁环绕 #4A6741。焦褐木箱精心堆放 #2C1810。火把投出舞动阴影。水面反射琥珀光。生存的神圣隐蔽所。
```

### 卢老板餐馆 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, humble old wooden restaurant interior, warm oil lamp light mingling with kitchen fire glow, humble diners gathered around weathered wooden tables, cooking steam and smoke rising from open kitchen, straw-yellow and saddle-brown wood tones throughout, worn timber walls showing age and use, brass cookware and ceramic bowls, charming chaos of modest hospitality, characters in low conversations at bar counter, intimate human moment within daily routine, golden-hour warmth contrasting with shadows, simple but lived-in space, evidence of decades of service, background showing street through small windows, cozy yet melancholic atmosphere, emphasize warmth and hidden depths beneath ordinariness.
```

**中文：**
```
电影级画面，2.39:1超宽屏，简陋老旧木制餐馆内部，温暖的油灯光与厨房火焰混合，简朴食客围坐在磨损的木桌前，烹饪蒸汽和烟雾从开放式厨房升起，整体呈现枯草黄与鞍褐的木质色调，显示岁月痕迹的粗糙木板墙，铜制餐具和陶土碗碟，简朴人情味的有序混乱，人物在吧台前进行低声交谈，日常套路中的亲密人类时刻，金色暖光与阴影形成对比，简朴但充满生活痕迹的空间，数十年服务的证据随处可见，背景通过小窗户显示街道，舒适却略显悲伤的气氛，强调温暖和隐藏在平凡之下的深度。
```

### 周庄 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, remote mountain village hidden in isolation, ancient stone houses scattered across misty slopes, weathered slate roofs and walls covered in moss and lichen, dappled sunlight filtering through dense forest canopy, ancient well as gathering point in village center, lush green foliage surrounding small settlement like protective embrace, warm golden hour light across stone architecture, figures resting in quiet sanctuary, intimate moment in simple shelter with glowing hearth, sense of time standing still, people living at slow rhythm with nature, mountain silence broken only by wind and water, refuge from conflict and chaos, emphasize sense of hidden safety and temporary peace.
```

**中文：**
```
电影级画面，2.39:1超宽屏，隐蔽在雾气中的偏远山村，古老的石屋散落在陡峭山坡，风化的板岩屋顶和苔藓覆盖的墙体，密集森林顶棚散落的斑驳阳光，村中心的古老石井聚集点，郁郁葱葱的绿色植被如同保护性拥抱围绕小村落，温暖的黄金时段光线照亮石墙建筑，人物在安静的避难所中休息，简陋庇护所内发光的篝火中的亲密时刻，时间似乎停滞的感受，人们以与自然缓慢的节奏共生，山谷沉寂仅被风和水声打破，远离冲突和混乱的庇护所，强调隐蔽安全感和短暂的宁静。
```

### 少林寺 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Ancient Shaolin temple nestled in misty mountains. Saddle brown wooden beams and pillars #6B4423 supporting grand architecture. Dark gold candlelight #DAA520 illuminates sacred space. Clouds swirl around rooftops. Timeless, reverent, sacred martial spirit atmosphere.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。古老少林寺隐于云雾山峰。鞍褐木梁与柱子 #6B4423 撑起宏伟建筑。暗金烛火 #DAA520 照亮神圣空间。云雾环绕屋顶。永恒、庄敬、神圣武术精神。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Secret prayer chamber deep within temple. Eighteen crystal rods glowing in darkness, emanating mystical light. Saddle brown wooden altar #6B4423. Dark gold incense smoke #DAA520 curling upward. Ancient Buddhist sculptures watching. Sacred, hidden treasure room.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。深藏于寺内的秘密禅房。十八根水晶棒在黑暗中发光，散发神秘之光。鞍褐木质祭坛 #6B4423。暗金檀香烟雾 #DAA520 盘旋上升。古老佛像守护。神圣隐秘的宝藏室。
```

### 山谷旅行团被困 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Deep mountain valley near Niutai Mountain. Steep twilight blue rock walls #3A4A6B closing in. Moss-green dead vegetation #4A6741 on valley floor. Stranded travelers' temporary camp with small bonfire. Freezing wind visible. Desperate, isolated, survival atmosphere. Dark sky narrow above.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。牛台山附近深山谷地。陡峭暮蓝石壁 #3A4A6B 逼近。苔绿枯死植被 #4A6741 铺满谷底。被困旅行团临时营地与篝火。刺骨寒风可见。绝望、孤立、生存氛围。狭窄黑暗天空。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Stranded travelers huddled around small bonfire in mountain valley. Twilight blue stone walls #3A4A6B tower above. Moss-green dead grass #4A6741 around them. Cold wind whips flames. Desperate faces illuminated by fire. Hope fading. Freezing night of survival.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。被困旅客围聚篝火，暮蓝石壁 #3A4A6B 高耸。苔绿枯草 #4A6741 周围蔓延。寒风吹拂火焰。绝望的脸在火光中。希望消逝。冻寒的生存之夜。
```

### 望海河 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, treacherous river at night, destroyed bridge with broken pilings emerging from dark water, urgent crossing scene with rope systems, fierce rapids with white water turbulence, moonlit scene with deep blue twilight palette, figures silhouetted against breaking waves, adjacent forest in deep brown shadows, enemy torches visible on distant bank, water spray catching moonlight, tense escape atmosphere, cold dark water threatening swimmers, rope taut across churning rapids, desperation and danger in every detail, chiaroscuro lighting with river as focal point, emphasize the barrier between freedom and capture.
```

**中文：**
```
电影级画面，2.39:1超宽屏，深夜凶险的河流，毁坏的桥梁断墩从暗水中露出，紧急渡河场景配备绳索系统，狂暴的急流翻滚着白色浪花，月光映照的深蓝暮色调，身影在碎浪中成为剪影，临近森林笼罩焦褐阴影，敌军火把在远方河岸可见，水花在月光中飞溅，逃脱的紧张气氛，冷黑河水威胁涉水者，绳索在翻滚急流上绷紧，绝望和危险充满每一帧，明暗对比照明以河流为焦点，强调自由与被俘的屏障。
```

### 杨弘秘密实验室 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, sealed underground laboratory deep beneath city, multiple interconnected experimental chambers with cold blue-purple scientific lighting, transparent incubation tanks containing digitized human forms suspended in nutrient fluid, monitoring screens displaying countless data streams and biometric readouts, stainless steel surfaces and precise medical equipment, mechanical arms and surgical tools arranged in clinical precision, life support systems with visible tubing and electrical connections, control center with wall of monitors and blinking indicator lights, genetic and digital human cultivation infrastructure, dehumanized scientific madness, chilling technological achievement married with ethical nightmare, deep purple shadows contrasting with clinical blue-white illumination, sealed and isolated from the world above, emphasize cold institutional horror and humanity perverted by science.
```

**中文：**
```
电影级画面，2.39:1超宽屏，城市地下深处密封的地下实验室，多个相连的实验舱室采用冷蓝紫色科学照明，透明的培育舱内悬浮着数字化人形生物在营养液中，监控屏幕显示无数数据流和生物特征读数，不锈钢表面和精确的医疗设备，机械臂和手术工具以临床精确排列，可见管道和电气连接的生命维持系统，拥有墙壁屏幕墙和闪烁指示灯的控制中心，遗传学和数字人类培育基础设施，非人性化的科学疯狂，令人寒栗的科技成就与伦理噩梦结合，深紫色阴影与临床青白色照明形成对比，密封隔离于上方的世界，强调冷酷的制度恐怖和被科学扭曲的人性。
```

### 清平镇 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, occupied coastal town, ancient granary repurposed as dark prison, massive stone walls casting deep shadows, cramped interior warehouse filled with desperate confined figures, narrow gaps of light from small ventilation openings, deteriorating wooden structures and rushed structures, faded straw-yellow walls contrasting with deep purple darkness, occupier flags and banners overhead, haunting atmosphere of desperation and suppression, damp stale air visible in haze, rusted iron chains and crude barricades, hopeless captives in shadow, desolate seaside backdrop with enemy fleet in harbor, claustrophobic brutalism, desaturated color palette, emphasize imprisonment and oppression.
```

**中文：**
```
电影级画面，2.39:1超宽屏，被占领的沿海小镇，古老的粮仓改为暗黑监狱，巨大的石墙投出深重阴影，拥挤的仓库内部充满绝望的被囚者，狭窄的通风口散入微弱光线，破败的木制结构和仓促建造的隔间，褪色的枯草黄墙壁与深紫黑暗形成对比，占领者旗帜在头顶飘扬，绝望和压迫的阴森氛围，潮湿浑浊的空气以雾霾呈现，生锈的铁链和粗陋的栅栏，被困者在阴影中的无力姿态，荒凉的海边背景与敌军舰队停泊港口，压抑的粗粝主义，去饱和色调，强调囚禁感和压迫统治。
```

### 白巨神兽的隐谷 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, hidden valley deep in mountain range, towering granite cliffs enclosing isolated sanctuary, primitive massive stone cooking pot, diameter six meters, ancient and weathered, moss-covered ground and primordial vegetation, clearing in center of valley showing wear from enormous creature presence, mysterious white-furred giant beast five to six meters tall standing majestically, moss green and dark brown earth tones, dappled light from valley opening above creating dramatic chiaroscuro, steam from ancient pot rising into misty air, scattered bone fragments and marks on stone telling dark history, complete isolation and confinement, prehistoric atmosphere, creature and human meeting in unearthly space, emphasize overwhelming scale and ancient mystery.
```

**中文：**
```
电影级画面，2.39:1超宽屏，隐藏在山脉深处的秘密山谷，耸立的花岗岩悬崖包围孤立的圣地，原始的巨大石制烹饪大锅，直径六米，古老且风化，苔藓覆盖的地面和原始植被，谷中心显示被庞大生物踩踏的痕迹，神秘的白色毛发的巨型生物五到六米高雄伟而立，苔绿和焦褐的地球色调，谷顶开口投下的斑驳光线制造戏剧性的明暗对比，古老大锅升起的蒸汽飘散在雾气中，散落的骨骼碎片和石面刻痕诉说黑暗历史，完全的孤立和困囿，史前时代的气氛，生物和人类在异世空间的相遇，强调令人压倒的规模和古老神秘。
```

### 石岭关 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, narrow mountain pass fortress under siege, steep stone staircases, thick smoke and fire, ancient oil barrel defenses positioned on narrow ledges, dark brown stone walls weathered by time, deep red flames consuming wooden barriers, warriors in silhouette against raging fires, scattered boulders positioned for defense, blood-stained stone surfaces, ash and embers drifting through the air, tactical defense line crumbling under assault, desperate figures holding positions on narrow steps, flickering light from oil fires casting long shadows, mountainous backdrop obscured by smoke, cinematic war photography, gritty realism, tragic heroism, emphasize claustrophobic depth and vertical danger.
```

**中文：**
```
电影级画面，2.39:1超宽屏，狭窄山区关隘被围困，陡峭石阶梯，浓烟和大火弥漫，古老的油桶防御工事排列在狭窄的凸起处，焦褐色岁月沧桑的石墙，深红色火焰吞噬木制防线，战士的剪影在熊熊火焰中，散落的巨石用于防御，血迹斑驳的石面，灰烬和火星飘散空气，战术防线在进攻下分崩离析，绝望的身影守卫在狭窄的台阶，油火闪烁投出长长的阴影，山峦背景被浓烟笼罩，电影级战争摄影，粗粝写实主义，英勇的悲剧感，强调幽闭的纵深感和垂直危险。
```

### 老码头 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Ancient harbor pier at dusk. Twilight blue water #3A4A6B reflecting fading light. Weathered brown wooden docks #2C1810 stretching into sea. Abandoned warehouses and lighthouse silhouettes. Sea salt wind visible. Melancholic, nostalgic, solitary atmosphere. Timeless harbor.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。傍晚古老港口码头。暮蓝海水 #3A4A6B 反射落日光。风化焦褐木栈道 #2C1810 延伸入海。废弃仓库与灯塔剪影。海盐风可见。忧郁、怀旧、孤独氛围。永恒港口。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Two figures stepping off ship onto wooden docks of old pier. Twilight blue harbor water #3A4A6B. Burned brown timber docks #2C1810 beneath their feet. Salt wind whips hair and clothes. Distant lighthouse. Beginning of unknown journey. Vulnerable newcomers arriving.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。两个身影从船上踏上老码头木板。暮蓝港湾 #3A4A6B。焦褐木料 #2C1810 脚下延伸。海盐风吹拂衣物。远方灯塔。未知旅程的开始。脆弱的新来者抵达。
```

### 葛家堡 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen, mountain fortress in chaos, thick stone walls showing signs of internal collapse, central courtyard descending into anarchy and violence, internal betrayal unfolding, daylight fading as fires spread inside fortification, figures struggling against narrow stone corridors, wooden gates splintered and breached, dark brown stone construction showing cracks, chaos spreading through military encampment, dust and smoke rising from courtyard, evidence of failed defense systems, desperate soldiers attempting escape through destroyed gates, dark purple shadows consuming once-secure fortress, Trojan infiltration aftermath, internal destruction more devastating than external siege, emphasize claustrophobic stone architecture becoming a death trap.
```

**中文：**
```
电影级画面，2.39:1超宽屏，山区堡垒陷入混乱，厚重石墙显示内部崩坏迹象，中央广场沦为暴力和无序，内部背叛正在上演，日光消逝而堡垒内火焰蔓延，身影在狭窄的石走廊中挣扎，木制大门碎裂被攻破，焦褐石构建筑显现裂纹，混乱蔓延穿过军事营地，尘埃和烟雾从广场升起，防御体系失效的证据，绝望的士兵试图通过被摧毁的大门逃脱，暗紫色阴影吞没曾经的坚固堡垒，特洛伊木马式渗透的后果，内部摧毁比外部围困更加致命，强调幽闭的石墙建筑变成死亡陷阱。
```

### 虎口镇 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Coastal town square at dusk, dominated by withered yellow buildings #8B7355 casting dark purple shadows #5B3A6B. Thick clouds block sunlight. Gathered crowds show despair and defeat. Ocean visible in background, wind-swept palm trees. Abandoned fortification barriers. Color graded cool, hopeless atmosphere.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。傍晚海滨城镇广场，枯草黄建筑 #8B7355 投出暗紫阴影 #5B3A6B。厚重云层遮挡阳光。聚集的人群表现绝望与战败。背景可见大海，风吹棕榈树。废弃防线栅栏。冷色调，绝望氛围。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Town leader standing before crowd in square, announcing surrender. Withered yellow stone platform #8B7355, dark purple dusk light #5B3A6B. Soldiers lowering banners. Silence and resignation visible on faces. Ocean wind traces through hair and cloth. Cinematically composed, moments before conquest.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。镇长站在广场人群前宣布投降。枯草黄石台 #8B7355，暗紫暮光 #5B3A6B。士兵放下旗帜。脸上可见沉寂与屈服。海风吹过头发衣物。电影级构图，征服前夕。
```

### 黄阳镇 (locations, , P5)

#### 1. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Coastal town engulfed in warfare chaos. Withered yellow buildings #8B7355 illuminated by dark red fire #8B1A1A. Smoke columns rise. Multiple soldiers fighting in ruins. Explosions and gunfire flashes. Ocean harbor damaged. Apocalyptic, intense battle atmosphere.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。沿海城镇陷入战争混乱。枯草黄建筑 #8B7355 被暗红烈火 #8B1A1A 照亮。烟柱升起。多名士兵在废墟间交火。炮火爆炸闪光。海港受损。末日战争氛围。
```

#### 2. 

**English：**
```
Cinematic still, 2.39:1 widescreen. Northern defense line of yellow town #8B7355, crumbling under assault. Soldiers fighting desperately among broken walls. Dark red flames #8B1A1A illuminate desperate faces. Dust and smoke everywhere. Incoming fire. Cinematically composed chaos of battle.
```

**中文：**
```
电影质感静帧，2.39:1宽屏幅。黄色城镇北部防线 #8B7355 在猛烈攻势下崩溃。士兵在破碎墙壁间绝望搏击。暗红火焰 #8B1A1A 照亮绝望的脸庞。尘烟弥漫。炮火袭来。电影级战争混乱构图。
```
