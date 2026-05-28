#!/usr/bin/env python3
"""Produce a manually reviewable routing-gold worksheet from TACO manifests."""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import load_settings  # noqa: E402
from src.io_utils import append_jsonl, load_jsonl  # noqa: E402
from src.reranker import SkillReranker  # noqa: E402
from src.retriever import HybridRetriever  # noqa: E402
from src.schemas import AnnotationRow  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Build manual gold annotation worksheet.")
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--no-rerank", action="store_true")
    parser.add_argument("--device", default=None, help="Override retrieval/reranker device, for example cuda:0.")
    parser.add_argument("--output", type=Path, default=None, help="Write to this JSONL path instead of the configured worksheet.")
    parser.add_argument("--progress-every", type=int, default=1, help="Print completed progress every N rows.")
    existing = parser.add_mutually_exclusive_group()
    existing.add_argument("--resume", action="store_true", help="Append only problems not already present in output.")
    existing.add_argument("--overwrite", action="store_true", help="Replace an existing output worksheet.")
    args = parser.parse_args()

    if args.progress_every < 1:
        parser.error("--progress-every must be >= 1")
    overrides = {"retrieval": {"device": args.device}} if args.device else None
    settings = load_settings(args.config, overrides=overrides)
    output = args.output or settings.path("annotation_dir", create=True) / "bank67_route_gold_workbook.jsonl"
    output = output.expanduser().resolve()
    if output.exists() and not (args.resume or args.overwrite):
        raise SystemExit(f"Output already exists: {output}. Use --resume or --overwrite.")
    if args.overwrite and output.exists():
        output.unlink()

    rows = load_jsonl(settings.path("single_eval_manifest")) + load_jsonl(settings.path("multi_eval_manifest"))
    if args.limit > 0:
        rows = rows[: args.limit]

    completed_ids = set()
    if args.resume and output.exists():
        completed_ids = {str(row["problem_id"]) for row in load_jsonl(output)}
    pending = [row for row in rows if str(row["problem_id"]) not in completed_ids]
    device = str(settings.data["retrieval"].get("device", "cpu"))
    rerank_mode = "disabled" if args.no_rerank else "enabled"
    print(
        f"Worksheet: {len(rows)} total, {len(completed_ids)} already written, "
        f"{len(pending)} pending; rerank={rerank_mode}; device={device}",
        flush=True,
    )
    if not pending:
        print(f"Nothing to do. Output is up to date: {output}", flush=True)
        return

    print("Loading dense retrieval index/model; the first reranked row may also load reranker weights.", flush=True)
    retriever = HybridRetriever.from_index(settings)
    reranker = None if args.no_rerank else SkillReranker(settings)
    started = time.perf_counter()
    try:
        for row_number, problem in enumerate(pending, start=1):
            problem_id = str(problem["problem_id"])
            row_started = time.perf_counter()
            print(f"[{row_number}/{len(pending)}] routing {problem_id} ...", flush=True)
            statement = str(problem.get("problem_statement") or "")
            candidates = retriever.retrieve(statement)
            if reranker:
                candidates = reranker.rerank(statement, candidates)
            sheet_row = AnnotationRow(
                problem_id=problem_id,
                scope=str(problem.get("scope") or ""),
                difficulty_bucket=str(problem.get("difficulty_bucket") or ""),
                problem_summary=statement[:400].replace("\n", " "),
                candidate_skill_ids=[candidate.skill_id for candidate in candidates],
            )
            append_jsonl(output, sheet_row.model_dump(mode="json"))
            if row_number % args.progress_every == 0 or row_number == len(pending):
                elapsed = time.perf_counter() - started
                row_elapsed = time.perf_counter() - row_started
                print(
                    f"[{row_number}/{len(pending)}] wrote {problem_id} "
                    f"({row_elapsed:.1f}s row, {elapsed:.1f}s elapsed)",
                    flush=True,
                )
    except KeyboardInterrupt:
        print(f"\nInterrupted. Partial rows are saved in {output}; rerun with --resume.", file=sys.stderr, flush=True)
        raise SystemExit(130)

    print(f"Wrote {len(pending)} new pending-review rows to {output}", flush=True)


if __name__ == "__main__":
    main()
