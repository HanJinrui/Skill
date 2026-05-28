"""Policy tests: no rule-only final labels in labeled_solutions."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

FACTORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FACTORY_ROOT))
sys.path.insert(0, str(FACTORY_ROOT.parent / "rag_experiment" / "src"))

from sdf.pass2_rule_candidates import build_rule_candidates  # noqa: E402
from sdf.pass2_llm_label_multi import _composition_candidate_space  # noqa: E402
from sdf.pass1_route import decide_algorithm_scope  # noqa: E402
from src.taxonomy import CORE_FAMILIES  # noqa: E402


def test_rule_candidates_do_not_set_primary_subtype():
    row = {
        "problem_statement": "Given an array, find maximum subarray sum using dynamic programming.",
        "solution_code": "def solve():\n    dp = [0]*n\n    for i in range(n):\n        dp[i]=max(dp[i-1],0)+a[i]\n",
        "problem_families": ["dynamic_programming"],
        "original_skill_types": ["dynamic programming"],
        "original_tags": [],
    }
    pack = build_rule_candidates(row)
    assert "rule_top_subtype" in pack
    assert "candidate_subtypes" in pack
    assert "primary_subtype" not in pack


def test_codecontests_open_candidates_are_not_taco_family_gated():
    row = {
        "problem_statement": "Repeatedly extract the minimum available item.",
        "solution_code": (
            "import heapq\n"
            "heap = []\n"
            "heapq.heappush(heap, 2)\n"
            "heapq.heappop(heap)\n"
        ),
        "problem_families": ["sorting"],
        "original_skill_types": [],
        "original_tags": [],
        "open_family_candidates": True,
    }
    pack = build_rule_candidates(row)
    families = {item["family"] for item in pack["candidate_subtypes"]}
    assert "data_structures" in families
    candidates, candidate_families = _composition_candidate_space(row, pack)
    assert set(candidate_families) == set(CORE_FAMILIES)
    assert {item["family"] for item in candidates} == set(CORE_FAMILIES)


def test_mechanism_scope_single_vs_multi():
    problem = {"problem_families": ["dynamic_programming"], "clean_split": "single_clean"}
    row = {
        "problem_statement": problem,
        "solution_code": "dp=[0]*10\nfor i in range(10): dp[i]=dp[i-1]+1\n",
        "problem_families": ["dynamic_programming"],
        "full_pass": True,
        "passed_tests": 10,
        "total_tests": 10,
        "pass_rate": 1.0,
    }
    scope = decide_algorithm_scope(
        problem,
        [row],
        route_cfg={"single_top2_score_gap": 8.0, "multi_min_subtype_score": 4.0, "allow_problem_multi_tag": True},
    )
    assert scope in {"single", "multi", "quarantine"}


def test_config_requires_llm():
    import yaml

    cfg = yaml.safe_load((Path(__file__).parents[1] / "config.yaml").read_text(encoding="utf-8"))
    assert cfg["pass2"]["require_llm"] is True
    assert cfg["pass2"]["allow_rule_fallback_final"] is False
