"""Stage C0 - verify raw TACO train reference solutions and build base datasets.

This stage deliberately reads the raw TACO train split instead of Stage A's
sampled universe. Its job is to establish a correctness gate before later
solution labeling or skill construction consumes reference solutions.
"""
from __future__ import annotations

import ast
import contextlib
import json
import os
import re
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .evaluation.executor import _apply_rlimits, execute_stdio, report_to_dict
from .io_utils import read_jsonl, save_json
from .logging_utils import get_logger
from .rules import ast_to_family_hints, solution_ast_features
from .settings import Settings
from .stage_a_filter import (
    _canonical_problem_id,
    _extract_input_output,
    _extract_solutions,
    _extract_text_list,
    _iterate_taco,
)
from .taxonomy import tags_to_core_families

LOG = get_logger(__name__)


DEFAULT_BLOCKED_IMPORTS = {
    "os",
    "subprocess",
    "socket",
    "requests",
    "urllib",
    "http",
    "ftplib",
    "pathlib",
    "shutil",
    "glob",
    "multiprocessing",
    "threading",
    "ctypes",
}
DEFAULT_BLOCKED_CALLS = {
    "eval",
    "exec",
    "compile",
    "open",
    "__import__",
    "breakpoint",
}
BLOCKED_ATTR_CALLS = {
    "system",
    "popen",
    "spawn",
    "fork",
}


@dataclass(frozen=True)
class RawTacoProblem:
    problem_id: str
    source_index: int
    source: str | None
    difficulty: str | None
    problem_statement: str
    reference_solutions: list[dict[str, str]]
    input_output: dict[str, Any] | None
    original_skill_types: list[str]
    original_tags: list[str]
    candidate_families: list[str]


@dataclass(frozen=True)
class StageC0Overrides:
    limit: int = 0
    problem_ids: set[str] | None = None
    max_tests: int | None = None
    max_solutions: int | None = None
    show_progress: bool | None = None
    log_every: int | None = None
    resume: bool = False
    verified_source: str | None = None


class _JsonlSink:
    def __init__(self, path: Path, *, append: bool = False) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._fh = path.open("a" if append else "w", encoding="utf-8")
        self.count = 0

    def write(self, row: dict[str, Any]) -> None:
        self._fh.write(json.dumps(row, ensure_ascii=False, sort_keys=False))
        self._fh.write("\n")
        self._fh.flush()
        self.count += 1

    def close(self) -> None:
        self._fh.close()

    def __enter__(self) -> "_JsonlSink":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


def _parse_raw_taco_problem(dataset_index: int, record: dict[str, Any]) -> RawTacoProblem | None:
    question = record.get("question") or record.get("problem") or ""
    if not isinstance(question, str) or not question.strip():
        return None
    solutions = _extract_solutions(record.get("solutions"))
    skill_types = _extract_text_list(record.get("skill_types"))
    raw_tags = _extract_text_list(record.get("tags") or record.get("raw_tags"))
    candidate_families = tags_to_core_families(skill_types + raw_tags)
    return RawTacoProblem(
        problem_id=_canonical_problem_id(dataset_index, record),
        source_index=dataset_index,
        source=record.get("source") if isinstance(record.get("source"), str) else None,
        difficulty=record.get("difficulty") if isinstance(record.get("difficulty"), str) else None,
        problem_statement=question.strip(),
        reference_solutions=[
            {"solution_id": f"s{idx}", "code": code}
            for idx, code in enumerate(solutions)
        ],
        input_output=_extract_input_output(record.get("input_output")),
        original_skill_types=skill_types,
        original_tags=raw_tags,
        candidate_families=candidate_families,
    )


def _syntax_check(code: str) -> tuple[bool, str, ast.Module | None]:
    try:
        return True, "", ast.parse(code)
    except SyntaxError as exc:
        return False, f"{exc.__class__.__name__}: {exc}", None


def _safe_execution_precheck(
    tree: ast.Module | None,
    *,
    blocked_imports: set[str],
    blocked_calls: set[str],
) -> tuple[bool, list[str]]:
    if tree is None:
        return False, ["syntax_error"]
    issues: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".", 1)[0]
                if root in blocked_imports:
                    issues.append(f"blocked_import:{alias.name}")
        elif isinstance(node, ast.ImportFrom):
            root = (node.module or "").split(".", 1)[0]
            if root in blocked_imports:
                issues.append(f"blocked_import:{node.module}")
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in blocked_calls:
                issues.append(f"blocked_call:{node.func.id}")
            elif isinstance(node.func, ast.Attribute):
                attr = node.func.attr
                root = _attribute_root_name(node.func)
                if attr in BLOCKED_ATTR_CALLS:
                    issues.append(f"blocked_attr_call:{root}.{attr}" if root else f"blocked_attr_call:{attr}")
                if root and root.split(".", 1)[0] in blocked_imports:
                    issues.append(f"blocked_module_call:{root}.{attr}")
    return not issues, sorted(set(issues))


def _attribute_root_name(node: ast.Attribute) -> str:
    parts: list[str] = [node.attr]
    value: ast.AST = node.value
    while isinstance(value, ast.Attribute):
        parts.append(value.attr)
        value = value.value
    if isinstance(value, ast.Name):
        parts.append(value.id)
    return ".".join(reversed(parts))


def _max_tests(input_output: dict[str, Any], max_tests_override: int | None, default_max_tests: int) -> int:
    inputs = input_output.get("inputs") or []
    outputs = input_output.get("outputs") or []
    available = min(len(inputs), len(outputs))
    raw = max_tests_override if max_tests_override is not None else default_max_tests
    if raw is None or int(raw) <= 0:
        return available
    return min(available, int(raw))


def _coerce_value(value: Any) -> Any:
    if isinstance(value, list):
        return [_coerce_value(v) for v in value]
    if isinstance(value, dict):
        return {str(k): _coerce_value(v) for k, v in value.items()}
    if not isinstance(value, str):
        return value
    text = value.strip()
    if text[:1] in {"[", "{", "("}:
        with contextlib.suppress(Exception):
            return _coerce_value(ast.literal_eval(text))
    if re.fullmatch(r"[-+]?\d+", text) and len(text.lstrip("+-")) <= 18:
        try:
            return int(text)
        except ValueError:
            return value
    if re.fullmatch(r"[-+]?\d+\.\d+", text):
        try:
            return float(text)
        except ValueError:
            return value
    return value


def _normalise_text(value: Any) -> str:
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value).replace("\r\n", "\n").strip()


def _values_equivalent(actual: Any, expected: Any, stdout: str = "") -> bool:
    expected_coerced = _coerce_value(expected)
    if actual == expected_coerced:
        return True
    if _normalise_text(actual) == _normalise_text(expected_coerced):
        return True
    if stdout and _normalise_text(stdout) == _normalise_text(expected_coerced):
        return True
    return False


_CALL_HARNESS = r"""
import bisect
import collections
import contextlib
import functools
import heapq
import itertools
import io
import json
import math
import sys
import traceback
from typing import *

payload = json.loads(sys.stdin.read())
namespace = {
    "__name__": "__main__",
    "bisect": bisect,
    "collections": collections,
    "functools": functools,
    "heapq": heapq,
    "itertools": itertools,
    "math": math,
    "List": List,
    "Dict": Dict,
    "Set": Set,
    "Tuple": Tuple,
    "Optional": Optional,
    "defaultdict": collections.defaultdict,
    "Counter": collections.Counter,
    "deque": collections.deque,
}
captured = io.StringIO()
try:
    with contextlib.redirect_stdout(captured):
        exec(payload["code"], namespace)
        fn_name = payload["fn_name"]
        target = namespace.get(fn_name)
        if target is None:
            cls = namespace.get("Solution")
            if cls is not None:
                target = getattr(cls(), fn_name, None)
        if not callable(target):
            raise AttributeError(f"call target not found: {fn_name}")
        args = payload["args"]
        if isinstance(args, list):
            result = target(*args)
        else:
            result = target(args)
    print(json.dumps({"ok": True, "result": result, "stdout": captured.getvalue()}, default=str))
except Exception:
    print(json.dumps({"ok": False, "error": traceback.format_exc()[-1500:], "stdout": captured.getvalue()}))
    sys.exit(1)
"""


def _execute_call_based(
    *,
    code: str,
    input_output: dict[str, Any],
    per_test_timeout: int,
    cpu_limit_seconds: int,
    memory_limit_mb: int,
    python_executable: str,
    max_tests: int,
) -> dict[str, Any]:
    fn_name = input_output.get("fn_name")
    inputs = input_output.get("inputs") or []
    outputs = input_output.get("outputs") or []
    n = min(len(inputs), len(outputs), max_tests)
    per_test: list[dict[str, Any]] = []
    reason_summary: dict[str, int] = {}

    with tempfile.TemporaryDirectory() as tmpdir:
        harness_path = Path(tmpdir) / "call_harness.py"
        harness_path.write_text(_CALL_HARNESS, encoding="utf-8")
        for idx in range(n):
            payload = {
                "code": code,
                "fn_name": fn_name,
                "args": _coerce_value(inputs[idx]),
            }
            started = time.perf_counter()
            try:
                proc = subprocess.run(
                    [python_executable, str(harness_path)],
                    input=json.dumps(payload, ensure_ascii=False),
                    capture_output=True,
                    timeout=per_test_timeout,
                    text=True,
                    preexec_fn=(lambda: _apply_rlimits(cpu_limit_seconds, memory_limit_mb)) if os.name == "posix" else None,
                    cwd=tmpdir,
                    env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
                )
            except subprocess.TimeoutExpired as exc:
                duration_ms = int((time.perf_counter() - started) * 1000)
                per_test.append({
                    "index": idx,
                    "passed": False,
                    "reason": "timeout",
                    "stdout_tail": "",
                    "stderr_tail": str(exc)[-200:],
                    "duration_ms": duration_ms,
                })
                reason_summary["timeout"] = reason_summary.get("timeout", 0) + 1
                continue

            duration_ms = int((time.perf_counter() - started) * 1000)
            stdout = proc.stdout or ""
            stderr = proc.stderr or ""
            payload_out: dict[str, Any] = {}
            with contextlib.suppress(json.JSONDecodeError):
                payload_out = json.loads(stdout.strip().splitlines()[-1])

            if proc.returncode != 0 or not payload_out.get("ok"):
                reason = "runtime_error"
                per_test.append({
                    "index": idx,
                    "passed": False,
                    "reason": reason,
                    "stdout_tail": stdout[-200:],
                    "stderr_tail": (payload_out.get("error") or stderr)[-200:],
                    "duration_ms": duration_ms,
                })
                reason_summary[reason] = reason_summary.get(reason, 0) + 1
                continue

            passed = _values_equivalent(
                payload_out.get("result"),
                outputs[idx],
                stdout=payload_out.get("stdout") or "",
            )
            reason = "ok" if passed else "wrong_answer"
            per_test.append({
                "index": idx,
                "passed": passed,
                "reason": reason,
                "stdout_tail": (payload_out.get("stdout") or "")[-200:],
                "stderr_tail": "",
                "duration_ms": duration_ms,
            })
            reason_summary[reason] = reason_summary.get(reason, 0) + 1

    num_passed = sum(1 for row in per_test if row["passed"])
    return {
        "all_passed": n > 0 and num_passed == n,
        "num_tests": n,
        "num_passed": num_passed,
        "reason_summary": reason_summary,
        "per_test": per_test,
    }


def _execute_solution_tests(
    *,
    code: str,
    input_output: dict[str, Any] | None,
    max_tests: int,
    eval_cfg: dict[str, Any],
) -> tuple[dict[str, Any], float]:
    if not input_output or not input_output.get("inputs") or not input_output.get("outputs"):
        return {
            "all_passed": False,
            "num_tests": 0,
            "num_passed": 0,
            "reason_summary": {"missing_official_tests": 1},
            "per_test": [],
        }, 0.0

    sandbox = eval_cfg.get("sandbox", {}) or {}
    per_test_timeout = int(eval_cfg.get("per_test_timeout_seconds", 5))
    cpu_limit_seconds = int(sandbox.get("cpu_limit_seconds", 10))
    memory_limit_mb = int(sandbox.get("memory_limit_mb", 512))
    python_executable = str(sandbox.get("python_executable", "python3"))

    started = time.perf_counter()
    if input_output.get("fn_name"):
        report = _execute_call_based(
            code=code,
            input_output=input_output,
            per_test_timeout=per_test_timeout,
            cpu_limit_seconds=cpu_limit_seconds,
            memory_limit_mb=memory_limit_mb,
            python_executable=python_executable,
            max_tests=max_tests,
        )
    else:
        stdio_report = execute_stdio(
            code=code,
            inputs=input_output.get("inputs") or [],
            outputs=input_output.get("outputs") or [],
            fn_name=None,
            per_test_timeout=per_test_timeout,
            cpu_limit_seconds=cpu_limit_seconds,
            memory_limit_mb=memory_limit_mb,
            python_executable=python_executable,
            max_tests=max_tests,
        )
        report = report_to_dict(stdio_report)
    elapsed_ms = (time.perf_counter() - started) * 1000
    avg_time_ms = elapsed_ms / max(1, int(report.get("num_tests") or 0))
    return report, avg_time_ms


def _runtime_error_from_report(report: dict[str, Any]) -> str:
    reasons = report.get("reason_summary") or {}
    if not reasons:
        return ""
    if reasons.get("runtime_error"):
        for row in report.get("per_test") or []:
            if row.get("reason") == "runtime_error":
                return str(row.get("stderr_tail") or row.get("stdout_tail") or "runtime_error")
        return "runtime_error"
    if reasons.get("timeout"):
        return "timeout"
    if reasons.get("missing_official_tests"):
        return "missing_official_tests"
    return ""


def _problem_scope(candidate_families: list[str]) -> str:
    if len(candidate_families) >= 2:
        return "multi"
    if len(candidate_families) == 1:
        return "single"
    return "unknown"


def _is_obvious_mismatch(problem_families: list[str], full_pass_rows: list[dict[str, Any]]) -> bool:
    if not problem_families or not full_pass_rows:
        return False
    problem_set = set(problem_families)
    rows_with_hints = [set(r.get("solution_family_hints") or []) for r in full_pass_rows]
    rows_with_hints = [h for h in rows_with_hints if h]
    if not rows_with_hints:
        return False
    return all(problem_set.isdisjoint(hints) for hints in rows_with_hints)


def _classify_clean_split(problem: RawTacoProblem, full_pass_rows: list[dict[str, Any]]) -> str:
    severe_missing = (
        not problem.problem_statement
        or not problem.candidate_families
        or not problem.input_output
        or not problem.reference_solutions
    )
    if severe_missing or not full_pass_rows:
        return "noisy_or_unverified"
    if _is_obvious_mismatch(problem.candidate_families, full_pass_rows):
        return "mismatch"
    if len(problem.candidate_families) == 1:
        return "single_clean"
    if len(problem.candidate_families) >= 2:
        return "multi_clean"
    return "noisy_or_unverified"


def _problem_base(problem: RawTacoProblem) -> dict[str, Any]:
    scope = _problem_scope(problem.candidate_families)
    return {
        "problem_id": problem.problem_id,
        "source_dataset": "TACO",
        "split": "train",
        "source_index": problem.source_index,
        "source_id_field": problem.problem_id,
        "source": problem.source,
        "difficulty": problem.difficulty,
        "problem_statement": problem.problem_statement,
        "original_skill_types": problem.original_skill_types,
        "original_tags": problem.original_tags,
        "candidate_families": problem.candidate_families,
        "scope": scope,
        "is_multi_skill_problem": scope == "multi",
    }


def _dataset_row(problem: RawTacoProblem, verification_row: dict[str, Any], *, split_type: str) -> dict[str, Any]:
    base = _problem_base(problem)
    return {
        **base,
        "clean_split": split_type,
        "solution_id": verification_row["solution_id"],
        "solution_code": verification_row["solution_code"],
        "solution_family_hints": verification_row.get("solution_family_hints") or [],
        "syntax_ok": verification_row["syntax_ok"],
        "safe_exec_ok": verification_row["safe_exec_ok"],
        "full_pass": verification_row["full_pass"],
        "passed_tests": verification_row["passed_tests"],
        "total_tests": verification_row["total_tests"],
        "pass_rate": verification_row["pass_rate"],
        "avg_time_ms": verification_row["avg_time_ms"],
    }


def _config_int(config: dict[str, Any], key: str, default: int) -> int:
    value = config.get(key, default)
    return int(value) if value is not None else default


def _config_bool(config: dict[str, Any], key: str, default: bool) -> bool:
    value = config.get(key, default)
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)


def _safe_len(value: Any) -> int | None:
    try:
        return len(value)
    except Exception:
        return None


def _format_elapsed(started_at: float) -> str:
    elapsed = int(time.perf_counter() - started_at)
    hours, rem = divmod(elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    if hours:
        return f"{hours}h{minutes:02d}m{seconds:02d}s"
    if minutes:
        return f"{minutes}m{seconds:02d}s"
    return f"{seconds}s"


def _progress_bar(
    *,
    enabled: bool,
    total: int | None,
) -> Any:
    if not enabled:
        return None
    try:
        from tqdm.auto import tqdm
    except ImportError:
        LOG.warning("tqdm is not installed; progress display falls back to periodic log lines.")
        return None
    return tqdm(total=total, desc="Stage C0 raw train", unit="rec", dynamic_ncols=True)


def _filter_jsonl_for_completed(
    path: Path,
    completed_problem_ids: set[str],
    *,
    key_fields: tuple[str, ...] = (),
) -> int:
    """Keep only completed problems, dropping duplicate keys and partial rows."""
    if not path.exists():
        return 0
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    seen: set[tuple[Any, ...]] = set()
    count = 0
    with tmp_path.open("w", encoding="utf-8") as fh:
        for row in read_jsonl(path):
            pid = row.get("problem_id")
            if pid not in completed_problem_ids:
                continue
            if key_fields:
                key = tuple(row.get(field) for field in key_fields)
                if key in seen:
                    continue
                seen.add(key)
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=False))
            fh.write("\n")
            count += 1
    tmp_path.replace(path)
    return count


def _load_resume_state(
    *,
    router_path: Path,
    verification_path: Path,
    single_path: Path,
    multi_path: Path,
    stats: dict[str, int],
    split_counts: dict[str, int],
) -> tuple[set[str], dict[str, int]]:
    completed_problem_ids: set[str] = set()
    router_rows: list[dict[str, Any]] = []
    if router_path.exists():
        for row in read_jsonl(router_path):
            pid = row.get("problem_id")
            if not isinstance(pid, str) or not pid or pid in completed_problem_ids:
                continue
            completed_problem_ids.add(pid)
            router_rows.append(row)

    if not completed_problem_ids:
        for path in (verification_path, router_path, single_path, multi_path):
            if path.exists() and path.stat().st_size > 0:
                LOG.warning(
                    "Resume requested but no completed router checkpoint exists; "
                    "resetting partial Stage C0 artifact: %s",
                    path,
                )
                path.write_text("", encoding="utf-8")
        return set(), {
            "router_dataset_rows": 0,
            "single_skill_generation_rows": 0,
            "multi_skill_composition_rows": 0,
        }

    for row in router_rows:
        stats["parsed_problems"] += 1
        if int(row.get("num_reference_solutions") or 0) > 0:
            stats["problems_with_solutions"] += 1
        if row.get("has_official_tests"):
            stats["problems_with_tests"] += 1
        split = row.get("clean_split")
        if split in split_counts:
            split_counts[split] += 1

    router_count = _filter_jsonl_for_completed(
        router_path,
        completed_problem_ids,
        key_fields=("problem_id",),
    )
    verification_count = _filter_jsonl_for_completed(
        verification_path,
        completed_problem_ids,
        key_fields=("problem_id", "solution_id"),
    )
    single_count = _filter_jsonl_for_completed(
        single_path,
        completed_problem_ids,
        key_fields=("problem_id", "solution_id"),
    )
    multi_count = _filter_jsonl_for_completed(
        multi_path,
        completed_problem_ids,
        key_fields=("problem_id", "solution_id"),
    )

    for row in read_jsonl(verification_path):
        stats["solutions_seen"] += 1
        if row.get("syntax_ok") and row.get("safe_exec_ok"):
            stats["solutions_verified"] += 1
        if row.get("full_pass"):
            stats["full_pass_solutions"] += 1
        if not row.get("syntax_ok"):
            stats["syntax_fail_solutions"] += 1
        if row.get("syntax_ok") and not row.get("safe_exec_ok"):
            stats["unsafe_solutions"] += 1
        if row.get("timeout"):
            stats["timeout_solutions"] += 1
        runtime_error = row.get("runtime_error")
        if runtime_error and runtime_error != "missing_official_tests":
            stats["runtime_error_solutions"] += 1

    LOG.info(
        "Stage C0 resume checkpoint: completed_problems=%d verification_rows=%d single_rows=%d multi_rows=%d",
        router_count,
        verification_count,
        single_count,
        multi_count,
    )
    return completed_problem_ids, {
        "router_dataset_rows": router_count,
        "single_skill_generation_rows": single_count,
        "multi_skill_composition_rows": multi_count,
    }


def _load_taco_verified_by_source_index(
    settings: Settings,
    cfg: dict[str, Any],
) -> tuple[dict[int, dict[str, Any]], dict[str, str]]:
    hf_name = str(cfg.get("taco_verified_hf_name", "likaixin/TACO-verified"))
    split = str(cfg.get("taco_verified_split", "train"))
    cache_dir = settings.cache_dir / "hf_datasets"
    cache_dir.mkdir(parents=True, exist_ok=True)
    try:
        from datasets import load_dataset
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("Need datasets to read TACO-verified: pip install datasets") from exc

    LOG.info("Loading external verified source %s split=%s", hf_name, split)
    ds = load_dataset(hf_name, split=split, cache_dir=str(cache_dir))
    verified: dict[int, dict[str, Any]] = {}
    duplicate_ids = 0
    for row in ds:
        raw_id = row.get("id")
        try:
            source_index = int(raw_id)
        except (TypeError, ValueError):
            LOG.warning("Skipping TACO-verified row with non-integer id=%r", raw_id)
            continue
        if source_index in verified:
            duplicate_ids += 1
            continue
        verified[source_index] = dict(row)
    if duplicate_ids:
        LOG.warning("Skipped %d duplicate TACO-verified ids", duplicate_ids)
    LOG.info("Loaded %d TACO-verified problem rows", len(verified))
    return verified, {"dataset": hf_name, "split": split}


def _external_verified_rows(
    *,
    problem: RawTacoProblem,
    verified_record: dict[str, Any] | None,
    max_solutions: int,
) -> list[dict[str, Any]]:
    if verified_record is None:
        return []
    codes = _extract_solutions(verified_record.get("solutions"))
    if max_solutions and max_solutions > 0:
        codes = codes[:max_solutions]
    tests = _extract_input_output(verified_record.get("input_output")) or problem.input_output or {}
    total_tests = min(len(tests.get("inputs") or []), len(tests.get("outputs") or []))
    eval_mode = "call" if tests.get("fn_name") else "stdio"

    rows: list[dict[str, Any]] = []
    for idx, code in enumerate(codes):
        syntax_ok, syntax_error, _tree = _syntax_check(code)
        solution_hints = (
            ast_to_family_hints(solution_ast_features(code))
            if syntax_ok else []
        )
        full_pass = bool(syntax_ok)
        row = {
            "problem_id": problem.problem_id,
            "solution_id": f"v{idx}",
            "solution_code": code,
            "source_dataset": "TACO",
            "split": "train",
            "source_index": problem.source_index,
            "syntax_ok": syntax_ok,
            "syntax_error": syntax_error,
            "safe_exec_ok": syntax_ok,
            "safety_issues": [],
            "full_pass": full_pass,
            "passed_tests": total_tests if full_pass else 0,
            "total_tests": total_tests,
            "pass_rate": 1.0 if full_pass and total_tests > 0 else 0.0,
            "runtime_error": "" if syntax_ok else syntax_error,
            "timeout": False,
            "avg_time_ms": 0.0,
            "eval_mode": eval_mode,
            "reason_summary": {"external_verified": 1} if full_pass else {"external_verified_syntax_error": 1},
            "execution_result": {
                "all_passed": full_pass,
                "num_tests": total_tests,
                "num_passed": total_tests if full_pass else 0,
                "reason_summary": {"external_verified": 1} if full_pass else {"external_verified_syntax_error": 1},
                "per_test": [],
            },
            "problem_candidate_families": problem.candidate_families,
            "solution_family_hints": solution_hints,
            "verification_source": "taco-verified",
            "external_problem_id": verified_record.get("id"),
            "external_solution_index": idx,
        }
        rows.append(row)
    return rows


def _write_problem_outputs(
    *,
    problem: RawTacoProblem,
    solutions: list[dict[str, str]],
    full_pass_rows: list[dict[str, Any]],
    split_type: str,
    router_sink: _JsonlSink,
    single_sink: _JsonlSink,
    multi_sink: _JsonlSink,
    artifact_counts: dict[str, int],
) -> None:
    full_pass_solution_ids = [row["solution_id"] for row in full_pass_rows]
    router_row = {
        **_problem_base(problem),
        "clean_split": split_type,
        "num_reference_solutions": len(problem.reference_solutions),
        "num_verified_solutions": len(solutions),
        "num_full_pass_solutions": len(full_pass_rows),
        "full_pass_solution_ids": full_pass_solution_ids,
        "has_official_tests": bool(
            problem.input_output
            and problem.input_output.get("inputs")
            and problem.input_output.get("outputs")
        ),
    }
    router_sink.write(router_row)
    artifact_counts["router_dataset_rows"] += 1

    if split_type == "single_clean":
        for row in full_pass_rows:
            single_sink.write({
                **_dataset_row(problem, row, split_type=split_type),
                "family": problem.candidate_families[0],
            })
            artifact_counts["single_skill_generation_rows"] += 1
    elif split_type == "multi_clean":
        for row in full_pass_rows:
            multi_sink.write({
                **_dataset_row(problem, row, split_type=split_type),
                "family_set": problem.candidate_families,
            })
            artifact_counts["multi_skill_composition_rows"] += 1


def _run_stage_c0_taco_verified(settings: Settings, overrides: StageC0Overrides) -> dict[str, Path]:
    cfg = settings.config.get("stage_c0", {}) if isinstance(settings.config, dict) else {}
    split = str(cfg.get("taco_split", settings.config.get("paths", {}).get("taco_hf_split", "train")))
    max_solutions_default = _config_int(cfg, "max_solutions_per_problem", 0)
    show_progress = overrides.show_progress
    if show_progress is None:
        show_progress = _config_bool(cfg, "show_progress", True)
    log_every = overrides.log_every
    if log_every is None:
        log_every = _config_int(cfg, "log_every_problems", 100)
    log_every = max(1, int(log_every))

    out_dir = settings.stage_dir("stage_c0")
    verification_path = out_dir / "solution_verification.jsonl"
    router_path = out_dir / "router_dataset.jsonl"
    single_path = out_dir / "single_skill_generation_dataset.jsonl"
    multi_path = out_dir / "multi_skill_composition_dataset.jsonl"
    summary_path = out_dir / "summary.json"

    split_counts = {
        "single_clean": 0,
        "multi_clean": 0,
        "mismatch": 0,
        "noisy_or_unverified": 0,
    }
    stats = {
        "raw_records_scanned": 0,
        "parsed_problems": 0,
        "problems_with_solutions": 0,
        "problems_with_tests": 0,
        "solutions_seen": 0,
        "solutions_verified": 0,
        "full_pass_solutions": 0,
        "syntax_fail_solutions": 0,
        "unsafe_solutions": 0,
        "timeout_solutions": 0,
        "runtime_error_solutions": 0,
    }
    found_problem_ids: set[str] = set()
    completed_problem_ids: set[str] = set()
    artifact_counts = {
        "router_dataset_rows": 0,
        "single_skill_generation_rows": 0,
        "multi_skill_composition_rows": 0,
    }
    if overrides.resume:
        completed_problem_ids, artifact_counts = _load_resume_state(
            router_path=router_path,
            verification_path=verification_path,
            single_path=single_path,
            multi_path=multi_path,
            stats=stats,
            split_counts=split_counts,
        )

    verified_by_source_index, external_meta = _load_taco_verified_by_source_index(settings, cfg)

    hf_name = settings.config["paths"]["taco_hf_name"]
    hf_cache = settings.cache_dir / "hf_datasets"
    hf_cache.mkdir(parents=True, exist_ok=True)
    LOG.info(
        "Stage C0: building datasets from raw TACO %s split=%s plus %s split=%s",
        hf_name,
        split,
        external_meta["dataset"],
        external_meta["split"],
    )
    dataset = _iterate_taco(hf_name, split, cache_dir=hf_cache)
    total_records = _safe_len(dataset)
    started_at = time.perf_counter()
    processed_this_run = 0

    with (
        _JsonlSink(verification_path, append=overrides.resume) as verification_sink,
        _JsonlSink(router_path, append=overrides.resume) as router_sink,
        _JsonlSink(single_path, append=overrides.resume) as single_sink,
        _JsonlSink(multi_path, append=overrides.resume) as multi_sink,
    ):
        progress = _progress_bar(enabled=bool(show_progress), total=total_records)
        try:
            for dataset_index, raw in enumerate(dataset):
                stats["raw_records_scanned"] += 1
                if progress is not None:
                    progress.update(1)

                problem = _parse_raw_taco_problem(dataset_index, raw)
                if problem is None:
                    continue
                if overrides.problem_ids and problem.problem_id not in overrides.problem_ids:
                    continue
                if problem.problem_id in completed_problem_ids:
                    found_problem_ids.add(problem.problem_id)
                    if overrides.problem_ids and found_problem_ids >= overrides.problem_ids:
                        break
                    continue

                found_problem_ids.add(problem.problem_id)
                stats["parsed_problems"] += 1
                processed_this_run += 1
                if problem.reference_solutions:
                    stats["problems_with_solutions"] += 1
                if problem.input_output and problem.input_output.get("inputs") and problem.input_output.get("outputs"):
                    stats["problems_with_tests"] += 1

                max_solutions = overrides.max_solutions
                if max_solutions is None:
                    max_solutions = max_solutions_default
                verification_rows = _external_verified_rows(
                    problem=problem,
                    verified_record=verified_by_source_index.get(problem.source_index),
                    max_solutions=max_solutions,
                )
                stats["solutions_seen"] += len(verification_rows)
                full_pass_rows: list[dict[str, Any]] = []
                for row in verification_rows:
                    verification_sink.write(row)
                    if row.get("syntax_ok") and row.get("safe_exec_ok"):
                        stats["solutions_verified"] += 1
                    if row.get("full_pass"):
                        stats["full_pass_solutions"] += 1
                        full_pass_rows.append(row)
                    if not row.get("syntax_ok"):
                        stats["syntax_fail_solutions"] += 1
                    if row.get("syntax_ok") and not row.get("safe_exec_ok"):
                        stats["unsafe_solutions"] += 1
                    runtime_error = row.get("runtime_error")
                    if runtime_error and runtime_error != "missing_official_tests":
                        stats["runtime_error_solutions"] += 1

                split_type = _classify_clean_split(problem, full_pass_rows)
                split_counts[split_type] += 1
                _write_problem_outputs(
                    problem=problem,
                    solutions=[{"solution_id": row["solution_id"], "code": row["solution_code"]} for row in verification_rows],
                    full_pass_rows=full_pass_rows,
                    split_type=split_type,
                    router_sink=router_sink,
                    single_sink=single_sink,
                    multi_sink=multi_sink,
                    artifact_counts=artifact_counts,
                )
                completed_problem_ids.add(problem.problem_id)

                if progress is not None:
                    progress.set_postfix(
                        problems=stats["parsed_problems"],
                        verified=stats["solutions_verified"],
                        full_pass=stats["full_pass_solutions"],
                        refresh=False,
                    )
                if stats["parsed_problems"] % log_every == 0:
                    LOG.info(
                        "Stage C0 TACO-verified progress: elapsed=%s raw_scanned=%d/%s problems=%d "
                        "verified_solutions=%d full_pass=%d single=%d multi=%d mismatch=%d noisy=%d",
                        _format_elapsed(started_at),
                        stats["raw_records_scanned"],
                        total_records if total_records is not None else "?",
                        stats["parsed_problems"],
                        stats["solutions_verified"],
                        stats["full_pass_solutions"],
                        split_counts["single_clean"],
                        split_counts["multi_clean"],
                        split_counts["mismatch"],
                        split_counts["noisy_or_unverified"],
                    )
                if overrides.limit and processed_this_run >= overrides.limit:
                    break
                if overrides.problem_ids and found_problem_ids >= overrides.problem_ids:
                    break
        finally:
            if progress is not None:
                progress.close()

    missing_problem_ids = sorted((overrides.problem_ids or set()) - found_problem_ids)
    summary = {
        "stage": "stage_c0",
        "verification_source": "taco-verified",
        "source": {
            "dataset": hf_name,
            "split": split,
            "note": "Router rows are read from raw TACO train; verified solutions come from TACO-verified.",
        },
        "external_verified_source": external_meta,
        "run_args": {
            "limit": overrides.limit,
            "problem_ids": sorted(overrides.problem_ids or []),
            "max_tests": overrides.max_tests,
            "max_solutions": overrides.max_solutions,
            "show_progress": show_progress,
            "log_every": log_every,
            "resume": overrides.resume,
            "processed_this_run": processed_this_run,
            "resumed_completed_problems": max(0, stats["parsed_problems"] - processed_this_run),
        },
        "definitions": {
            "single_clean": "problem-level family count is 1, fields are usable, and at least one externally verified solution is usable.",
            "multi_clean": "problem-level family count is >=2, fields are usable, and at least one externally verified solution is usable.",
            "mismatch": "at least one externally verified solution exists, but solution AST family hints are disjoint from the problem-level families for every full_pass solution.",
            "noisy_or_unverified": "no externally verified usable solution, missing official tests/solutions/families, or severe problem-field gaps.",
        },
        "counts": {
            **stats,
            **artifact_counts,
            "clean_split": split_counts,
            "external_verified_problem_rows": len(verified_by_source_index),
        },
        "missing_problem_ids": missing_problem_ids,
        "outputs": {
            "solution_verification": str(verification_path),
            "router_dataset": str(router_path),
            "single_skill_generation_dataset": str(single_path),
            "multi_skill_composition_dataset": str(multi_path),
            "summary": str(summary_path),
        },
    }
    save_json(summary_path, summary)
    LOG.info("Stage C0 TACO-verified done: %s", summary["counts"])
    return {
        "solution_verification": verification_path,
        "router_dataset": router_path,
        "single_skill_generation_dataset": single_path,
        "multi_skill_composition_dataset": multi_path,
        "summary": summary_path,
    }


def run_stage_c0(settings: Settings, overrides: StageC0Overrides | None = None) -> dict[str, Path]:
    overrides = overrides or StageC0Overrides()
    cfg = settings.config.get("stage_c0", {}) if isinstance(settings.config, dict) else {}
    verified_source = overrides.verified_source or str(cfg.get("verified_source", "local"))
    if verified_source == "taco-verified":
        return _run_stage_c0_taco_verified(settings, overrides)
    if verified_source != "local":
        raise ValueError(f"Unknown Stage C0 verified source: {verified_source}")

    eval_cfg = settings.config.get("evaluation", {}) if isinstance(settings.config, dict) else {}
    split = str(cfg.get("taco_split", settings.config.get("paths", {}).get("taco_hf_split", "train")))
    max_solutions_default = _config_int(cfg, "max_solutions_per_problem", 0)
    max_tests_default = _config_int(cfg, "max_tests_per_solution", 0)
    show_progress = overrides.show_progress
    if show_progress is None:
        show_progress = _config_bool(cfg, "show_progress", True)
    log_every = overrides.log_every
    if log_every is None:
        log_every = _config_int(cfg, "log_every_problems", 100)
    log_every = max(1, int(log_every))
    blocked_imports = set(cfg.get("blocked_imports") or DEFAULT_BLOCKED_IMPORTS)
    blocked_calls = set(cfg.get("blocked_calls") or DEFAULT_BLOCKED_CALLS)

    out_dir = settings.stage_dir("stage_c0")
    verification_path = out_dir / "solution_verification.jsonl"
    router_path = out_dir / "router_dataset.jsonl"
    single_path = out_dir / "single_skill_generation_dataset.jsonl"
    multi_path = out_dir / "multi_skill_composition_dataset.jsonl"
    summary_path = out_dir / "summary.json"

    hf_name = settings.config["paths"]["taco_hf_name"]
    hf_cache = settings.cache_dir / "hf_datasets"
    hf_cache.mkdir(parents=True, exist_ok=True)

    split_counts = {
        "single_clean": 0,
        "multi_clean": 0,
        "mismatch": 0,
        "noisy_or_unverified": 0,
    }
    stats = {
        "raw_records_scanned": 0,
        "parsed_problems": 0,
        "problems_with_solutions": 0,
        "problems_with_tests": 0,
        "solutions_seen": 0,
        "solutions_verified": 0,
        "full_pass_solutions": 0,
        "syntax_fail_solutions": 0,
        "unsafe_solutions": 0,
        "timeout_solutions": 0,
        "runtime_error_solutions": 0,
    }
    found_problem_ids: set[str] = set()
    completed_problem_ids: set[str] = set()
    artifact_counts = {
        "router_dataset_rows": 0,
        "single_skill_generation_rows": 0,
        "multi_skill_composition_rows": 0,
    }
    if overrides.resume:
        completed_problem_ids, artifact_counts = _load_resume_state(
            router_path=router_path,
            verification_path=verification_path,
            single_path=single_path,
            multi_path=multi_path,
            stats=stats,
            split_counts=split_counts,
        )

    LOG.info(
        "Stage C0: reading raw TACO %s split=%s progress=%s log_every=%d",
        hf_name,
        split,
        bool(show_progress),
        log_every,
    )
    dataset = _iterate_taco(hf_name, split, cache_dir=hf_cache)
    total_records = _safe_len(dataset)
    started_at = time.perf_counter()

    processed_this_run = 0
    with (
        _JsonlSink(verification_path, append=overrides.resume) as verification_sink,
        _JsonlSink(router_path, append=overrides.resume) as router_sink,
        _JsonlSink(single_path, append=overrides.resume) as single_sink,
        _JsonlSink(multi_path, append=overrides.resume) as multi_sink,
    ):
        progress = _progress_bar(enabled=bool(show_progress), total=total_records)
        try:
            for dataset_index, raw in enumerate(dataset):
                stats["raw_records_scanned"] += 1
                if progress is not None:
                    progress.update(1)

                problem = _parse_raw_taco_problem(dataset_index, raw)
                if problem is None:
                    continue
                if overrides.problem_ids and problem.problem_id not in overrides.problem_ids:
                    continue
                if problem.problem_id in completed_problem_ids:
                    found_problem_ids.add(problem.problem_id)
                    if progress is not None:
                        progress.set_postfix(
                            problems=stats["parsed_problems"],
                            resumed=len(completed_problem_ids),
                            verified=stats["solutions_verified"],
                            full_pass=stats["full_pass_solutions"],
                            refresh=False,
                        )
                    if overrides.problem_ids and found_problem_ids >= overrides.problem_ids:
                        break
                    continue

                found_problem_ids.add(problem.problem_id)
                stats["parsed_problems"] += 1
                processed_this_run += 1
                if problem.reference_solutions:
                    stats["problems_with_solutions"] += 1
                if problem.input_output and problem.input_output.get("inputs") and problem.input_output.get("outputs"):
                    stats["problems_with_tests"] += 1

                full_pass_rows: list[dict[str, Any]] = []
                max_solutions = overrides.max_solutions
                if max_solutions is None:
                    max_solutions = max_solutions_default
                solutions = problem.reference_solutions
                if max_solutions and max_solutions > 0:
                    solutions = solutions[:max_solutions]
                stats["solutions_seen"] += len(solutions)

                for sol in solutions:
                    code = sol["code"]
                    syntax_ok, syntax_error, tree = _syntax_check(code)
                    safe_exec_ok, safety_issues = _safe_execution_precheck(
                        tree,
                        blocked_imports=blocked_imports,
                        blocked_calls=blocked_calls,
                    )
                    solution_hints = (
                        ast_to_family_hints(solution_ast_features(code))
                        if syntax_ok else []
                    )

                    if not syntax_ok:
                        report = {
                            "all_passed": False,
                            "num_tests": 0,
                            "num_passed": 0,
                            "reason_summary": {"syntax_error": 1},
                            "per_test": [],
                        }
                        avg_time_ms = 0.0
                        stats["syntax_fail_solutions"] += 1
                    elif not safe_exec_ok:
                        report = {
                            "all_passed": False,
                            "num_tests": 0,
                            "num_passed": 0,
                            "reason_summary": {"unsafe_precheck": 1},
                            "per_test": [],
                        }
                        avg_time_ms = 0.0
                        stats["unsafe_solutions"] += 1
                    else:
                        test_limit = (
                            _max_tests(problem.input_output, overrides.max_tests, max_tests_default)
                            if problem.input_output else 0
                        )
                        report, avg_time_ms = _execute_solution_tests(
                            code=code,
                            input_output=problem.input_output,
                            max_tests=test_limit,
                            eval_cfg=eval_cfg,
                        )
                        stats["solutions_verified"] += 1

                    passed_tests = int(report.get("num_passed") or 0)
                    total_tests = int(report.get("num_tests") or 0)
                    pass_rate = passed_tests / total_tests if total_tests else 0.0
                    timeout = bool((report.get("reason_summary") or {}).get("timeout"))
                    runtime_error = syntax_error if not syntax_ok else _runtime_error_from_report(report)
                    full_pass = bool(report.get("all_passed")) and syntax_ok and safe_exec_ok

                    verification_row = {
                        "problem_id": problem.problem_id,
                        "solution_id": sol["solution_id"],
                        "solution_code": code,
                        "source_dataset": "TACO",
                        "split": "train",
                        "source_index": problem.source_index,
                        "syntax_ok": syntax_ok,
                        "syntax_error": syntax_error,
                        "safe_exec_ok": safe_exec_ok,
                        "safety_issues": safety_issues,
                        "full_pass": full_pass,
                        "passed_tests": passed_tests,
                        "total_tests": total_tests,
                        "pass_rate": pass_rate,
                        "runtime_error": runtime_error,
                        "timeout": timeout,
                        "avg_time_ms": round(avg_time_ms, 3),
                        "eval_mode": "call" if problem.input_output and problem.input_output.get("fn_name") else "stdio",
                        "reason_summary": report.get("reason_summary") or {},
                        "execution_result": report,
                        "problem_candidate_families": problem.candidate_families,
                        "solution_family_hints": solution_hints,
                        "verification_source": "local_executor",
                    }
                    verification_sink.write(verification_row)
                    if full_pass:
                        stats["full_pass_solutions"] += 1
                        full_pass_rows.append(verification_row)
                    if timeout:
                        stats["timeout_solutions"] += 1
                    if runtime_error and runtime_error not in {"missing_official_tests"}:
                        stats["runtime_error_solutions"] += 1

                split_type = _classify_clean_split(problem, full_pass_rows)
                split_counts[split_type] += 1

                full_pass_solution_ids = [row["solution_id"] for row in full_pass_rows]
                router_row = {
                    **_problem_base(problem),
                    "clean_split": split_type,
                    "num_reference_solutions": len(problem.reference_solutions),
                    "num_verified_solutions": len(solutions),
                    "num_full_pass_solutions": len(full_pass_rows),
                    "full_pass_solution_ids": full_pass_solution_ids,
                    "has_official_tests": bool(
                        problem.input_output
                        and problem.input_output.get("inputs")
                        and problem.input_output.get("outputs")
                    ),
                }
                router_sink.write(router_row)
                artifact_counts["router_dataset_rows"] += 1
                completed_problem_ids.add(problem.problem_id)

                if split_type == "single_clean":
                    for row in full_pass_rows:
                        single_sink.write({
                            **_dataset_row(problem, row, split_type=split_type),
                            "family": problem.candidate_families[0],
                        })
                        artifact_counts["single_skill_generation_rows"] += 1
                elif split_type == "multi_clean":
                    for row in full_pass_rows:
                        multi_sink.write({
                            **_dataset_row(problem, row, split_type=split_type),
                            "family_set": problem.candidate_families,
                        })
                        artifact_counts["multi_skill_composition_rows"] += 1

                if progress is not None:
                    progress.set_postfix(
                        problems=stats["parsed_problems"],
                        new=processed_this_run,
                        verified=stats["solutions_verified"],
                        full_pass=stats["full_pass_solutions"],
                        refresh=False,
                    )

                if stats["parsed_problems"] % log_every == 0:
                    LOG.info(
                        "Stage C0 progress: elapsed=%s raw_scanned=%d/%s problems=%d "
                        "verified_solutions=%d full_pass=%d single=%d multi=%d mismatch=%d noisy=%d",
                        _format_elapsed(started_at),
                        stats["raw_records_scanned"],
                        total_records if total_records is not None else "?",
                        stats["parsed_problems"],
                        stats["solutions_verified"],
                        stats["full_pass_solutions"],
                        split_counts["single_clean"],
                        split_counts["multi_clean"],
                        split_counts["mismatch"],
                        split_counts["noisy_or_unverified"],
                    )
                if overrides.limit and processed_this_run >= overrides.limit:
                    break
                if overrides.problem_ids and found_problem_ids >= overrides.problem_ids:
                    break
        finally:
            if progress is not None:
                progress.close()

    missing_problem_ids = sorted((overrides.problem_ids or set()) - found_problem_ids)
    summary = {
        "stage": "stage_c0",
        "verification_source": "local_executor",
        "source": {
            "dataset": hf_name,
            "split": split,
            "note": "Read from raw TACO split, not Stage A sampled outputs.",
        },
        "run_args": {
            "limit": overrides.limit,
            "problem_ids": sorted(overrides.problem_ids or []),
            "max_tests": overrides.max_tests,
            "max_solutions": overrides.max_solutions,
            "show_progress": show_progress,
            "log_every": log_every,
            "resume": overrides.resume,
            "processed_this_run": processed_this_run,
            "resumed_completed_problems": max(0, stats["parsed_problems"] - processed_this_run),
        },
        "config": {
            "max_solutions_per_problem": max_solutions_default,
            "max_tests_per_solution": max_tests_default,
            "blocked_imports": sorted(blocked_imports),
            "blocked_calls": sorted(blocked_calls),
        },
        "definitions": {
            "single_clean": "problem-level family count is 1, fields are usable, and at least one solution full_passes.",
            "multi_clean": "problem-level family count is >=2, fields are usable, and at least one solution full_passes.",
            "mismatch": "at least one full_pass solution exists, but solution AST family hints are disjoint from the problem-level families for every full_pass solution.",
            "noisy_or_unverified": "no full_pass solution, missing official tests/solutions/families, or severe problem-field gaps.",
        },
        "counts": {
            **stats,
            **artifact_counts,
            "clean_split": split_counts,
        },
        "missing_problem_ids": missing_problem_ids,
        "outputs": {
            "solution_verification": str(verification_path),
            "router_dataset": str(router_path),
            "single_skill_generation_dataset": str(single_path),
            "multi_skill_composition_dataset": str(multi_path),
            "summary": str(summary_path),
        },
    }
    save_json(summary_path, summary)
    LOG.info("Stage C0 done: %s", summary["counts"])
    return {
        "solution_verification": verification_path,
        "router_dataset": router_path,
        "single_skill_generation_dataset": single_path,
        "multi_skill_composition_dataset": multi_path,
        "summary": summary_path,
    }
