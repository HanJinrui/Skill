"""Pass1: verify source solutions and build the shared evidence manifest."""
from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

from sdf.io_utils import append_jsonl, save_json
from sdf.factory_settings import Settings, cfg_section
from sdf.codecontests_adapter import parse_codecontests_problem
from sdf.codecontests_executor import execute_python2_stdio, safe_python2_precheck
from sdf.shared import bootstrap  # noqa: F401

from src.logging_utils import get_logger
from src.stage_a_filter import _iterate_taco
from src.stage_c0_verify import (
    DEFAULT_BLOCKED_CALLS,
    DEFAULT_BLOCKED_IMPORTS,
    RawTacoProblem,
    _classify_clean_split,
    _execute_solution_tests,
    _is_obvious_mismatch,
    _max_tests,
    _parse_raw_taco_problem,
    _safe_execution_precheck,
    _syntax_check,
)
from src.rules import ast_to_family_hints, solution_ast_features

LOG = get_logger(__name__)


@dataclass
class Pass1Options:
    limit_problems: int = 0
    resume: bool = False
    problem_ids: set[str] | None = None
    verified_source: str | None = None


def _judge_style(io: dict[str, Any] | None) -> str:
    if io and io.get("fn_name"):
        return "function"
    return "stdio"


def _pre_scan_ok(problem: RawTacoProblem, *, min_tests: int, min_statement_chars: int) -> bool:
    if len(problem.problem_statement) < min_statement_chars:
        return False
    if not problem.reference_solutions:
        return False
    if not problem.candidate_families:
        return False
    io = problem.input_output
    if not io or not io.get("inputs") or not io.get("outputs"):
        return False
    n = min(len(io["inputs"]), len(io["outputs"]))
    return n >= min_tests


def _qualified_full_pass(row: dict[str, Any], *, min_tests: int) -> bool:
    if not row.get("full_pass"):
        return False
    total = int(row.get("total_tests") or 0)
    return total >= min_tests and int(row.get("passed_tests") or 0) == total


def _load_completed(path: Path) -> set[str]:
    done: set[str] = set()
    if not path.exists():
        return done
    for row in _iter_jsonl(path):
        pid = row.get("problem_id")
        if pid:
            done.add(str(pid))
    return done


def _iter_jsonl(path: Path):
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def _resolve_verified_source(settings: Settings, options: Pass1Options) -> str:
    p1 = cfg_section(settings, "pass1")
    raw = options.verified_source or p1.get("verified_source", "local")
    source = str(raw).strip().lower()
    if source in {"taco-verified", "taco_verified", "verified"}:
        return "taco-verified"
    if source in {"codecontests-local", "codecontests_local", "codecontests"}:
        return "codecontests-local"
    if source == "local":
        return "local"
    raise ValueError(
        f"Unknown pass1.verified_source: {raw!r} "
        "(use local | taco-verified | codecontests-local)"
    )


def _iterate_taco_verified(hf_name: str, split: str, cache_dir: Path) -> Iterator[dict[str, Any]]:
    try:
        from datasets import load_dataset
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("Need datasets to read TACO-verified: pip install datasets") from exc
    cache_dir.mkdir(parents=True, exist_ok=True)
    LOG.info("Loading TACO-verified %s split=%s …", hf_name, split)
    ds = load_dataset(hf_name, split=split, cache_dir=str(cache_dir))
    for row in ds:
        yield dict(row)


def _iterate_codecontests(
    hf_name: str,
    split: str,
    cache_dir: Path,
    *,
    streaming: bool = False,
) -> Iterator[dict[str, Any]]:
    try:
        from datasets import load_dataset
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("Need datasets to read CodeContests: pip install datasets") from exc
    cache_dir.mkdir(parents=True, exist_ok=True)
    LOG.info("Loading CodeContests %s split=%s streaming=%s", hf_name, split, streaming)
    ds = load_dataset(hf_name, split=split, cache_dir=str(cache_dir), streaming=streaming)
    for row in ds:
        yield dict(row)


def _problem_provenance(problem: Any) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "source_dataset": str(getattr(problem, "source_dataset", "TACO")),
        "split": str(getattr(problem, "split", "train")),
    }
    for field in (
        "source_problem_fingerprint",
        "selected_test_counts",
        "test_selection_policy",
        "family_evidence_method",
        "open_family_candidates",
        "cf_tags",
        "cf_contest_id",
        "cf_index",
    ):
        value = getattr(problem, field, None)
        if value not in (None, "", {}):
            payload[field] = value
    return payload


def _parse_verified_record(record: dict[str, Any]) -> RawTacoProblem | None:
    raw_id = record.get("id")
    try:
        source_index = int(raw_id)
    except (TypeError, ValueError):
        LOG.warning("Skipping TACO-verified row with non-integer id=%r", raw_id)
        return None
    return _parse_raw_taco_problem(source_index, record)


def _verified_solution_rows(
    problem: RawTacoProblem,
    *,
    max_solutions: int,
    min_tests: int,
) -> list[dict[str, Any]]:
    """Trust likaixin/TACO-verified correctness; only syntax-check locally."""
    solutions = problem.reference_solutions
    if max_solutions > 0:
        solutions = solutions[:max_solutions]
    io = problem.input_output or {}
    total_tests = min(len(io.get("inputs") or []), len(io.get("outputs") or []))
    rows: list[dict[str, Any]] = []
    for sol in solutions:
        code = sol["code"]
        syntax_ok, syntax_error, _tree = _syntax_check(code)
        hints = ast_to_family_hints(solution_ast_features(code)) if syntax_ok else []
        full_pass = bool(syntax_ok and total_tests >= min_tests)
        passed = total_tests if full_pass else 0
        report = {
            "all_passed": full_pass,
            "num_tests": total_tests,
            "num_passed": passed,
            "reason_summary": {"external_verified": 1} if full_pass else {"external_verified_syntax_error": 1},
            "per_test": [],
        }
        rows.append(
            {
                **_problem_provenance(problem),
                "problem_id": problem.problem_id,
                "solution_id": sol["solution_id"],
                "solution_code": code,
                "source_language": sol.get("source_language", "PYTHON3"),
                "source_index": problem.source_index,
                "source": problem.source,
                "difficulty": problem.difficulty,
                "problem_statement": problem.problem_statement,
                "original_skill_types": problem.original_skill_types,
                "original_tags": problem.original_tags,
                "problem_families": list(problem.candidate_families),
                "candidate_families": list(problem.candidate_families),
                "solution_family_hints": hints,
                "input_output": problem.input_output,
                "judge_style": _judge_style(problem.input_output),
                "syntax_ok": syntax_ok,
                "syntax_error": syntax_error,
                "safe_exec_ok": syntax_ok,
                "safety_issues": [],
                "full_pass": full_pass,
                "passed_tests": passed,
                "total_tests": total_tests,
                "pass_rate": (passed / total_tests) if total_tests else 0.0,
                "avg_time_ms": 0.0,
                "execution_result": report,
                "verification_source": "taco-verified",
            }
        )
    return rows


def _finalize_problem(
    *,
    problem: RawTacoProblem,
    candidates_path: Path,
    problems_path: Path,
    full_pass_rows: list[dict[str, Any]],
    stats: dict[str, Any],
    completed: set[str],
) -> None:
    if getattr(problem, "open_family_candidates", False):
        split_type = "multi_clean" if full_pass_rows else "noisy_or_unverified"
    elif _is_obvious_mismatch(problem.candidate_families, full_pass_rows):
        split_type = "mismatch"
    else:
        split_type = _classify_clean_split(problem, full_pass_rows)
    stats["clean_split_counts"][split_type] = stats["clean_split_counts"].get(split_type, 0) + 1

    if not full_pass_rows or split_type in {"noisy_or_unverified", "mismatch"}:
        completed.add(problem.problem_id)
        return

    prob_row = {
        **_problem_provenance(problem),
        "problem_id": problem.problem_id,
        "source_index": problem.source_index,
        "problem_statement": problem.problem_statement,
        "problem_families": list(problem.candidate_families),
        "original_skill_types": problem.original_skill_types,
        "original_tags": problem.original_tags,
        "difficulty": problem.difficulty,
        "clean_split": split_type,
        "judge_style": _judge_style(problem.input_output),
        "num_full_pass_solutions": len(full_pass_rows),
        "full_pass_solution_ids": [r["solution_id"] for r in full_pass_rows],
    }
    append_jsonl(candidates_path, prob_row)
    append_jsonl(problems_path, prob_row)
    stats["problems_verified"] += 1
    completed.add(problem.problem_id)


def _pass1_paths(settings: Settings) -> dict[str, Path]:
    out_dir = settings.output_dir / "pass1_manifest"
    out_dir.mkdir(parents=True, exist_ok=True)
    return {
        "out_dir": out_dir,
        "candidates": out_dir / "candidates.jsonl",
        "verified_solutions": out_dir / "verified_solutions.jsonl",
        "verified_problems": out_dir / "verified_problems.jsonl",
        "summary": out_dir / "summary.json",
    }


def _run_pass1_taco_verified(settings: Settings, options: Pass1Options, p1: dict[str, Any]) -> dict[str, Path]:
    min_tests = int(p1.get("min_official_tests", 5))
    min_statement = int(p1.get("min_statement_chars", 80))
    max_solutions = int(p1.get("max_solutions_per_problem", 5))
    log_every = max(1, int(p1.get("log_every_problems", 100)))

    paths = _pass1_paths(settings)
    hf_name = str(p1.get("taco_verified_hf_name", "likaixin/TACO-verified"))
    hf_split = str(p1.get("taco_verified_split", "train"))
    cache_dir = settings.cache_dir / "hf_datasets"

    completed = _load_completed(paths["verified_problems"]) if options.resume else set()
    stats = {
        "scanned": 0,
        "pre_scan_pass": 0,
        "problems_verified": 0,
        "solutions_verified": 0,
        "full_pass_solutions": 0,
        "clean_split_counts": {"single_clean": 0, "multi_clean": 0, "mismatch": 0, "noisy_or_unverified": 0},
    }
    started = time.monotonic()

    LOG.info(
        "Pass1 using TACO-verified (no local test execution): %s split=%s",
        hf_name,
        hf_split,
    )

    for record in _iterate_taco_verified(hf_name, hf_split, cache_dir):
        stats["scanned"] += 1
        problem = _parse_verified_record(record)
        if problem is None:
            continue
        if options.problem_ids and problem.problem_id not in options.problem_ids:
            continue
        if not _pre_scan_ok(problem, min_tests=min_tests, min_statement_chars=min_statement):
            continue
        stats["pre_scan_pass"] += 1
        if problem.problem_id in completed:
            if options.limit_problems and stats["problems_verified"] >= options.limit_problems:
                break
            continue
        if options.limit_problems and stats["problems_verified"] >= options.limit_problems:
            break

        solution_rows = _verified_solution_rows(problem, max_solutions=max_solutions, min_tests=min_tests)
        full_pass_rows: list[dict[str, Any]] = []
        for row in solution_rows:
            append_jsonl(paths["verified_solutions"], row)
            stats["solutions_verified"] += 1
            if _qualified_full_pass(row, min_tests=min_tests):
                full_pass_rows.append(row)
                stats["full_pass_solutions"] += 1

        _finalize_problem(
            problem=problem,
            candidates_path=paths["candidates"],
            problems_path=paths["verified_problems"],
            full_pass_rows=full_pass_rows,
            stats=stats,
            completed=completed,
        )

        if stats["problems_verified"] % log_every == 0:
            LOG.info(
                "Pass1 progress (taco-verified): verified_problems=%d full_pass_solutions=%d",
                stats["problems_verified"],
                stats["full_pass_solutions"],
            )

    summary = {
        "verification_source": "taco-verified",
        "external_dataset": {"name": hf_name, "split": hf_split},
        "elapsed_seconds": round(time.monotonic() - started, 2),
        "min_official_tests": min_tests,
        "outputs": {k: str(v) for k, v in paths.items() if k != "out_dir"},
        "stats": stats,
    }
    save_json(paths["summary"], summary)
    LOG.info("Pass1 done (taco-verified): %s", summary["stats"])
    return {
        "candidates": paths["candidates"],
        "verified_solutions": paths["verified_solutions"],
        "verified_problems": paths["verified_problems"],
        "summary": paths["summary"],
    }


def _run_pass1_local(settings: Settings, options: Pass1Options, p1: dict[str, Any]) -> dict[str, Path]:
    eval_cfg = settings.config.get("evaluation") or {}
    min_tests = int(p1.get("min_official_tests", 5))
    min_statement = int(p1.get("min_statement_chars", 80))
    max_solutions = int(p1.get("max_solutions_per_problem", 5))
    max_tests_default = int(p1.get("max_tests_per_solution", 0))
    log_every = max(1, int(p1.get("log_every_problems", 100)))
    blocked_imports = set(p1.get("blocked_imports") or DEFAULT_BLOCKED_IMPORTS)
    blocked_calls = set(p1.get("blocked_calls") or DEFAULT_BLOCKED_CALLS)

    paths = _pass1_paths(settings)
    hf_name = settings.config["paths"]["taco_hf_name"]
    hf_split = settings.config["paths"]["taco_hf_split"]
    cache_dir = settings.cache_dir / "hf_datasets"
    cache_dir.mkdir(parents=True, exist_ok=True)

    completed = _load_completed(paths["verified_problems"]) if options.resume else set()
    stats = {
        "scanned": 0,
        "pre_scan_pass": 0,
        "problems_verified": 0,
        "solutions_verified": 0,
        "full_pass_solutions": 0,
        "clean_split_counts": {"single_clean": 0, "multi_clean": 0, "mismatch": 0, "noisy_or_unverified": 0},
    }
    started = time.monotonic()

    LOG.info("Pass1 using local test execution on %s split=%s", hf_name, hf_split)
    dataset = _iterate_taco(hf_name, hf_split, cache_dir=cache_dir)
    for dataset_index, raw in enumerate(dataset):
        stats["scanned"] += 1
        problem = _parse_raw_taco_problem(dataset_index, raw)
        if problem is None:
            continue
        if options.problem_ids and problem.problem_id not in options.problem_ids:
            continue
        if not _pre_scan_ok(problem, min_tests=min_tests, min_statement_chars=min_statement):
            continue
        stats["pre_scan_pass"] += 1
        if problem.problem_id in completed:
            if options.limit_problems and stats["problems_verified"] >= options.limit_problems:
                break
            continue
        if options.limit_problems and stats["problems_verified"] >= options.limit_problems:
            break

        solutions = problem.reference_solutions[:max_solutions] if max_solutions > 0 else problem.reference_solutions
        full_pass_rows: list[dict[str, Any]] = []
        test_limit = _max_tests(problem.input_output, None, max_tests_default) if problem.input_output else 0

        for sol in solutions:
            code = sol["code"]
            syntax_ok, syntax_error, tree = _syntax_check(code)
            safe_ok, safety_issues = _safe_execution_precheck(
                tree, blocked_imports=blocked_imports, blocked_calls=blocked_calls
            )
            hints = ast_to_family_hints(solution_ast_features(code)) if syntax_ok else []
            if not syntax_ok:
                report = {"all_passed": False, "num_tests": 0, "num_passed": 0, "reason_summary": {"syntax_error": 1}}
                avg_ms = 0.0
            elif not safe_ok:
                report = {"all_passed": False, "num_tests": 0, "num_passed": 0, "reason_summary": {"unsafe_precheck": 1}}
                avg_ms = 0.0
            else:
                report, avg_ms = _execute_solution_tests(
                    code=code,
                    input_output=problem.input_output,
                    max_tests=test_limit,
                    eval_cfg=eval_cfg,
                )
                stats["solutions_verified"] += 1

            passed = int(report.get("num_passed") or 0)
            total = int(report.get("num_tests") or 0)
            full_pass = bool(report.get("all_passed")) and total >= min_tests
            row = {
                **_problem_provenance(problem),
                "problem_id": problem.problem_id,
                "solution_id": sol["solution_id"],
                "solution_code": code,
                "source_language": sol.get("source_language", "PYTHON3"),
                "source_index": problem.source_index,
                "source": problem.source,
                "difficulty": problem.difficulty,
                "problem_statement": problem.problem_statement,
                "original_skill_types": problem.original_skill_types,
                "original_tags": problem.original_tags,
                "problem_families": list(problem.candidate_families),
                "candidate_families": list(problem.candidate_families),
                "solution_family_hints": hints,
                "input_output": problem.input_output,
                "judge_style": _judge_style(problem.input_output),
                "syntax_ok": syntax_ok,
                "syntax_error": syntax_error,
                "safe_exec_ok": safe_ok and syntax_ok,
                "safety_issues": safety_issues,
                "full_pass": full_pass,
                "passed_tests": passed,
                "total_tests": total,
                "pass_rate": (passed / total) if total else 0.0,
                "avg_time_ms": avg_ms,
                "execution_result": report,
                "verification_source": "local",
            }
            append_jsonl(paths["verified_solutions"], row)
            if _qualified_full_pass(row, min_tests=min_tests):
                full_pass_rows.append(row)
                stats["full_pass_solutions"] += 1

        _finalize_problem(
            problem=problem,
            candidates_path=paths["candidates"],
            problems_path=paths["verified_problems"],
            full_pass_rows=full_pass_rows,
            stats=stats,
            completed=completed,
        )

        if stats["problems_verified"] % log_every == 0:
            LOG.info("Pass1 progress: verified_problems=%d full_pass_solutions=%d", stats["problems_verified"], stats["full_pass_solutions"])

    summary = {
        "verification_source": "local",
        "elapsed_seconds": round(time.monotonic() - started, 2),
        "min_official_tests": min_tests,
        "outputs": {k: str(v) for k, v in paths.items() if k != "out_dir"},
        "stats": stats,
    }
    save_json(paths["summary"], summary)
    LOG.info("Pass1 done: %s", summary["stats"])
    return {
        "candidates": paths["candidates"],
        "verified_solutions": paths["verified_solutions"],
        "verified_problems": paths["verified_problems"],
        "summary": paths["summary"],
    }


def _run_pass1_codecontests_local(
    settings: Settings,
    options: Pass1Options,
    p1: dict[str, Any],
) -> dict[str, Path]:
    eval_cfg = settings.config.get("evaluation") or {}
    source_cfg = p1.get("codecontests") or {}
    min_tests = int(p1.get("min_official_tests", 5))
    min_statement = int(p1.get("min_statement_chars", 80))
    max_solutions = int(p1.get("max_solutions_per_problem", 5))
    max_tests = int(source_cfg.get("max_tests_per_solution", p1.get("max_tests_per_solution", 20)) or 20)
    allowed_languages = source_cfg.get("allowed_languages") or ["PYTHON3", "PYTHON"]
    streaming = bool(source_cfg.get("streaming", False))
    docker_image = str(source_cfg.get("python2_docker_image", "python:2.7.18-slim-buster"))
    log_every = max(1, int(p1.get("log_every_problems", 100)))
    blocked_imports = set(p1.get("blocked_imports") or DEFAULT_BLOCKED_IMPORTS)
    blocked_calls = set(p1.get("blocked_calls") or DEFAULT_BLOCKED_CALLS)
    sandbox = eval_cfg.get("sandbox", {}) or {}
    memory_mb = int(sandbox.get("memory_limit_mb", eval_cfg.get("memory_mb", 512)))
    per_test_timeout = int(eval_cfg.get("per_test_timeout_seconds", eval_cfg.get("timeout_sec", 5)))

    paths = _pass1_paths(settings)
    hf_name = str(source_cfg.get("hf_name", "deepmind/code_contests"))
    hf_split = str(source_cfg.get("split", "train"))
    cache_dir = settings.cache_dir / "hf_datasets"
    completed = _load_completed(paths["verified_problems"]) if options.resume else set()
    stats: dict[str, Any] = {
        "scanned": 0,
        "pre_scan_pass": 0,
        "problems_verified": 0,
        "solutions_verified": 0,
        "full_pass_solutions": 0,
        "language_candidates": {},
        "full_pass_solution_language_counts": {},
        "failure_reasons": {},
        "clean_split_counts": {"single_clean": 0, "multi_clean": 0, "mismatch": 0, "noisy_or_unverified": 0},
    }
    started = time.monotonic()
    LOG.info("Pass1 using local CodeContests verification: %s split=%s", hf_name, hf_split)

    for dataset_index, raw in enumerate(
        _iterate_codecontests(hf_name, hf_split, cache_dir, streaming=streaming)
    ):
        stats["scanned"] += 1
        if stats["scanned"] % log_every == 0:
            LOG.info(
                "Pass1 CodeContests progress: scanned=%d verified_problems=%d full_pass_solutions=%d",
                stats["scanned"],
                stats["problems_verified"],
                stats["full_pass_solutions"],
            )
        problem = parse_codecontests_problem(
            dataset_index,
            raw,
            split=hf_split,
            allowed_languages=allowed_languages,
            max_solutions=max_solutions,
            max_tests=max_tests,
            min_tests=min_tests,
        )
        if problem is None:
            continue
        if options.problem_ids and problem.problem_id not in options.problem_ids:
            continue
        if not _pre_scan_ok(problem, min_tests=min_tests, min_statement_chars=min_statement):
            continue
        stats["pre_scan_pass"] += 1
        if problem.problem_id in completed:
            continue
        if options.limit_problems and stats["problems_verified"] >= options.limit_problems:
            break

        full_pass_rows: list[dict[str, Any]] = []
        for sol in problem.reference_solutions:
            language = str(sol.get("source_language") or "")
            stats["language_candidates"][language] = stats["language_candidates"].get(language, 0) + 1
            code = sol["code"]
            if language == "PYTHON":
                safe_ok, safety_issues = safe_python2_precheck(
                    code,
                    blocked_imports=blocked_imports,
                    blocked_calls=blocked_calls,
                )
                syntax_ok = safe_ok
                syntax_error = ""
                if safe_ok:
                    report, avg_ms = execute_python2_stdio(
                        code=code,
                        input_output=problem.input_output or {},
                        image=docker_image,
                        per_test_timeout=per_test_timeout,
                        memory_mb=memory_mb,
                    )
                else:
                    report = {"all_passed": False, "num_tests": 0, "num_passed": 0, "reason_summary": {"unsafe_precheck": 1}, "per_test": []}
                    avg_ms = 0.0
                verification_source = "codecontests-local-python2-docker"
            else:
                syntax_ok, syntax_error, tree = _syntax_check(code)
                safe_ok, safety_issues = _safe_execution_precheck(
                    tree, blocked_imports=blocked_imports, blocked_calls=blocked_calls
                )
                if syntax_ok and safe_ok:
                    report, avg_ms = _execute_solution_tests(
                        code=code,
                        input_output=problem.input_output,
                        max_tests=max_tests,
                        eval_cfg=eval_cfg,
                    )
                else:
                    reason = "syntax_error" if not syntax_ok else "unsafe_precheck"
                    report = {"all_passed": False, "num_tests": 0, "num_passed": 0, "reason_summary": {reason: 1}, "per_test": []}
                    avg_ms = 0.0
                verification_source = "codecontests-local-python3"

            passed = int(report.get("num_passed") or 0)
            total = int(report.get("num_tests") or 0)
            full_pass = bool(report.get("all_passed")) and total >= min_tests
            hints = (
                ast_to_family_hints(solution_ast_features(code))
                if language == "PYTHON3" and syntax_ok
                else []
            )
            row = {
                **_problem_provenance(problem),
                "problem_id": problem.problem_id,
                "solution_id": sol["solution_id"],
                "solution_code": code,
                "source_language": language,
                "source_index": problem.source_index,
                "source": problem.source,
                "difficulty": problem.difficulty,
                "problem_statement": problem.problem_statement,
                "original_skill_types": problem.original_skill_types,
                "original_tags": problem.original_tags,
                "problem_families": list(problem.candidate_families),
                "candidate_families": list(problem.candidate_families),
                "solution_family_hints": hints,
                "input_output": problem.input_output,
                "judge_style": "stdio",
                "syntax_ok": syntax_ok,
                "syntax_error": syntax_error,
                "safe_exec_ok": safe_ok and syntax_ok,
                "safety_issues": safety_issues,
                "full_pass": full_pass,
                "passed_tests": passed,
                "total_tests": total,
                "pass_rate": (passed / total) if total else 0.0,
                "avg_time_ms": avg_ms,
                "execution_result": report,
                "verification_source": verification_source,
            }
            append_jsonl(paths["verified_solutions"], row)
            stats["solutions_verified"] += 1
            if _qualified_full_pass(row, min_tests=min_tests):
                full_pass_rows.append(row)
                stats["full_pass_solutions"] += 1
                stats["full_pass_solution_language_counts"][language] = (
                    stats["full_pass_solution_language_counts"].get(language, 0) + 1
                )
            else:
                for reason, count in (report.get("reason_summary") or {}).items():
                    stats["failure_reasons"][reason] = stats["failure_reasons"].get(reason, 0) + int(count)

        _finalize_problem(
            problem=problem,
            candidates_path=paths["candidates"],
            problems_path=paths["verified_problems"],
            full_pass_rows=full_pass_rows,
            stats=stats,
            completed=completed,
        )

    summary = {
        "verification_source": "codecontests-local",
        "external_dataset": {"name": hf_name, "split": hf_split},
        "elapsed_seconds": round(time.monotonic() - started, 2),
        "min_official_tests": min_tests,
        "max_tests_per_solution": max_tests,
        "streaming": streaming,
        "python2_docker_image": docker_image,
        "outputs": {k: str(v) for k, v in paths.items() if k != "out_dir"},
        "stats": stats,
    }
    save_json(paths["summary"], summary)
    LOG.info("Pass1 CodeContests done: %s", stats)
    return {
        "candidates": paths["candidates"],
        "verified_solutions": paths["verified_solutions"],
        "verified_problems": paths["verified_problems"],
        "summary": paths["summary"],
    }


def run_pass1(settings: Settings, options: Pass1Options | None = None) -> dict[str, Path]:
    options = options or Pass1Options()
    p1 = cfg_section(settings, "pass1")
    source = _resolve_verified_source(settings, options)
    if source == "taco-verified":
        return _run_pass1_taco_verified(settings, options, p1)
    if source == "codecontests-local":
        return _run_pass1_codecontests_local(settings, options, p1)
    return _run_pass1_local(settings, options, p1)
