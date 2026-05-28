from __future__ import annotations

from typing import Any

from .prompt_builder import build_critique_prompt


def critique_skill(
    skill: dict[str, Any],
    generation_input: dict[str, Any],
    llm_client: Any,
    config: dict[str, Any],
) -> dict[str, Any]:
    prompt = build_critique_prompt(skill, generation_input, config)
    sig = generation_input.get("composition_signature") or []
    return llm_client.generate_json(
        prompt,
        cache_key={
            "task": "critique",
            "skill_id": skill.get("skill_id"),
            "signature": sig,
        },
        routing_key=str(skill.get("skill_id") or ""),
    )
