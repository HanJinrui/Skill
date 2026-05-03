"""Centralised configuration loader.

Reads `.env` (via python-dotenv) for secrets + runtime knobs, and `config.yaml`
for experiment configuration. Nothing in this module should read environment
variables directly except through the `get_settings()` function.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PARENT_ROOT = PROJECT_ROOT.parent
_ENV_PATH = PROJECT_ROOT / ".env"
_ENV_EXAMPLE = PROJECT_ROOT / ".env.example"

if _ENV_PATH.exists():
    load_dotenv(dotenv_path=_ENV_PATH)
elif _ENV_EXAMPLE.exists():
    load_dotenv(dotenv_path=_ENV_EXAMPLE)


def _env(name: str, default: str | None = None) -> str | None:
    value = os.getenv(name)
    if value is None:
        return default
    stripped = value.strip()
    return stripped if stripped else default


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
class GLMConfig:
    api_key: str
    base_url: str
    model: str
    temperature: float
    max_tokens: int
    timeout: float


@dataclass(frozen=True)
class DeepSeekConfig:
    api_key: str
    base_url: str
    model: str
    temperature: float
    max_tokens: int
    timeout: float


@dataclass(frozen=True)
class QwenConfig:
    local_model_dir: Path | None
    model_id: str
    device_map: str
    dtype: str
    temperature: float
    top_p: float
    max_new_tokens: int
    trust_remote_code: bool


@dataclass(frozen=True)
class EmbedConfig:
    model: str
    device: str


@dataclass(frozen=True)
class Settings:
    project_root: Path
    parent_root: Path
    output_dir: Path
    cache_dir: Path
    prompts_dir: Path
    reports_dir: Path
    taco_tests_path: Path
    glm: GLMConfig
    deepseek: DeepSeekConfig
    qwen: QwenConfig
    embed: EmbedConfig
    config: dict[str, Any] = field(default_factory=dict)

    @property
    def core_families(self) -> list[str]:
        return list(self.config["experiment"]["core_families"])

    @property
    def top_n_per_family(self) -> int:
        return int(self.config["experiment"]["top_n_per_family"])

    @property
    def parent_datasets_dir(self) -> Path:
        raw = self.config["paths"]["parent_datasets_dir"]
        p = Path(raw)
        return (self.project_root / p).resolve() if not p.is_absolute() else p

    def stage_dir(self, stage: str) -> Path:
        p = self.output_dir / stage
        p.mkdir(parents=True, exist_ok=True)
        return p


def _resolve_path(raw: str | None) -> Path | None:
    if raw is None:
        return None
    p = Path(raw)
    if not p.is_absolute():
        p = PROJECT_ROOT / p
    return p


def _load_config_yaml() -> dict[str, Any]:
    path = PROJECT_ROOT / "config.yaml"
    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"config.yaml must be a mapping, got {type(data)}")
    return data


def get_settings() -> Settings:
    config = _load_config_yaml()
    output_dir = _resolve_path(_env("RAG_OUTPUT_DIR", "outputs")) or (PROJECT_ROOT / "outputs")
    cache_dir = _resolve_path(_env("RAG_CACHE_DIR", ".cache")) or (PROJECT_ROOT / ".cache")
    prompts_dir = PROJECT_ROOT / "prompts"
    reports_dir = PARENT_ROOT / "reports"
    taco_tests_path = _resolve_path(_env("RAG_TACO_TESTS_PATH", "outputs/stage_a/taco_tests.jsonl")) or (
        output_dir / "stage_a" / "taco_tests.jsonl"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    glm = GLMConfig(
        api_key=_env("ZHIPU_API_KEY", "") or "",
        base_url=_env("GLM_BASE_URL", "https://open.bigmodel.cn/api/paas/v4/") or "https://open.bigmodel.cn/api/paas/v4/",
        model=_env("GLM_MODEL", "glm-4.7") or "glm-4.7",
        temperature=_env_float("GLM_TEMPERATURE", 0.1),
        max_tokens=_env_int("GLM_MAX_TOKENS", 4096),
        timeout=_env_float("GLM_TIMEOUT", 120.0),
    )
    deepseek_base_url = _env("GLM_BASE_URL", "https://api.deepseek.com/v1") or "https://api.deepseek.com/v1"
    deepseek_model = _env("GLM_MODEL", "deepseek-chat") or "deepseek-chat"
    deepseek = DeepSeekConfig(
        api_key=_env("DEEPSEEK_API_KEY", _env("ZHIPU_API_KEY", "") or "") or "",
        base_url=_env("DEEPSEEK_BASE_URL", deepseek_base_url) or deepseek_base_url,
        model=_env("DEEPSEEK_MODEL", deepseek_model) or deepseek_model,
        temperature=_env_float("DEEPSEEK_TEMPERATURE", _env_float("GLM_TEMPERATURE", 0.1)),
        max_tokens=_env_int("DEEPSEEK_MAX_TOKENS", _env_int("GLM_MAX_TOKENS", 4096)),
        timeout=_env_float("DEEPSEEK_TIMEOUT", _env_float("GLM_TIMEOUT", 120.0)),
    )
    qwen = QwenConfig(
        local_model_dir=_resolve_path(_env("QWEN_LOCAL_MODEL_DIR")),
        model_id=_env("QWEN_MODEL_ID", "Qwen/Qwen2.5-Coder-7B-Instruct") or "Qwen/Qwen2.5-Coder-7B-Instruct",
        device_map=_env("QWEN_DEVICE_MAP", "auto") or "auto",
        dtype=_env("QWEN_DTYPE", "auto") or "auto",
        temperature=_env_float("QWEN_TEMPERATURE", 0.8),
        top_p=_env_float("QWEN_TOP_P", 0.95),
        max_new_tokens=_env_int("QWEN_MAX_NEW_TOKENS", 2048),
        trust_remote_code=_env_bool("QWEN_TRUST_REMOTE_CODE", False),
    )
    embed = EmbedConfig(
        model=_env("EMBED_MODEL", "BAAI/bge-base-en-v1.5") or "BAAI/bge-base-en-v1.5",
        device=_env("EMBED_DEVICE", "cpu") or "cpu",
    )

    return Settings(
        project_root=PROJECT_ROOT,
        parent_root=PARENT_ROOT,
        output_dir=output_dir,
        cache_dir=cache_dir,
        prompts_dir=prompts_dir,
        reports_dir=reports_dir,
        taco_tests_path=taco_tests_path,
        glm=glm,
        deepseek=deepseek,
        qwen=qwen,
        embed=embed,
        config=config,
    )
