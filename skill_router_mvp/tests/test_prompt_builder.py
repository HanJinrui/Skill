from __future__ import annotations

from src.prompt_builder import PromptBuilder
from src.schemas import AlgorithmPlan, GateAssessment, GateDecision, SelectedPlanSkill


def test_planned_code_prompt_does_not_expose_unselected_candidate(settings, bank) -> None:
    selected = bank.by_id["single.prefix_sum_1d.v1"]
    runner = bank.by_id["single.prefix_sum_2d.v1"]
    hidden = bank.by_id["single.graph_dijkstra_shortest_path.v1"]
    gate = GateDecision(
        assessments=[GateAssessment(skill_id=selected.skill_id, applicable=True, confidence=0.9)],
        selected_skill_ids=[selected.skill_id],
        selection_type="single",
        runner_up_skill_id=runner.skill_id,
        runner_up_reason="Not a 2D problem.",
    )
    plan = AlgorithmPlan(
        selected_skills=[SelectedPlanSkill(skill_id=selected.skill_id, confidence=0.9)],
        problem_decomposition=["prefix"],
    )
    _, user = PromptBuilder(settings).code_planned("range sum", [selected], gate, plan)
    assert selected.skill_id in user
    assert runner.skill_id in user
    assert hidden.skill_id not in user
