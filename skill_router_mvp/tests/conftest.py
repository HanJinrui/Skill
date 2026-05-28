from __future__ import annotations

import json
import sys
from collections.abc import Iterable
from pathlib import Path
from typing import Any

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import Settings, load_settings
from src.skill_bank import SkillBank


class FakeEncoder:
    terms = ["binary", "search", "prefix", "sum", "window", "sorting", "dp", "graph"]

    def encode(self, texts: list[str], **kwargs: Any) -> np.ndarray:
        values = []
        for text in texts:
            lowered = text.lower()
            vec = np.asarray([lowered.count(term) for term in self.terms], dtype=np.float32)
            if not np.any(vec):
                vec[0] = 0.01
            values.append(vec)
        return np.vstack(values)


class FakeLLM:
    model_name = "fake-qwen"

    def __init__(self, responses: Iterable[str]) -> None:
        self.responses = list(responses)
        self.calls: list[tuple[str, str]] = []

    def generate(
        self,
        system: str,
        user: str,
        *,
        temperature: float,
        top_p: float = 0.95,
        max_new_tokens: int,
        seed: int | None = None,
    ) -> str:
        self.calls.append((system, user))
        if not self.responses:
            raise AssertionError("FakeLLM has no queued response.")
        return self.responses.pop(0)


@pytest.fixture
def settings(tmp_path: Path) -> Settings:
    return load_settings(
        overrides={
            "paths": {
                "output_dir": str(tmp_path / "outputs"),
                "index_dir": str(tmp_path / "outputs" / "index"),
                "annotation_dir": str(tmp_path / "outputs" / "annotations"),
                "runs_dir": str(tmp_path / "outputs" / "runs"),
                "reports_dir": str(tmp_path / "outputs" / "reports"),
            },
            "evaluation": {"max_tests_per_problem": 4, "per_test_timeout_seconds": 1},
        }
    )


@pytest.fixture
def bank(settings: Settings) -> SkillBank:
    return SkillBank.from_settings(settings)


def gate_payload(skill_id: str, *, confidence: float = 0.92) -> str:
    return json.dumps(
        {
            "assessments": [
                {
                    "skill_id": skill_id,
                    "applicable": True,
                    "confidence": confidence,
                    "matched_signals": ["matching signal"],
                    "violated_conditions": [],
                    "complexity_fit": "good",
                    "component_scores": {},
                    "reason": "Best direct fit.",
                }
            ],
            "selected_skill_ids": [],
            "selection_type": "fallback",
        }
    )
