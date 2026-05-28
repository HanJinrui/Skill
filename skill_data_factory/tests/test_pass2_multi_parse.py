"""Robust parsing of multi-track LLM JSON payloads."""
from __future__ import annotations

import sys
from pathlib import Path

FACTORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FACTORY_ROOT))
sys.path.insert(0, str(FACTORY_ROOT.parent / "rag_experiment" / "src"))

from sdf.pass2_llm_label_multi import (  # noqa: E402
    _parse_composition_order,
    _parse_composition_subtypes,
)
from sdf.pass2_payload_parse import parse_confidence  # noqa: E402


def test_composition_subtypes_scalar_int_does_not_crash() -> None:
    out = _parse_composition_subtypes(1, {"dp_knapsack", "greedy_exchange"})
    assert out == []


def test_composition_order_scalar_falls_back_to_subtype_order() -> None:
    comp = [{"subtype": "dp_knapsack", "role": "dp"}, {"subtype": "greedy_exchange", "role": "greedy"}]
    assert _parse_composition_order(1, comp) == ["dp_knapsack", "greedy_exchange"]


def test_confidence_word_high_maps_to_float() -> None:
    assert parse_confidence("high") == 0.85


def test_confidence_numeric_clamped() -> None:
    assert parse_confidence(1.5) == 0.98
    assert parse_confidence(85) == 0.85
