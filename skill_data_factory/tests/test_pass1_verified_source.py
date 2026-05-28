"""Pass1 external verification row builder."""
from __future__ import annotations

import sys
from pathlib import Path

FACTORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FACTORY_ROOT))
sys.path.insert(0, str(FACTORY_ROOT.parent / "rag_experiment" / "src"))

from src.stage_c0_verify import RawTacoProblem  # noqa: E402
from sdf.pass1_verify import (  # noqa: E402
    _qualified_full_pass,
    _resolve_verified_source,
    _verified_solution_rows,
)
from sdf.factory_settings import get_settings  # noqa: E402


def test_verified_rows_trust_external_without_execution():
    problem = RawTacoProblem(
        problem_id="taco_train_000001",
        source_index=1,
        source="codeforces",
        difficulty="EASY",
        problem_statement="Given n numbers, print their sum.",
        reference_solutions=[{"solution_id": "s0", "code": "n=int(input())\nprint(sum(map(int,input().split())))\n"}],
        input_output={
            "inputs": ["3\n1 2 3", "1\n5"],
            "outputs": ["6", "5"],
            "fn_name": None,
        },
        original_skill_types=["math"],
        original_tags=[],
        candidate_families=["greedy_algorithms"],
    )
    rows = _verified_solution_rows(problem, max_solutions=5, min_tests=2)
    assert len(rows) == 1
    row = rows[0]
    assert row["verification_source"] == "taco-verified"
    assert row["full_pass"] is True
    assert row["total_tests"] == 2
    assert row["passed_tests"] == 2
    assert _qualified_full_pass(row, min_tests=2)


def test_config_defaults_to_taco_verified():
    settings = get_settings()
    assert _resolve_verified_source(settings, type("O", (), {"verified_source": None})()) == "taco-verified"
