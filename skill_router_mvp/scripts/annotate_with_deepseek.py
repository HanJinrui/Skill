#!/usr/bin/env python3
"""Create an independent DeepSeek silver-label route worksheet."""
from __future__ import annotations

import argparse
import os
import queue
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.annotation_judge import DeepSeekAnnotationClient, RouteAutoAnnotator  # noqa: E402
from src.config import load_settings  # noqa: E402
from src.io_utils import append_jsonl, load_jsonl  # noqa: E402
from src.schemas import AnnotationRow  # noqa: E402


def api_keys_from_env(primary_name: str) -> list[str]:
    raw = os.getenv(primary_name, "").strip()
    if not raw and primary_name == "DEEPSEEK_API_KEYS":
        raw = os.getenv("DEEPSEEK_API_KEY", "").strip()
    keys: list[str] = []
    for value in raw.split(","):
        key = value.strip()
        if key and key not in keys:
            keys.append(key)
    return keys


def main() -> None:
    parser = argparse.ArgumentParser(description="Label route-gold candidates with DeepSeek V4 Pro.")
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--worksheet", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--model", default=None)
    parser.add_argument("--base-url", default=None)
    parser.add_argument("--max-tokens", type=int, default=None)
    parser.add_argument("--thinking", choices=["enabled", "disabled"], default=None)
    parser.add_argument("--api-keys-env", default="DEEPSEEK_API_KEYS")
    parser.add_argument("--workers", type=int, default=None, help="Concurrent workers; default is one per API key.")
    parser.add_argument("--confidence-threshold", type=float, default=None)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--single-pass", action="store_true", help="Skip the independent second-pass audit.")
    existing = parser.add_mutually_exclusive_group()
    existing.add_argument("--resume", action="store_true")
    existing.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    settings = load_settings(args.config)
    judge_cfg = settings.data.get("annotation_judge") or {}
    model = args.model or str(judge_cfg.get("model", "deepseek-v4-pro"))
    base_url = args.base_url or str(judge_cfg.get("base_url", "https://api.deepseek.com"))
    max_tokens = args.max_tokens or int(judge_cfg.get("max_tokens", 1400))
    thinking = args.thinking or str(judge_cfg.get("thinking", "disabled"))
    timeout_seconds = float(judge_cfg.get("timeout_seconds", 120.0))
    max_retries = int(judge_cfg.get("max_retries", 3))
    threshold = args.confidence_threshold
    if threshold is None:
        threshold = float(judge_cfg.get("confidence_threshold", 0.75))
    second_pass = not args.single_pass and bool(judge_cfg.get("second_pass", True))

    api_keys = api_keys_from_env(args.api_keys_env)
    if not api_keys:
        raise SystemExit(
            f"Missing {args.api_keys_env}. Export comma-separated DeepSeek API keys "
            "(or DEEPSEEK_API_KEY for a single-key fallback) before running."
        )
    if not 0.0 <= threshold <= 1.0:
        parser.error("--confidence-threshold must be between 0 and 1.")

    worksheet = (args.worksheet or settings.path("annotation_dir") / "bank67_route_gold_workbook.jsonl").resolve()
    output = (args.output or settings.path("annotation_dir", create=True) / "bank67_route_deepseek_silver.jsonl").resolve()
    if output.exists() and not (args.resume or args.overwrite):
        raise SystemExit(f"Output already exists: {output}. Use --resume or --overwrite.")
    if args.overwrite and output.exists():
        output.unlink()

    workbook_rows = [AnnotationRow.model_validate(row) for row in load_jsonl(worksheet)]
    if args.limit > 0:
        workbook_rows = workbook_rows[: args.limit]
    completed = {str(row["problem_id"]) for row in load_jsonl(output)} if args.resume and output.exists() else set()
    workbook_rows = [row for row in workbook_rows if row.problem_id not in completed]

    manifests = load_jsonl(settings.path("single_eval_manifest")) + load_jsonl(settings.path("multi_eval_manifest"))
    problem_by_id = {str(problem["problem_id"]): problem for problem in manifests}
    missing = [row.problem_id for row in workbook_rows if row.problem_id not in problem_by_id]
    if missing:
        raise SystemExit(f"Worksheet problem IDs are absent from evaluation manifests: {missing[:3]}")

    workers = args.workers or len(api_keys)
    if workers < 1:
        parser.error("--workers must be >= 1.")
    if workers > len(api_keys):
        parser.error("--workers cannot exceed the number of configured API keys.")
    workers = min(workers, len(workbook_rows)) if workbook_rows else workers
    annotator_pool: queue.Queue[RouteAutoAnnotator] = queue.Queue()
    for api_key in api_keys[:workers]:
        client = DeepSeekAnnotationClient(
            api_key=api_key,
            base_url=base_url,
            model=model,
            max_tokens=max_tokens,
            timeout_seconds=timeout_seconds,
            max_retries=max_retries,
            thinking_type=thinking,
        )
        annotator_pool.put(RouteAutoAnnotator(settings, client.complete))
    mode = "label + independent audit" if second_pass else "one pass"
    print(
        f"DeepSeek silver annotation: {len(workbook_rows)} pending, model={model}, "
        f"mode={mode}, thinking={thinking}, threshold={threshold:.2f}, keys={len(api_keys)}, workers={workers}",
        flush=True,
    )
    accepted = 0
    flagged = 0
    failed: list[str] = []

    def label_one(workbook_row: AnnotationRow) -> tuple[dict[str, object], float, float]:
        started = time.perf_counter()
        annotator = annotator_pool.get()
        try:
            final, initial = annotator.annotate(
                problem_by_id[workbook_row.problem_id],
                second_pass=second_pass,
            )
            output_row = annotator.to_annotation_row(
                workbook_row,
                final,
                model=model,
                confidence_threshold=threshold,
                initial=initial,
            )
            return output_row, final.confidence, time.perf_counter() - started
        finally:
            annotator_pool.put(annotator)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_by_id = {
            executor.submit(label_one, workbook_row): workbook_row.problem_id
            for workbook_row in workbook_rows
        }
        for index, future in enumerate(as_completed(future_by_id), start=1):
            problem_id = future_by_id[future]
            try:
                output_row, confidence, duration = future.result()
                append_jsonl(output, output_row)
                if output_row["review_status"] == "reviewed":
                    accepted += 1
                else:
                    flagged += 1
                print(
                    f"[{index}/{len(workbook_rows)}] wrote {problem_id}: "
                    f"{output_row['review_status']}, confidence={confidence:.2f}, "
                    f"{duration:.1f}s",
                    flush=True,
                )
            except Exception as exc:
                failed.append(problem_id)
                print(f"[{index}/{len(workbook_rows)}] failed {problem_id}: {exc}", file=sys.stderr, flush=True)

    print(f"Output: {output}; accepted={accepted}; needs_review={flagged}; failed={len(failed)}", flush=True)
    if failed:
        print("Rerun with --resume to retry failed rows.", file=sys.stderr, flush=True)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
