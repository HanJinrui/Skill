from __future__ import annotations

import ast
import json
import re
from typing import Any

from .schema import REQUIRED_SKILL_FIELDS, SKILL_ID_PATTERN

TEMPLATE_TYPES = {"executable_python", "pseudocode_python"}


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
            "algorithm_steps",
            "common_pitfalls",
            "retrieval_keywords",
        }:
            if not _non_empty_list(val):
                errors.append(f"empty or invalid list: {field}")
        elif isinstance(val, str) and not val.strip():
            errors.append(f"empty string: {field}")
    return len(errors) == 0, errors


def validate_field_types(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if skill.get("skill_type") != "single_algorithm":
        errors.append("skill_type must be single_algorithm")
    cp = skill.get("complexity_pattern")
    if not isinstance(cp, dict):
        errors.append("complexity_pattern must be object")
    rs = skill.get("related_subtypes")
    if not isinstance(rs, dict):
        errors.append("related_subtypes must be object")
    return len(errors) == 0, errors


def validate_skill_id(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    sid = str(skill.get("skill_id") or "")
    if not re.match(SKILL_ID_PATTERN, sid):
        return False, [f"invalid skill_id: {sid}"]
    return True, []


def validate_primary_subtype(skill: dict[str, Any], expected_subtype: str) -> tuple[bool, list[str]]:
    if skill.get("primary_subtype") != expected_subtype:
        return False, [f"primary_subtype mismatch: {skill.get('primary_subtype')} != {expected_subtype}"]
    return True, []


def validate_algorithm_family(skill: dict[str, Any], expected_family: str) -> tuple[bool, list[str]]:
    if expected_family and skill.get("algorithm_family") != expected_family:
        return False, [f"algorithm_family mismatch: {skill.get('algorithm_family')} != {expected_family}"]
    return True, []


def validate_code_template(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    tmpl = str(skill.get("code_template") or "").strip()
    if len(tmpl) < 20:
        return False, ["code_template too short"]
    try:
        tree = ast.parse(tmpl)
    except SyntaxError as exc:
        return False, [f"code_template must parse as Python: {exc.msg} at line {exc.lineno}"]
    if skill.get("template_type", "executable_python") == "executable_python" and _has_placeholder_nodes(tree):
        return False, ["executable_python code_template must not contain pass or ellipsis placeholders"]
    return True, []


def _has_placeholder_nodes(tree: ast.AST) -> bool:
    return any(
        isinstance(node, ast.Pass)
        or (isinstance(node, ast.Constant) and node.value is Ellipsis)
        for node in ast.walk(tree)
    )


def infer_template_type(template: str) -> str:
    try:
        tree = ast.parse(str(template or ""))
    except SyntaxError:
        return "executable_python"
    return "pseudocode_python" if _has_placeholder_nodes(tree) else "executable_python"


def validate_normalized_metadata(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if not str(skill.get("canonical_subtype") or "").strip():
        errors.append("missing or empty canonical_subtype")
    if not isinstance(skill.get("alias_subtypes"), list):
        errors.append("alias_subtypes must be list")
    if skill.get("template_type") not in TEMPLATE_TYPES:
        errors.append("template_type must be executable_python or pseudocode_python")
    related = skill.get("related_subtypes")
    required_keys = {"similar", "prerequisite", "often_combined_with", "should_not_confuse_with"}
    if not isinstance(related, dict) or set(related) != required_keys:
        errors.append("related_subtypes must contain normalized relationship keys")
    elif any(not isinstance(related[key], list) for key in required_keys):
        errors.append("related_subtypes values must be lists")
    for field in ("related_existing_subtypes", "related_future_subtypes"):
        if not isinstance(skill.get(field), list):
            errors.append(f"{field} must be list")
    return len(errors) == 0, errors


def validate_evidence_consistency(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    evidence = skill.get("evidence")
    if not isinstance(evidence, dict) or "num_representative_rows" not in evidence:
        return True, []
    examples = skill.get("representative_examples") or []
    declared = int(evidence.get("num_representative_rows") or 0)
    if declared != len(examples):
        return False, [
            f"evidence.num_representative_rows mismatch: {declared} != {len(examples)}"
        ]
    return True, []


def validate_no_empty_core_fields(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    for field in ("core_mechanism", "state_or_structure_design", "transition_or_decision_rule"):
        if not str(skill.get(field) or "").strip():
            errors.append(f"empty: {field}")
    return len(errors) == 0, errors


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
                and a_lines[i + length].strip() == a_lines[i].strip()
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

    skill_text = json_dumps_skill(skill)
    issues: list[str] = []

    for row in source_rows:
        stmt = str(row.get("problem_statement") or "")
        code = str(row.get("solution_code") or "")
        if stmt:
            run = _longest_common_token_run(_tokenize(skill_text), _tokenize(stmt))
            if run > max_tokens:
                issues.append(f"problem_statement leakage ({run} tokens)")
        if code:
            a_lines = [ln for ln in skill_text.splitlines() if ln.strip()]
            b_lines = code.splitlines()
            run = _longest_common_line_run(a_lines, b_lines)
            if run > max_code_lines:
                issues.append(f"solution_code leakage ({run} lines)")

    return len(issues) == 0, issues


def json_dumps_skill(skill: dict[str, Any]) -> str:
    return json.dumps(skill, ensure_ascii=False)


def validate_skill_schema(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    checks = [
        validate_required_fields,
        validate_field_types,
        validate_skill_id,
        validate_code_template,
        validate_no_empty_core_fields,
    ]
    all_errors: list[str] = []
    ok = True
    for fn in checks:
        passed, errs = fn(skill)
        ok = ok and passed
        all_errors.extend(errs)
    return ok, all_errors


def validate_normalized_skill_schema(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    ok, errors = validate_skill_schema(skill)
    metadata_ok, metadata_errors = validate_normalized_metadata(skill)
    evidence_ok, evidence_errors = validate_evidence_consistency(skill)
    return ok and metadata_ok and evidence_ok, errors + metadata_errors + evidence_errors


def validate_skill_consistency(
    skill: dict[str, Any],
    expected_subtype: str,
    expected_family: str,
) -> tuple[bool, list[str]]:
    errors: list[str] = []
    for fn, args in (
        (validate_primary_subtype, (skill, expected_subtype)),
        (validate_algorithm_family, (skill, expected_family)),
    ):
        passed, errs = fn(*args)
        if not passed:
            errors.extend(errs)
    return len(errors) == 0, errors


def completeness_score(skill: dict[str, Any]) -> float:
    fields = [
        "core_mechanism",
        "algorithm_steps",
        "code_template",
        "implementation_notes",
        "common_pitfalls",
        "retrieval_keywords",
        "trigger_signals",
        "applicability_conditions",
        "non_applicability_conditions",
    ]
    filled = 0
    for f in fields:
        val = skill.get(f)
        if isinstance(val, list) and val:
            filled += 1
        elif isinstance(val, str) and val.strip():
            filled += 1
    return filled / len(fields)


def score_skill(skill: dict[str, Any], critique: dict[str, Any] | None = None) -> dict[str, Any]:
    c = critique or {}
    abstraction = float(c.get("abstraction_score") or 0.8)
    consistency = float(c.get("consistency_score") or 0.8)
    retrieval = float(c.get("retrieval_score") or 0.8)
    template = float(c.get("template_score") or 0.8)
    leakage = float(c.get("leakage_score") or 0.8)
    complete = completeness_score(skill)

    final_score = (
        0.25 * abstraction
        + 0.20 * consistency
        + 0.20 * retrieval
        + 0.15 * template
        + 0.10 * leakage
        + 0.10 * complete
    )

    return {
        "abstraction_score": abstraction,
        "consistency_score": consistency,
        "retrieval_score": retrieval,
        "template_score": template,
        "leakage_score": leakage,
        "completeness_score": complete,
        "final_score": round(final_score, 4),
    }


def apply_final_decision(
    skill: dict[str, Any],
    scores: dict[str, Any],
    config: dict[str, Any],
    *,
    schema_ok: bool,
    leakage_ok: bool,
    consistency_ok: bool,
) -> dict[str, Any]:
    vc = config.get("validation", config)
    min_accept = float(vc.get("min_final_score", 0.85))
    min_revise = float(vc.get("revise_score_threshold", 0.70))
    final = float(scores.get("final_score") or 0)

    if not schema_ok or not leakage_ok or not consistency_ok:
        decision = "reject"
    elif final >= min_accept:
        decision = "accept"
    elif final >= min_revise:
        decision = "revise"
    else:
        decision = "reject"

    qc = skill.setdefault("quality_control", {})
    qc["schema_valid"] = schema_ok
    qc["abstraction_check"] = "pass" if scores.get("abstraction_score", 0) >= 0.7 else "fail"
    qc["leakage_check"] = "pass" if leakage_ok else "fail"
    qc["consistency_check"] = "pass" if consistency_ok else "fail"
    qc["final_decision"] = decision
    qc["final_score"] = final
    return skill
