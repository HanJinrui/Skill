import json
from pathlib import Path

from src.additional_evidence import (
    algorithm_index,
    build_curated_rows,
    load_algorithm_catalog,
    load_validated_curated_evidence,
    materialize_solution_candidates,
)
from src.main import load_config, merge_base_and_additional_banks, merge_incremental_rows
from src.prompt_builder import build_generation_prompt


ROOT = Path(__file__).resolve().parent.parent


def _config():
    return load_config(ROOT / "configs" / "final_release.yaml")


def test_priority_catalog_and_curated_templates_cover_all_targets():
    config = _config()
    catalog = load_algorithm_catalog(config)
    entries = load_validated_curated_evidence(config, catalog)
    rows = build_curated_rows(config, catalog, entries)
    assert len(algorithm_index(catalog)) == 35
    assert set(rows) == set(algorithm_index(catalog))
    assert all(len(group) == 5 for group in rows.values())
    assert all(row["evidence_origin"] == "curated" for group in rows.values() for row in group)


def test_prompt_describes_curated_samples_without_claiming_taco():
    config = _config()
    catalog = load_algorithm_catalog(config)
    entries = load_validated_curated_evidence(config, catalog)
    rows = build_curated_rows(config, catalog, entries)["dp_lis"]
    prompt = build_generation_prompt(
        "dp_lis",
        rows,
        config,
        generation_input={"status": "seed"},
    )
    assert "these are not TACO samples" in prompt
    assert '"source_dataset": "curated"' in prompt
    assert '"generation_method": "targeted_evidence_distillation"' in prompt


def test_prompt_marks_mixed_sources_separately():
    config = _config()
    catalog = load_algorithm_catalog(config)
    entries = load_validated_curated_evidence(config, catalog)
    rows = build_curated_rows(config, catalog, entries)["graph_topological_sort"]
    rows[0] = {**rows[0], "evidence_origin": "taco_verified"}
    prompt = build_generation_prompt(
        "graph_topological_sort",
        rows,
        config,
        generation_input={"status": "seed"},
    )
    assert '"source_dataset": "TACO+curated"' in prompt
    assert "curated examples are not TACO samples" in prompt


def test_incremental_and_base_merge_preserve_unrelated_skills_and_replace_alias():
    prior_additions = [{"skill_id": "single.dp_lis.v1", "primary_subtype": "dp_lis", "revision": 1}]
    replacement = [{"skill_id": "single.dp_lis.v1", "primary_subtype": "dp_lis", "revision": 2}]
    assert merge_incremental_rows(prior_additions, replacement) == replacement

    base = [
        {"skill_id": "single.sorting_binary_search_answer.v1", "primary_subtype": "sorting_binary_search_answer"},
        {"skill_id": "single.dp_1d_state.v1", "primary_subtype": "dp_1d_state"},
    ]
    addition = [
        {
            "skill_id": "single.binary_search_on_answer.v1",
            "primary_subtype": "binary_search_on_answer",
            "alias_subtypes": ["sorting_binary_search_answer"],
        }
    ]
    merged = merge_base_and_additional_banks(base, addition)
    assert {row["skill_id"] for row in merged} == {
        "single.dp_1d_state.v1",
        "single.binary_search_on_answer.v1",
    }


def test_materialize_solution_candidates_reads_only_selected_problem(tmp_path):
    source = tmp_path / "solutions.jsonl"
    rows = [
        {"problem_id": "keep", "solution_id": "s0", "solution_code": "def solve_case(): pass"},
        {"problem_id": "ignore", "solution_id": "s1", "solution_code": "def solve_case(): pass"},
    ]
    source.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")
    selected = materialize_solution_candidates(
        {"dp_lis": [{"problem_id": "keep"}]},
        source,
        {"additional": {"max_verified_candidates_per_skill": 8}},
    )
    assert [row["problem_id"] for row in selected["dp_lis"]] == ["keep"]
