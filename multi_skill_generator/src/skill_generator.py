from __future__ import annotations

import hashlib
import json
from collections import Counter
from typing import Any

from .group_compositions import classify_composition_status
from .prompt_builder import (
    build_generate_prompt,
    build_generation_input,
    signature_to_skill_id,
)
from .relation_classifier import classify_relation
from .scoring import compute_quality_score
from .skill_critic import critique_skill
from .skill_normalizer import build_canonical_representative_examples, normalize_skill_for_cluster
from .skill_reviser import revise_skill
from .skill_validator import validate_final_skill

PROMPT_VERSION = "multi_en_v1"


def slim_source_row(row: dict[str, Any]) -> dict[str, Any]:
    """Lean row for JSONL storage; keeps fields needed for validation."""
    code = str(row.get("solution_code") or "")
    return {
        "problem_id": row.get("problem_id"),
        "solution_id": row.get("solution_id"),
        "quality_score": row.get("quality_score"),
        "subtype_confidence": row.get("subtype_confidence"),
        "evidence_tier": row.get("evidence_tier"),
        "source_dataset": row.get("source_dataset", "TACO"),
        "source_language": row.get("source_language"),
        "verification_source": row.get("verification_source", "taco-verified"),
        "source_problem_fingerprint": row.get("source_problem_fingerprint"),
        "test_selection_policy": row.get("test_selection_policy"),
        "selected_test_counts": row.get("selected_test_counts"),
        "family_evidence_method": row.get("family_evidence_method"),
        "composition_order": row.get("normalized_composition_order") or row.get("composition_order"),
        "order_repaired": row.get("order_repaired"),
        "core_composition_summary": row.get("core_composition_summary"),
        "problem_statement": str(row.get("problem_statement") or "")[:1200],
        "solution_code": code[:6000] if len(code) > 6000 else code,
    }


def _source_dataset_label(rows: list[dict[str, Any]]) -> str:
    datasets = {str(row.get("source_dataset") or "TACO") for row in rows}
    if datasets == {"TACO"}:
        return "TACO"
    if datasets == {"CodeContests"}:
        return "CodeContests"
    return "+".join(name for name in ("TACO", "CodeContests") if name in datasets) or "TACO"


def build_generation_cache_key(generation_input: dict[str, Any]) -> dict[str, Any]:
    rows = generation_input.get("all_source_rows") or []
    provenance = [
        {
            "problem_id": row.get("problem_id"),
            "fingerprint": row.get("source_problem_fingerprint"),
            "source_dataset": row.get("source_dataset", "TACO"),
            "source_language": row.get("source_language"),
        }
        for row in rows
    ]
    digest = hashlib.sha256(
        json.dumps(provenance, ensure_ascii=True, sort_keys=True).encode("utf-8")
    ).hexdigest()[:20]
    return {
        "prompt_version": PROMPT_VERSION,
        "task": "generate",
        "signature": generation_input.get("composition_signature") or [],
        "n_reps": len(generation_input.get("representative_samples") or []),
        "evidence_digest": digest,
        "source_dataset": _source_dataset_label(rows),
    }


def prepare_generation_inputs(
    groups: dict[tuple[str, ...], list[dict[str, Any]]],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    gc = config.get("grouping", config)
    min_gen = int(gc.get("min_rows_for_generation", 3))
    inputs: list[dict[str, Any]] = []

    for signature, rows in sorted(groups.items()):
        if len(rows) < min_gen:
            continue
        status = classify_composition_status(len(rows), signature, config)
        if status == "hold":
            continue
        relation = classify_relation(signature, rows)
        gi = build_generation_input(
            signature, rows, config, status=status, relation=relation
        )
        inputs.append(gi)
    return inputs


def fill_program_owned_fields(skill: dict[str, Any], gen_input: dict[str, Any]) -> dict[str, Any]:
    all_rows = gen_input.get("all_source_rows") or []
    reps = gen_input.get("representative_samples") or []
    tiers = Counter(str(r.get("evidence_tier") or "") for r in all_rows)
    dataset_counts = Counter(str(r.get("source_dataset") or "TACO") for r in all_rows)
    verification_counts = Counter(str(r.get("verification_source") or "taco-verified") for r in all_rows)
    language_counts = Counter(str(r.get("source_language") or "") for r in all_rows if r.get("source_language"))
    sig = gen_input.get("composition_signature") or []
    orders: Counter[str] = Counter()
    for r in all_rows:
        order = r.get("normalized_composition_order") or r.get("composition_order") or []
        orders[" -> ".join(order)] += 1

    skill["evidence"] = {
        "num_source_rows": len(all_rows),
        "num_representative_rows": len(reps),
        "evidence_tiers": dict(tiers),
        "avg_subtype_confidence": round(
            sum(float(r.get("subtype_confidence") or 0) for r in all_rows) / max(len(all_rows), 1),
            4,
        ),
        "source_problem_ids": [str(r.get("problem_id") or "") for r in all_rows[:200]],
        "num_unique_source_problems": len({str(r.get("problem_id") or "") for r in all_rows}),
        "source_dataset_counts": dict(dataset_counts),
        "verification_source_counts": dict(verification_counts),
        "source_language_counts": dict(language_counts),
        "composition_orders": dict(orders),
        "support_count": gen_input.get("support_count", len(all_rows)),
        "low_support_warning": len(all_rows) < 5,
    }
    skill["source_dataset"] = _source_dataset_label(all_rows)
    skill["skill_id"] = signature_to_skill_id(tuple(sig))
    skill["status"] = gen_input.get("status", skill.get("status"))
    skill["composition_signature"] = sig
    skill["composition_relation"] = gen_input.get("composition_relation", skill.get("composition_relation"))
    skill["composition_families"] = gen_input.get("composition_families", skill.get("composition_families"))
    skill["representative_examples"] = build_canonical_representative_examples(gen_input)
    skill["quality_control"] = {}
    return skill


def generate_skill_for_composition(
    generation_input: dict[str, Any],
    llm_client: Any,
    config: dict[str, Any],
) -> dict[str, Any]:
    sig = generation_input["composition_signature"]
    routing = generation_input.get("skill_id") or signature_to_skill_id(tuple(sig))

    prompt = build_generate_prompt(generation_input, config)
    skill = llm_client.generate_json(
        prompt,
        cache_key=build_generation_cache_key(generation_input),
        routing_key=routing,
    )
    skill = normalize_skill_for_cluster(skill, generation_input)
    skill = fill_program_owned_fields(skill, generation_input)

    critique = critique_skill(skill, generation_input, llm_client, config)
    max_rounds = int(config.get("llm", {}).get("max_revision_rounds", 2))
    rounds = 0
    while str(critique.get("decision") or "").lower() == "revise" and rounds < max_rounds:
        skill = revise_skill(skill, critique, generation_input, llm_client, config)
        skill = normalize_skill_for_cluster(skill, generation_input)
        skill = fill_program_owned_fields(skill, generation_input)
        critique = critique_skill(skill, generation_input, llm_client, config)
        rounds += 1

    validation = validate_final_skill(skill, generation_input, config, critique=critique)
    skill["_validation"] = {**validation, "critique": critique}
    return skill


def generate_all_skills(
    generation_inputs: list[dict[str, Any]],
    llm_client: Any,
    config: dict[str, Any],
    *,
    signatures: list[str] | None = None,
) -> list[dict[str, Any]]:
    from concurrent.futures import ThreadPoolExecutor, as_completed

    allow = set(signatures) if signatures else None

    def _sig_key(gi: dict[str, Any]) -> str:
        return " -> ".join(gi.get("composition_signature") or [])

    tasks = [gi for gi in generation_inputs if allow is None or _sig_key(gi) in allow]
    if not tasks:
        return []

    max_workers = int(config.get("llm", {}).get("max_workers", 1))

    def _run_one(gen_input: dict[str, Any]) -> dict[str, Any]:
        key = _sig_key(gen_input)
        print(f"[generate] start {key}", flush=True)
        skill = generate_skill_for_composition(gen_input, llm_client, config)
        decision = (skill.get("quality_control") or {}).get("final_decision", "?")
        print(f"[generate] done {key} -> {decision}", flush=True)
        return skill

    if max_workers <= 1 or len(tasks) == 1:
        return [_run_one(gi) for gi in tasks]

    by_key: dict[str, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(_run_one, gi): _sig_key(gi) for gi in tasks}
        for future in as_completed(futures):
            k = futures[future]
            by_key[k] = future.result()
    return [by_key[_sig_key(gi)] for gi in tasks]
