"""Configuration for the standalone skill router MVP."""
from __future__ import annotations

import copy
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = PACKAGE_ROOT.parent
DEFAULT_CONFIG_PATH = PACKAGE_ROOT / "config.yaml"

load_dotenv(PACKAGE_ROOT / ".env", override=False)


def _merge(base: dict[str, Any], patch: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(base)
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _merge(out[key], value)
        else:
            out[key] = copy.deepcopy(value)
    return out


@dataclass(frozen=True)
class Settings:
    config_path: Path
    package_root: Path
    workspace_root: Path
    data: dict[str, Any]

    def section(self, key: str) -> dict[str, Any]:
        return dict(self.data.get(key) or {})

    def path(self, key: str, *, create: bool = False) -> Path:
        raw = str(self.data["paths"][key])
        path = Path(raw).expanduser()
        if not path.is_absolute():
            path = (self.package_root / path).resolve()
        if create:
            path.mkdir(parents=True, exist_ok=True)
        return path

    @property
    def bank_version(self) -> str:
        return str(self.data["experiment"]["bank_version"])

    @property
    def seed(self) -> int:
        return int(self.data["experiment"].get("seed", 0))

    def model_ref(self) -> str:
        raw = str(os.getenv("SKILL_ROUTER_QWEN_LOCAL_MODEL_DIR", "") or self.data["model"].get("local_model_dir", "")).strip()
        if raw:
            path = Path(raw).expanduser()
            if not path.is_absolute():
                path = (self.package_root / path).resolve()
            if path.exists():
                return str(path)
        return str(os.getenv("SKILL_ROUTER_QWEN_MODEL_ID", "") or self.data["model"]["model_id"])


def load_settings(config_path: str | Path | None = None, *, overrides: dict[str, Any] | None = None) -> Settings:
    path = Path(config_path).expanduser().resolve() if config_path else DEFAULT_CONFIG_PATH
    with path.open("r", encoding="utf-8") as fh:
        raw = yaml.safe_load(fh) or {}
    if not isinstance(raw, dict):
        raise ValueError(f"Configuration must be a mapping: {path}")
    data = _merge(raw, overrides or {})
    return Settings(
        config_path=path,
        package_root=PACKAGE_ROOT,
        workspace_root=WORKSPACE_ROOT,
        data=data,
    )
