from __future__ import annotations

import json

import pytest

from src import main


def _write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row) + "\n" for row in rows),
        encoding="utf-8",
    )


def _config(tmp_path):
    return {
        "output": {
            "output_dir": str(tmp_path / "candidate"),
            "skill_bank_path": str(tmp_path / "candidate" / "bank.jsonl"),
        },
        "release": {
            "baseline_skill_bank_path": str(tmp_path / "released.jsonl"),
            "baseline_snapshot_path": str(tmp_path / "candidate" / "baseline.jsonl"),
            "publish_path": str(tmp_path / "released.jsonl"),
        },
    }


def test_publish_accepts_only_growing_candidate_that_keeps_baseline(tmp_path, monkeypatch):
    config = _config(tmp_path)
    _write_jsonl(tmp_path / "released.jsonl", [{"skill_id": "existing"}])
    _write_jsonl(
        tmp_path / "candidate" / "bank.jsonl",
        [{"skill_id": "existing"}, {"skill_id": "added"}],
    )
    monkeypatch.setattr(
        main,
        "mode_validate",
        lambda _config: {
            "results": [
                {"skill_id": "existing", "valid": True},
                {"skill_id": "added", "valid": True},
            ]
        },
    )

    report = main.mode_publish(config)

    assert report["published"] is True
    assert (tmp_path / "candidate" / "baseline.jsonl").exists()
    assert {row["skill_id"] for row in main.load_jsonl(tmp_path / "released.jsonl")} == {
        "existing",
        "added",
    }


def test_publish_rejects_candidate_that_drops_baseline_skill(tmp_path, monkeypatch):
    config = _config(tmp_path)
    _write_jsonl(
        tmp_path / "released.jsonl",
        [{"skill_id": "existing"}, {"skill_id": "must-remain"}],
    )
    _write_jsonl(
        tmp_path / "candidate" / "bank.jsonl",
        [{"skill_id": "existing"}, {"skill_id": "added"}, {"skill_id": "added-2"}],
    )
    monkeypatch.setattr(
        main,
        "mode_validate",
        lambda _config: {"results": [{"skill_id": "existing", "valid": True}]},
    )

    with pytest.raises(RuntimeError, match="must-remain"):
        main.mode_publish(config)

    assert not (tmp_path / "candidate" / "baseline.jsonl").exists()


def test_merged_input_never_falls_back_to_taco_ledger(tmp_path):
    project_root = tmp_path / "multi_skill_generator"
    taco_ledger = (
        tmp_path
        / "skill_data_factory"
        / "outputs"
        / "multi_algorithm"
        / "pass3_evidence"
        / "composition_rows.jsonl"
    )
    _write_jsonl(taco_ledger, [{"problem_id": "taco"}])
    merged_input = project_root / "missing_merged.jsonl"
    strict_config = {
        "_project_root": str(project_root),
        "input": {"composition_path": str(merged_input)},
    }

    with pytest.raises(FileNotFoundError):
        main._resolve_input_path(strict_config)

    legacy_config = {
        **strict_config,
        "input": {
            "composition_path": str(merged_input),
            "allow_legacy_taco_fallback": True,
        },
    }
    assert main._resolve_input_path(legacy_config) == str(taco_ledger)
