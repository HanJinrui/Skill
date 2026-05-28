from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _prompts_dir(config: dict[str, Any]) -> Path:
    return Path(config.get("_project_root", ".")) / "prompts"


def _load_template(name: str, config: dict[str, Any]) -> str:
    path = _prompts_dir(config) / name
    return path.read_text(encoding="utf-8")


def build_mechanism_text(row: dict[str, Any]) -> str:
    candidate_subtypes = row.get("candidate_subtypes")
    if isinstance(candidate_subtypes, (list, dict)):
        cand_str = json.dumps(candidate_subtypes, ensure_ascii=False, indent=2)
    else:
        cand_str = str(candidate_subtypes or "")

    ast_features = row.get("ast_features")
    if isinstance(ast_features, dict):
        ast_str = json.dumps(ast_features, ensure_ascii=False, indent=2)
    else:
        ast_str = str(ast_features or "")

    original_tags = row.get("original_tags")
    if isinstance(original_tags, list):
        tags_str = ", ".join(str(t) for t in original_tags)
    else:
        tags_str = str(original_tags or "")

    families = row.get("problem_families")
    if isinstance(families, list):
        fam_str = ", ".join(str(f) for f in families)
    else:
        fam_str = str(families or "")

    return (
        f"Problem ID: {row.get('problem_id')}\n"
        f"Solution ID: {row.get('solution_id')}\n"
        f"Source: {row.get('source')}\n"
        f"Difficulty: {row.get('difficulty')}\n\n"
        f"Algorithm family:\n{row.get('detected_single_skill')}\n\n"
        f"Primary subtype:\n{row.get('primary_subtype')}\n\n"
        f"Core mechanism summary:\n{row.get('core_mechanism_summary')}\n\n"
        f"Subtype rationale:\n{row.get('subtype_rationale')}\n\n"
        f"Candidate subtypes:\n{cand_str}\n\n"
        f"AST features:\n{ast_str}\n\n"
        f"Original tags:\n{tags_str}\n\n"
        f"Problem families:\n{fam_str}\n\n"
        f"Problem statement:\n{row.get('problem_statement')}\n\n"
        f"Solution code:\n{row.get('solution_code')}\n"
    )


def build_generation_prompt(
    subtype: str,
    rows: list[dict[str, Any]],
    config: dict[str, Any],
    *,
    generation_input: dict[str, Any] | None = None,
) -> str:
    tmpl = _load_template("generate_single_skill.md", config)
    if not rows:
        raise ValueError(f"No rows for subtype {subtype}")

    algorithm_family = str(rows[0].get("detected_single_skill") or "")
    from .group_rows import classify_evidence_status

    status = str((generation_input or {}).get("status") or classify_evidence_status(rows, config))
    origins = {str(row.get("evidence_origin") or "taco_verified") for row in rows}
    if origins == {"taco_verified"}:
        evidence_description = "verified single-algorithm solution annotations from the TACO dataset"
        source_dataset = "TACO"
    elif origins == {"curated"}:
        evidence_description = "executable curated canonical single-algorithm examples; these are not TACO samples"
        source_dataset = "curated"
    else:
        evidence_description = (
            "a mixture of verified TACO solution annotations and executable curated examples; "
            "curated examples are not TACO samples"
        )
        source_dataset = "TACO+curated"
    generation_method = (
        "targeted_evidence_distillation"
        if config.get("additional", {}).get("enabled", False)
        else "subtype_group_distillation"
    )
    mechanism_boundary = str(
        (generation_input or {}).get("mechanism_boundary")
        or "Distill only the precise mechanism supported by the supplied evidence."
    )
    samples = "\n\n---\n\n".join(build_mechanism_text(r) for r in rows)

    return (
        tmpl.replace("{{algorithm_family}}", algorithm_family)
        .replace("{{primary_subtype}}", subtype)
        .replace("{{status}}", status)
        .replace("{{evidence_description}}", evidence_description)
        .replace("{{source_dataset}}", source_dataset)
        .replace("{{generation_method}}", generation_method)
        .replace("{{mechanism_boundary}}", mechanism_boundary)
        .replace("{{representative_samples}}", samples)
    )


def build_critique_prompt(skill_json: dict[str, Any], config: dict[str, Any]) -> str:
    tmpl = _load_template("critique_single_skill.md", config)
    body = json.dumps(skill_json, ensure_ascii=False, indent=2)
    return tmpl.replace("{{skill_json}}", body)


def build_revision_prompt(
    skill_json: dict[str, Any],
    critique_json: dict[str, Any],
    config: dict[str, Any],
) -> str:
    tmpl = _load_template("revise_single_skill.md", config)
    return tmpl.replace("{{skill_json}}", json.dumps(skill_json, ensure_ascii=False, indent=2)).replace(
        "{{critique_json}}",
        json.dumps(critique_json, ensure_ascii=False, indent=2),
    )
