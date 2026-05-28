"""Restricted Python execution against TACO-style tests."""
from __future__ import annotations

import ast
import json
import os
import resource
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

from .config import Settings
from .schemas import ExecutionReport, TestCaseResult


BLOCKED_IMPORTS = {
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
BLOCKED_CALLS = {"eval", "exec", "compile", "open", "__import__", "breakpoint"}


def _rlimits(cpu_seconds: int, memory_mb: int) -> None:
    try:
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds))
    except (OSError, ValueError):
        pass
    try:
        memory = memory_mb * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (memory, memory))
    except (OSError, ValueError):
        pass


def _normalise(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.replace("\r\n", "\n").rstrip("\n").split("\n"))


def _as_stdin(value: Any) -> str:
    if isinstance(value, str):
        return value if value.endswith("\n") else value + "\n"
    if isinstance(value, list):
        return "\n".join(str(item) for item in value) + "\n"
    return str(value) + "\n"


def _as_expected(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(str(item) for item in value)
    return str(value)


def _safety_issue(code: str) -> str | None:
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        return f"syntax_error:{exc.msg}"
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in BLOCKED_IMPORTS:
                    return f"blocked_import:{alias.name}"
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".")[0] in BLOCKED_IMPORTS:
                return f"blocked_import:{node.module}"
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in BLOCKED_CALLS:
            return f"blocked_call:{node.func.id}"
    return None


FN_RUNNER = """\
import importlib.util
import json
import sys

path, fn_name, args_json = sys.argv[1], sys.argv[2], sys.argv[3]
spec = importlib.util.spec_from_file_location("candidate_solution", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
args = json.loads(args_json)
if not isinstance(args, list):
    args = [args]
result = getattr(module, fn_name)(*args)
sys.stdout.write(json.dumps(result, default=str))
"""


class PythonExecutor:
    def __init__(self, settings: Settings) -> None:
        self.cfg = settings.data["evaluation"]

    def execute(self, code: str, input_output: dict[str, Any], *, fn_name: str | None = None) -> ExecutionReport:
        issue = _safety_issue(code)
        inputs = list(input_output.get("inputs") or [])
        outputs = list(input_output.get("outputs") or [])
        n = min(len(inputs), len(outputs), int(self.cfg["max_tests_per_problem"]))
        if issue:
            reason = "compile_error" if issue.startswith("syntax_error") else "unsafe_code"
            return ExecutionReport(
                all_passed=False,
                num_tests=n,
                num_passed=0,
                reason_summary={reason: 1},
                per_test=[TestCaseResult(index=-1, passed=False, reason=reason, stderr=issue)],
            )
        if fn_name:
            return self._execute_function(code, inputs, outputs, fn_name, n)
        return self._execute_stdio(code, inputs, outputs, n)

    def _run(self, command: list[str], *, cwd: str, stdin: str | None = None) -> tuple[subprocess.CompletedProcess[str] | None, str, int]:
        started = time.perf_counter()
        try:
            proc = subprocess.run(
                command,
                input=stdin,
                capture_output=True,
                text=True,
                cwd=cwd,
                timeout=int(self.cfg["per_test_timeout_seconds"]),
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
                preexec_fn=lambda: _rlimits(int(self.cfg["cpu_limit_seconds"]), int(self.cfg["memory_limit_mb"]))
                if os.name == "posix"
                else None,
            )
            return proc, "", int((time.perf_counter() - started) * 1000)
        except subprocess.TimeoutExpired as exc:
            return None, str(exc), int(self.cfg["per_test_timeout_seconds"]) * 1000

    def _execute_stdio(self, code: str, inputs: list[Any], outputs: list[Any], n: int) -> ExecutionReport:
        results: list[TestCaseResult] = []
        summary: dict[str, int] = {}
        with tempfile.TemporaryDirectory(prefix="skill_router_exec_") as tmp:
            path = Path(tmp) / "solution.py"
            path.write_text(code, encoding="utf-8")
            for idx in range(n):
                proc, timeout_error, duration = self._run(
                    [str(self.cfg["python_executable"]), str(path)],
                    cwd=tmp,
                    stdin=_as_stdin(inputs[idx]),
                )
                if proc is None:
                    result = TestCaseResult(index=idx, passed=False, reason="timeout", stderr=timeout_error, duration_ms=duration)
                elif proc.returncode != 0:
                    result = TestCaseResult(
                        index=idx,
                        passed=False,
                        reason="runtime_error",
                        stdout=(proc.stdout or "")[-500:],
                        stderr=(proc.stderr or "")[-1000:],
                        duration_ms=duration,
                    )
                else:
                    passed = _normalise(proc.stdout or "") == _normalise(_as_expected(outputs[idx]))
                    result = TestCaseResult(
                        index=idx,
                        passed=passed,
                        reason="ok" if passed else "wrong_answer",
                        stdout=(proc.stdout or "")[-500:],
                        stderr=(proc.stderr or "")[-500:],
                        duration_ms=duration,
                    )
                results.append(result)
                summary[result.reason] = summary.get(result.reason, 0) + 1
        passed_count = sum(1 for result in results if result.passed)
        return ExecutionReport(
            all_passed=n > 0 and passed_count == n,
            num_tests=n,
            num_passed=passed_count,
            reason_summary=summary,
            per_test=results,
        )

    def _execute_function(self, code: str, inputs: list[Any], outputs: list[Any], fn_name: str, n: int) -> ExecutionReport:
        results: list[TestCaseResult] = []
        summary: dict[str, int] = {}
        with tempfile.TemporaryDirectory(prefix="skill_router_fn_") as tmp:
            path = Path(tmp) / "solution.py"
            runner = Path(tmp) / "_runner.py"
            path.write_text(code, encoding="utf-8")
            runner.write_text(FN_RUNNER, encoding="utf-8")
            for idx in range(n):
                args = inputs[idx] if isinstance(inputs[idx], list) else [inputs[idx]]
                proc, timeout_error, duration = self._run(
                    [str(self.cfg["python_executable"]), str(runner), str(path), fn_name, json.dumps(args)],
                    cwd=tmp,
                )
                if proc is None:
                    result = TestCaseResult(index=idx, passed=False, reason="timeout", stderr=timeout_error, duration_ms=duration)
                elif proc.returncode != 0:
                    result = TestCaseResult(index=idx, passed=False, reason="runtime_error", stderr=(proc.stderr or "")[-1000:], duration_ms=duration)
                else:
                    try:
                        actual = json.loads((proc.stdout or "").strip())
                        passed = actual == outputs[idx]
                    except json.JSONDecodeError:
                        passed = False
                    result = TestCaseResult(index=idx, passed=passed, reason="ok" if passed else "wrong_answer", stdout=(proc.stdout or "")[-500:], duration_ms=duration)
                results.append(result)
                summary[result.reason] = summary.get(result.reason, 0) + 1
        passed_count = sum(1 for result in results if result.passed)
        return ExecutionReport(all_passed=n > 0 and passed_count == n, num_tests=n, num_passed=passed_count, reason_summary=summary, per_test=results)
