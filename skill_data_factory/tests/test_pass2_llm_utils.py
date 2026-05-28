"""Pass2 token retry helper."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

FACTORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FACTORY_ROOT))
sys.path.insert(0, str(FACTORY_ROOT.parent / "rag_experiment" / "src"))

from src.llm.base import LLMError  # noqa: E402
from sdf.pass2_llm_utils import chat_json_label, pass2_base_max_tokens  # noqa: E402


class _FakeClient:
    def __init__(self, outcomes: list[Exception | dict]) -> None:
        self.outcomes = list(outcomes)
        self.calls: list[int] = []

    def chat_json(self, *, system: str, user: str, temperature: float, max_tokens: int) -> dict:
        self.calls.append(max_tokens)
        item = self.outcomes.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


def test_truncation_bumps_max_tokens_then_succeeds() -> None:
    client = _FakeClient(
        [
            LLMError("DeepSeek output truncated (finish_reason=length); increase max_tokens."),
            {"primary_subtype": "dp_knapsack", "confidence": 0.8},
        ]
    )
    out = chat_json_label(
        client,
        system="s",
        user="u",
        base_max_tokens=2048,
        max_retries=4,
        token_ceiling=8192,
        log_label="test",
        jump_to_ceiling_on_truncation=True,
    )
    assert out["primary_subtype"] == "dp_knapsack"
    assert client.calls[0] == 2048
    assert client.calls[1] == 8192


def test_truncation_jumps_to_ceiling() -> None:
    client = _FakeClient(
        [
            LLMError("DeepSeek output truncated (finish_reason=length); increase max_tokens."),
            {"is_true_composition": False},
        ]
    )
    out = chat_json_label(
        client,
        system="s",
        user="u",
        base_max_tokens=12288,
        max_retries=2,
        token_ceiling=24576,
        log_label="multi",
        jump_to_ceiling_on_truncation=True,
    )
    assert out["is_true_composition"] is False
    assert client.calls == [12288, 24576]


def test_pass2_base_max_tokens_from_config() -> None:
    p2 = {"llm_max_tokens_single": 3000, "llm_max_tokens_multi": 3500}
    assert pass2_base_max_tokens(p2, track="single") == 3000
    assert pass2_base_max_tokens(p2, track="multi") == 3500
