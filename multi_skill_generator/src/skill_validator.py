from __future__ import annotations

import json
import re
from typing import Any

from .schema import (
    REQUIRED_REPRESENTATIVE_EXAMPLE_FIELDS,
    REQUIRED_SKILL_FIELDS,
    SKILL_ID_PATTERN,
)

GENERIC_BAD_PHRASES = [
    "use the first algorithm and then the second algorithm",
    "first sort then greedily solve",
    "improve efficiency",
    "solve the problem",
    "get the answer",
    "process according to the statement",
    "先使用第一个算法再使用第二个算法",
    "先排序再贪心",
    "提高效率",
    "根据题意处理",
    "得到答案",
]

PROBLEM_CONTEXT_PHRASES = [
    "frog gorf",
    "jumping out of well",
    "bridges to gaps",
    "broken pixels",
    "broken square",
    "threshold year",
    "discount problems",
    "minimum flips",
    "maximum significance",
    "shovels by price",
    "dancers",
]


def _non_empty_list(value: Any) -> bool:
    return isinstance(value, list) and len(value) > 0 and all(str(x).strip() for x in value)


def validate_required_fields(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    for field in REQUIRED_SKILL_FIELDS:
        if field not in skill:
            errors.append(f"missing field: {field}")
            continue
        val = skill[field]
        if field in {
            "trigger_signals",
            "applicability_conditions",
            "non_applicability_conditions",
            "composition_invariants",
            "common_pitfalls",
        }:
            if not _non_empty_list(val):
                errors.append(f"empty or invalid list: {field}")
        elif field == "algorithm_flow":
            if not isinstance(val, list) or len(val) < 2:
                errors.append("algorithm_flow must have at least 2 steps")
        elif field == "state_interface":
            if not isinstance(val, dict):
                errors.append("state_interface must be object")
        elif isinstance(val, str) and not val.strip():
            errors.append(f"empty string: {field}")
    return len(errors) == 0, errors


def validate_skill_schema(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    ok, errs = validate_required_fields(skill)
    errors.extend(errs)
    if skill.get("skill_type") != "multi_algorithm":
        errors.append("skill_type must be multi_algorithm")
    sid = str(skill.get("skill_id") or "")
    if not re.match(SKILL_ID_PATTERN, sid):
        errors.append(f"invalid skill_id: {sid}")
    examples_ok, example_errs = validate_representative_examples(skill)
    errors.extend(example_errs)
    evidence = skill.get("evidence")
    if isinstance(evidence, dict) and evidence:
        actual_count = len(skill.get("representative_examples") or [])
        if evidence.get("num_representative_rows") != actual_count:
            errors.append("evidence.num_representative_rows does not match representative_examples")
    return len(errors) == 0, errors


def validate_representative_examples(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    examples = skill.get("representative_examples")
    errors: list[str] = []
    if not isinstance(examples, list) or not examples:
        return False, ["representative_examples must be a non-empty list"]
    for index, example in enumerate(examples):
        if not isinstance(example, dict):
            errors.append(f"representative_examples[{index}] must be object")
            continue
        for field in REQUIRED_REPRESENTATIVE_EXAMPLE_FIELDS:
            value = example.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"representative_examples[{index}] missing non-empty {field}")
    return len(errors) == 0, errors


def validate_order_consistency(
    skill: dict[str, Any],
    expected_signature: list[str],
) -> tuple[bool, list[str]]:
    actual = skill.get("composition_signature")
    flow_algorithms = [step.get("algorithm") for step in skill.get("algorithm_flow", [])]
    errors: list[str] = []
    if actual != expected_signature:
        errors.append("composition_signature does not match expected signature")
    if flow_algorithms != expected_signature:
        errors.append("algorithm_flow algorithms do not match expected signature order")
    return len(errors) == 0, errors


def validate_interface(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    for step in skill.get("algorithm_flow", []):
        for field in ("role", "input", "output"):
            if not step.get(field):
                errors.append(f"missing {field} in step {step.get('step')}")
    sig_len = len(skill.get("composition_signature", []))
    if sig_len > 1:
        for step in skill.get("algorithm_flow", [])[:-1]:
            if not step.get("handoff_to_next"):
                errors.append(f"missing handoff_to_next in step {step.get('step')}")
    state_interface = skill.get("state_interface", {})
    for field in ("input_state", "intermediate_state", "output_state", "handoff_description"):
        if not state_interface.get(field):
            errors.append(f"missing state_interface.{field}")
    return len(errors) == 0, errors


def validate_invariants(skill: dict[str, Any], config: dict[str, Any]) -> tuple[bool, list[str]]:
    vc = config.get("validation", config)
    min_inv = int(vc.get("min_invariants", 2))
    inv = skill.get("composition_invariants") or []
    errors: list[str] = []
    if len(inv) < min_inv:
        errors.append(f"composition_invariants count {len(inv)} < {min_inv}")
    min_pitfalls = int(vc.get("min_common_pitfalls", 3))
    pitfalls = skill.get("common_pitfalls") or []
    if len(pitfalls) < min_pitfalls:
        errors.append(f"common_pitfalls count {len(pitfalls)} < {min_pitfalls}")
    non_app = skill.get("non_applicability_conditions") or []
    if len(non_app) < 2:
        errors.append("non_applicability_conditions need at least 2 items")
    return len(errors) == 0, errors


def validate_not_generic(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    texts = [
        str(skill.get("core_composition_mechanism") or ""),
        json.dumps(skill.get("state_interface") or {}, ensure_ascii=False),
        " ".join(str(x) for x in skill.get("composition_invariants") or []),
    ]
    combined = " ".join(texts).lower()
    hits = [p for p in GENERIC_BAD_PHRASES if p.lower() in combined]
    if len(hits) >= 2:
        return False, [f"generic phrasing detected: {hits[:3]}"]
    return True, []


def validate_abstract_language(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    content = {key: value for key, value in skill.items() if key != "evidence"}
    text = json.dumps(content, ensure_ascii=False).lower()
    hits = [phrase for phrase in PROBLEM_CONTEXT_PHRASES if phrase in text]
    if hits:
        return False, [f"problem-specific wording detected: {hits}"]
    return True, []


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z_][a-zA-Z0-9_]{2,}|\d{4,}", text)


def _longest_common_token_run(a_tokens: list[str], b_tokens: list[str]) -> int:
    if not a_tokens or not b_tokens:
        return 0
    best = 0
    index_b: dict[str, list[int]] = {}
    for j, tok in enumerate(b_tokens):
        index_b.setdefault(tok, []).append(j)
    for i, tok in enumerate(a_tokens):
        for j in index_b.get(tok, []):
            length = 1
            while (
                i + length < len(a_tokens)
                and j + length < len(b_tokens)
                and a_tokens[i + length] == b_tokens[j + length]
            ):
                length += 1
            best = max(best, length)
    return best


def _longest_common_line_run(a_lines: list[str], b_lines: list[str]) -> int:
    best = 0
    for i, la in enumerate(a_lines):
        la = la.strip()
        if not la:
            continue
        for j, lb in enumerate(b_lines):
            lb = lb.strip()
            if la != lb:
                continue
            length = 1
            while (
                i + length < len(a_lines)
                and j + length < len(b_lines)
                and a_lines[i + length].strip() == la
                and a_lines[i + length].strip() == b_lines[j + length].strip()
            ):
                length += 1
            best = max(best, length)
    return best


def validate_no_leakage(
    skill: dict[str, Any],
    source_rows: list[dict[str, Any]],
    config: dict[str, Any],
) -> tuple[bool, list[str]]:
    vc = config.get("validation", config)
    max_tokens = int(vc.get("max_repeated_problem_tokens", 50))
    max_code_lines = int(vc.get("max_repeated_code_lines", 5))
    skill_text = json.dumps(skill, ensure_ascii=False)
    issues: list[str] = []

    for row in source_rows:
        for field in ("problem_statement", "solution_code", "core_composition_summary"):
            text = str(row.get(field) or "")
            if not text:
                continue
            if field == "solution_code":
                run = _longest_common_line_run(
                    [ln for ln in skill_text.splitlines() if ln.strip()],
                    text.splitlines(),
                )
                if run > max_code_lines:
                    issues.append(f"{field} leakage ({run} lines)")
            else:
                run = _longest_common_token_run(_tokenize(skill_text), _tokenize(text))
                if run > max_tokens:
                    issues.append(f"{field} leakage ({run} tokens)")
    return len(issues) == 0, issues


def validate_evidence_integrity(
    skill: dict[str, Any],
    generation_input: dict[str, Any],
) -> tuple[bool, list[str]]:
    errors: list[str] = []
    examples = skill.get("representative_examples") or []
    expected_examples = generation_input.get("representative_samples") or []
    expected_pairs = [
        (str(sample.get("problem_id") or ""), str(sample.get("solution_id") or ""))
        for sample in expected_examples
    ]
    actual_pairs = [
        (str(example.get("problem_id") or ""), str(example.get("solution_id") or ""))
        for example in examples
        if isinstance(example, dict)
    ]
    if actual_pairs != expected_pairs:
        errors.append("representative_examples do not match selected evidence rows")

    evidence = skill.get("evidence")
    if not isinstance(evidence, dict):
        return False, errors + ["evidence must be object"]
    expected_source_count = len(generation_input.get("all_source_rows") or [])
    expected_rep_count = len(expected_examples)
    expected_support = int(generation_input.get("support_count", expected_source_count))
    if evidence.get("num_source_rows") != expected_source_count:
        errors.append("evidence.num_source_rows does not match generation input")
    if evidence.get("num_representative_rows") != expected_rep_count:
        errors.append("evidence.num_representative_rows does not match selected representatives")
    if evidence.get("support_count") != expected_support:
        errors.append("evidence.support_count does not match generation input")
    return len(errors) == 0, errors


def validate_template(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    template = str(skill.get("implementation_template") or "").strip()
    if not template:
        return False, ["implementation_template is empty"]
    return True, []


def score_skill(
    skill: dict[str, Any],
    critique: dict[str, Any] | None = None,
    *,
    checks: dict[str, bool] | None = None,
    support_count: int | None = None,
    stable_min_rows: int = 5,
) -> dict[str, Any]:
    del critique
    check = checks or {}
    support = int(
        support_count
        if support_count is not None
        else (skill.get("evidence") or {}).get("support_count", 0)
    )
    evidence_score = min(1.0, support / max(stable_min_rows, 1))
    components = {
        "order_consistency_score": 1.0 if check.get("order", True) else 0.0,
        "interface_clarity_score": 1.0 if check.get("interface", True) else 0.0,
        "composition_abstraction_score": 1.0 if check.get("abstraction", True) else 0.0,
        "invariant_quality_score": 1.0 if check.get("invariants", True) else 0.0,
        "template_score": 1.0 if check.get("template", True) else 0.0,
        "leakage_score": 1.0 if check.get("leakage", True) else 0.0,
        "evidence_support_score": evidence_score if check.get("evidence", True) else 0.0,
    }
    final_score = (
        0.20 * components["order_consistency_score"]
        + 0.20 * components["interface_clarity_score"]
        + 0.20 * components["composition_abstraction_score"]
        + 0.15 * components["invariant_quality_score"]
        + 0.10 * components["template_score"]
        + 0.10 * components["leakage_score"]
        + 0.05 * components["evidence_support_score"]
    )
    return {**components, "final_score": round(final_score, 4)}


def validate_final_skill(
    skill: dict[str, Any],
    generation_input: dict[str, Any],
    config: dict[str, Any],
    *,
    critique: dict[str, Any] | None = None,
) -> dict[str, Any]:
    expected = list(generation_input.get("composition_signature") or [])
    source_rows = generation_input.get("all_source_rows") or []

    schema_ok, schema_errs = validate_skill_schema(skill)
    order_ok, order_errs = validate_order_consistency(skill, expected)
    iface_ok, iface_errs = validate_interface(skill)
    inv_ok, inv_errs = validate_invariants(skill, config)
    generic_ok, generic_errs = validate_not_generic(skill)
    abstract_ok, abstract_errs = validate_abstract_language(skill)
    leakage_ok, leakage_errs = validate_no_leakage(skill, source_rows, config)
    evidence_ok, evidence_errs = validate_evidence_integrity(skill, generation_input)
    template_ok, template_errs = validate_template(skill)
    vc = config.get("validation", config)
    stable_min_rows = int(config.get("grouping", {}).get("stable_min_rows", 5))
    support_count = int(generation_input.get("support_count", len(source_rows)))
    scores = score_skill(
        skill,
        checks={
            "order": order_ok,
            "interface": iface_ok,
            "abstraction": generic_ok and abstract_ok,
            "invariants": inv_ok,
            "template": template_ok,
            "leakage": leakage_ok,
            "evidence": evidence_ok,
        },
        support_count=support_count,
        stable_min_rows=stable_min_rows,
    )
    min_accept = float(vc.get("min_final_score", 0.85))
    min_revise = float(vc.get("revise_score_threshold", 0.70))
    final = float(scores.get("final_score") or 0)

    hard_reject = (
        skill.get("skill_type") != "multi_algorithm"
        or not order_ok
        or not iface_ok
        or not inv_ok
        or not leakage_ok
        or not generic_ok
        or not abstract_ok
        or not evidence_ok
        or not template_ok
    )

    if hard_reject or not schema_ok:
        decision = "reject"
    elif support_count < stable_min_rows or skill.get("status") != "stable":
        decision = "provisional_review_required"
    elif final >= min_accept:
        decision = "accept"
    elif final >= min_revise:
        decision = "revise"
    else:
        decision = "reject"

    skill["quality_control"] = {
        "validator": "skill_validator.py",
        "validation_policy_version": "multi_skill_v2",
        "schema_valid": schema_ok,
        "order_consistency_check": "pass" if order_ok else "fail",
        "interface_check": "pass" if iface_ok else "fail",
        "abstraction_check": "pass" if generic_ok and abstract_ok else "fail",
        "invariant_check": "pass" if inv_ok else "fail",
        "template_check": "pass" if template_ok else "fail",
        "leakage_check": "pass" if leakage_ok else "fail",
        "evidence_check": "pass" if evidence_ok else "fail",
        "composition_consistency_check": "pass" if order_ok else "fail",
        "support_count": support_count,
        "low_support_warning": support_count < stable_min_rows,
        "final_score": final,
        "final_decision": decision,
    }

    return {
        "decision": decision,
        "scores": scores,
        "errors": (
            schema_errs
            + order_errs
            + iface_errs
            + inv_errs
            + generic_errs
            + abstract_errs
            + leakage_errs
            + evidence_errs
            + template_errs
        ),
    }
