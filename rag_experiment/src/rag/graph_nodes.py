"""Build all graph-node tables from existing Stage A/B/C/D artifacts.

Every builder is pure — it takes the already-loaded rows and returns a
list of node dicts ready to persist as JSONL.

Node-id conventions (see graph_schema.py):

* `skill::<skill_id>`
* `family::<family>`
* `mechanism::<mechanism_id>`
* `signal::<signal_id>`
* `proto_prob::<prototype_problem_id>`
* `proto_sol::<prototype_solution_id>`
"""
from __future__ import annotations

from typing import Any, Dict, List, Sequence, Tuple

from .facet_extract import (
    FacetBundle,
    extract_problem_facets,
    extract_skill_facets,
    extract_solution_facets,
)
from .graph_schema import (
    CORE_FAMILIES,
    MECHANISMS,
    SIGNALS,
    family_node_id,
    mechanism_node_id,
    prototype_problem_node_id,
    prototype_solution_node_id,
    signal_node_id,
    skill_node_id,
)


# --------------------------------------------------------------------------- #
# Skill nodes
# --------------------------------------------------------------------------- #

def build_skill_nodes(skills: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return one skill node per unique skill_id with derived facet tags.

    We never mutate the original skill card; we only *append* derived
    fields so downstream code can still use the untouched Stage D shape.
    """
    out: List[Dict[str, Any]] = []
    seen: set[str] = set()
    for skill in skills:
        sid = skill.get("skill_id")
        if not isinstance(sid, str) or not sid or sid in seen:
            continue
        seen.add(sid)
        facets = extract_skill_facets(skill)
        node = dict(skill)  # preserve original card shape
        node["node_type"] = "skill"
        node["node_id"] = skill_node_id(sid)
        node["is_bundle"] = (skill.get("scope") == "multi")
        # Derived / standardized facet fields — added, never overwriting.
        node["facets"] = facets.to_dict()
        node["mechanism_tags"] = list(facets.mechanism_tags)
        node["signal_tags"] = list(facets.signal_tags)
        node["input_shape_tags"] = list(facets.input_shape_tags)
        node["operation_tags"] = list(facets.operation_tags)
        node["goal_tags"] = list(facets.goal_tags)
        node["complexity_tags"] = list(facets.complexity_tags)
        node["negative_tags"] = list(facets.negative_tags)
        out.append(node)
    return out


# --------------------------------------------------------------------------- #
# Family / mechanism / signal nodes (static from vocab)
# --------------------------------------------------------------------------- #

def build_family_nodes() -> List[Dict[str, Any]]:
    return [
        {
            "node_type": "family",
            "node_id": family_node_id(fam),
            "family_id": fam,
            "display_name": fam,
        }
        for fam in sorted(CORE_FAMILIES)
    ]


def build_mechanism_nodes() -> List[Dict[str, Any]]:
    return [
        {
            "node_type": "mechanism",
            "node_id": mechanism_node_id(m.mechanism_id),
            "mechanism_id": m.mechanism_id,
            "families": list(m.families),
            "aliases": list(m.aliases),
            "description": m.description,
        }
        for m in MECHANISMS
    ]


def build_signal_nodes() -> List[Dict[str, Any]]:
    return [
        {
            "node_type": "signal",
            "node_id": signal_node_id(s.signal_id),
            "signal_id": s.signal_id,
            "category": s.category,
            "surface_forms": list(s.surface_forms),
            "linked_mechanisms": list(s.linked_mechanisms),
        }
        for s in SIGNALS
    ]


# --------------------------------------------------------------------------- #
# Prototype nodes
# --------------------------------------------------------------------------- #

def _prototype_problem_id(problem_id: str, skill_id: str, idx: int) -> str:
    return f"proto_prob__{skill_id}__{idx:03d}__{problem_id}"


def _prototype_solution_id(problem_id: str, solution_id: str, skill_id: str, idx: int) -> str:
    return f"proto_sol__{skill_id}__{idx:03d}__{problem_id}__{solution_id}"


def _select_prototype_solutions_per_skill(
    solutions: Sequence[Dict[str, Any]],
    *,
    max_prototypes_per_skill: int,
) -> Dict[str, List[Dict[str, Any]]]:
    """Group solutions by skill_id and rank them by prototype quality.

    A solution row yields candidate prototypes for every skill_id it
    claims — we include single-skill cards for each detected family, plus
    the multi-skill card if there are 2+ detected families.
    """
    from ..taxonomy import CORE_FAMILY_SET, skill_id_for_multi, skill_id_for_single

    def quality_score(row: Dict[str, Any]) -> Tuple[int, int, float]:
        # Prefer consistent > partial, glm_ast_fused > glm_only, higher conf.
        ctype = 1 if row.get("consistency_type") == "consistent" else 0
        src = 1 if row.get("label_source") == "glm_ast_fused" else 0
        conf = float(row.get("fused_confidence") or row.get("llm_confidence") or 0.0)
        return (ctype, src, conf)

    per_skill: Dict[str, List[Dict[str, Any]]] = {}
    for row in solutions:
        detected = [s for s in (row.get("detected_multi_skills") or []) if s in CORE_FAMILY_SET]
        if not detected:
            continue
        skill_ids: List[str] = [skill_id_for_single(f) for f in detected]
        if len(set(detected)) >= 2:
            skill_ids.append(skill_id_for_multi(detected))
        for sid in set(skill_ids):
            per_skill.setdefault(sid, []).append(row)

    # Sort and cap per skill.
    trimmed: Dict[str, List[Dict[str, Any]]] = {}
    for sid, rows in per_skill.items():
        rows.sort(key=quality_score, reverse=True)
        trimmed[sid] = rows[:max_prototypes_per_skill]
    return trimmed


def build_prototype_nodes(
    *,
    solutions: Sequence[Dict[str, Any]],
    problems_by_id: Dict[str, Dict[str, Any]],
    problem_labels_by_id: Dict[str, Dict[str, Any]],
    existing_skill_ids: Sequence[str],
    max_prototype_per_skill: int = 8,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Build PrototypeProblemNode and PrototypeSolutionNode tables."""
    existing = set(existing_skill_ids)
    selected = _select_prototype_solutions_per_skill(
        solutions, max_prototypes_per_skill=max_prototype_per_skill
    )

    prob_nodes: List[Dict[str, Any]] = []
    sol_nodes: List[Dict[str, Any]] = []
    seen_proto_prob: set[str] = set()
    seen_proto_sol: set[str] = set()

    for sid, rows in selected.items():
        if sid not in existing:
            continue
        for idx, row in enumerate(rows):
            pid = row.get("problem_id")
            if not isinstance(pid, str):
                continue
            prob = problems_by_id.get(pid, {})
            label = problem_labels_by_id.get(pid, {})
            sol_facets = extract_solution_facets(row)
            prob_facets = extract_problem_facets(prob, label=label)

            # Prototype problem node (one per (problem, skill) pair)
            pp_local_id = _prototype_problem_id(pid, sid, idx)
            if pp_local_id not in seen_proto_prob:
                seen_proto_prob.add(pp_local_id)
                prob_nodes.append({
                    "node_type": "prototype_problem",
                    "node_id": prototype_problem_node_id(pp_local_id),
                    "prototype_problem_id": pp_local_id,
                    "problem_id": pid,
                    "skill_id": sid,
                    "problem_summary": label.get("problem_summary") or "",
                    "problem_text_snippet": (prob.get("problem_statement") or "")[:1200],
                    "problem_skills": list(label.get("normalized_multi_skills") or []),
                    "signals": list(prob_facets.signal_tags),
                    "input_shape": list(prob_facets.input_shape_tags),
                    "operation_tags": list(prob_facets.operation_tags),
                    "goal_tags": list(prob_facets.goal_tags),
                    "constraint_tags": [
                        s for s in prob_facets.signal_tags
                        if s.startswith("n_le_") or s in ("q_large", "small_alphabet")
                    ],
                    "facets": prob_facets.to_dict(),
                })

            # Prototype solution node (one per (problem, solution_id, skill) triple)
            sol_id = str(row.get("solution_id") or "s0")
            ps_local_id = _prototype_solution_id(pid, sol_id, sid, idx)
            if ps_local_id not in seen_proto_sol:
                seen_proto_sol.add(ps_local_id)
                sol_nodes.append({
                    "node_type": "prototype_solution",
                    "node_id": prototype_solution_node_id(ps_local_id),
                    "prototype_solution_id": ps_local_id,
                    "problem_id": pid,
                    "solution_id": sol_id,
                    "skill_id": sid,
                    "detected_multi_skills": list(row.get("detected_multi_skills") or []),
                    "core_mechanism_summary": row.get("core_mechanism_summary") or "",
                    "ast_hints": list(row.get("ast_hints") or []),
                    "ast_features": dict(row.get("ast_features") or {}),
                    "consistency_type": row.get("consistency_type") or "",
                    "label_source": row.get("label_source") or "",
                    "llm_confidence": float(row.get("llm_confidence") or 0.0),
                    "facets": sol_facets.to_dict(),
                    "mechanism_tags": list(sol_facets.mechanism_tags),
                })
    return prob_nodes, sol_nodes
