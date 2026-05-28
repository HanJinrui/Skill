"""Normalize messy DeepSeek JSON fields for Pass2 labeling."""
from __future__ import annotations

from typing import Any

_CONFIDENCE_WORDS = {
    "very_high": 0.9,
    "very high": 0.9,
    "high": 0.85,
    "medium": 0.65,
    "med": 0.65,
    "low": 0.45,
    "very_low": 0.35,
    "very low": 0.35,
}


def coerce_bool(value: Any, *, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "1", "yes", "y"}
    if isinstance(value, (int, float)):
        return bool(value)
    return default


def parse_confidence(value: Any, *, default: float = 0.55) -> float:
    """Map numeric or textual confidence to [0.25, 0.98]."""
    if value is None:
        return default
    if isinstance(value, bool):
        return 0.75 if value else default
    if isinstance(value, (int, float)):
        score = float(value)
    elif isinstance(value, str):
        text = value.strip().lower()
        if text in _CONFIDENCE_WORDS:
            return _CONFIDENCE_WORDS[text]
        try:
            score = float(text)
        except ValueError:
            return default
    else:
        return default

    if score > 1.0:
        if score <= 2.0:
            score = min(0.98, score)
        elif score <= 100.0:
            score /= 100.0
        else:
            return default
    return max(0.25, min(0.98, score))
