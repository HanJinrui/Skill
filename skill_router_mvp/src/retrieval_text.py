"""Render heterogeneous skill cards into consistent retrieval documents."""
from __future__ import annotations

import re
from typing import Any


TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_RE.findall(text or "")]


def _list_text(value: Any, limit: int = 6) -> str:
    if not isinstance(value, list):
        return ""
    return " | ".join(str(item).strip() for item in value[:limit] if str(item).strip())


def _complexity_text(value: Any) -> str:
    if isinstance(value, dict):
        return "; ".join(f"{key}={val}" for key, val in value.items() if val)
    return str(value or "")


def _flow_text(value: Any) -> str:
    if not isinstance(value, list):
        return ""
    parts: list[str] = []
    for item in value[:6]:
        if isinstance(item, dict):
            algorithm = item.get("algorithm") or ""
            role = item.get("role") or ""
            parts.append(f"{algorithm} {role}".strip())
        else:
            parts.append(str(item))
    return " -> ".join(part for part in parts if part)


def build_gate_card(raw: dict[str, Any], rank: int = 0) -> str:
    """Compact text card for the gate prompt (~60-80 tokens per candidate).

    Omits scores and large JSON blobs so the 7B model focuses on the
    discriminating signals rather than numerical noise.
    """
    skill_type = str(raw.get("skill_type") or "")
    lines = [f"[Candidate {rank + 1}] skill_id={raw.get('skill_id', '')}"]
    if skill_type == "single_algorithm":
        if raw.get("primary_subtype"):
            lines.append(f"  Subtype: {raw['primary_subtype']}")
        if raw.get("core_mechanism"):
            lines.append(f"  Mechanism: {str(raw['core_mechanism'])[:130]}")
    else:
        sig = raw.get("composition_signature") or []
        lines.append(f"  Components: {' + '.join(str(s) for s in sig)}")
        if raw.get("core_composition_mechanism"):
            lines.append(f"  Mechanism: {str(raw['core_composition_mechanism'])[:130]}")
    triggers = raw.get("trigger_signals") or []
    if triggers:
        lines.append(f"  Triggers: {' | '.join(str(t) for t in triggers[:4])}")
    applicable = raw.get("applicability_conditions") or []
    if applicable:
        lines.append(f"  Use when: {str(applicable[0])[:110]}")
    reject = raw.get("non_applicability_conditions") or []
    if reject:
        lines.append(f"  Reject when: {str(reject[0])[:90]}")
    return "\n".join(lines)


def build_retrieval_text(raw: dict[str, Any]) -> str:
    skill_type = str(raw.get("skill_type") or "")
    lines = [
        f"SKILL_ID: {raw.get('skill_id', '')}",
        f"TYPE: {skill_type}",
        f"TITLE: {raw.get('skill_name', '')}",
    ]
    if skill_type == "single_algorithm":
        lines.extend(
            [
                f"FAMILY: {raw.get('algorithm_family', '')}",
                f"SUBTYPE: {raw.get('primary_subtype', '')}",
                f"MECHANISM: {raw.get('core_mechanism', '')}",
            ]
        )
    else:
        lines.extend(
            [
                f"COMPONENTS: {_list_text(raw.get('composition_signature'), 8)}",
                f"FAMILIES: {_list_text(raw.get('composition_families'), 8)}",
                f"COMPOSITION: {raw.get('core_composition_mechanism', '')}",
                f"FLOW: {_flow_text(raw.get('algorithm_flow'))}",
            ]
        )
    lines.extend(
        [
            f"TRIGGERS: {_list_text(raw.get('trigger_signals'))}",
            f"APPLICABLE: {_list_text(raw.get('applicability_conditions'))}",
            f"REJECT_WHEN: {_list_text(raw.get('non_applicability_conditions'))}",
            f"COMPLEXITY: {_complexity_text(raw.get('complexity_pattern'))}",
            f"KEYWORDS: {_list_text(raw.get('retrieval_keywords'), 12)}",
            f"NOTES: {_list_text(raw.get('implementation_notes'), 4)}",
        ]
    )
    return "\n".join(line for line in lines if line.split(":", 1)[-1].strip())
