"""Subprocess sandbox to execute a generated Python program against TACO tests.

For each test case we:
  * spawn a fresh `python3 -c ...` (or `python3 path/to/script.py`) subprocess,
    pass the input via stdin, capture stdout,
  * limit wall-clock time with `timeout`,
  * apply RLIMIT_CPU / RLIMIT_AS on POSIX (best-effort).

We *do not* support TACO's call-based `fn_name` mode here (TACO has two eval
modes: stdio and import-and-call-function). Stdio covers the majority of TACO
problems. Records that require `fn_name` are marked skipped in the summary.
"""
from __future__ import annotations

import os
import resource
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class TestResult:
    index: int
    passed: bool
    reason: str            # "ok" | "wrong_answer" | "timeout" | "runtime_error" | "skipped_fn_name"
    stdout: str
    stderr: str
    duration_ms: int


@dataclass
class ExecutionReport:
    all_passed: bool
    num_tests: int
    num_passed: int
    per_test: list[TestResult]
    reason_summary: dict[str, int]


def _apply_rlimits(cpu_seconds: int, mem_mb: int) -> None:
    try:
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds))
    except (ValueError, OSError):
        pass
    try:
        mem_bytes = mem_mb * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (mem_bytes, mem_bytes))
    except (ValueError, OSError):
        pass


def _normalise(text: str) -> str:
    # Competitive-programming graders ignore trailing whitespace/newlines.
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").rstrip("\n").split("\n")]
    return "\n".join(lines)


def _input_to_stdin(value: Any) -> str:
    if isinstance(value, str):
        return value if value.endswith("\n") else value + "\n"
    if isinstance(value, list):
        return "\n".join(str(x) for x in value) + "\n"
    return str(value) + "\n"


def _expected_to_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(str(x) for x in value)
    return str(value)


def execute_stdio(
    *,
    code: str,
    inputs: list[Any],
    outputs: list[Any],
    fn_name: str | None,
    per_test_timeout: int,
    cpu_limit_seconds: int,
    memory_limit_mb: int,
    python_executable: str,
    max_tests: int,
) -> ExecutionReport:
    if fn_name:
        rep = ExecutionReport(
            all_passed=False,
            num_tests=0,
            num_passed=0,
            per_test=[],
            reason_summary={"skipped_fn_name": 1},
        )
        return rep

    n = min(len(inputs), len(outputs), max_tests)
    per_test: list[TestResult] = []
    reasons: dict[str, int] = {}

    with tempfile.TemporaryDirectory() as tmpdir:
        script_path = Path(tmpdir) / "solution.py"
        script_path.write_text(code, encoding="utf-8")
        for i in range(n):
            stdin = _input_to_stdin(inputs[i])
            expected = _normalise(_expected_to_text(outputs[i]))
            try:
                proc = subprocess.run(
                    [python_executable, str(script_path)],
                    input=stdin,
                    capture_output=True,
                    timeout=per_test_timeout,
                    text=True,
                    preexec_fn=(lambda: _apply_rlimits(cpu_limit_seconds, memory_limit_mb)) if os.name == "posix" else None,
                    cwd=tmpdir,
                    env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
                )
            except subprocess.TimeoutExpired as te:
                per_test.append(TestResult(
                    index=i, passed=False, reason="timeout",
                    stdout="", stderr=str(te), duration_ms=per_test_timeout * 1000,
                ))
                reasons["timeout"] = reasons.get("timeout", 0) + 1
                continue

            stdout = proc.stdout or ""
            stderr = proc.stderr or ""
            if proc.returncode != 0:
                per_test.append(TestResult(
                    index=i, passed=False, reason="runtime_error",
                    stdout=stdout[-1000:], stderr=stderr[-1500:], duration_ms=0,
                ))
                reasons["runtime_error"] = reasons.get("runtime_error", 0) + 1
                continue

            actual = _normalise(stdout)
            if actual == expected:
                per_test.append(TestResult(
                    index=i, passed=True, reason="ok",
                    stdout=stdout[-500:], stderr="", duration_ms=0,
                ))
                reasons["ok"] = reasons.get("ok", 0) + 1
            else:
                per_test.append(TestResult(
                    index=i, passed=False, reason="wrong_answer",
                    stdout=stdout[-500:], stderr=stderr[-500:], duration_ms=0,
                ))
                reasons["wrong_answer"] = reasons.get("wrong_answer", 0) + 1

    num_passed = sum(1 for t in per_test if t.passed)
    return ExecutionReport(
        all_passed=(n > 0 and num_passed == n),
        num_tests=n,
        num_passed=num_passed,
        per_test=per_test,
        reason_summary=reasons,
    )


def report_to_dict(report: ExecutionReport) -> dict[str, Any]:
    return {
        "all_passed": report.all_passed,
        "num_tests": report.num_tests,
        "num_passed": report.num_passed,
        "reason_summary": report.reason_summary,
        "per_test": [
            {
                "index": t.index, "passed": t.passed, "reason": t.reason,
                "stdout_tail": t.stdout[-200:], "stderr_tail": t.stderr[-200:],
                "duration_ms": t.duration_ms,
            }
            for t in report.per_test
        ],
    }
