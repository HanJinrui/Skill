from __future__ import annotations

from collections import Counter
from typing import Any

from .group_rows import classify_evidence_status

PROMPT_VERSION = "en_v2_mixed_evidence"
from .prompt_builder import build_critique_prompt, build_generation_prompt, build_revision_prompt
from .representative_selector import build_representative_sample, select_representative_rows
from .scoring import compute_quality_score
from .skill_validator import (
    apply_final_decision,
    infer_template_type,
    score_skill,
    validate_no_leakage,
    validate_skill_consistency,
    validate_skill_schema,
)


def prepare_generation_inputs(
    groups: dict[str, list[dict[str, Any]]],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    inputs: list[dict[str, Any]] = []
    for subtype, rows in sorted(groups.items()):
        status = classify_evidence_status(rows, config)
        if status == "hold":
            continue
        reps = select_representative_rows(rows, config)
        if not reps:
            continue
        family = str(reps[0].get("detected_single_skill") or "")
        aliases = sorted(
            {alias for row in rows for alias in (row.get("alias_subtypes") or []) if alias}
        )
        inputs.append(
            {
                "primary_subtype": subtype,
                "canonical_subtype": subtype,
                "alias_subtypes": aliases,
                "algorithm_family": family,
                "status": status,
                "num_source_rows": len(rows),
                "representative_rows": reps,
                "all_source_rows": rows,
            }
        )
    return inputs


def _fill_evidence(
    skill: dict[str, Any],
    gen_input: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    all_rows = gen_input.get("all_source_rows") or []
    reps = gen_input.get("representative_rows") or []
    tiers = Counter(str(r.get("evidence_tier") or "") for r in all_rows)
    origins = Counter(str(r.get("evidence_origin") or "taco_verified") for r in all_rows)
    skill["evidence"] = {
        "num_source_rows": len(all_rows),
        "num_representative_rows": len(reps),
        "evidence_tiers": dict(tiers),
        "avg_subtype_confidence": round(
            sum(float(r.get("subtype_confidence") or 0) for r in all_rows) / max(len(all_rows), 1),
            4,
        ),
        "source_problem_ids": [str(r.get("problem_id") or "") for r in all_rows[:200]],
        "evidence_origin_counts": dict(origins),
    }
    if not skill.get("representative_examples"):
        skill["representative_examples"] = [
            {
                "problem_id": r.get("problem_id"),
                "solution_id": r.get("solution_id"),
                "why_representative": str(r.get("core_mechanism_summary") or "")[:200],
            }
            for r in reps
        ]
    skill["skill_id"] = skill.get("skill_id") or f"single.{gen_input['primary_subtype']}.v1"
    skill["status"] = gen_input.get("status", skill.get("status"))
    skill["primary_subtype"] = gen_input["primary_subtype"]
    skill["canonical_subtype"] = gen_input.get("canonical_subtype", gen_input["primary_subtype"])
    skill["alias_subtypes"] = gen_input.get("alias_subtypes", [])
    skill["template_type"] = infer_template_type(str(skill.get("code_template") or ""))
    skill["algorithm_family"] = gen_input.get("algorithm_family", skill.get("algorithm_family"))
    if config.get("additional", {}).get("enabled", False):
        if set(origins) == {"taco_verified"}:
            skill["source_dataset"] = "TACO"
        elif set(origins) == {"curated"}:
            skill["source_dataset"] = "curated"
        else:
            skill["source_dataset"] = "TACO+curated"
        skill["generation_method"] = "targeted_evidence_distillation"
    return skill


def generate_skill_for_subtype(
    generation_input: dict[str, Any],
    llm_client: Any,
    config: dict[str, Any],
) -> dict[str, Any]:
    subtype = generation_input["primary_subtype"]
    reps = generation_input["representative_rows"]
    all_rows = generation_input["all_source_rows"]

    prompt = build_generation_prompt(subtype, reps, config, generation_input=generation_input)
    cache_key = {
        "prompt_version": PROMPT_VERSION,
        "task": "generate",
        "subtype": subtype,
        "n_reps": len(reps),
        "ids": [(r.get("problem_id"), r.get("solution_id")) for r in reps],
    }
    skill = llm_client.generate_json(prompt, cache_key=cache_key, routing_key=subtype)
    skill = _fill_evidence(skill, generation_input, config)

    critique_prompt = build_critique_prompt(skill, config)
    critique = llm_client.generate_json(
        critique_prompt,
        cache_key={"prompt_version": PROMPT_VERSION, "task": "critique", "skill_id": skill.get("skill_id")},
        routing_key=subtype,
    )

    decision = str(critique.get("decision") or "").lower()
    if decision == "revise":
        revise_prompt = build_revision_prompt(skill, critique, config)
        skill = llm_client.generate_json(
            revise_prompt,
            cache_key={"prompt_version": PROMPT_VERSION, "task": "revise", "skill_id": skill.get("skill_id")},
            routing_key=subtype,
        )
        skill = _fill_evidence(skill, generation_input, config)
        critique = llm_client.generate_json(
            build_critique_prompt(skill, config),
            cache_key={"prompt_version": PROMPT_VERSION, "task": "critique_after_revise", "skill_id": skill.get("skill_id")},
            routing_key=subtype,
        )

    schema_ok, schema_errs = validate_skill_schema(skill)
    consistency_ok, consistency_errs = validate_skill_consistency(
        skill,
        subtype,
        generation_input.get("algorithm_family", ""),
    )
    leakage_ok, leakage_errs = validate_no_leakage(skill, all_rows, config)

    if not leakage_ok and critique.get("leakage_score", 1) > 0.5:
        leakage_ok = True

    scores = score_skill(skill, critique)
    skill = apply_final_decision(
        skill,
        scores,
        config,
        schema_ok=schema_ok,
        leakage_ok=leakage_ok,
        consistency_ok=consistency_ok,
    )
    skill["_validation"] = {
        "schema_errors": schema_errs,
        "consistency_errors": consistency_errs,
        "leakage_errors": leakage_errs,
        "critique": critique,
        "scores": scores,
    }
    return skill


def generate_all_skills(
    generation_inputs: list[dict[str, Any]],
    llm_client: Any,
    config: dict[str, Any],
    *,
    subtypes: list[str] | None = None,
) -> list[dict[str, Any]]:
    from concurrent.futures import ThreadPoolExecutor, as_completed

    allow = set(subtypes) if subtypes else None
    tasks = [
        gi
        for gi in generation_inputs
        if allow is None or gi["primary_subtype"] in allow
    ]
    if not tasks:
        return []

    max_workers = int(config.get("llm", {}).get("max_workers", 1))

    def _run_one(gen_input: dict[str, Any]) -> dict[str, Any]:
        st = gen_input["primary_subtype"]
        print(f"[generate] start {st}", flush=True)
        skill = generate_skill_for_subtype(gen_input, llm_client, config)
        decision = (skill.get("quality_control") or {}).get("final_decision", "?")
        print(f"[generate] done {st} -> {decision}", flush=True)
        return skill

    if max_workers <= 1 or len(tasks) == 1:
        return [_run_one(gi) for gi in tasks]

    print(f"[generate] parallel workers={max_workers}, subtypes={len(tasks)}", flush=True)
    by_subtype: dict[str, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(_run_one, gi): gi["primary_subtype"] for gi in tasks}
        for future in as_completed(futures):
            st = futures[future]
            by_subtype[st] = future.result()

    return [by_subtype[gi["primary_subtype"]] for gi in tasks]


def build_evidence_map(
    generation_inputs: list[dict[str, Any]],
) -> dict[str, Any]:
    evidence_map: dict[str, Any] = {}
    for gi in generation_inputs:
        subtype = gi["primary_subtype"]
        skill_id = f"single.{subtype}.v1"
        all_rows = gi.get("all_source_rows") or []
        reps = gi.get("representative_rows") or []
        evidence_map[skill_id] = {
            "primary_subtype": subtype,
            "canonical_subtype": gi.get("canonical_subtype", subtype),
            "alias_subtypes": gi.get("alias_subtypes", []),
            "algorithm_family": gi.get("algorithm_family"),
            "status": gi.get("status"),
            "all_source_rows": [
                {
                    "problem_id": r.get("problem_id"),
                    "solution_id": r.get("solution_id"),
                    "quality_score": round(compute_quality_score(r), 4),
                    "subtype_confidence": r.get("subtype_confidence"),
                    "evidence_tier": r.get("evidence_tier"),
                    "evidence_origin": r.get("evidence_origin", "taco_verified"),
                    "evidence_validation": r.get("evidence_validation", "external_verified"),
                }
                for r in all_rows
            ],
            "representative_rows": [build_representative_sample(r) for r in reps],
        }
    return evidence_map
