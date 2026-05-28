from __future__ import annotations

import sys
from pathlib import Path

FACTORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FACTORY_ROOT))
sys.path.insert(0, str(FACTORY_ROOT.parent / "rag_experiment" / "src"))

from sdf.codecontests_adapter import (  # noqa: E402
    parse_codecontests_problem,
    problem_fingerprint,
    select_python_solutions,
    select_stratified_tests,
)
from sdf.codecontests_executor import (  # noqa: E402
    build_python2_docker_command,
    execute_python2_stdio,
    safe_python2_precheck,
)
from src.stage_c0_verify import _execute_solution_tests  # noqa: E402


def _record() -> dict:
    return {
        "description": "Sort numbers and greedily take values while answering dynamic programming transitions.",
        "solutions": {
            "language": [2, 1, 3, 3],
            "solution": ["cpp", "print raw_input()", "print(input())", ""],
        },
        "public_tests": {"input": ["a", "a", "b"], "output": ["1", "1", "2"]},
        "private_tests": {"input": [f"p{i}" for i in range(12)], "output": [str(i) for i in range(12)]},
        "generated_tests": {"input": [f"g{i}" for i in range(7)], "output": [str(i) for i in range(7)]},
        "cf_tags": ["dp", "greedy", "sortings"],
        "cf_contest_id": 123,
        "cf_index": "C",
        "source": 2,
        "difficulty": 1600,
    }


def test_selects_python3_then_python_and_builds_provenance() -> None:
    record = _record()
    solutions = select_python_solutions(record, max_solutions=5)
    assert [row["source_language"] for row in solutions] == ["PYTHON3", "PYTHON"]
    problem = parse_codecontests_problem(12, record)
    assert problem is not None
    assert problem.problem_id == "codecontests_train_000012"
    assert problem.open_family_candidates is True
    assert set(problem.candidate_families) >= {"dynamic_programming", "greedy_algorithms", "sorting"}
    assert problem.source_problem_fingerprint == problem_fingerprint(record["description"])
    assert problem.cf_contest_id == 123
    assert problem.cf_index == "C"


def test_stratified_tests_are_deduplicated_and_capped() -> None:
    tests, counts = select_stratified_tests(_record())
    assert tests is not None
    assert len(tests["inputs"]) == 20
    assert len(set(zip(tests["inputs"], tests["outputs"]))) == 20
    assert counts == {"public": 2, "private": 12, "generated": 6}


def test_problem_requires_python_solution_and_at_least_five_unique_tests() -> None:
    too_few_tests = _record()
    too_few_tests["public_tests"] = {"input": ["only"], "output": ["one"]}
    too_few_tests["private_tests"] = {"input": [], "output": []}
    too_few_tests["generated_tests"] = {"input": [], "output": []}
    assert parse_codecontests_problem(1, too_few_tests) is None

    no_python = _record()
    no_python["solutions"] = {"language": [2], "solution": ["int main() {}"]}
    assert parse_codecontests_problem(2, no_python) is None


def test_python3_reference_executes_through_existing_executor() -> None:
    report, _ = _execute_solution_tests(
        code="print(input().strip())",
        input_output={"inputs": ["ok\n", "yes\n"], "outputs": ["ok\n", "yes\n"]},
        max_tests=2,
        eval_cfg={"per_test_timeout_seconds": 2, "sandbox": {"python_executable": "python3"}},
    )
    assert report["all_passed"] is True


def test_python2_container_command_is_restricted_and_missing_docker_fails(monkeypatch) -> None:
    command = build_python2_docker_command(
        image="python:2.7.18-slim-buster",
        code="print raw_input()",
        memory_mb=512,
        cpu_limit=1.0,
    )
    assert command[:3] == ["docker", "run", "--rm"]
    assert "--network" in command and "none" in command
    assert "--read-only" in command
    assert "--pids-limit" in command
    monkeypatch.setattr("sdf.codecontests_executor.shutil.which", lambda _: None)
    try:
        execute_python2_stdio(
            code="print raw_input()",
            input_output={"inputs": ["x"], "outputs": ["x"]},
            image="python:2.7.18-slim-buster",
            per_test_timeout=1,
            memory_mb=256,
        )
    except RuntimeError as exc:
        assert "requires Docker" in str(exc)
    else:
        raise AssertionError("missing Docker must not silently trust Python 2 evidence")


def test_python2_precheck_rejects_unsafe_calls() -> None:
    ok, issues = safe_python2_precheck(
        "import os\nprint raw_input()\nopen('x')",
        blocked_imports={"os"},
        blocked_calls={"open"},
    )
    assert ok is False
    assert "blocked_import:os" in issues
    assert "blocked_call:open" in issues
