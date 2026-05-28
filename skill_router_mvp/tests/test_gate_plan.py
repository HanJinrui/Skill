from __future__ import annotations

import json

from src.gater import SkillGater
from src.planner import AlgorithmPlanner
from src.prompt_builder import PromptBuilder
from src.schemas import GateAssessment, GateDecision, ProblemProfile, RetrievalCandidate

from conftest import FakeLLM, gate_payload


def _candidate(card) -> RetrievalCandidate:
    return RetrievalCandidate(
        skill_id=card.skill_id,
        skill_type=card.skill_type,
        final_score=0.9,
        router_score=0.9,
        card=card,
    )


def test_gate_repairs_invalid_json_then_selects_applicable_single(settings, bank) -> None:
    card = bank.by_id["single.binary_search_on_answer.v1"]
    llm = FakeLLM(["not-json", gate_payload(card.skill_id)])
    gater = SkillGater(settings, llm, PromptBuilder(settings), bank.edges)
    profile = ProblemProfile(statement_summary="minimum feasible capacity", algorithm_signals=["monotonic feasibility"])
    result = gater.gate("minimize maximum capacity", profile, [_candidate(card)])
    assert result.selected_skill_ids == [card.skill_id]
    assert len(llm.calls) == 2


def test_multi_requires_component_evidence(settings, bank) -> None:
    single = bank.by_id["single.binary_search_on_answer.v1"]
    multi = bank.by_id["multi.sorting_binary_search_answer__greedy_two_pointers.v1"]
    decision = GateDecision(
        assessments=[
            GateAssessment(skill_id=single.skill_id, applicable=True, confidence=0.80, complexity_fit="good"),
            GateAssessment(skill_id=multi.skill_id, applicable=True, confidence=0.99, complexity_fit="good", component_scores={}),
        ]
    )
    result = SkillGater(settings, FakeLLM([]), PromptBuilder(settings), bank.edges)._apply_policy(
        decision, [_candidate(single), _candidate(multi)]
    )
    assert result.selected_skill_ids == [single.skill_id]


def test_planner_rejects_hallucinated_skill_then_accepts_repaired_plan(settings, bank) -> None:
    selected = bank.by_id["single.prefix_sum_1d.v1"]
    gate = GateDecision(
        assessments=[GateAssessment(skill_id=selected.skill_id, applicable=True, confidence=0.9)],
        selected_skill_ids=[selected.skill_id],
        selected_confidence=0.9,
        selection_type="single",
    )
    invalid = {
        "selected_skills": [{"skill_id": "single.graph_dijkstra_shortest_path.v1", "role": "main", "confidence": 0.9}],
        "problem_decomposition": ["do it"],
    }
    valid = {
        "problem_id": "p",
        "selected_skills": [{"skill_id": selected.skill_id, "role": "main", "confidence": 0.9}],
        "problem_decomposition": ["build prefix sums", "answer range sum"],
        "complexity": {"time": "O(n)"},
    }
    planner = AlgorithmPlanner(settings, FakeLLM([json.dumps(invalid), json.dumps(valid)]), PromptBuilder(settings))
    plan = planner.plan("p", "range sums", [selected], gate)
    assert plan.selected_skills[0].skill_id == selected.skill_id
