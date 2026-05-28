from __future__ import annotations

from typing import Any

from .prompt_builder import build_revision_prompt


def revise_skill(
    skill: dict[str, Any],
    critique: dict[str, Any],
    generation_input: dict[str, Any],
    llm_client: Any,
    config: dict[str, Any],
) -> dict[str, Any]:
    prompt = build_revision_prompt(skill, critique, generation_input, config)
    return llm_client.generate_json(
        prompt,
        cache_key={
            "task": "revise",
            "skill_id": skill.get("skill_id"),
            "critique_decision": critique.get("decision"),
        },
        routing_key=str(skill.get("skill_id") or ""),
    )
