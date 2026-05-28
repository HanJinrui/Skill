from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


def load_jsonl(
    path: str | Path,
    *,
    bad_lines_path: str | Path | None = None,
) -> list[dict[str, Any]]:
    path = Path(path)
    rows: list[dict[str, Any]] = []
    bad_path = Path(bad_lines_path) if bad_lines_path else path.parent / "bad_json_lines.jsonl"
    bad_path.parent.mkdir(parents=True, exist_ok=True)
    bad_written = bad_path.exists() and bad_path.stat().st_size > 0

    with open(path, "r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, start=1):
            raw = line.strip()
            if not raw:
                continue
            try:
                obj = json.loads(raw)
            except json.JSONDecodeError as exc:
                entry = {
                    "row_index": line_no,
                    "raw_line": raw[:2000],
                    "error": str(exc),
                }
                mode = "a" if bad_written else "w"
                with open(bad_path, mode, encoding="utf-8") as bad_fh:
                    bad_fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
                bad_written = True
                continue
            if not isinstance(obj, dict):
                entry = {"row_index": line_no, "error": "line is not a JSON object"}
                mode = "a" if bad_written else "w"
                with open(bad_path, mode, encoding="utf-8") as bad_fh:
                    bad_fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
                bad_written = True
                continue
            obj["row_index"] = line_no
            rows.append(obj)
    return rows


def write_jsonl(path: str | Path, rows: list[dict[str, Any]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def load_yaml(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return data if isinstance(data, dict) else {}


def write_json(path: str | Path, obj: Any) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def resolve_path(base: Path, raw: str) -> Path:
    candidate = Path(raw)
    if candidate.is_absolute():
        return candidate
    return (base / candidate).resolve()
