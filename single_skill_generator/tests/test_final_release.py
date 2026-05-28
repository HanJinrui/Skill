from pathlib import Path

from src.final_release import (
    GCD_MST_SUBTYPE,
    _generic_gcd_fallback,
    apply_maturity_and_retrieval,
    build_registry,
    route_legacy_binary_search_evidence,
    is_gcd_mst_evidence,
    load_alias_metadata,
    load_release_config,
    normalize_skill,
)
from src.skill_validator import validate_normalized_skill_schema


ROOT = Path(__file__).resolve().parent.parent


def _config():
    return load_release_config(ROOT / "configs" / "final_release.yaml")


def _skill(subtype, keyword):
    return {
        "skill_id": f"single.{subtype}.v1",
        "skill_name": subtype,
        "skill_type": "single_algorithm",
        "algorithm_family": "testing",
        "primary_subtype": subtype,
        "canonical_subtype": subtype,
        "alias_subtypes": [],
        "status": "seed",
        "trigger_signals": [keyword],
        "applicability_conditions": [keyword],
        "non_applicability_conditions": ["different mechanism"],
        "core_mechanism": keyword,
        "algorithm_steps": ["apply mechanism"],
        "state_or_structure_design": "state",
        "transition_or_decision_rule": "transition",
        "complexity_pattern": {"time": "O(n)", "space": "O(n)", "notes": ""},
        "code_template": "def solve(values):\n    return values\n",
        "template_type": "executable_python",
        "common_pitfalls": ["wrong mechanism"],
        "retrieval_keywords": [keyword],
        "related_subtypes": {
            "similar": [],
            "prerequisite": [],
            "often_combined_with": [],
            "should_not_confuse_with": [],
        },
        "related_existing_subtypes": [],
        "related_future_subtypes": [],
    }


def test_gcd_mst_evidence_is_not_generic_gcd():
    row = {
        "problem_id": "taco_train_006404__6404",
        "core_mechanism_summary": "Use DSU for a minimum spanning tree with gcd edges.",
    }
    assert is_gcd_mst_evidence(row)
    assert GCD_MST_SUBTYPE == "graph_gcd_mst_dsu"


def test_binary_answer_evidence_routes_ordered_lookup_away_from_answer_search():
    ordered = {
        "core_mechanism_summary": "Sort values, then binary search to find the rightmost base."
    }
    feasibility = {
        "core_mechanism_summary": "Binary search on minimum required capacity with feasibility check."
    }
    assert route_legacy_binary_search_evidence(ordered)[0] == "binary_search_lower_upper_bound"
    assert route_legacy_binary_search_evidence(feasibility)[0] == "binary_search_on_answer"


def test_generic_gcd_repair_is_not_a_graph_composition():
    skill = _generic_gcd_fallback(
        [{"evidence_origin": "curated"}, {"evidence_origin": "taco_verified"}]
    )
    content = (skill["skill_name"] + " " + skill["core_mechanism"]).lower()
    assert "minimum spanning" not in content
    assert "dsu" not in content
    valid, errors = validate_normalized_skill_schema(skill)
    assert valid, errors
    assert skill["template_type"] == "executable_python"


def test_maturity_counts_unique_taco_problems_and_requires_retrieval_hit():
    config = _config()
    skill = _skill("prefix_sum_1d", "prefix sum interval query")
    distractor = _skill("graph_dijkstra_shortest_path", "weighted graph heap")
    ledger = []
    for i in range(5):
        ledger.append(
            {
                "canonical_subtype": "prefix_sum_1d",
                "problem_id": f"p{i}",
                "solution_id": "s0",
                "evidence_origin": "taco_verified",
                "problem_statement": "prefix sum interval query on an array",
                "core_mechanism_summary": "prefix sum interval query",
            }
        )
    ledger.append({**ledger[0], "solution_id": "s1"})
    ledger.append(
        {
            "canonical_subtype": "graph_dijkstra_shortest_path",
            "problem_id": "curated.graph.dijkstra.1",
            "solution_id": "reference",
            "evidence_origin": "curated",
            "problem_statement": "weighted graph shortest path",
            "core_mechanism_summary": "weighted graph heap",
        }
    )
    normalized, maturity, retrieval = apply_maturity_and_retrieval([skill, distractor], ledger, config)
    assert maturity["skills"]["prefix_sum_1d"]["num_unique_taco_problems"] == 5
    assert normalized[0]["status"] == "stable"
    assert normalized[0]["source_dataset"] == "TACO"
    assert normalized[1]["source_dataset"] == "curated"
    assert retrieval["results"]["prefix_sum_1d"]["all_hit"] is True
    assert normalized[0]["evidence"]["num_representative_rows"] == len(
        normalized[0]["representative_examples"]
    )


def test_normalization_repairs_template_and_registry_registers_planned_refs():
    config = _config()
    aliases, family_overrides = load_alias_metadata(config)
    legacy = _skill("ds_heap_priority_queue", "heap")
    legacy.pop("canonical_subtype")
    legacy.pop("alias_subtypes")
    legacy["skill_id"] = "single.ds_heap_priority_queue.v1"
    legacy["code_template"] = "def solve(...):\n    pass\n"
    legacy["related_subtypes"] = {"similar": ["ds_sparse_table"], "should_not_confuse_with": []}
    normalized = normalize_skill(
        legacy,
        aliases=aliases,
        family_overrides=family_overrides,
        published={"ds_heap_priority_queue"},
    )
    valid, errors = validate_normalized_skill_schema(normalized)
    assert valid, errors
    registry = build_registry([normalized], [], aliases)
    assert registry["entries"]["ds_sparse_table"]["publication_status"] == "planned"


def test_family_overrides_are_retrieval_oriented():
    config = _config()
    aliases, family_overrides = load_alias_metadata(config)
    skill = _skill("binary_search_on_answer", "feasibility predicate")
    normalized = normalize_skill(
        skill,
        aliases=aliases,
        family_overrides=family_overrides,
        published={"binary_search_on_answer"},
    )
    assert normalized["algorithm_family"] == "binary_search"
