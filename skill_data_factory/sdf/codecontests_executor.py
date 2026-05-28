"""Execution helpers for CodeContests language-specific reference solutions."""
from __future__ import annotations

import re
import shutil
import subprocess
import time
from typing import Any


def safe_python2_precheck(
    code: str,
    *,
    blocked_imports: set[str],
    blocked_calls: set[str],
) -> tuple[bool, list[str]]:
    issues: list[str] = []
    for module in blocked_imports:
        if re.search(rf"(?m)^\s*(?:import\s+{re.escape(module)}\b|from\s+{re.escape(module)}\b)", code):
            issues.append(f"blocked_import:{module}")
    for call in blocked_calls:
        if re.search(rf"\b{re.escape(call)}\s*\(", code):
            issues.append(f"blocked_call:{call}")
    return not issues, sorted(set(issues))


def build_python2_docker_command(
    *,
    image: str,
    code: str,
    memory_mb: int,
    cpu_limit: float,
) -> list[str]:
    return [
        "docker",
        "run",
        "--rm",
        "--network",
        "none",
        "--read-only",
        "--pids-limit",
        "64",
        "--memory",
        f"{memory_mb}m",
        "--cpus",
        str(cpu_limit),
        "--user",
        "65534:65534",
        "--tmpfs",
        "/tmp:rw,noexec,nosuid,size=64m",
        "-e",
        "PYTHONDONTWRITEBYTECODE=1",
        "-i",
        image,
        "python",
        "-c",
        code,
    ]


def _output_equivalent(actual: str, expected: str) -> bool:
    return actual.strip().split() == str(expected).strip().split()


def execute_python2_stdio(
    *,
    code: str,
    input_output: dict[str, Any],
    image: str,
    per_test_timeout: int,
    memory_mb: int,
    cpu_limit: float = 1.0,
) -> tuple[dict[str, Any], float]:
    if shutil.which("docker") is None:
        raise RuntimeError("Python 2 CodeContests verification requires Docker, but docker is not installed.")
    inputs = input_output.get("inputs") or []
    outputs = input_output.get("outputs") or []
    command = build_python2_docker_command(
        image=image,
        code=code,
        memory_mb=memory_mb,
        cpu_limit=cpu_limit,
    )
    results: list[dict[str, Any]] = []
    reasons: dict[str, int] = {}
    started_all = time.perf_counter()
    for index, (case_input, expected) in enumerate(zip(inputs, outputs)):
        started = time.perf_counter()
        try:
            proc = subprocess.run(
                command,
                input=str(case_input),
                capture_output=True,
                timeout=per_test_timeout,
                text=True,
            )
            elapsed = int((time.perf_counter() - started) * 1000)
        except subprocess.TimeoutExpired as exc:
            results.append(
                {
                    "index": index,
                    "passed": False,
                    "reason": "timeout",
                    "stdout_tail": "",
                    "stderr_tail": str(exc)[-200:],
                    "duration_ms": per_test_timeout * 1000,
                }
            )
            reasons["timeout"] = reasons.get("timeout", 0) + 1
            continue
        if proc.returncode != 0:
            reason = "runtime_error"
            passed = False
        else:
            passed = _output_equivalent(proc.stdout or "", str(expected))
            reason = "ok" if passed else "wrong_answer"
        results.append(
            {
                "index": index,
                "passed": passed,
                "reason": reason,
                "stdout_tail": (proc.stdout or "")[-200:],
                "stderr_tail": (proc.stderr or "")[-200:],
                "duration_ms": elapsed,
            }
        )
        reasons[reason] = reasons.get(reason, 0) + 1
    passed_count = sum(1 for row in results if row["passed"])
    elapsed_ms = (time.perf_counter() - started_all) * 1000
    report = {
        "all_passed": bool(results) and passed_count == len(results),
        "num_tests": len(results),
        "num_passed": passed_count,
        "reason_summary": reasons,
        "per_test": results,
    }
    return report, elapsed_ms / max(len(results), 1)
