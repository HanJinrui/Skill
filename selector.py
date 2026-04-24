from __future__ import annotations

from pathlib import Path
import json
import re


FAMILY_HEURISTICS = {
    "amortized_analysis": [
        "amortized",
        "aggregate analysis",
        "potential method",
        "many operations",
    ],
    "bit_manipulation": [
        "bit",
        "xor",
        "mask",
        "binary representation",
    ],
    "complete_search": [
        "brute force",
        "enumerate all",
        "search all possibilities",
        "subset",
    ],
    "data_structures": [
        "stack",
        "queue",
        "heap",
        "balanced tree",
    ],
    "dynamic_programming": [
        "dynamic programming",
        "dp",
        "subproblem",
        "state",
        "transition",
        "longest",
        "minimum",
        "maximum",
        "ways",
    ],
    "greedy_algorithms": [
        "greedy",
        "sort",
        "earliest finish",
        "locally optimal",
    ],
    "range_queries": [
        "range query",
        "interval query",
        "prefix sum",
        "segment tree",
    ],
    "sorting": [
        "sort",
        "sorted order",
        "ordering",
        "comparator",
    ],
    "other": [],
}

SUBTYPE_HEURISTICS = {
    "linear_prefix": [
        "subsequence",
        "prefix",
        "position",
        "previous",
        "earlier",
    ],
    "interval": [
        "interval",
        "substring",
        "split",
        "cut",
        "triangulation",
    ],
    "interval_scheduling": [
        "interval",
        "schedule",
        "finish time",
        "compatible",
    ],
}


def classify_family(problem_text: str, manifests_dir: Path) -> dict[str, object]:
    router_manifest = _load_json(manifests_dir / "router.json")
    candidates = router_manifest["router"]["supported_families"]
    scored = [
        {
            "family_name": entry["family_name"],
            "score": _score_text(
                problem_text,
                entry["trigger_summary"] + FAMILY_HEURISTICS.get(entry["family_name"], []),
                [],
            ),
            "reason": f"matched {entry['family_name']} routing signals",
        }
        for entry in candidates
    ]
    best = max(scored, key=lambda item: item["score"])
    if best["score"] <= 0:
        return {
            "family_name": "other",
            "confidence": 0.0,
            "reason": "no generated family achieved a positive routing score",
            "candidates": scored,
        }
    total_positive = sum(max(item["score"], 0.0) for item in scored) or 1.0
    return {
        "family_name": best["family_name"],
        "confidence": round(max(best["score"], 0.0) / total_positive, 3),
        "reason": best["reason"],
        "candidates": scored,
    }


def classify_subtype(problem_text: str, manifests_dir: Path, family_name: str) -> dict[str, object]:
    subtype_registry = _load_json(manifests_dir / "subtype_registry.json")
    candidates = [
        entry for entry in subtype_registry["subskills"] if entry["algorithm_family"] == family_name
    ]
    if not candidates:
        return {
            "subtype": "unknown",
            "skill_name": "",
            "confidence": 0.0,
            "reason": f"no generated subtype skills are available for family '{family_name}'",
            "candidates": [],
        }

    scored = [
        {
            "skill_name": entry["skill_name"],
            "subtype": entry["subtype"],
            "score": _score_text(
                problem_text,
                entry["trigger_signals"] + SUBTYPE_HEURISTICS.get(entry["subtype"], []),
                entry["non_triggers"],
            ),
            "reason": f"matched subtype cues for {entry['skill_name']}",
        }
        for entry in candidates
    ]
    best = max(scored, key=lambda item: item["score"])
    if best["score"] <= 0:
        return {
            "subtype": "unknown",
            "skill_name": "",
            "confidence": 0.0,
            "reason": f"no subtype in family '{family_name}' achieved a positive routing score",
            "candidates": scored,
        }
    total_positive = sum(max(item["score"], 0.0) for item in scored) or 1.0
    return {
        "subtype": best["subtype"],
        "skill_name": best["skill_name"],
        "confidence": round(max(best["score"], 0.0) / total_positive, 3),
        "reason": best["reason"],
        "candidates": scored,
    }


def solve_with_selected_skill(
    manifests_dir: Path,
    skill_name: str,
    problem_text: str,
    emit_code: bool = False,
) -> str:
    subtype_registry = _load_json(manifests_dir / "subtype_registry.json")
    entry = next(
        (item for item in subtype_registry["subskills"] if item["skill_name"] == skill_name),
        None,
    )
    if entry is None:
        raise ValueError(f"subtype skill '{skill_name}' was not found in subtype_registry.json")

    pattern = entry["pattern_abstraction"]
    transfer = entry["transfer_strategy"]
    sections = entry["output_contract"]["sections"]
    lines = [
        sections[0],
        pattern["core_recognition"],
        "",
        sections[1],
    ]
    lines.extend(f"- {item}" for item in pattern["state_templates"])
    lines.append("")
    lines.append(sections[2])
    lines.extend(f"- {item}" for item in pattern["transition_templates"])
    lines.extend(f"- base case: {item}" for item in pattern["base_case_rules"])
    lines.extend(f"- iteration order: {item}" for item in pattern["iteration_order_rules"])
    lines.append("")
    lines.append(sections[3])
    lines.append("- map the problem to the reusable state or invariant before writing code")
    lines.append("- verify the refusal boundaries before committing to this subtype")
    lines.append("")
    lines.append("迁移清单")
    lines.extend(f"- {item}" for item in transfer["mapping_steps"])
    lines.append(f"- problem excerpt length: {len(problem_text.strip())} characters")
    if emit_code:
        lines.append("")
        lines.append("代码")
        lines.append("- emit python code only because the caller explicitly requested it")
        lines.append("- keep the implementation aligned with the selected subtype state and transition rules")
    return "\n".join(lines)


def _load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"required manifest not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _score_text(problem_text: str, trigger_signals: list[str], non_triggers: list[str]) -> float:
    normalized = problem_text.lower()
    positive = sum(_phrase_matches(normalized, phrase) for phrase in trigger_signals)
    negative = sum(_phrase_matches(normalized, phrase) for phrase in non_triggers)
    return float(positive - negative)


def _phrase_matches(normalized_text: str, phrase: str) -> int:
    phrase_lower = phrase.lower()
    if phrase_lower in normalized_text:
        return 2

    tokens = [token for token in re.findall(r"[a-z0-9_]+", phrase_lower) if len(token) >= 4]
    if not tokens:
        return 0
    matches = sum(1 for token in tokens if token in normalized_text)
    if matches == 0:
        return 0
    return 1 if matches < len(tokens) else 2
