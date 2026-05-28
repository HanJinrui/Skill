from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .relation_classifier import get_relation_description
from .representative_selector import build_representative_sample
from .schema import multi_skill_schema_json


def _prompts_dir(config: dict[str, Any]) -> Path:
    return Path(config.get("_project_root", ".")) / "prompts"


def _load_template(name: str, config: dict[str, Any]) -> str:
    return (_prompts_dir(config) / name).read_text(encoding="utf-8")


def signature_to_skill_id(signature: tuple[str, ...]) -> str:
    body = "__".join(signature)
    return f"multi.{body}.v1"


def build_generation_input(
    signature: tuple[str, ...],
    rows: list[dict[str, Any]],
    config: dict[str, Any],
    *,
    status: str,
    relation: str,
) -> dict[str, Any]:
    from .representative_selector import select_representative_rows

    reps = select_representative_rows(rows, config)
    families: set[str] = set()
    for r in rows:
        for f in r.get("composition_families_normalized") or r.get("composition_families") or []:
            families.add(str(f))

    return {
        "composition_signature": list(signature),
        "composition_relation": relation,
        "composition_relation_description": get_relation_description(relation),
        "status": status,
        "support_count": len(rows),
        "composition_families": sorted(families),
        "representative_samples": [build_representative_sample(r, config) for r in reps],
        "all_source_rows": rows,
        "skill_id": signature_to_skill_id(signature),
    }


def build_generate_prompt(generation_input: dict[str, Any], config: dict[str, Any]) -> str:
    tmpl = _load_template("generate_multi_skill.md", config)
    samples = json.dumps(
        generation_input.get("representative_samples") or [],
        ensure_ascii=False,
        indent=2,
    )
    sig = json.dumps(generation_input.get("composition_signature") or [], ensure_ascii=False)
    expected_id = generation_input.get("skill_id") or signature_to_skill_id(
        tuple(generation_input.get("composition_signature") or [])
    )
    return (
        tmpl.replace("{{composition_signature}}", sig)
        .replace("{{composition_relation}}", str(generation_input.get("composition_relation") or ""))
        .replace("{{status}}", str(generation_input.get("status") or ""))
        .replace("{{support_count}}", str(generation_input.get("support_count") or 0))
        .replace("{{representative_samples}}", samples)
        .replace("{{multi_skill_schema}}", multi_skill_schema_json())
        .replace("{{expected_skill_id}}", expected_id)
    )


def build_critique_prompt(
    skill_json: dict[str, Any],
    generation_input: dict[str, Any],
    config: dict[str, Any],
) -> str:
    tmpl = _load_template("critique_multi_skill.md", config)
    summary = json.dumps(
        [
            {
                "problem_id": s.get("problem_id"),
                "core_composition_summary": s.get("core_composition_summary"),
            }
            for s in generation_input.get("representative_samples") or []
        ],
        ensure_ascii=False,
        indent=2,
    )
    sig = json.dumps(generation_input.get("composition_signature") or [], ensure_ascii=False)
    return (
        tmpl.replace("{{skill_json}}", json.dumps(skill_json, ensure_ascii=False, indent=2))
        .replace("{{composition_signature}}", sig)
        .replace("{{representative_samples_summary}}", summary)
    )


def build_revision_prompt(
    skill_json: dict[str, Any],
    critique_json: dict[str, Any],
    generation_input: dict[str, Any],
    config: dict[str, Any],
) -> str:
    del generation_input
    tmpl = _load_template("revise_multi_skill.md", config)
    return tmpl.replace("{{skill_json}}", json.dumps(skill_json, ensure_ascii=False, indent=2)).replace(
        "{{critique_json}}",
        json.dumps(critique_json, ensure_ascii=False, indent=2),
    )
