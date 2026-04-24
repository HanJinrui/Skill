from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def package_skill(skill_dir: Path, output_zip: Path) -> Path:
    if not skill_dir.exists():
        raise FileNotFoundError(f"skill directory does not exist: {skill_dir}")
    output_zip.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output_zip, "w", compression=ZIP_DEFLATED) as archive:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file():
                if path.resolve() == output_zip.resolve():
                    continue
                archive.write(path, path.relative_to(skill_dir))
    return output_zip
