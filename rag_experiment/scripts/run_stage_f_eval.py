"""Stage F — 3-sample Qwen generation + PASS@3 + retrieval stats.

For every selected problem:
  * retrieve top-k skills (RAG on);
  * ask Qwen for 3 independent samples;
  * execute each sample against the TACO stdio tests;
  * record run_id / retrieval trace / execution verdict.

Run rows stream to `outputs/stage_f/runs.jsonl`; aggregated metrics land in
`outputs/stage_f/metrics_summary.json` and a human-readable
`reports/experiment_report.md`.

Supports `--limit` (subset), `--ablation-no-rag`, `--scope single|multi`,
and `--eval-source stage_a|taco_test`.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.evaluation.executor import execute_stdio, report_to_dict  # noqa: E402
from src.evaluation.metrics import aggregate  # noqa: E402
from src.evaluation.retrieval_eval import gold_skill_ids_for_problem, is_retrieval_hit  # noqa: E402
from src.generation.generate_with_rag import generate_with_rag  # noqa: E402
from src.io_utils import append_jsonl, load_jsonl, save_json  # noqa: E402
from src.llm import build_qwen_client  # noqa: E402
from src.llm.base import LLMError  # noqa: E402
from src.logging_utils import setup_logging, get_logger  # noqa: E402
from src.rag.pipeline import RAGContext  # noqa: E402
from src.settings import get_settings  # noqa: E402
from src.stage_a_filter import _iterate_taco, _parse_record, load_selected  # noqa: E402
from src.stage_b_problem_label import load_problem_labels  # noqa: E402


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Stage F: PASS@3 + retrieval eval with Qwen2.5-Coder-7B")
    parser.add_argument("--scope", choices=["single", "multi"], default="multi",
                        help="which Stage A view to iterate (does not change the 240-problem universe)")
    parser.add_argument("--limit", type=int, default=0, help="if >0, only evaluate this many problems")
    parser.add_argument("--ablation-no-rag", action="store_true",
                        help="disable RAG retrieval; skill cards are not injected into the Qwen prompt")
    parser.add_argument(
        "--eval-source",
        choices=["stage_a", "taco_test"],
        default="stage_a",
        help="problem source: existing Stage A universe or raw TACO test split",
    )
    parser.add_argument(
        "--eval-manifest",
        type=Path,
        default=None,
        help="optional JSONL manifest of evaluation problems; each row must include input_output",
    )
    parser.add_argument("--resume", action="store_true", default=True)
    return parser.parse_args()


def _load_tests(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    return {row["problem_id"]: row["input_output"] for row in load_jsonl(path)}


def _canonical_taco_problem_id(dataset_index: int, record: dict[str, Any], split: str) -> str:
    explicit = record.get("id") or record.get("problem_id") or record.get("source_id")
    if isinstance(explicit, (int, str)) and str(explicit).strip():
        slug = re.sub(r"[^a-zA-Z0-9_-]+", "_", str(explicit).strip()).strip("_")
        return f"taco_{split}_{int(dataset_index):06d}__{slug}"[:96]
    return f"taco_{split}_{int(dataset_index):06d}"


def _load_taco_test_eval(
    settings: Any,
    *,
    scope: str,
    limit: int = 0,
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    hf_name = settings.config["paths"]["taco_hf_name"]
    hf_cache = settings.cache_dir / "hf_datasets"
    hf_cache.mkdir(parents=True, exist_ok=True)
    dataset = _iterate_taco(hf_name, "test", cache_dir=hf_cache)

    problems: list[dict[str, Any]] = []
    tests: dict[str, dict[str, Any]] = {}
    pseudo_labels: dict[str, dict[str, Any]] = {}

    for idx, record in enumerate(dataset):
        parsed = _parse_record(idx, record)
        if parsed is None:
            continue
        if not parsed.input_output or not parsed.input_output.get("inputs"):
            continue
        is_multi = len(parsed.core_families) >= 2
        if scope == "single" and is_multi:
            continue
        if scope == "multi" and not is_multi:
            continue

        pid = _canonical_taco_problem_id(idx, record, "test")
        primary_family = parsed.core_families[0]
        problems.append({
            "problem_id": pid,
            "source_dataset": "TACO",
            "split": "test",
            "source_index": idx,
            "source": parsed.source,
            "difficulty": parsed.difficulty,
            "problem_statement": parsed.question,
            "reference_solutions": [],
            "original_skill_types": parsed.skill_types,
            "original_tags": parsed.raw_tags,
            "candidate_families": list(parsed.core_families),
            "scope": "multi" if is_multi else "single",
            "primary_family": primary_family,
            "is_multi_skill_candidate": is_multi,
        })
        tests[pid] = parsed.input_output
        pseudo_labels[pid] = {
            "normalized_single_skill": primary_family,
            "normalized_multi_skills": list(parsed.core_families),
            "is_multi_skill": is_multi,
        }
        if limit > 0 and len(problems) >= limit:
            break

    return problems, tests, pseudo_labels


def _load_eval_manifest(path: Path) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    rows = load_jsonl(path)
    problems: list[dict[str, Any]] = []
    tests: dict[str, dict[str, Any]] = {}
    pseudo_labels: dict[str, dict[str, Any]] = {}
    for row in rows:
        pid = row["problem_id"]
        test_payload = row.get("input_output")
        if not isinstance(test_payload, dict):
            continue
        problem = dict(row)
        problem.pop("input_output", None)
        problems.append(problem)
        tests[pid] = test_payload
        fams = [f for f in (row.get("candidate_families") or []) if isinstance(f, str)]
        primary = row.get("primary_family")
        pseudo_labels[pid] = {
            "normalized_single_skill": primary if isinstance(primary, str) else (fams[0] if fams else None),
            "normalized_multi_skills": fams,
            "is_multi_skill": bool(row.get("is_multi_skill_candidate")) or len(fams) >= 2,
        }
    return problems, tests, pseudo_labels


def _resolve_eval_inputs(settings: Any, args: argparse.Namespace, log: Any) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    if args.eval_manifest is not None:
        manifest_path = args.eval_manifest.resolve()
        problems, tests, pseudo_labels = _load_eval_manifest(manifest_path)
        log.info(
            "Loaded Stage F eval manifest: %s (problems=%d tests=%d)",
            manifest_path, len(problems), len(tests),
        )
        return problems, tests, pseudo_labels

    if args.eval_source == "stage_a":
        problems = load_selected(settings, scope=args.scope)
        tests = _load_tests(settings.taco_tests_path)
        problem_labels = load_problem_labels(settings)
        if not problem_labels:
            log.warning("Stage B labels missing; gold skill ids will fall back to candidate_families.")
        return problems, tests, problem_labels

    problems, tests, pseudo_labels = _load_taco_test_eval(
        settings,
        scope=args.scope,
        limit=args.limit,
    )
    log.info(
        "Loaded TACO test split for Stage F: scope=%s problems=%d tests=%d",
        args.scope, len(problems), len(tests),
    )
    return problems, tests, pseudo_labels


def _resolve_output_paths(
    settings: Any,
    *,
    eval_source: str,
    scope: str,
    eval_manifest: Path | None = None,
    rag_enabled: bool = True,
) -> tuple[Path, Path, Path]:
    out_dir = settings.stage_dir("stage_f")
    rag_tag = "rag" if rag_enabled else "no_rag"
    if eval_manifest is not None:
        stem = re.sub(r"[^a-zA-Z0-9_-]+", "_", eval_manifest.stem).strip("_") or "manifest"
        suffix = f"manifest_{stem}" if rag_enabled else f"manifest_{stem}_{rag_tag}"
        return (
            out_dir / f"runs_{suffix}.jsonl",
            out_dir / f"metrics_summary_{suffix}.json",
            settings.reports_dir / f"experiment_report_{suffix}.md",
        )
    if eval_source == "stage_a":
        if not rag_enabled:
            return (
                out_dir / f"runs_{rag_tag}.jsonl",
                out_dir / f"metrics_summary_{rag_tag}.json",
                settings.reports_dir / f"experiment_report_{rag_tag}.md",
            )
        return (
            out_dir / "runs.jsonl",
            out_dir / "metrics_summary.json",
            settings.reports_dir / "experiment_report.md",
        )
    suffix = f"{eval_source}_{scope}" if rag_enabled else f"{eval_source}_{scope}_{rag_tag}"
    return (
        out_dir / f"runs_{suffix}.jsonl",
        out_dir / f"metrics_summary_{suffix}.json",
        settings.reports_dir / f"experiment_report_{suffix}.md",
    )


def main() -> int:
    args = _parse_args()
    settings = get_settings()
    setup_logging(settings.config["logging"]["level"], settings.output_dir / "run.log")
    log = get_logger("stage_f")

    problems, tests, problem_labels = _resolve_eval_inputs(settings, args, log)
    if args.eval_source == "stage_a" and args.limit > 0:
        problems = problems[: args.limit]

    rag_ctx = RAGContext.from_settings(settings, enabled=not args.ablation_no_rag)

    log.info("Loading Qwen code LLM: %s", settings.qwen.model_id)
    code_llm = build_qwen_client(settings.qwen)

    gen_cfg = settings.config["generation"]
    eval_cfg = settings.config["evaluation"]
    n_samples = int(gen_cfg["samples_per_problem"])
    per_test_timeout = int(eval_cfg["per_test_timeout_seconds"])
    max_tests = int(eval_cfg["max_tests_per_problem"])
    sandbox = eval_cfg["sandbox"]

    runs_path, metrics_path, report_path = _resolve_output_paths(
        settings,
        eval_source=args.eval_source,
        scope=args.scope,
        eval_manifest=args.eval_manifest,
        rag_enabled=not args.ablation_no_rag,
    )

    done: set[str] = set()
    if args.resume and runs_path.exists():
        for row in load_jsonl(runs_path):
            done.add(f"{row['problem_id']}::{row['run_id']}")
        log.info("Resume: %d runs already present.", len(done))

    for idx, prob in enumerate(problems, start=1):
        pid = prob["problem_id"]
        if all(f"{pid}::r{i}" in done for i in range(n_samples)):
            continue
        if pid not in tests:
            log.warning("No test cases for %s — skipping.", pid)
            continue

        label = problem_labels.get(pid, {})
        gold = gold_skill_ids_for_problem(label) if label else []
        if not gold:
            gold = [f for f in (prob.get("candidate_families") or []) if isinstance(f, str)]

        log.info("[%d/%d] Generating %d samples for %s", idx, len(problems), n_samples, pid)
        try:
            trace = generate_with_rag(
                code_llm=code_llm,
                rag_ctx=rag_ctx,
                problem_statement=prob["problem_statement"],
                n_samples=n_samples,
                seed_base=hash(pid) & 0xFFFF,
            )
        except (LLMError, RuntimeError, MemoryError) as exc:
            # Includes torch.cuda.OutOfMemoryError (subclass of RuntimeError).
            # Do NOT write any rows for this problem: on resume we will retry
            # once the GPU is free.
            log.warning(
                "Generation failed for %s: %s — skipping (will retry on resume).",
                pid, exc,
            )
            try:
                import torch
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            except Exception:
                pass
            continue

        tests_payload = tests[pid]
        total_tests_for_problem = min(
            len(tests_payload.get("inputs") or []),
            len(tests_payload.get("outputs") or []),
            max_tests,
        )
        for run_idx in range(n_samples):
            key = f"{pid}::r{run_idx}"
            if key in done:
                continue
            run_id = f"r{run_idx}"
            log.info(
                "[%d/%d] %s %s start: executing up to %d tests",
                idx, len(problems), pid, run_id, total_tests_for_problem,
            )
            code = trace.extracted_codes[run_idx] or ""
            if not code.strip():
                exec_report = {
                    "all_passed": False, "num_tests": 0, "num_passed": 0,
                    "reason_summary": {"empty_output": 1}, "per_test": [],
                }
                passed = False
            else:
                report = execute_stdio(
                    code=code,
                    inputs=tests_payload.get("inputs") or [],
                    outputs=tests_payload.get("outputs") or [],
                    fn_name=tests_payload.get("fn_name"),
                    per_test_timeout=per_test_timeout,
                    cpu_limit_seconds=int(sandbox["cpu_limit_seconds"]),
                    memory_limit_mb=int(sandbox["memory_limit_mb"]),
                    python_executable=sandbox["python_executable"],
                    max_tests=max_tests,
                )
                exec_report = report_to_dict(report)
                passed = report.all_passed

            row = {
                "run_id": run_id,
                "problem_id": pid,
                "eval_source": "manifest" if args.eval_manifest is not None else args.eval_source,
                "eval_split": prob.get("split"),
                "rag_enabled": not args.ablation_no_rag,
                "primary_family": prob.get("primary_family"),
                "candidate_families": prob.get("candidate_families") or [],
                "gold_skill_ids": gold,
                "retrieved_skill_ids": trace.retrieved_skill_ids,
                "retrieved_topk": len(trace.retrieved_skill_ids),
                "retrieval_scores": trace.retrieval_scores,
                "retrieval_method": trace.retrieval_method,
                "dense_topk": trace.dense_ids,
                "bm25_topk": trace.bm25_ids,
                "retrieval_hit": is_retrieval_hit(trace.retrieved_skill_ids, gold),
                "bundle_type": trace.bundle_type,
                "graph_evidence": trace.graph_evidence or [],
                "seed_ids": trace.seed_ids or {},
                "supporting_prototypes": trace.supporting_prototypes or [],
                "matched_signals": trace.matched_signals or [],
                "matched_mechanisms": trace.matched_mechanisms or [],
                "query_schema": trace.query_schema or {},
                "generated_code": code,
                "raw_completion": trace.raw_completions[run_idx][:6000],
                "execution_result": exec_report,
                "passed": passed,
            }
            append_jsonl(runs_path, row)
            log.info(
                "[%d/%d] %s %s done: passed=%s tests=%d/%d reasons=%s",
                idx,
                len(problems),
                pid,
                run_id,
                passed,
                int(exec_report.get("num_passed", 0)),
                int(exec_report.get("num_tests", 0)),
                exec_report.get("reason_summary", {}),
            )

    # Aggregate + write summary.
    runs = load_jsonl(runs_path)
    metrics = aggregate(runs, problem_labels)
    save_json(metrics_path, metrics)
    _write_experiment_report(report_path, metrics, args)
    log.info("Stage F done. Summary: %s", json.dumps({
        "pass@1": metrics["pass_at_1"], "pass@3": metrics["pass_at_3"],
        "retrieval_hit_rate": metrics["retrieval"]["overall_correct_rate"],
    }))
    return 0


def _write_experiment_report(path: Path, metrics: dict[str, Any], args: argparse.Namespace) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# Experiment Report — Qwen2.5-Coder-7B + Skill RAG\n")
    if args.eval_manifest is not None:
        source_text = f"manifest:{args.eval_manifest.name}"
    else:
        source_text = args.eval_source
    lines.append(
        f"- Scope: `{args.scope}`, eval source: `{source_text}`, "
        f"RAG enabled: `{not args.ablation_no_rag}`\n"
    )
    lines.append(f"- Total problems: {metrics['total_problems']}, total runs: {metrics['total_runs']}\n\n")
    lines.append("## Core metrics\n")
    lines.append(f"- **PASS@1** = {metrics['pass_at_1']:.4f}\n")
    lines.append(f"- **PASS@3** = {metrics['pass_at_3']:.4f}\n")
    lines.append(f"- Single-skill PASS@3 = {metrics['single_subset']['pass_at_3']:.4f} "
                 f"({metrics['single_subset']['passed']}/{metrics['single_subset']['problems']})\n")
    lines.append(f"- Multi-skill PASS@3 = {metrics['multi_subset']['pass_at_3']:.4f} "
                 f"({metrics['multi_subset']['passed']}/{metrics['multi_subset']['problems']})\n\n")
    lines.append("## Retrieval statistics\n")
    r = metrics["retrieval"]
    lines.append(f"- Total retrieval calls: {r['total_calls']}\n")
    lines.append(f"- Total hits: {r['total_hits']}\n")
    lines.append(f"- Overall correct-retrieval rate: {r['overall_correct_rate']:.4f}\n")
    lines.append(f"- Avg retrieval calls per problem: {r['avg_calls_per_problem']:.2f}\n")
    lines.append(f"- Avg correct retrievals per problem: {r['avg_correct_per_problem']:.2f}\n\n")
    lines.append("## Per-family breakdown\n\n")
    lines.append("| family | problems | PASS@3 | PASS@1 | retrieval hit rate |\n| --- | ---: | ---: | ---: | ---: |\n")
    for fam, st in sorted(metrics["per_family"].items()):
        lines.append(
            f"| {fam} | {st['problems']} | {st['pass_at_3']:.4f} | {st['pass_at_1']:.4f} | {st['retrieval_hit_rate']:.4f} |\n"
        )
    path.write_text("".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
