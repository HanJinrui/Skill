"""Settings for skill_data_factory."""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

from sdf.shared.bootstrap import FACTORY_ROOT

_ENV_PATH = FACTORY_ROOT / ".env"
_RAG_ENV = (FACTORY_ROOT / ".." / "rag_experiment" / ".env").resolve()

if _ENV_PATH.exists():
    load_dotenv(_ENV_PATH)
elif _RAG_ENV.exists():
    load_dotenv(_RAG_ENV)


def _env(name: str, default: str | None = None) -> str | None:
    v = os.getenv(name)
    if v is None:
        return default
    s = v.strip()
    return s if s else default


def _env_float(name: str, default: float) -> float:
    raw = _env(name)
    return float(raw) if raw is not None else default


def _env_int(name: str, default: int) -> int:
    raw = _env(name)
    return int(raw) if raw is not None else default


def _env_bool(name: str, default: bool) -> bool:
    raw = _env(name)
    if raw is None:
        return default
    return raw.lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class DeepSeekConfig:
    api_key: str
    api_keys: tuple[str, ...]
    base_url: str
    model: str
    temperature: float
    max_tokens: int
    timeout: float


@dataclass(frozen=True)
class Settings:
    factory_root: Path
    config_path: Path
    output_dir: Path
    prompts_dir: Path
    reports_dir: Path
    cache_dir: Path
    config: dict[str, Any]
    deepseek: DeepSeekConfig

    def track_dir(self, track: str, pass_name: str) -> Path:
        return self.output_dir / track / pass_name

    def pass1_dir(self, track: str = "_shared") -> Path:
        if track == "_shared":
            return self.output_dir / "pass1_manifest"
        return self.track_dir(track, "pass1_manifest")

    def pass2_dir(self, track: str) -> Path:
        return self.track_dir(track, "pass2_label")

    def pass3_dir(self, track: str) -> Path:
        return self.track_dir(track, "pass3_evidence")


def _resolve_from_factory(raw: str | Path | None, default: Path) -> Path:
    if raw is None or not str(raw).strip():
        return default
    candidate = Path(raw)
    if not candidate.is_absolute():
        candidate = FACTORY_ROOT / candidate
    return candidate.resolve()


def _deepseek_api_keys() -> tuple[str, ...]:
    candidates: list[str] = []
    raw = _env("DEEPSEEK_API_KEYS", "") or ""
    candidates.extend(part for part in re.split(r"[\s,;]+", raw) if part)
    for index in range(1, 4):
        key = _env(f"DEEPSEEK_API_KEY_{index}", "") or ""
        if key:
            candidates.append(key)
    if not candidates:
        single = _env("DEEPSEEK_API_KEY", "") or ""
        if single:
            candidates.append(single)
    return tuple(dict.fromkeys(candidates))


def get_settings(config_path: str | Path | None = None) -> Settings:
    resolved_config = _resolve_from_factory(config_path, FACTORY_ROOT / "config.yaml")
    with open(resolved_config, "r", encoding="utf-8") as fh:
        config = yaml.safe_load(fh) or {}
    factory_root = FACTORY_ROOT
    paths = config.get("paths") or {}
    output_dir = _resolve_from_factory(paths.get("output_dir"), factory_root / "outputs")
    prompts_dir = _resolve_from_factory(paths.get("prompts_dir"), factory_root / "prompts")
    cache_dir = _resolve_from_factory(paths.get("cache_dir"), factory_root / "cache")
    deepseek_api_keys = _deepseek_api_keys()
    return Settings(
        factory_root=factory_root,
        config_path=resolved_config,
        output_dir=output_dir,
        prompts_dir=prompts_dir,
        reports_dir=output_dir / "reports",
        cache_dir=cache_dir,
        config=config,
        deepseek=DeepSeekConfig(
            api_key=deepseek_api_keys[0] if deepseek_api_keys else "",
            api_keys=deepseek_api_keys,
            base_url=_env("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1") or "https://api.deepseek.com/v1",
            model=_env("DEEPSEEK_MODEL", "deepseek-v4-pro") or "deepseek-v4-pro",
            temperature=_env_float("DEEPSEEK_TEMPERATURE", 0.0),
            max_tokens=_env_int("DEEPSEEK_MAX_TOKENS", 2048),
            timeout=_env_float("DEEPSEEK_TIMEOUT", 180.0),
        ),
    )


def cfg_section(settings: Settings, name: str) -> dict[str, Any]:
    raw = settings.config.get(name)
    return dict(raw) if isinstance(raw, dict) else {}
