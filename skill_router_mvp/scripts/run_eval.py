#!/usr/bin/env python3
"""Run one or more independent code-generation modes on a read-only manifest."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import load_settings  # noqa: E402
from src.io_utils import load_jsonl, write_json, write_jsonl  # noqa: E402
from src.metrics import aggregate  # noqa: E402
from src.pipeline import MODES, SkillRouterPipeline  # noqa: E402
from src.qwen_client import QwenLocalClient  # noqa: E402
from src.schemas import AnnotationRow  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate independent bank67 skill routing with local Qwen.")
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--manifest", type=Path, default=None)
    parser.add_argument("--scope", choices=["single", "multi"], default="single")
    parser.add_argument("--modes", default="direct_qwen,legacy_hint,routed_plan,routed_plan_closed_loop")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--samples", type=int, default=0)
    parser.add_argument("--device", default=None, help="Override retrieval/reranker device, for example cuda:0.")
    parser.add_argument("--run-tag", default="run")
    parser.add_argument("--annotations", type=Path, default=None)
    args = parser.parse_args()
    overrides = {"retrieval": {"device": args.device}} if args.device else None
    settings = load_settings(args.config, overrides=overrides)
    modes = [mode.strip() for mode in args.modes.split(",") if mode.strip()]
    invalid = set(modes) - MODES
    if invalid:
        raise SystemExit(f"Unknown mode(s): {sorted(invalid)}")
    manifest = args.manifest or settings.path("single_eval_manifest" if args.scope == "single" else "multi_eval_manifest")
    problems = load_jsonl(manifest)
    if args.limit > 0:
        problems = problems[: args.limit]
    llm = QwenLocalClient(settings)
    pipeline = SkillRouterPipeline.from_settings(settings, llm)
    traces = []
    for mode in modes:
        for offset, problem in enumerate(problems, start=1):
            print(f"[{mode}] {offset}/{len(problems)} {problem.get('problem_id')}", flush=True)
            traces.append(pipeline.run_problem(problem, mode=mode, n_samples=args.samples or None))
    output_dir = settings.path("runs_dir", create=True)
    run_path = output_dir / f"{args.run_tag}.jsonl"
    write_jsonl(run_path, (trace.model_dump(mode="json") for trace in traces))
    annotations = None
    annotation_info = None
    if args.annotations:
        annotation_rows = load_jsonl(args.annotations)
        annotations = [AnnotationRow.model_validate(row) for row in annotation_rows]
        annotation_info = {
            "path": str(args.annotations),
            "total_rows": len(annotation_rows),
            "reviewed_rows": sum(1 for row in annotations if row.review_status == "reviewed"),
            "needs_review_rows": sum(1 for row in annotations if row.review_status == "needs_review"),
            "reviewed_out_of_bank_rows": sum(
                1 for row in annotations if row.review_status == "reviewed" and bool(row.out_of_bank)
            ),
            "label_sources": sorted({str(row.get("label_source", "human_or_unspecified")) for row in annotation_rows}),
        }
    result = aggregate(traces, annotations)
    summary_path = settings.path("reports_dir", create=True) / f"{args.run_tag}_metrics.json"
    write_json(summary_path, {"manifest": str(manifest), "modes": modes, "annotations": annotation_info, "metrics": result})
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"Runs: {run_path}\nMetrics: {summary_path}")


if __name__ == "__main__":
    main()
