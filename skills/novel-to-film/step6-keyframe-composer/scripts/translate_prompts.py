#!/usr/bin/env python3
"""
translate_prompts.py — 调用 LLM 将中文画面描述翻译为英文 Seedream Prompt (Layer 3)

核心功能：
1. 读取 prompt_assembly.json（由 assemble_prompts.py 生成）
2. 对每个 layer3_visual_content 为空的条目，调用 Claude API 翻译
3. 翻译规则：
   - 角色不用真名，使用通用描述
   - 提取冻结时刻（第 0 秒状态）
   - 前景/中景/背景分层描述
   - 光影和色彩具体化
4. 输出填充后的 prompt_assembly_translated.json

用法：
    export ANTHROPIC_API_KEY="your-key"
    python3 translate_prompts.py [--base-dir /path/to/production]
    python3 translate_prompts.py --dry-run       # 不调 API
    python3 translate_prompts.py --limit 5       # 只翻译前 5 个
    python3 translate_prompts.py --shot SC001-001  # 只翻译指定镜头

依赖：
    pip install requests
"""

import os
import sys
import json
import time
import argparse
import logging

try:
    import requests
except ImportError:
    print("请先安装 requests: pip install requests --break-system-packages")
    sys.exit(1)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from storyboard_utils import DEFAULT_BASE

# ---------------------------------------------------------------------------
# 日志 & 常量
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("translate")

DEFAULT_API_URL = "https://api.anthropic.com/v1/messages"
DEFAULT_MODEL = "claude-sonnet-4-5-20250929"
MAX_RETRIES = 3
RETRY_BACKOFF = 2.0
QPS_DELAY = 0.5  # API 调用间隔（秒）


# ---------------------------------------------------------------------------
# 翻译 System Prompt
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """You are a professional film production translator specializing in converting Chinese director's visual descriptions into structured English prompts for the Seedream AI image generation model.

## Your Task
Translate the Chinese visual description into a structured English Seedream image prompt. This is NOT a simple translation — it requires creative restructuring for AI image generation.

## Rules

1. **No character real names** — Use generic physical descriptions instead (e.g., "a sturdy Chinese man in his 30s" not "朱围庸")
2. **Freeze the moment** — The prompt describes a STILL IMAGE (frame 0). Extract only the static state from the motion description, not the action itself.
3. **Spatial layers** — Structure the description as: foreground → midground → background
4. **Concrete lighting** — Replace vague descriptions ("atmospheric lighting") with specific terms ("golden hour side lighting from the left, long shadows stretching right, warm rim light on silhouette")
5. **Concrete colors** — Use specific color words ("deep burgundy robe" not "dark robe")
6. **Follow the structure**: [Subject + pose/action] + [clothing/props] + [environment] + [lighting] + [atmosphere]
7. **Output ONLY the English prompt text** — No explanations, no markdown, no labels.
8. **Keep it concise** — Aim for 80-150 words. Seedream works best with focused descriptions.
"""

USER_TEMPLATE = """Translate this Chinese visual description into an English Seedream image prompt.

## Shot Info
- Scale: {scale}
- Angle: {angle}

## Frozen Moment (frame 0 state)
{frozen_moment}

## Visual Description (Chinese)

**Foreground:**
{foreground}

**Midground:**
{midground}

**Background:**
{background}

## Full Visual Description (for reference)
{full_visual}

---
Output ONLY the English prompt text (80-150 words):"""


# ---------------------------------------------------------------------------
# API 调用
# ---------------------------------------------------------------------------
def call_claude_api(
    api_url: str,
    api_key: str,
    model: str,
    system: str,
    user_message: str,
) -> str:
    """
    调用 Claude Messages API 进行翻译。
    返回生成的英文文本，失败返回空字符串。
    """
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }
    payload = {
        "model": model,
        "max_tokens": 1024,
        "system": system,
        "messages": [
            {"role": "user", "content": user_message},
        ],
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.post(api_url, headers=headers, json=payload, timeout=60)

            if resp.status_code == 429:
                wait = RETRY_BACKOFF ** attempt * 2
                log.warning(f"  ⚠️ 限流 429, {wait:.1f}s 后重试")
                time.sleep(wait)
                continue

            if resp.status_code != 200:
                raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:200]}")

            data = resp.json()
            content = data.get("content", [])
            if content and content[0].get("type") == "text":
                return content[0]["text"].strip()
            else:
                raise RuntimeError(f"未知响应格式: {json.dumps(data, ensure_ascii=False)[:200]}")

        except Exception as e:
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF ** attempt
                log.warning(f"  ⚠️ 第{attempt}次失败: {str(e)[:80]}... {wait:.1f}s 后重试")
                time.sleep(wait)
            else:
                log.error(f"  ❌ 翻译失败: {str(e)[:120]}")
                return ""

    return ""


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="调用 LLM 翻译中文画面描述为英文 Seedream Prompt")
    parser.add_argument("--base-dir", default=DEFAULT_BASE, help="production 目录")
    parser.add_argument("--input", default=None,
                        help="prompt_assembly.json 路径")
    parser.add_argument("--output", default=None,
                        help="输出路径 (默认: prompt_assembly_translated.json)")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Claude 模型 (默认: {DEFAULT_MODEL})")
    parser.add_argument("--api-url", default=DEFAULT_API_URL, help="API URL")
    parser.add_argument("--dry-run", action="store_true", help="不调 API，输出翻译请求示例")
    parser.add_argument("--limit", type=int, default=0, help="最多翻译 N 个 (默认: 0=全部)")
    parser.add_argument("--shot", default=None, help="只翻译指定镜头 (如: SC001-001)")
    parser.add_argument("--no-skip", action="store_true", help="不跳过已翻译的条目")
    parser.add_argument("--delay", type=float, default=QPS_DELAY, help=f"API 调用间隔 (默认: {QPS_DELAY}s)")
    args = parser.parse_args()

    base = os.path.abspath(args.base_dir)
    input_path = args.input or os.path.join(base, "step6-keyframes", "prompt_assembly.json")
    output_path = args.output or os.path.join(base, "step6-keyframes", "prompt_assembly_translated.json")

    # 1. 加载半成品 prompt
    if not os.path.exists(input_path):
        log.error(f"输入文件不存在: {input_path}")
        log.error("请先运行: python3 assemble_prompts.py")
        sys.exit(1)

    with open(input_path, 'r', encoding='utf-8') as f:
        assemblies = json.load(f)
    log.info(f"加载 {len(assemblies)} 个半成品 prompt")

    # 2. 过滤
    tasks = assemblies
    if args.shot:
        tasks = [a for a in tasks if a["shot_id"] == args.shot]
        log.info(f"过滤镜头 {args.shot}: {len(tasks)} 个")

    if not args.no_skip:
        before = len(tasks)
        tasks = [a for a in tasks if not a.get("layer3_visual_content")]
        skipped = before - len(tasks)
        if skipped:
            log.info(f"跳过已翻译: {skipped} 个")

    # 过滤无源文本的
    tasks = [a for a in tasks if a.get("layer3_source_cn")]
    log.info(f"待翻译: {len(tasks)} 个")

    if args.limit > 0:
        tasks = tasks[:args.limit]
        log.info(f"限制翻译数量: {len(tasks)}")

    if not tasks:
        log.info("无待翻译任务")
        # 仍然输出文件（可能有之前已翻译的）
        if not args.dry_run:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(assemblies, f, ensure_ascii=False, indent=2)
        return

    # 3. 翻译
    if args.dry_run:
        print(f"\nDRY RUN — 共 {len(tasks)} 个待翻译\n")
        for a in tasks[:3]:
            user_msg = USER_TEMPLATE.format(
                scale=a["metadata"]["scale_cn"],
                angle=a["metadata"]["angle_cn"],
                frozen_moment=a.get("frozen_moment_cn", "N/A"),
                foreground=a.get("foreground_cn", "N/A"),
                midground=a.get("midground_cn", "N/A"),
                background=a.get("background_cn", "N/A"),
                full_visual=a.get("layer3_source_cn", "")[:500],
            )
            print(f"--- {a['shot_id']} ---")
            print(f"User message preview:\n{user_msg[:400]}...\n")
        return

    # API Key
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        log.error("未设置 ANTHROPIC_API_KEY 环境变量！")
        sys.exit(1)

    # 建立 shot_id → assembly 的索引（用于回写）
    assembly_map = {a["shot_id"]: a for a in assemblies}

    total = len(tasks)
    success = 0
    failed = 0
    start_time = time.time()

    log.info(f"\n开始翻译 {total} 个画面描述 (模型: {args.model})\n")

    for i, task in enumerate(tasks, 1):
        sid = task["shot_id"]
        log.info(f"[{i}/{total}] 翻译 {sid}")

        user_msg = USER_TEMPLATE.format(
            scale=task["metadata"]["scale_cn"],
            angle=task["metadata"]["angle_cn"],
            frozen_moment=task.get("frozen_moment_cn", "N/A"),
            foreground=task.get("foreground_cn", "N/A"),
            midground=task.get("midground_cn", "N/A"),
            background=task.get("background_cn", "N/A"),
            full_visual=task.get("layer3_source_cn", "")[:1000],
        )

        result = call_claude_api(
            api_url=args.api_url,
            api_key=api_key,
            model=args.model,
            system=SYSTEM_PROMPT,
            user_message=user_msg,
        )

        if result:
            # 回写到 assemblies
            assembly_map[sid]["layer3_visual_content"] = result
            success += 1
            log.info(f"  ✅ {len(result)} chars: {result[:80]}...")
        else:
            failed += 1
            log.error(f"  ❌ 翻译失败")

        # 每 20 个保存一次（断点续跑）
        if i % 20 == 0:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(assemblies, f, ensure_ascii=False, indent=2)
            log.info(f"  💾 中间保存 ({i}/{total})")

        if i < total:
            time.sleep(args.delay)

    # 最终保存
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(assemblies, f, ensure_ascii=False, indent=2)

    elapsed = time.time() - start_time
    log.info(f"\n{'='*50}")
    log.info(f"翻译完成！用时 {elapsed:.1f}s")
    log.info(f"  成功: {success}/{total}")
    log.info(f"  失败: {failed}/{total}")
    log.info(f"  输出: {output_path}")
    log.info(f"{'='*50}")


if __name__ == "__main__":
    main()
