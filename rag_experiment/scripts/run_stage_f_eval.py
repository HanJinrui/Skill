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
import zlib
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.evaluation.executor import execute_stdio, report_to_dict  # noqa: E402
from src.evaluation.metrics import aggregate  # noqa: E402
from src.evaluation.retrieval_eval import (  # noqa: E402
    bundle_gold_ids,
    family_ids_for_problem,
    family_skill_ids,
    gold_skill_ids_for_problem,
    is_retrieval_hit,
    subtype_gold_ids,
)
from src.generation.generate_with_rag import generate_with_rag  # noqa: E402
from src.io_utils import append_jsonl, load_jsonl, read_jsonl, save_json  # noqa: E402
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
        "--rag-mode",
        choices=["config", "no_rag", "flat_family_rag", "subtype_rag", "graph_subtype_rag"],
        default="config",
        help="retrieval mode for comparison; no_rag overrides --ablation-no-rag",
    )
    parser.add_argument(
        "--retrieval-only",
        action="store_true",
        help="only run retrieval and metrics; skip Qwen generation/execution",
    )
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
    parser.add_argument("--seed", type=int, default=0, help="stable seed base; 0 means config experiment.seed")
    parser.add_argument("--run-tag", type=str, default="", help="optional run tag to group outputs and avoid mixing runs")
    parser.add_argument("--gpu-policy", type=str, default="auto", help="metadata only: records expected GPU policy for reproducibility")
    return parser.parse_args()


def _load_primary_rows_by_problem(settings: Any) -> dict[str, dict[str, Any]]:
    stage_c = settings.output_dir / "stage_c"
    out: dict[str, dict[str, Any]] = {}
    for path in (stage_c / "solution_labeled.jsonl", stage_c / "primary_solutions_deepseek.jsonl", stage_c / "primary_solutions_merged.jsonl"):
        if not path.exists():
            continue
        for row in read_jsonl(path):
            if path.name == "solution_labeled.jsonl" and not row.get("is_primary_solution"):
                continue
            pid = row.get("problem_id")
            if isinstance(pid, str):
                out[pid] = {**out.get(pid, {}), **row}
    return out


def _retrieved_families(skills: list[dict[str, Any]]) -> list[str]:
    fams: list[str] = []
    for skill in skills:
        for fam in skill.get("families") or []:
            if isinstance(fam, str) and fam not in fams:
                fams.append(fam)
    return fams


def _family_recall_hit(retrieved_families: list[str], gold_families: list[str]) -> bool:
    return bool(set(retrieved_families) & set(gold_families))


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
    rag_mode: str = "config",
    retrieval_only: bool = False,
    run_tag: str = "",
) -> tuple[Path, Path, Path]:
    out_dir = settings.stage_dir("stage_f")
    rag_tag = "retrieval_only_" if retrieval_only else ""
    rag_tag += rag_mode if rag_mode != "config" else ("rag" if rag_enabled else "no_rag")
    if run_tag:
        clean_run_tag = re.sub(r"[^a-zA-Z0-9_-]+", "_", run_tag).strip("_")
        if clean_run_tag:
            rag_tag = f"{rag_tag}_{clean_run_tag}"
    if eval_manifest is not None:
        stem = re.sub(r"[^a-zA-Z0-9_-]+", "_", eval_manifest.stem).strip("_") or "manifest"
        suffix = f"manifest_{stem}_{rag_tag}"
        return (
            out_dir / f"runs_{suffix}.jsonl",
            out_dir / f"metrics_summary_{suffix}.json",
            settings.reports_dir / f"experiment_report_{suffix}.md",
        )
    if eval_source == "stage_a":
        if rag_mode != "config" or retrieval_only:
            return (
                out_dir / f"runs_{rag_tag}.jsonl",
                out_dir / f"metrics_summary_{rag_tag}.json",
                settings.reports_dir / f"experiment_report_{rag_tag}.md",
            )
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
    suffix = f"{eval_source}_{scope}_{rag_tag}"
    return (
        out_dir / f"runs_{suffix}.jsonl",
        out_dir / f"metrics_summary_{suffix}.json",
        settings.reports_dir / f"experiment_report_{suffix}.md",
    )


def _diagnose_failure(row: dict[str, Any]) -> str:
    if row.get("passed"):
        return "none"
    if not row.get("retrieved_skill_ids"):
        return "no_retrieval_context"
    if not row.get("router_top1_hit"):
        return "routing_error"
    if not row.get("retrieval_hit"):
        return "skill_noise_or_mismatch"
    reasons = (row.get("execution_result") or {}).get("reason_summary") or {}
    if "timeout" in reasons or "time_limit_exceeded" in reasons:
        return "complexity_mismatch"
    if "memory_limit_exceeded" in reasons:
        return "complexity_mismatch"
    if "wrong_answer" in reasons:
        return "implementation_bug"
    return "prompt_conflict"


def main() -> int:
    args = _parse_args()
    settings = get_settings()
    base_seed = int(args.seed or settings.config.get("experiment", {}).get("seed") or 0)
    setup_logging(settings.config["logging"]["level"], settings.output_dir / "run.log")
    log = get_logger("stage_f")

    problems, tests, problem_labels = _resolve_eval_inputs(settings, args, log)
    if args.eval_source == "stage_a" and args.limit > 0:
        problems = problems[: args.limit]

    rag_mode = args.rag_mode
    rag_enabled = not args.ablation_no_rag and rag_mode != "no_rag"
    rag_mode_override = None
    if rag_mode == "flat_family_rag":
        rag_mode_override = "flat"
    elif rag_mode == "subtype_rag":
        rag_mode_override = "subtype_rag"
    elif rag_mode == "graph_subtype_rag":
        rag_mode_override = "graph_subtype_rag"

    rag_ctx = RAGContext.from_settings(settings, enabled=rag_enabled, mode=rag_mode_override)

    code_llm = None
    if not args.retrieval_only:
        log.info("Loading Qwen code LLM: %s", settings.qwen.model_id)
        code_llm = build_qwen_client(settings.qwen)

    gen_cfg = settings.config["generation"]
    eval_cfg = settings.config["evaluation"]
    n_samples = int(gen_cfg["samples_per_problem"])
    first_sample_temperature = gen_cfg.get("first_sample_temperature")
    first_sample_top_p = gen_cfg.get("first_sample_top_p")
    per_test_timeout = int(eval_cfg["per_test_timeout_seconds"])
    max_tests = int(eval_cfg["max_tests_per_problem"])
    sandbox = eval_cfg["sandbox"]

    runs_path, metrics_path, report_path = _resolve_output_paths(
        settings,
        eval_source=args.eval_source,
        scope=args.scope,
        eval_manifest=args.eval_manifest,
        rag_enabled=rag_enabled,
        rag_mode=rag_mode,
        retrieval_only=args.retrieval_only,
        run_tag=args.run_tag,
    )
    failure_path = runs_path.with_name(runs_path.name.replace("runs_", "failure_diagnosis_"))
    oom_flag_path = runs_path.with_suffix(".oom.flag")

    done: set[str] = set()
    if args.resume and runs_path.exists() and not oom_flag_path.exists():
        for row in load_jsonl(runs_path):
            done.add(f"{row['problem_id']}::{row['run_id']}")
        log.info("Resume: %d runs already present.", len(done))
    elif args.resume and oom_flag_path.exists():
        log.warning("OOM flag detected for %s; forcing clean rerun to avoid mixed outputs.", runs_path)
        if runs_path.exists():
            runs_path.unlink()
        if failure_path.exists():
            failure_path.unlink()
        if metrics_path.exists():
            metrics_path.unlink()
        if report_path.exists():
            report_path.unlink()
        oom_flag_path.unlink()

    primary_rows_by_problem = _load_primary_rows_by_problem(settings)

    for idx, prob in enumerate(problems, start=1):
        pid = prob["problem_id"]
        expected_run_ids = ["retrieval"] if args.retrieval_only else [f"r{i}" for i in range(n_samples)]
        if all(f"{pid}::{rid}" in done for rid in expected_run_ids):
            continue
        if not args.retrieval_only and pid not in tests:
            log.warning("No test cases for %s — skipping.", pid)
            continue

        label = problem_labels.get(pid, {})
        gold = gold_skill_ids_for_problem(label) if label else []
        if not gold:
            gold = [f for f in (prob.get("candidate_families") or []) if isinstance(f, str)]
        gold_families = family_ids_for_problem(prob, label)
        gold_family_ids = family_skill_ids(gold_families)
        gold_subtypes = subtype_gold_ids(primary_rows_by_problem, pid)
        gold_bundles = bundle_gold_ids(gold_families)

        if args.retrieval_only:
            log.info("[%d/%d] Retrieval-only for %s", idx, len(problems), pid)
            retrieved = rag_ctx.retrieve(prob["problem_statement"]) if rag_enabled else None
            retrieved_ids = list(retrieved.skill_ids) if retrieved else []
            retrieved_skills = list(retrieved.skills) if retrieved else []
            retrieved_families = _retrieved_families(retrieved_skills)
            schema = dict(getattr(retrieved, "query_schema", {}) or {}) if retrieved else {}
            router_top1 = (schema.get("candidate_families") or [None])[0]
            family_hit = _family_recall_hit(retrieved_families, gold_families)
            subtype_hit = is_retrieval_hit(retrieved_ids, gold_subtypes) if gold_subtypes else False
            bundle_hit = is_retrieval_hit(retrieved_ids, gold_bundles) if gold_bundles else False
            row = {
                "run_id": "retrieval",
                "problem_id": pid,
                "eval_source": "manifest" if args.eval_manifest is not None else args.eval_source,
                "eval_split": prob.get("split"),
                "difficulty": prob.get("difficulty"),
                "difficulty_bucket": prob.get("difficulty_bucket"),
                "scope": prob.get("scope"),
                "rag_enabled": rag_enabled,
                "rag_mode": rag_mode,
                "seed_base": base_seed,
                "run_tag": args.run_tag,
                "gpu_policy": args.gpu_policy,
                "primary_family": prob.get("primary_family"),
                "candidate_families": prob.get("candidate_families") or [],
                "gold_skill_ids": gold,
                "gold_family_ids": gold_family_ids,
                "gold_families": gold_families,
                "gold_subtype_ids": gold_subtypes,
                "gold_bundle_ids": gold_bundles,
                "retrieved_skill_ids": retrieved_ids,
                "retrieved_families": retrieved_families,
                "retrieved_topk": len(retrieved_ids),
                "retrieval_scores": list(retrieved.scores) if retrieved else [],
                "retrieval_method": retrieved.method if retrieved else "disabled",
                "dense_topk": list(retrieved.dense_ids) if retrieved else [],
                "bm25_topk": list(retrieved.bm25_ids) if retrieved else [],
                "retrieval_hit": family_hit or subtype_hit or bundle_hit or is_retrieval_hit(retrieved_ids, gold),
                "router_top1_hit": bool(router_top1 and router_top1 in gold_families),
                "family_recall_hit": family_hit,
                "subtype_recall_hit": subtype_hit,
                "bundle_recall_hit": bundle_hit,
                "bundle_type": getattr(retrieved, "bundle_type", "") if retrieved else "",
                "graph_evidence": list(getattr(retrieved, "graph_evidence", []) or []) if retrieved else [],
                "seed_ids": dict(getattr(retrieved, "seed_ids", {}) or {}) if retrieved else {},
                "supporting_prototypes": list(getattr(retrieved, "supporting_prototypes", []) or []) if retrieved else [],
                "matched_signals": list(getattr(retrieved, "matched_signals", []) or []) if retrieved else [],
                "matched_mechanisms": list(getattr(retrieved, "matched_mechanisms", []) or []) if retrieved else [],
                "query_schema": schema,
                "fallback_to_no_rag": False,
                "fallback_reason": "",
                "generated_code": "",
                "raw_completion": "",
                "execution_result": {},
                "passed": False,
            }
            append_jsonl(runs_path, row)
            continue

        log.info("[%d/%d] Generating %d samples for %s", idx, len(problems), n_samples, pid)
        try:
            trace = generate_with_rag(
                code_llm=code_llm,
                rag_ctx=rag_ctx,
                problem_statement=prob["problem_statement"],
                n_samples=n_samples,
                seed_base=(base_seed + zlib.crc32(pid.encode("utf-8"))) & 0xFFFF,
                first_sample_temperature=float(first_sample_temperature) if first_sample_temperature is not None else None,
                first_sample_top_p=float(first_sample_top_p) if first_sample_top_p is not None else None,
            )
        except (LLMError, RuntimeError, MemoryError) as exc:
            # Includes torch.cuda.OutOfMemoryError (subclass of RuntimeError).
            # Do NOT write any rows for this problem: on resume we will retry
            # once the GPU is free.
            log.warning(
                "Generation failed for %s: %s — skipping (will retry on resume).",
                pid, exc,
            )
            oom_flag_path.write_text("oom_detected\n", encoding="utf-8")
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
                "difficulty": prob.get("difficulty"),
                "difficulty_bucket": prob.get("difficulty_bucket"),
                "scope": prob.get("scope"),
                "rag_enabled": rag_enabled,
                "rag_mode": rag_mode,
                "seed_base": base_seed,
                "run_tag": args.run_tag,
                "gpu_policy": args.gpu_policy,
                "primary_family": prob.get("primary_family"),
                "candidate_families": prob.get("candidate_families") or [],
                "gold_skill_ids": gold,
                "gold_family_ids": gold_family_ids,
                "gold_families": gold_families,
                "gold_subtype_ids": gold_subtypes,
                "gold_bundle_ids": gold_bundles,
                "retrieved_skill_ids": trace.retrieved_skill_ids,
                "retrieved_families": _retrieved_families(trace.retrieved_skills),
                "retrieved_topk": len(trace.retrieved_skill_ids),
                "retrieval_scores": trace.retrieval_scores,
                "retrieval_method": trace.retrieval_method,
                "dense_topk": trace.dense_ids,
                "bm25_topk": trace.bm25_ids,
                "retrieval_hit": (
                    _family_recall_hit(_retrieved_families(trace.retrieved_skills), gold_families)
                    or is_retrieval_hit(trace.retrieved_skill_ids, gold + gold_subtypes + gold_bundles)
                ),
                "router_top1_hit": bool(((trace.query_schema or {}).get("candidate_families") or [None])[0] in gold_families),
                "family_recall_hit": _family_recall_hit(_retrieved_families(trace.retrieved_skills), gold_families),
                "subtype_recall_hit": is_retrieval_hit(trace.retrieved_skill_ids, gold_subtypes) if gold_subtypes else False,
                "bundle_recall_hit": is_retrieval_hit(trace.retrieved_skill_ids, gold_bundles) if gold_bundles else False,
                "bundle_type": trace.bundle_type,
                "graph_evidence": trace.graph_evidence or [],
                "seed_ids": trace.seed_ids or {},
                "supporting_prototypes": trace.supporting_prototypes or [],
                "matched_signals": trace.matched_signals or [],
                "matched_mechanisms": trace.matched_mechanisms or [],
                "query_schema": trace.query_schema or {},
                "fallback_to_no_rag": bool(trace.fallback_to_no_rag),
                "fallback_reason": trace.fallback_reason,
                "generated_code": code,
                "raw_completion": trace.raw_completions[run_idx][:6000],
                "execution_result": exec_report,
                "passed": passed,
            }
            row["failure_diagnosis"] = _diagnose_failure(row)
            append_jsonl(runs_path, row)
            if row["failure_diagnosis"] not in {"none", "no_retrieval_context"}:
                append_jsonl(failure_path, {
                    "problem_id": pid,
                    "run_id": run_id,
                    "rag_mode": rag_mode,
                    "failure_diagnosis": row["failure_diagnosis"],
                    "retrieved_skill_ids": row.get("retrieved_skill_ids", []),
                    "fallback_to_no_rag": row.get("fallback_to_no_rag", False),
                    "fallback_reason": row.get("fallback_reason", ""),
                    "reason_summary": exec_report.get("reason_summary", {}),
                })
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
    metrics["protocol"] = {
        "seed": base_seed,
        "run_tag": args.run_tag,
        "gpu_policy": args.gpu_policy,
        "rag_mode": rag_mode,
        "retrieval_only": bool(args.retrieval_only),
        "runs_path": str(runs_path),
        "failure_diagnosis_path": str(failure_path),
    }
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
    lines.append("# 实验报告：保守层级 Skill RAG\n")
    if args.eval_manifest is not None:
        source_text = f"manifest:{args.eval_manifest.name}"
    else:
        source_text = args.eval_source
    lines.append(
        f"- Scope: `{args.scope}`, eval source: `{source_text}`, "
        f"RAG mode: `{args.rag_mode}`, retrieval only: `{args.retrieval_only}`\n"
    )
    lines.append(f"- Total problems: {metrics['total_problems']}, total runs: {metrics['total_runs']}\n\n")
    lines.append("## 核心指标\n")
    lines.append(f"- **PASS@1** = {metrics['pass_at_1']:.4f}\n")
    lines.append(f"- **PASS@3** = {metrics['pass_at_3']:.4f}\n")
    lines.append(f"- Single-skill PASS@3 = {metrics['single_subset']['pass_at_3']:.4f} "
                 f"({metrics['single_subset']['passed']}/{metrics['single_subset']['problems']})\n")
    lines.append(f"- Multi-skill PASS@3 = {metrics['multi_subset']['pass_at_3']:.4f} "
                 f"({metrics['multi_subset']['passed']}/{metrics['multi_subset']['problems']})\n\n")
    lines.append("## 检索统计\n")
    r = metrics["retrieval"]
    lines.append(f"- Total retrieval calls: {r['total_calls']}\n")
    lines.append(f"- Total hits: {r['total_hits']}\n")
    lines.append(f"- Overall correct-retrieval rate: {r['overall_correct_rate']:.4f}\n")
    lines.append(f"- Router top1 acc: {r.get('router_top1_acc', 0.0):.4f}\n")
    lines.append(f"- Family recall@k: {r.get('family_recall_at_k', 0.0):.4f}\n")
    lines.append(f"- Subtype recall@k: {r.get('subtype_recall_at_k', 0.0):.4f}\n")
    lines.append(f"- Bundle recall@k: {r.get('bundle_recall_at_k', 0.0):.4f}\n")
    lines.append(f"- Hit to pass conversion: {r.get('hit_to_pass_conversion', 0.0):.4f}\n")
    lines.append(f"- False mechanism rate: {r.get('false_mechanism_rate', 0.0):.4f}\n")
    lines.append(f"- Avg retrieval calls per problem: {r['avg_calls_per_problem']:.2f}\n")
    lines.append(f"- Avg correct retrievals per problem: {r['avg_correct_per_problem']:.2f}\n\n")
    lines.append("## 新旧流水线差异\n")
    lines.append("- 旧路径以 family skill card 为主，弱 query 信号容易被 Graph RAG 放大。\n")
    lines.append("- 新路径采用 router -> family -> subtype -> optional bundle，默认只注入 top1 subtype 和 1 个 prototype。\n")
    lines.append("- multi-skill 只用于 bundle/composition，不再参与纯 subtype 定义。\n\n")
    lines.append("## 新旧检索差异\n")
    lines.append("- `flat_family_rag` 保留旧 family 粒度对照。\n")
    lines.append("- `subtype_rag` 使用 Stage D v2 层级 skill，保守 family filter 后检索 subtype。\n")
    lines.append("- `graph_subtype_rag` 使用 subtype-level graph，hydration 不再伪造 matched signals/mechanisms。\n\n")
    lines.append("## 为什么更稳定\n")
    lines.append("- 弱证据时 QuerySchema 不再开启全部 family。\n")
    lines.append("- 在线 query 不再从 family_hint 展开全 mechanism。\n")
    lines.append("- 泛目标信号如 maximize/minimize/construct 不再作为强传播证据。\n")
    lines.append("- prompt 不再默认塞 3 张宽泛 card，减少误导生成。\n\n")
    lines.append("## 当前问题\n")
    lines.append("- subtype gold 依赖 Stage C primary_solution，测试集或 manifest 可能没有 subtype gold。\n")
    lines.append("- `graph_subtype_rag` 需要先重建 `outputs/stage_e/graph_index_v2`。\n")
    lines.append("- retrieval-only 只能衡量检索质量，不能替代完整 PASS@k 生成评测。\n\n")
    lines.append("## Per-family breakdown\n\n")
    lines.append("| family | problems | PASS@3 | PASS@1 | retrieval hit rate |\n| --- | ---: | ---: | ---: | ---: |\n")
    for fam, st in sorted(metrics["per_family"].items()):
        lines.append(
            f"| {fam} | {st['problems']} | {st['pass_at_3']:.4f} | {st['pass_at_1']:.4f} | {st['retrieval_hit_rate']:.4f} |\n"
        )
    path.write_text("".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
