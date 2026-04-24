from __future__ import annotations

from pathlib import Path
from typing import Protocol


class _RenderableSpec(Protocol):
    files: list


class SkillRenderer:
    def __init__(self, templates_dir: Path) -> None:
        self.templates_dir = templates_dir

    def render_to_directory(self, spec: _RenderableSpec, output_dir: Path) -> list[Path]:
        output_dir.mkdir(parents=True, exist_ok=True)
        written_paths: list[Path] = []
        for file_spec in spec.files:
            target = output_dir / file_spec.path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(file_spec.content.rstrip() + "\n", encoding="utf-8")
            written_paths.append(target)
        return written_paths
