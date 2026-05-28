from __future__ import annotations

import json

from src.annotation_judge import RouteAutoAnnotator
from src.schemas import AnnotationRow, AutoAnnotationDecision


class FakeCompletion:
    def __init__(self, responses: list[str]) -> None:
        self.responses = responses
        self.users: list[str] = []

    def __call__(self, system: str, user: str) -> str:
        self.users.append(user)
        return self.responses.pop(0)


def _decision(skill_id: str, *, confidence: float = 0.9, review: bool = False) -> str:
    return json.dumps(
        {
            "selected_skill_ids": [skill_id],
            "out_of_bank": False,
            "confidence": confidence,
            "annotation_reason": "The method directly matches the required recurrence.",
            "alternative_skill_ids": [],
            "uncertainty_flags": [],
            "requires_human_review": review,
        }
    )


def test_annotation_uses_full_catalog_and_repairs_unknown_id(settings, bank) -> None:
    valid_id = bank.cards[0].skill_id
    invalid = _decision("unknown.skill.v1")
    completion = FakeCompletion([invalid, _decision(valid_id)])
    annotator = RouteAutoAnnotator(settings, completion)
    result, initial = annotator.annotate(
        {"problem_id": "p1", "scope": "single", "problem_statement": "Solve a recurrence."},
        second_pass=False,
    )
    assert result.selected_skill_ids == [valid_id]
    assert initial is None
    assert "[Complete Skill Catalog]" in completion.users[0]
    assert "candidate_skill_ids" not in completion.users[0]
    assert "[Evaluation Scope]" not in completion.users[0]
    assert len(completion.users) == 2


def test_low_confidence_silver_label_is_held_for_review(settings) -> None:
    workbook = AnnotationRow(problem_id="p2", scope="single")
    decision = AutoAnnotationDecision(
        selected_skill_ids=["single.dp_1d_state.v1"],
        confidence=0.55,
        annotation_reason="A possible one-dimensional recurrence.",
    )
    row = RouteAutoAnnotator.to_annotation_row(
        workbook,
        decision,
        model="deepseek-v4-pro",
        confidence_threshold=0.75,
        initial=None,
    )
    assert row["review_status"] == "needs_review"
    assert row["label_source"] == "deepseek_silver"


def test_annotation_normalizes_omitted_version_and_drops_unknown_alternative(settings) -> None:
    response = json.dumps(
        {
            "selected_skill_ids": ["single.dp_1d_state"],
            "out_of_bank": False,
            "confidence": 0.9,
            "annotation_reason": "One-dimensional dynamic programming.",
            "alternative_skill_ids": ["not_in_bank"],
            "uncertainty_flags": [],
        }
    )
    result, _ = RouteAutoAnnotator(settings, FakeCompletion([response])).annotate(
        {"problem_id": "p3", "problem_statement": "Dynamic programming."},
        second_pass=False,
    )
    assert result.selected_skill_ids == ["single.dp_1d_state.v1"]
    assert result.alternative_skill_ids == []
