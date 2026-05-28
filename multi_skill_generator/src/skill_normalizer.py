from __future__ import annotations

import re
from typing import Any

from .prompt_builder import signature_to_skill_id
from .relation_classifier import get_relation_description
from .schema import skill_template

ABSTRACTION_REPLACEMENTS = {
    "frog gorf": "moving state",
    "jumping out of well": "advancing through bounded positions",
    "well": "bounded state range",
    "dancers": "moving records",
    "bridges to gaps": "interval resources to demands",
    "broken pixels": "invalid cells",
    "broken square": "invalid subregion",
    "threshold year": "threshold value",
    "discount problems": "cost-threshold pairing instances",
    "minimum flips": "minimum transformation cost",
    "maximum significance": "maximum weighted objective",
    "shovels by price": "items by cost",
}


def _as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if value is None or value == "":
        return []
    return [value]


def _non_empty_strings(items: list[Any]) -> list[str]:
    return [str(x).strip() for x in items if str(x).strip()]


def _abstract_problem_context(value: Any) -> Any:
    if isinstance(value, str):
        out = value
        for problem_phrase, abstract_phrase in ABSTRACTION_REPLACEMENTS.items():
            out = re.sub(re.escape(problem_phrase), abstract_phrase, out, flags=re.IGNORECASE)
        return out
    if isinstance(value, list):
        return [_abstract_problem_context(item) for item in value]
    if isinstance(value, dict):
        return {key: _abstract_problem_context(item) for key, item in value.items()}
    return value


def build_canonical_representative_examples(gen_input: dict[str, Any]) -> list[dict[str, str]]:
    signature = " -> ".join(str(x) for x in gen_input.get("composition_signature") or [])
    return [
        {
            "problem_id": str(sample.get("problem_id") or ""),
            "solution_id": str(sample.get("solution_id") or ""),
            "why_representative": f"Verified evidence of the ordered {signature} handoff.",
        }
        for sample in gen_input.get("representative_samples") or []
    ]


def _title_from_signature(signature: list[str]) -> str:
    parts = [p.replace("_", " ").title() for p in signature]
    return " Then ".join(parts)


def _normalize_algorithm_flow(skill: dict[str, Any], signature: list[str]) -> list[dict[str, Any]]:
    raw_flow = skill.get("algorithm_flow") or []
    by_algo: dict[str, dict[str, Any]] = {}
    ordered_extra: list[dict[str, Any]] = []

    for item in raw_flow:
        if not isinstance(item, dict):
            continue
        algo = str(item.get("algorithm") or "").strip()
        if algo and algo not in by_algo:
            by_algo[algo] = item
        else:
            ordered_extra.append(item)

    normalized: list[dict[str, Any]] = []
    for idx, algo in enumerate(signature):
        src = by_algo.get(algo)
        if src is None and idx < len(ordered_extra):
            src = ordered_extra[idx]
        src = dict(src or {})
        step_num = idx + 1
        normalized.append(
            {
                "step": step_num,
                "algorithm": algo,
                "role": str(src.get("role") or src.get("reasoning") or f"Apply {algo} in the composition pipeline."),
                "input": str(
                    src.get("input")
                    or src.get("inputs")
                    or ("Raw problem input and parameters." if idx == 0 else f"Output of step {step_num - 1}.")
                ),
                "output": str(
                    src.get("output")
                    or src.get("outputs")
                    or (
                        "Final answer."
                        if idx == len(signature) - 1
                        else f"Intermediate state for step {step_num + 1}."
                    )
                ),
                "handoff_to_next": (
                    str(src.get("handoff_to_next") or "")
                    if idx < len(signature) - 1
                    else ""
                ),
            }
        )
        if idx < len(signature) - 1 and not normalized[-1]["handoff_to_next"]:
            normalized[-1]["handoff_to_next"] = (
                f"Pass the output of {algo} as structured input to {signature[idx + 1]}."
            )

    return normalized


def _normalize_state_interface(skill: dict[str, Any], signature: list[str]) -> dict[str, str]:
    raw = skill.get("state_interface") or {}
    if not isinstance(raw, dict):
        raw = {}
    defaults = {
        "input_state": "Raw problem objects and parameters before any composition step runs.",
        "intermediate_state": (
            f"Structured state produced after {signature[0]} and consumed by later steps."
            if len(signature) > 1
            else "Processed state ready for final extraction."
        ),
        "output_state": "Final objective value, constructed object, or decision returned to the caller.",
        "handoff_description": (
            " -> ".join(signature)
            + " execute sequentially; each step reads the prior step's output as part of its input."
        ),
    }
    return {key: str(raw.get(key) or defaults[key]).strip() for key in defaults}


def _default_trigger_signals(signature: list[str], relation: str) -> list[str]:
    signals = [relation.replace("_", " "), "multi algorithm composition", "algorithm pipeline"]
    for algo in signature:
        signals.append(algo.replace("_", " "))
    return _non_empty_strings(signals)


def _default_applicability(signature: list[str], relation: str) -> list[str]:
    return _non_empty_strings(
        [
            f"Problem decomposes into ordered stages: {' -> '.join(signature)}.",
            get_relation_description(relation),
            "Later stage depends on structured output from the earlier stage.",
        ]
    )


def normalize_skill_for_cluster(skill: dict[str, Any], gen_input: dict[str, Any]) -> dict[str, Any]:
    """Force cluster-canonical metadata and fill missing required fields."""
    out = _abstract_problem_context(dict(skill))
    signature = list(gen_input.get("composition_signature") or [])
    relation = str(gen_input.get("composition_relation") or out.get("composition_relation") or "other_composition")
    families = list(gen_input.get("composition_families") or out.get("composition_families") or [])
    status = str(gen_input.get("status") or out.get("status") or "provisional")

    canonical_id = signature_to_skill_id(tuple(signature))
    out["skill_id"] = canonical_id
    out["skill_type"] = "multi_algorithm"
    out["version"] = "v1"
    out["status"] = status
    out["source_dataset"] = out.get("source_dataset") or "TACO"
    out["generation_method"] = out.get("generation_method") or "composition_signature_distillation"
    out["composition_signature"] = signature
    out["composition_relation"] = relation
    out["composition_families"] = families

    if not str(out.get("skill_name") or "").strip():
        out["skill_name"] = _title_from_signature(signature)

    why = str(out.get("why_multiple_algorithms_are_needed") or "").strip()
    if not str(out.get("core_composition_mechanism") or "").strip():
        out["core_composition_mechanism"] = why or (
            f"Combine {' then '.join(signature)} so each stage exposes structure the next stage consumes."
        )

    if not str(out.get("correctness_argument_pattern") or "").strip():
        inv_text = " ".join(_as_list(out.get("composition_invariants")))
        out["correctness_argument_pattern"] = inv_text or why or (
            "Correctness follows from preserving invariants across sequential algorithm handoffs."
        )

    cp = out.get("complexity_pattern")
    if not isinstance(cp, dict):
        cp = {}
    out["complexity_pattern"] = {
        "time": str(cp.get("time") or "Depends on dominant stage; often sort/search/DP term plus linear scan."),
        "space": str(cp.get("space") or "Intermediate structures from each stage."),
        "dominant_factor": str(cp.get("dominant_factor") or signature[-1] if signature else ""),
    }

    if not str(out.get("implementation_template") or "").strip():
        lines = []
        for idx, algo in enumerate(signature, start=1):
            lines.append(f"# Step {idx}: {algo}")
        out["implementation_template"] = "\n".join(lines)

    out["implementation_notes"] = _non_empty_strings(_as_list(out.get("implementation_notes")))
    out["algorithm_flow"] = _normalize_algorithm_flow(out, signature)
    out["state_interface"] = _normalize_state_interface(out, signature)

    trigger_signals = _non_empty_strings(_as_list(out.get("trigger_signals")))
    if not trigger_signals:
        trigger_signals = _default_trigger_signals(signature, relation)
    out["trigger_signals"] = trigger_signals

    applicability = _non_empty_strings(_as_list(out.get("applicability_conditions")))
    if not applicability:
        applicability = _default_applicability(signature, relation)
    out["applicability_conditions"] = applicability

    non_app = _non_empty_strings(_as_list(out.get("non_applicability_conditions")))
    if len(non_app) < 2:
        non_app.extend(
            [
                "A single algorithm already solves the task without an ordered handoff.",
                "The problem requires exploring multiple orderings or backtracking across stages.",
            ]
        )
    out["non_applicability_conditions"] = non_app[:8]

    invariants = _non_empty_strings(_as_list(out.get("composition_invariants")))
    if len(invariants) < 2:
        invariants.extend(
            [
                f"The output of {signature[0]} must remain valid input for {signature[1]}."
                if len(signature) > 1
                else "Stage outputs must preserve information needed by downstream decisions.",
                "Local decisions in later stages must remain safe given the ordering established earlier.",
            ]
        )
    out["composition_invariants"] = invariants[:8]

    pitfalls = _non_empty_strings(_as_list(out.get("common_pitfalls")))
    if len(pitfalls) < 3:
        pitfalls.extend(
            [
                "Using the wrong processing order relative to composition_signature.",
                "Mutating intermediate state in a way that breaks downstream assumptions.",
                "Treating the composition as independent single-algorithm skills without handoff design.",
            ]
        )
    out["common_pitfalls"] = pitfalls[:8]

    confusable = out.get("confusable_compositions")
    if not isinstance(confusable, dict):
        confusable = {}
    out["confusable_compositions"] = {
        "similar": _non_empty_strings(_as_list(confusable.get("similar"))),
        "should_not_confuse_with": _non_empty_strings(_as_list(confusable.get("should_not_confuse_with"))),
    }

    out["representative_examples"] = build_canonical_representative_examples(gen_input)

    # Validator owns this namespace; discard any model-authored acceptance claims.
    out["quality_control"] = {}

    evidence = out.get("evidence")
    if not isinstance(evidence, dict):
        out["evidence"] = dict(skill_template()["evidence"])

    # Drop unknown top-level keys that may confuse downstream consumers.
    template_keys = set(skill_template().keys())
    out = {k: v for k, v in out.items() if k in template_keys}
    return out


def is_valid_skill_id(skill_id: str) -> bool:
    return bool(re.match(r"^multi\.[a-z0-9_]+(__[a-z0-9_]+)*\.v\d+$", skill_id or ""))
