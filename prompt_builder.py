from __future__ import annotations

from pathlib import Path
import json
from typing import Any


def read_text_file(path: Path, label: str) -> str:
    if not path.exists():
        raise FileNotFoundError(f"{label} file not found: {path}")
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        raise ValueError(f"{label} file is empty: {path}")
    return content


def build_prompt(
    prompt_template_path: Path,
    target_kind: str,
    output_schema_name: str,
    output_schema: dict[str, Any],
    cluster_metadata: dict[str, Any] | None = None,
    samples: list[dict[str, Any]] | None = None,
    child_specs: list[dict[str, Any]] | None = None,
) -> str:
    template = read_text_file(prompt_template_path, "prompt template")
    return (
        f"{template}\n\n"
        f"[TARGET_KIND]\n{target_kind}\n\n"
        f"[OUTPUT_SCHEMA_NAME]\n{output_schema_name}\n\n"
        f"[OUTPUT_SCHEMA]\n{json.dumps(output_schema, ensure_ascii=False, indent=2)}\n\n"
        f"[CLUSTER_METADATA]\n{json.dumps(cluster_metadata or {}, ensure_ascii=False, indent=2)}\n\n"
        f"[SAMPLES]\n{json.dumps(samples or [], ensure_ascii=False, indent=2)}\n\n"
        f"[CHILD_SPECS]\n{json.dumps(child_specs or [], ensure_ascii=False, indent=2)}"
    )
