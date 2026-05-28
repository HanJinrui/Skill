import json

from src.prompt_builder import signature_to_skill_id
from src.skill_generator import build_generation_cache_key, fill_program_owned_fields
from src.skill_normalizer import normalize_skill_for_cluster
from src.skill_validator import validate_final_skill, validate_skill_schema


def test_normalize_partial_llm_skill_passes_schema():
    gen_input = {
        "composition_signature": ["sorting_custom_key", "greedy_sorting_order"],
        "composition_relation": "ordered_preprocessing_then_greedy",
        "composition_families": ["sorting", "greedy_algorithms"],
        "status": "stable",
        "support_count": 5,
        "representative_samples": [
            {
                "problem_id": "p1",
                "solution_id": "s1",
                "why_representative": "example",
            }
        ],
        "all_source_rows": [
            {
                "problem_id": f"p{i}",
                "solution_id": "s1",
                "composition_order": ["sorting_custom_key", "greedy_sorting_order"],
                "subtype_confidence": 0.95,
                "evidence_tier": "gold",
            }
            for i in range(5)
        ],
    }
    partial = {
        "skill_id": "TACO_MULTI_ALGO_001",
        "why_multiple_algorithms_are_needed": "Sorting exposes order for greedy.",
        "algorithm_flow": [
            {
                "step_number": 1,
                "algorithm": "sorting_custom_key",
                "role": "sort",
                "input": "items",
                "output": "sorted items",
                "handoff_to_next": "sorted items",
            },
            {
                "step_number": 2,
                "algorithm": "greedy_sorting_order",
                "role": "greedy",
                "input": "sorted items",
                "output": "answer",
            },
        ],
        "state_interface": {
            "input_state": "items",
            "intermediate_state": "sorted",
            "output_state": "answer",
            "handoff_description": "sorted to greedy",
        },
        "composition_invariants": ["order is safe", "greedy is safe"],
        "common_pitfalls": ["bad key", "wrong order", "mutate list"],
        "non_applicability_conditions": ["no order needed", "needs backtracking"],
        "representative_examples": ["bad-model-example"],
        "quality_control": {"final_decision": "accept", "reviewer": "model"},
    }
    skill = normalize_skill_for_cluster(partial, gen_input)
    skill = fill_program_owned_fields(skill, gen_input)
    assert skill["skill_id"] == signature_to_skill_id(
        ("sorting_custom_key", "greedy_sorting_order")
    )
    ok, errs = validate_skill_schema(skill)
    assert ok, errs
    assert skill["representative_examples"] == [
        {
            "problem_id": "p1",
            "solution_id": "s1",
            "why_representative": "Verified evidence of the ordered sorting_custom_key -> greedy_sorting_order handoff.",
        }
    ]
    assert skill["quality_control"] == {}
    validation = validate_final_skill(
        skill,
        gen_input,
        {"validation": {"min_final_score": 0.85, "min_invariants": 2, "min_common_pitfalls": 3}},
        critique={"decision": "pass", "final_score": 0.9},
    )
    assert validation["decision"] == "accept"
    assert skill["quality_control"]["validator"] == "skill_validator.py"
    assert "reviewer" not in skill["quality_control"]


def test_low_support_skill_requires_review():
    gen_input = {
        "composition_signature": ["sorting_custom_key", "greedy_two_pointers"],
        "composition_relation": "ordered_scan_then_two_pointers",
        "composition_families": ["sorting", "greedy_algorithms"],
        "status": "provisional",
        "support_count": 3,
        "representative_samples": [
            {"problem_id": "p1", "solution_id": "s1"},
            {"problem_id": "p2", "solution_id": "s1"},
            {"problem_id": "p3", "solution_id": "s1"},
        ],
        "all_source_rows": [
            {
                "problem_id": f"p{i}",
                "solution_id": "s1",
                "composition_order": ["sorting_custom_key", "greedy_two_pointers"],
                "subtype_confidence": 0.95,
                "evidence_tier": "gold",
            }
            for i in range(1, 4)
        ],
    }
    partial = {
        "skill_name": "Ordered pairing",
        "why_multiple_algorithms_are_needed": "Sorting enables a monotone pairing scan.",
        "core_composition_mechanism": "Create order, then pair candidates with moving pointers.",
        "algorithm_flow": [
            {
                "algorithm": "sorting_custom_key",
                "role": "sort",
                "input": "items",
                "output": "ordered items",
                "handoff_to_next": "pass ordered items",
            },
            {
                "algorithm": "greedy_two_pointers",
                "role": "scan",
                "input": "ordered items",
                "output": "matches",
            },
        ],
        "state_interface": {
            "input_state": "items",
            "intermediate_state": "ordered items",
            "output_state": "matches",
            "handoff_description": "The pointer scan consumes ordered items.",
        },
        "composition_invariants": ["Pointers preserve sorted order.", "Matched prefixes remain feasible."],
        "common_pitfalls": ["wrong key", "wrong pointer move", "unhandled ties"],
        "non_applicability_conditions": ["non-monotone relation", "requires backtracking"],
        "implementation_template": "ordered = sorted(items)\nreturn scan_with_two_pointers(ordered)",
    }
    skill = fill_program_owned_fields(normalize_skill_for_cluster(partial, gen_input), gen_input)
    validation = validate_final_skill(
        skill,
        gen_input,
        {"grouping": {"stable_min_rows": 5}, "validation": {"min_final_score": 0.85}},
    )
    assert validation["decision"] == "provisional_review_required"


def test_mixed_source_evidence_metadata_and_cache_key() -> None:
    rows = [
        {
            "problem_id": "taco1",
            "source_dataset": "TACO",
            "verification_source": "taco-verified",
            "source_problem_fingerprint": "a",
            "composition_order": ["sorting_custom_key", "greedy_sorting_order"],
            "subtype_confidence": 0.95,
            "evidence_tier": "gold",
        },
        {
            "problem_id": "cc1",
            "source_dataset": "CodeContests",
            "source_language": "PYTHON3",
            "verification_source": "codecontests-local-python3",
            "source_problem_fingerprint": "b",
            "composition_order": ["sorting_custom_key", "greedy_sorting_order"],
            "subtype_confidence": 0.96,
            "evidence_tier": "gold",
        },
    ]
    gen_input = {
        "composition_signature": ["sorting_custom_key", "greedy_sorting_order"],
        "composition_relation": "ordered_preprocessing_then_greedy",
        "composition_families": ["sorting", "greedy_algorithms"],
        "status": "provisional",
        "support_count": 2,
        "representative_samples": [{"problem_id": "cc1", "solution_id": "s0"}],
        "all_source_rows": rows,
    }
    skill = fill_program_owned_fields(normalize_skill_for_cluster({}, gen_input), gen_input)
    assert skill["source_dataset"] == "TACO+CodeContests"
    assert skill["evidence"]["source_dataset_counts"] == {"TACO": 1, "CodeContests": 1}
    assert skill["evidence"]["source_language_counts"] == {"PYTHON3": 1}
    assert skill["evidence"]["num_unique_source_problems"] == 2
    key_one = build_generation_cache_key(gen_input)
    changed = {**gen_input, "all_source_rows": [{**rows[1], "source_problem_fingerprint": "changed"}]}
    key_two = build_generation_cache_key(changed)
    assert key_one["source_dataset"] == "TACO+CodeContests"
    assert key_one["evidence_digest"] != key_two["evidence_digest"]


def test_normalize_from_cached_like_payload():
    cache_path = (
        "outputs/cache/multi_skill/67/67debf674b7e5181ff4b03ebeabf5f17705214f0b4700e71f1bfde5b4d052501.json"
    )
    try:
        payload = json.loads(open(cache_path, encoding="utf-8").read())
    except FileNotFoundError:
        return
    raw = json.loads(payload["text"])
    gen_input = {
        "composition_signature": raw["composition_signature"],
        "composition_relation": raw["composition_relation"],
        "composition_families": raw["composition_families"],
        "status": "stable",
        "representative_samples": raw.get("representative_examples", []),
        "all_source_rows": [],
    }
    skill = normalize_skill_for_cluster(raw, gen_input)
    ok, errs = validate_skill_schema(skill)
    assert ok, errs
