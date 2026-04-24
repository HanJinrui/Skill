"""Unified LLM interfaces for the experiment.

Two protocols:
  * `ChatLLM` – structured-output oriented, used for GLM labeling / skill synthesis.
  * `CodeLLM` – code generator with sampling controls, used for Qwen.

Both are kept provider-agnostic so we can swap Zhipu / OpenAI / vLLM trivially.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Protocol


class LLMError(RuntimeError):
    pass


@dataclass(frozen=True)
class ChatMessage:
    role: str  # "system" | "user" | "assistant"
    content: str


class ChatLLM(Protocol):
    provider: str
    model: str

    def chat_json(
        self,
        system: str,
        user: str,
        *,
        temperature: float | None = None,
        max_tokens: int | None = None,
        response_format_json: bool = True,
    ) -> dict[str, Any]:
        ...


class CodeLLM(Protocol):
    provider: str
    model: str

    def generate(
        self,
        system: str,
        user: str,
        *,
        temperature: float,
        top_p: float,
        max_new_tokens: int,
        n: int = 1,
        stop: list[str] | None = None,
        seed: int | None = None,
    ) -> list[str]:
        ...


def parse_json_object(text: str) -> dict[str, Any]:
    """Robustly parse a JSON object out of model output."""
    if not text:
        raise LLMError("empty model output")
    stripped = text.strip()
    if stripped.startswith("```"):
        # strip ```json ... ``` fences
        stripped = stripped.strip("`")
        if stripped.lower().startswith("json"):
            stripped = stripped[4:]
        stripped = stripped.strip("` \n")
    try:
        obj = json.loads(stripped)
        if isinstance(obj, dict):
            return obj
    except json.JSONDecodeError:
        pass
    decoder = json.JSONDecoder()
    for i, ch in enumerate(stripped):
        if ch != "{":
            continue
        try:
            obj, _ = decoder.raw_decode(stripped[i:])
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            return obj
    raise LLMError(f"could not parse JSON object from model output: {text[:200]!r}")
