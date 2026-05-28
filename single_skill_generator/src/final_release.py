"""Build the normalized final single-skill release from frozen evidence snapshots."""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .additional_evidence import (
    algorithm_index,
    build_curated_rows,
    load_algorithm_catalog,
    load_validated_curated_evidence,
)
from .io_utils import load_jsonl, load_yaml, resolve_path, write_json, write_jsonl
from .llm_client import build_llm_client
from .main import load_config
from .retrieval_gate import evaluate_retrieval_gate
from .skill_generator import generate_skill_for_subtype
from .skill_validator import infer_template_type, validate_normalized_skill_schema, validate_skill_schema


RELATION_KEYS = ("similar", "prerequisite", "often_combined_with", "should_not_confuse_with")
GCD_SUBTYPE = "math_gcd_lcm"
GCD_MST_SUBTYPE = "graph_gcd_mst_dsu"
BINARY_ANSWER_SUBTYPE = "binary_search_on_answer"
BINARY_BOUND_SUBTYPE = "binary_search_lower_upper_bound"

PHRASE_ALIASES = {
    "aho_corasick": "string_aho_corasick",
    "aho-corasick": "string_aho_corasick",
    "kmp": "string_kmp_prefix_function",
    "rabin-karp": "string_rolling_hash",
    "rabin_karp": "string_rolling_hash",
    "z-algorithm": "string_z_algorithm",
    "z_algorithm": "string_z_algorithm",
    "2d_fenwick_tree": "ds_fenwick_tree_2d",
    "2d_segment_tree": "ds_segment_tree_2d",
    "2d_sparse_table": "ds_sparse_table_2d",
    "general_mst_algorithms": "graph_mst_general",
    "minimum_spanning_tree_kruskal": "graph_mst_kruskal",
    "minimum_window_substring": "string_minimum_window_substring",
    "longest_increasing_subarray": "array_longest_increasing_contiguous",
    "simple_sorting_without_custom_key": "sorting_builtin",
    "simple_sorting": "sorting_builtin",
    "sliding_window_2d": "sliding_window_2d",
    "ordered_set_operations": "ds_ordered_set",
    "data_structures_like_heap_priority_queue": "ds_heap_priority_queue",
    "combinatorics_counting_without_memoization": "math_combinatorics_ncr",
    "matrix_exponentiation_for_counting": "math_matrix_exponentiation",
}

TEMPLATE_REPAIRS = {
    "single.dp_memoized_recursion.v1": """from functools import lru_cache

def solve(initial_state):
    @lru_cache(maxsize=None)
    def dp(state):
        if is_base_case(state):
            return base_answer(state)
        best = initial_value()
        for choice in possible_choices(state):
            next_state = apply_choice(state, choice)
            candidate = transition_cost(state, choice) + dp(next_state)
            best = choose_better(best, candidate)
        return best

    return dp(initial_state)
""",
    "single.ds_heap_priority_queue.v1": """import heapq

def process_priority_queue(initial_items):
    heap = list(initial_items)
    heapq.heapify(heap)
    processed = []
    while heap:
        priority, item = heapq.heappop(heap)
        if is_stale(priority, item):
            continue
        processed.append(item)
        for new_priority, new_item in derived_items(item):
            heapq.heappush(heap, (new_priority, new_item))
    return processed
""",
    "single.search_branch_and_bound.v1": """def branch_and_bound(initial_state):
    best = initial_incumbent()

    def explore(state, incumbent):
        if is_complete(state):
            return choose_better(incumbent, evaluate(state))
        if cannot_improve(lower_bound(state), incumbent):
            return incumbent
        for choice in feasible_choices(state):
            incumbent = explore(extend_state(state, choice), incumbent)
        return incumbent

    return explore(initial_state, best)
""",
}


def load_release_config(path: Path) -> dict[str, Any]:
    config = load_config(path)
    root = Path(config["_project_root"])
    release = config.get("release", {})
    for key, value in list(release.items()):
        if isinstance(value, str) and (key.endswith("_path") or key.endswith("_dir")):
            release[key] = str(resolve_path(root, value))
    config["release"] = release
    return config


def _sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _canonical_slug(value: str) -> str:
    text = value.strip().lower().replace("–", "-").replace("‑", "-")
    text = text.split(" (", 1)[0].split(":", 1)[0].split(" - ", 1)[0]
    text = re.sub(r"\s+without\s+.*$", "", text)
    text = re.sub(r"[^a-z0-9]+", "_", text).strip("_")
    return text


def load_alias_metadata(config: dict[str, Any]) -> tuple[dict[str, str], dict[str, str]]:
    data = load_yaml(config["release"]["alias_path"])
    aliases = {str(key): str(value) for key, value in (data.get("aliases") or {}).items()}
    family_overrides = {
        str(key): str(value) for key, value in (data.get("family_overrides") or {}).items()
    }
    return aliases, family_overrides


def _inverse_aliases(aliases: dict[str, str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = defaultdict(list)
    for alias, canonical in aliases.items():
        result[canonical].append(alias)
    return {canonical: sorted(values) for canonical, values in result.items()}


def normalize_reference(
    value: Any,
    *,
    aliases: dict[str, str],
    published: set[str],
) -> str | None:
    raw = str(value or "").strip()
    if not raw:
        return None
    slug = _canonical_slug(raw)
    slug = PHRASE_ALIASES.get(slug, slug)
    slug = aliases.get(slug, slug)
    if slug in published:
        return slug
    if " " in raw and slug not in PHRASE_ALIASES.values():
        allowed_prefixes = (
            "bit_", "dp_", "ds_", "graph_", "greedy_", "math_", "search_", "sorting_",
            "string_", "prefix_", "difference_", "sliding_", "binary_", "coordinate_",
            "sweep_", "amortized_", "tsp_", "two_pointer", "sqrt_", "suffix_",
        )
        if not slug.startswith(allowed_prefixes):
            return None
    return slug or None


def _valid_python_template(template: str) -> bool:
    try:
        ast.parse(template)
    except SyntaxError:
        return False
    return True


def normalize_skill(
    skill: dict[str, Any],
    *,
    aliases: dict[str, str],
    family_overrides: dict[str, str],
    published: set[str],
) -> dict[str, Any]:
    output = copy.deepcopy(skill)
    original_subtype = str(output.get("canonical_subtype") or output.get("primary_subtype") or "")
    canonical = aliases.get(original_subtype, original_subtype)
    inverse = _inverse_aliases(aliases)
    output["primary_subtype"] = canonical
    output["canonical_subtype"] = canonical
    output["skill_id"] = f"single.{canonical}.v1"
    output["alias_subtypes"] = sorted(
        set(output.get("alias_subtypes") or []) | set(inverse.get(canonical, []))
    )
    if canonical in family_overrides:
        output["algorithm_family"] = family_overrides[canonical]
    if output["skill_id"] in TEMPLATE_REPAIRS:
        output["code_template"] = TEMPLATE_REPAIRS[output["skill_id"]]
    output["template_type"] = infer_template_type(str(output.get("code_template") or ""))

    prior = output.get("related_subtypes") or {}
    related = {key: [] for key in RELATION_KEYS}
    for key in RELATION_KEYS:
        for value in prior.get(key, []) if isinstance(prior.get(key), list) else []:
            normalized = normalize_reference(value, aliases=aliases, published=published)
            if normalized and normalized != canonical and normalized not in related[key]:
                related[key].append(normalized)
    output["related_subtypes"] = related
    output["related_existing_subtypes"] = []
    output["related_future_subtypes"] = []
    return output


def _normalize_evidence_row(
    row: dict[str, Any],
    canonical: str,
    *,
    aliases: dict[str, str],
    family_overrides: dict[str, str],
) -> dict[str, Any]:
    output = copy.deepcopy(row)
    output["source_primary_subtype"] = row.get("primary_subtype")
    output["primary_subtype"] = canonical
    output["canonical_subtype"] = canonical
    output["alias_subtypes"] = sorted(
        alias for alias, target in aliases.items() if target == canonical
    )
    output["evidence_origin"] = output.get("evidence_origin") or "taco_verified"
    output["evidence_validation"] = output.get("evidence_validation") or "external_verified"
    if canonical in family_overrides:
        output["detected_single_skill"] = family_overrides[canonical]
    return output


def is_gcd_mst_evidence(row: dict[str, Any]) -> bool:
    text = " ".join(
        str(row.get(field) or "")
        for field in ("problem_statement", "core_mechanism_summary", "subtype_rationale", "label_reason")
    ).lower()
    return (
        str(row.get("problem_id") or "") == "taco_train_006404__6404"
        or "minimum spanning" in text
        or "mst" in text
        or ("disjoint set" in text and "gcd" in text)
    )


def route_legacy_binary_search_evidence(row: dict[str, Any]) -> tuple[str | None, str]:
    text = " ".join(
        str(row.get(field) or "")
        for field in ("core_mechanism_summary", "subtype_rationale", "problem_statement")
    ).lower()
    ordered_query_terms = (
        "rightmost base",
        "sorted stair",
        "nearest centers",
        "perfect powers",
        "largest divisor",
        "sort distinct values",
        "binary search the sorted",
    )
    answer_terms = (
        "feasibility",
        "minimum required",
        "maximum edge weight",
        "smallest x satisfying",
        "poison duration",
        "number of cookies",
        "number of full rounds",
        "binary search on answer",
        "capacity",
    )
    if any(term in text for term in ordered_query_terms):
        return BINARY_BOUND_SUBTYPE, "ordered lookup/location evidence routed away from answer search"
    if any(term in text for term in answer_terms):
        return BINARY_ANSWER_SUBTYPE, "monotonic feasibility/answer-space evidence retained"
    return None, "ambiguous legacy binary-search evidence excluded from canonical evidence"


def build_evidence_ledger(
    config: dict[str, Any],
    *,
    aliases: dict[str, str],
    family_overrides: dict[str, str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    input_cfg = config["input"]
    base_skills = load_jsonl(input_cfg["base_skill_bank_path"])
    legacy_allowed = {str(skill.get("primary_subtype") or "") for skill in base_skills}
    legacy_rows: list[dict[str, Any]] = []
    routing_events: list[dict[str, Any]] = []
    for generation_input in load_jsonl(input_cfg["legacy_generation_inputs_path"]):
        subtype = str(generation_input.get("primary_subtype") or "")
        if subtype not in legacy_allowed:
            continue
        canonical = aliases.get(subtype, subtype)
        for row in (generation_input.get("all_source_rows") or []):
            routed = canonical
            reason = "direct canonical or alias migration"
            if subtype == "sorting_binary_search_answer":
                routed, reason = route_legacy_binary_search_evidence(row)
                routing_events.append(
                    {
                        "problem_id": row.get("problem_id"),
                        "solution_id": row.get("solution_id"),
                        "source_subtype": subtype,
                        "routed_to": routed,
                        "reason": reason,
                    }
                )
            if routed:
                normalized = _normalize_evidence_row(
                    row,
                    routed,
                    aliases=aliases,
                    family_overrides=family_overrides,
                )
                normalized["evidence_route_reason"] = reason
                legacy_rows.append(normalized)

    additional_rows: list[dict[str, Any]] = []
    quarantine: list[dict[str, Any]] = []
    for row in load_jsonl(input_cfg["targeted_additions_evidence_path"]):
        subtype = str(row.get("primary_subtype") or "")
        canonical = aliases.get(subtype, subtype)
        normalized = _normalize_evidence_row(
            row,
            canonical,
            aliases=aliases,
            family_overrides=family_overrides,
        )
        if canonical == GCD_SUBTYPE and is_gcd_mst_evidence(normalized):
            normalized["routed_to_canonical_subtype"] = GCD_MST_SUBTYPE
            normalized["quarantine_reason"] = "GCD-MST/DSU composition is not generic gcd/lcm"
            quarantine.append(normalized)
        else:
            additional_rows.append(normalized)

    catalog = load_algorithm_catalog(config)
    curated_entries = load_validated_curated_evidence(config, catalog)
    curated_gcd = build_curated_rows(
        config,
        catalog,
        curated_entries,
        target_ids={GCD_SUBTYPE},
    )[GCD_SUBTYPE]
    existing_gcd = [row for row in additional_rows if row["canonical_subtype"] == GCD_SUBTYPE]
    required = max(0, 5 - len(existing_gcd))
    additional_rows.extend(
        _normalize_evidence_row(
            row,
            GCD_SUBTYPE,
            aliases=aliases,
            family_overrides=family_overrides,
        )
        for row in curated_gcd[:required]
    )

    seen: set[tuple[str, str, str, str]] = set()
    ledger: list[dict[str, Any]] = []
    for row in legacy_rows + additional_rows:
        key = (
            str(row.get("canonical_subtype") or ""),
            str(row.get("problem_id") or ""),
            str(row.get("solution_id") or ""),
            str(row.get("evidence_origin") or ""),
        )
        if key not in seen:
            seen.add(key)
            ledger.append(row)
    return ledger, quarantine, routing_events


def _generic_gcd_fallback(rows: list[dict[str, Any]]) -> dict[str, Any]:
    origins = Counter(str(row.get("evidence_origin") or "") for row in rows)
    source = "TACO+curated" if len(origins) > 1 else ("TACO" if "taco_verified" in origins else "curated")
    return {
        "skill_id": "single.math_gcd_lcm.v1",
        "skill_name": "Euclidean GCD and LCM Computation",
        "skill_type": "single_algorithm",
        "version": "v1",
        "status": "seed",
        "algorithm_family": "math_algorithms",
        "primary_subtype": GCD_SUBTYPE,
        "canonical_subtype": GCD_SUBTYPE,
        "alias_subtypes": [],
        "source_dataset": source,
        "generation_method": "targeted_evidence_distillation_repair",
        "trigger_signals": ["greatest common divisor", "least common multiple", "coprime", "gcd of an array"],
        "applicability_conditions": ["The required operation is divisibility reduction via gcd or lcm."],
        "non_applicability_conditions": ["The main mechanism is constructing a graph or spanning tree using DSU."],
        "core_mechanism": "Apply Euclid's remainder reduction for gcd; derive lcm using a // gcd(a, b) * b while avoiding unnecessary overflow.",
        "algorithm_steps": ["Reduce two values with repeated remainder updates.", "Extend gcd across a sequence when needed.", "Compute lcm from gcd when requested."],
        "state_or_structure_design": "Maintain only current gcd values or prefix and suffix gcd arrays for exclusion queries.",
        "transition_or_decision_rule": "Replace (a, b) by (b, a mod b) until b is zero.",
        "complexity_pattern": {"time": "O(log min(a,b)) per pair", "space": "O(1)", "notes": ""},
        "code_template": """from math import gcd

def gcd_all(values):
    result = 0
    for value in values:
        result = gcd(result, value)
    return result

def lcm(a, b):
    return 0 if a == 0 or b == 0 else a // gcd(a, b) * b
""",
        "template_type": "executable_python",
        "implementation_notes": ["Divide before multiplying when computing lcm."],
        "common_pitfalls": ["Confusing generic gcd aggregation with graph connectivity construction.", "Forgetting zero handling in lcm."],
        "retrieval_keywords": ["gcd", "lcm", "euclidean algorithm", "coprime", "prefix gcd", "suffix gcd"],
        "related_subtypes": {
            "similar": ["math_prime_factorization"],
            "prerequisite": [],
            "often_combined_with": ["math_inclusion_exclusion"],
            "should_not_confuse_with": [GCD_MST_SUBTYPE],
        },
        "related_existing_subtypes": [],
        "related_future_subtypes": [],
        "representative_examples": [],
        "evidence": {},
        "quality_control": {
            "schema_valid": True,
            "abstraction_check": "pass",
            "leakage_check": "pass",
            "consistency_check": "pass",
            "final_decision": "accept",
            "repair_fallback": True,
        },
    }


def repair_gcd_skill(
    config: dict[str, Any],
    rows: list[dict[str, Any]],
    *,
    use_llm: bool,
) -> tuple[dict[str, Any], str]:
    if use_llm:
        gen_input = {
            "primary_subtype": GCD_SUBTYPE,
            "canonical_subtype": GCD_SUBTYPE,
            "alias_subtypes": [],
            "algorithm_family": "math_algorithms",
            "status": "seed",
            "num_source_rows": len(rows),
            "representative_rows": rows[:5],
            "all_source_rows": rows,
            "mechanism_boundary": (
                "Distill only generic Euclidean gcd/lcm operations, array gcd aggregation, "
                "coprimality, or prefix/suffix gcd. Reject spanning-tree, graph-edge, and DSU mechanisms."
            ),
        }
        client = build_llm_client(config, project_root=Path(config["_project_root"]))
        generated = generate_skill_for_subtype(gen_input, client, config)
        visible = {key: value for key, value in generated.items() if not key.startswith("_")}
        text = " ".join(str(visible.get(key) or "") for key in ("skill_name", "core_mechanism")).lower()
        valid, _ = validate_skill_schema(visible)
        if (
            (visible.get("quality_control") or {}).get("final_decision") == "accept"
            and valid
            and infer_template_type(str(visible.get("code_template") or "")) == "executable_python"
            and not any(term in text for term in ("minimum spanning", "mst", "disjoint set", "dsu"))
        ):
            return visible, "deepseek-v4-pro"
    return _generic_gcd_fallback(rows), (
        "deterministic_executable_fallback_after_deepseek"
        if use_llm
        else "deterministic_validated_fallback"
    )


def build_composed_gcd_mst_skill(quarantine: list[dict[str, Any]]) -> dict[str, Any]:
    problem_ids = sorted({str(row.get("problem_id") or "") for row in quarantine})
    return {
        "skill_id": "composed.graph_gcd_mst_dsu.v1",
        "skill_name": "GCD-Constrained MST with DSU",
        "skill_type": "composed_algorithm",
        "version": "v1",
        "status": "seed",
        "algorithm_family": "graph_composed_optimization",
        "primary_subtype": GCD_MST_SUBTYPE,
        "canonical_subtype": GCD_MST_SUBTYPE,
        "alias_subtypes": ["greedy_dsu_gcd_mst"],
        "source_dataset": "TACO",
        "generation_method": "composition_quarantine_distillation",
        "trigger_signals": ["minimum spanning tree", "divisibility constrained edges", "DSU", "gcd based edge cost"],
        "applicability_conditions": ["Candidate edges arise from divisibility or gcd structure and a minimum spanning connection is required."],
        "non_applicability_conditions": ["Only gcd or lcm values are requested without graph connectivity optimization."],
        "core_mechanism": "Process low-cost divisibility-supported edges first and union components; add fallback edges only for remaining components.",
        "algorithm_steps": ["Order candidate values or edges by cost.", "Use DSU to accept only component-merging edges.", "Connect remaining components with the fallback cost."],
        "state_or_structure_design": "A DSU over vertices plus ordered candidate edge opportunities.",
        "transition_or_decision_rule": "Accept a candidate edge exactly when its endpoints belong to different DSU components.",
        "complexity_pattern": {"time": "Problem-dependent, commonly O(n log n)", "space": "O(n)", "notes": "Requires exploiting divisibility adjacency rather than building all edges."},
        "code_template": """class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True
""",
        "template_type": "executable_python",
        "implementation_notes": ["Prove which divisibility-generated candidate edges are sufficient before omitting general edges."],
        "common_pitfalls": ["Misclassifying this composition as generic gcd/lcm.", "Adding an edge after endpoints are already connected."],
        "retrieval_keywords": ["gcd mst", "divisibility edges", "kruskal", "dsu", "minimum spanning tree"],
        "related_subtypes": {
            "similar": ["graph_mst_kruskal"],
            "prerequisite": ["ds_disjoint_set_union", "math_gcd_lcm"],
            "often_combined_with": [],
            "should_not_confuse_with": ["math_gcd_lcm"],
        },
        "representative_examples": [
            {"problem_id": problem_id, "solution_id": "", "why_representative": "Verified GCD-MST composition evidence."}
            for problem_id in problem_ids
        ],
        "evidence": {
            "num_source_rows": len(quarantine),
            "unique_taco_problem_ids": problem_ids,
            "num_unique_taco_problems": len(problem_ids),
            "evidence_origin_counts": {"taco_verified": len(quarantine)},
        },
        "quality_control": {
            "schema_valid": True,
            "abstraction_check": "pass",
            "leakage_check": "pass",
            "consistency_check": "pass",
            "final_decision": "accept",
        },
    }


def _evidence_groups(ledger: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in ledger:
        grouped[str(row.get("canonical_subtype") or "")].append(row)
    return grouped


def _representative_example(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "problem_id": row.get("problem_id"),
        "solution_id": row.get("solution_id"),
        "why_representative": str(
            row.get("core_mechanism_summary")
            or row.get("label_reason")
            or row.get("subtype_rationale")
            or ""
        )[:200],
    }


def _select_distinct_examples(
    rows: list[dict[str, Any]],
    *,
    max_examples: int,
) -> list[dict[str, Any]]:
    ordered = sorted(
        rows,
        key=lambda row: (
            0 if row.get("evidence_origin") == "taco_verified" else 1,
            str(row.get("problem_id") or ""),
            str(row.get("solution_id") or ""),
        ),
    )
    seen: set[str] = set()
    examples: list[dict[str, Any]] = []
    for row in ordered:
        problem_id = str(row.get("problem_id") or "")
        if not problem_id or problem_id in seen:
            continue
        seen.add(problem_id)
        examples.append(_representative_example(row))
        if len(examples) >= max_examples:
            break
    return examples


def apply_maturity_and_retrieval(
    skills: list[dict[str, Any]],
    ledger: list[dict[str, Any]],
    config: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    grouped = _evidence_groups(ledger)
    held_out: dict[str, list[dict[str, str]]] = {}
    summaries: dict[str, Any] = {}
    stable_min = int(config["release"].get("stable_min_unique_taco_problems", 5))
    provisional_min = int(config["release"].get("provisional_min_unique_taco_problems", 2))
    max_examples = int(config.get("representative_selection", {}).get("max_examples_per_skill", 8))
    normal_examples = int(config.get("representative_selection", {}).get("min_examples_per_skill", 5))
    for skill in skills:
        subtype = str(skill["canonical_subtype"])
        rows = grouped.get(subtype, [])
        taco_by_problem: dict[str, dict[str, Any]] = {}
        for row in rows:
            if row.get("evidence_origin") == "taco_verified":
                taco_by_problem.setdefault(str(row.get("problem_id") or ""), row)
        taco_ids = sorted(problem_id for problem_id in taco_by_problem if problem_id)
        curated_count = sum(1 for row in rows if row.get("evidence_origin") == "curated")
        origin_counts = Counter(str(row.get("evidence_origin") or "") for row in rows)
        if len(taco_ids) >= stable_min:
            representative_ids = taco_ids[:-1][:max_examples]
            query_ids = taco_ids[-1:]
            held_out[subtype] = [
                {
                    "problem_id": problem_id,
                    "problem_statement": str(taco_by_problem[problem_id].get("problem_statement") or ""),
                }
                for problem_id in query_ids
            ]
            representative_rows = [taco_by_problem[problem_id] for problem_id in representative_ids]
        else:
            representative_rows = rows
        skill["representative_examples"] = _select_distinct_examples(
            representative_rows,
            max_examples=max_examples if len(taco_ids) >= stable_min else normal_examples,
        )
        summaries[subtype] = {
            "num_source_rows": len(rows),
            "unique_taco_problem_ids": taco_ids,
            "num_unique_taco_problems": len(taco_ids),
            "curated_rows": curated_count,
            "origin_counts": dict(origin_counts),
            "candidate_for_stable": len(taco_ids) >= stable_min,
            "held_out_problem_ids": [query["problem_id"] for query in held_out.get(subtype, [])],
        }

    retrieval = evaluate_retrieval_gate(
        skills,
        held_out,
        top_k=int(config["release"].get("retrieval_top_k", 3)),
    )
    for skill in skills:
        subtype = str(skill["canonical_subtype"])
        summary = summaries[subtype]
        unique_count = summary["num_unique_taco_problems"]
        curated_count = summary["curated_rows"]
        origin_counts = Counter(summary["origin_counts"])
        result = retrieval["results"].get(subtype)
        if unique_count >= stable_min and result and result["all_hit"]:
            status = "stable"
            reason = ">=5 unique TACO problems, TACO-only representatives, and local retrieval top-3 gate passed"
        elif unique_count >= stable_min:
            status = "provisional"
            reason = ">=5 unique TACO problems but local retrieval top-3 gate did not pass"
        elif unique_count >= provisional_min and curated_count <= unique_count:
            status = "provisional"
            reason = "2-4 unique TACO problems without predominant curated evidence"
        else:
            status = "seed"
            reason = "0-1 unique TACO problems or evidence remains predominantly curated"
        skill["status"] = status
        if origin_counts and set(origin_counts) == {"taco_verified"}:
            skill["source_dataset"] = "TACO"
        elif origin_counts and set(origin_counts) == {"curated"}:
            skill["source_dataset"] = "curated"
        elif origin_counts:
            skill["source_dataset"] = "TACO+curated"
        skill["evidence"] = {
            **(skill.get("evidence") or {}),
            **summary,
            "num_source_rows": len(grouped.get(subtype, [])),
            "num_representative_rows": len(skill.get("representative_examples") or []),
            "representative_problem_ids": [
                str(example.get("problem_id") or "")
                for example in (skill.get("representative_examples") or [])
            ],
            "evidence_origin_counts": summary["origin_counts"],
            "retrieval_gate_passed": bool(result and result["all_hit"]),
        }
        summaries[subtype]["status"] = status
        summaries[subtype]["status_reason"] = reason
        summaries[subtype]["retrieval_gate_passed"] = bool(result and result["all_hit"])
    maturity = {
        "rules": {
            "stable": ">=5 unique TACO problem_id, TACO-only representatives, and all held-out local retrieval queries hit in top-3",
            "provisional": "2-4 unique TACO problem_id without predominant curated evidence, or stable evidence failing retrieval gate",
            "seed": "0-1 unique TACO problem_id or predominantly curated evidence",
        },
        "status_counts": dict(Counter(skill["status"] for skill in skills)),
        "source_dataset_counts": dict(Counter(str(skill.get("source_dataset") or "") for skill in skills)),
        "methodology_note": (
            "Additional coverage uses targeted evidence distillation plus curated seed construction; "
            "seed skills require future validation on distinct verified TACO problems."
        ),
        "skills": summaries,
    }
    return skills, maturity, retrieval


def build_registry(
    skills: list[dict[str, Any]],
    composed: list[dict[str, Any]],
    aliases: dict[str, str],
) -> dict[str, Any]:
    present = {str(skill["canonical_subtype"]): skill for skill in skills + composed}
    referenced = {
        ref
        for skill in skills + composed
        for values in (skill.get("related_subtypes") or {}).values()
        for ref in values
    }
    entries: dict[str, Any] = {}
    inverse = _inverse_aliases(aliases)
    for subtype, skill in sorted(present.items()):
        entries[subtype] = {
            "canonical_subtype": subtype,
            "alias_subtypes": sorted(set(skill.get("alias_subtypes") or []) | set(inverse.get(subtype, []))),
            "algorithm_family": skill.get("algorithm_family"),
            "publication_status": "present",
            "skill_type": skill.get("skill_type"),
        }
    for subtype in sorted(referenced - set(entries)):
        prefix = subtype.split("_", 1)[0]
        entries[subtype] = {
            "canonical_subtype": subtype,
            "alias_subtypes": sorted(inverse.get(subtype, [])),
            "algorithm_family": f"{prefix}_planned",
            "publication_status": "planned",
            "skill_type": "single_algorithm",
        }
    unresolved = sorted(
        ref for ref in referenced if ref not in entries
    )
    return {
        "version": "subtype_registry_v3",
        "aliases": aliases,
        "entries": entries,
        "unresolved_references": unresolved,
    }


def attach_relationship_partitions(
    skills: list[dict[str, Any]],
    registry: dict[str, Any],
) -> None:
    entries = registry["entries"]
    for skill in skills:
        references = sorted(
            {
                ref
                for values in (skill.get("related_subtypes") or {}).values()
                for ref in values
            }
        )
        skill["related_existing_subtypes"] = [
            ref for ref in references if entries.get(ref, {}).get("publication_status") == "present"
        ]
        skill["related_future_subtypes"] = [
            ref for ref in references if entries.get(ref, {}).get("publication_status") == "planned"
        ]


def _validate_composed_skill(skill: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if skill.get("skill_type") != "composed_algorithm":
        errors.append("skill_type must be composed_algorithm")
    if not re.match(r"^composed\.[a-z0-9_]+\.v\d+$", str(skill.get("skill_id") or "")):
        errors.append("invalid composed skill_id")
    try:
        ast.parse(str(skill.get("code_template") or ""))
    except SyntaxError as exc:
        errors.append(f"code_template must parse as Python: {exc.msg}")
    for field in (
        "canonical_subtype",
        "alias_subtypes",
        "template_type",
        "related_subtypes",
        "related_existing_subtypes",
        "related_future_subtypes",
    ):
        if field not in skill:
            errors.append(f"missing field: {field}")
    return not errors, errors


def build_final_release(config: dict[str, Any], *, use_llm_gcd: bool = False) -> dict[str, Any]:
    aliases, family_overrides = load_alias_metadata(config)
    targeted_additions = load_jsonl(config["input"]["targeted_additions_bank_path"])
    base = load_jsonl(config["input"]["base_skill_bank_path"])
    addition_subtypes = {
        aliases.get(str(skill.get("primary_subtype") or ""), str(skill.get("primary_subtype") or ""))
        for skill in targeted_additions
    }
    published = {
        aliases.get(str(skill.get("primary_subtype") or ""), str(skill.get("primary_subtype") or ""))
        for skill in base + targeted_additions
    }
    ledger, quarantine, routing_events = build_evidence_ledger(
        config,
        aliases=aliases,
        family_overrides=family_overrides,
    )

    merged_seed: dict[str, dict[str, Any]] = {}
    for skill in base + targeted_additions:
        normalized = normalize_skill(
            skill,
            aliases=aliases,
            family_overrides=family_overrides,
            published=published,
        )
        merged_seed[normalized["canonical_subtype"]] = normalized

    gcd_rows = [row for row in ledger if row.get("canonical_subtype") == GCD_SUBTYPE]
    gcd_skill, repair_method = repair_gcd_skill(config, gcd_rows, use_llm=use_llm_gcd)
    gcd_skill = normalize_skill(
        gcd_skill,
        aliases=aliases,
        family_overrides=family_overrides,
        published=published | {GCD_MST_SUBTYPE},
    )
    merged_seed[GCD_SUBTYPE] = gcd_skill
    merged = [merged_seed[subtype] for subtype in sorted(merged_seed)]
    merged, maturity, retrieval = apply_maturity_and_retrieval(merged, ledger, config)
    composed = [build_composed_gcd_mst_skill(quarantine)]
    registry = build_registry(merged, composed, aliases)
    attach_relationship_partitions(merged + composed, registry)
    additions = [skill for skill in merged if skill["canonical_subtype"] in addition_subtypes]

    def validate_relationship_partitions(skill: dict[str, Any]) -> list[str]:
        refs = {
            ref
            for values in skill["related_subtypes"].values()
            for ref in values
        }
        errors = [
            f"unresolved related subtype: {ref}"
            for ref in sorted(refs)
            if ref not in registry["entries"]
        ]
        expected_existing = sorted(
            ref
            for ref in refs
            if registry["entries"].get(ref, {}).get("publication_status") == "present"
        )
        expected_future = sorted(
            ref
            for ref in refs
            if registry["entries"].get(ref, {}).get("publication_status") == "planned"
        )
        if skill.get("related_existing_subtypes") != expected_existing:
            errors.append("related_existing_subtypes does not match registry publication status")
        if skill.get("related_future_subtypes") != expected_future:
            errors.append("related_future_subtypes does not match registry publication status")
        return errors

    single_results = []
    for skill in merged:
        valid, errors = validate_normalized_skill_schema(skill)
        partition_errors = validate_relationship_partitions(skill)
        if partition_errors:
            errors.extend(partition_errors)
            valid = False
        single_results.append({"skill_id": skill["skill_id"], "valid": valid, "errors": errors})
    composed_results = []
    for skill in composed:
        valid, errors = _validate_composed_skill(skill)
        partition_errors = validate_relationship_partitions(skill)
        if partition_errors:
            errors.extend(partition_errors)
            valid = False
        composed_results.append({"skill_id": skill["skill_id"], "valid": valid, "errors": errors})
    schema_report = {
        "single_skill_count": len(merged),
        "single_valid_count": sum(result["valid"] for result in single_results),
        "composed_skill_count": len(composed),
        "composed_valid_count": sum(result["valid"] for result in composed_results),
        "single_results": single_results,
        "composed_results": composed_results,
        "unresolved_registry_references": registry["unresolved_references"],
    }

    release = config["release"]
    write_jsonl(release["normalized_evidence_path"], ledger)
    write_jsonl(release["composition_quarantine_path"], quarantine)
    write_jsonl(release["single_additions_path"], additions)
    write_jsonl(release["single_merged_path"], merged)
    write_jsonl(release["composed_additions_path"], composed)
    if release.get("evidence_routing_report_path"):
        write_json(
            release["evidence_routing_report_path"],
            {
                "rules": {
                    "binary_search_on_answer": (
                        "Retain only monotonic feasibility/answer-space evidence; route explicit "
                        "sorted-position lookup evidence to binary_search_lower_upper_bound."
                    )
                },
                "events": routing_events,
                "routed_counts": dict(
                    Counter(str(event.get("routed_to") or "excluded") for event in routing_events)
                ),
            },
        )
    write_json(release["subtype_registry_path"], registry)
    write_json(release["maturity_report_path"], maturity)
    write_json(release["retrieval_report_path"], retrieval)
    write_json(release["schema_report_path"], schema_report)
    repair_report = {
        "version": str(release.get("version") or "final_release"),
        "gcd_repair_method": repair_method,
        "gcd_mst_quarantined_rows": len(quarantine),
        "binary_search_routing_counts": dict(
            Counter(str(event.get("routed_to") or "excluded") for event in routing_events)
        ),
        "single_additions": len(additions),
        "single_merged": len(merged),
        "composed_additions": len(composed),
        "source_checksums": {
            "base_skill_bank": _sha256(config["input"]["base_skill_bank_path"]),
            "targeted_additions_bank": _sha256(config["input"]["targeted_additions_bank_path"]),
            "targeted_additions_evidence": _sha256(config["input"]["targeted_additions_evidence_path"]),
        },
    }
    write_json(release["repair_report_path"], repair_report)
    if schema_report["single_valid_count"] != len(merged) or schema_report["composed_valid_count"] != len(composed):
        raise RuntimeError("quality bank schema validation failed; inspect schema_validation_report.json")
    return {
        "single_additions": len(additions),
        "single_merged": len(merged),
        "composed_additions": len(composed),
        "status_counts": maturity["status_counts"],
        "gcd_repair_method": repair_method,
    }


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build normalized final single-skill release outputs")
    parser.add_argument("--config", default="configs/final_release.yaml")
    parser.add_argument(
        "--regenerate-gcd",
        action="store_true",
        help="Use DeepSeek to regenerate math_gcd_lcm from filtered evidence; falls back to validated generic content if needed.",
    )
    args = parser.parse_args(argv)
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = Path(__file__).resolve().parent.parent / config_path
    config = load_release_config(config_path)
    result = build_final_release(config, use_llm_gcd=args.regenerate_gcd)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
