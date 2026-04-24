from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent
ENV_PATH = PROJECT_ROOT / ".env"
ENV_EXAMPLE_PATH = PROJECT_ROOT / ".env.example"

if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)
elif ENV_EXAMPLE_PATH.exists():
    load_dotenv(dotenv_path=ENV_EXAMPLE_PATH)


@dataclass(frozen=True)
class Settings:
    project_root: Path
    inputs_dir: Path
    datasets_dir: Path
    datasets_composite_dir: Path
    generated_dir: Path
    generated_router_dir: Path
    generated_families_dir: Path
    generated_subskills_dir: Path
    generated_manifests_dir: Path
    templates_dir: Path
    prompts_dir: Path
    prompt_template_path: Path
    schemas_dir: Path
    subtype_skill_schema_path: Path
    family_skill_schema_path: Path
    algorithm_router_schema_path: Path
    dataset_manifest_schema_path: Path
    llm_backend: str
    llm_provider_name: str
    llm_api_key: str
    llm_base_url: str
    llm_model: str
    llm_local_model_dir: Path | None
    llm_cache_dir: Path
    llm_device_map: str
    llm_dtype: str
    llm_temperature: float
    llm_max_new_tokens: int
    llm_trust_remote_code: bool
    llm_validation_retries: int


def _resolve_optional_path(raw_value: str | None) -> Path | None:
    if raw_value is None:
        return None
    value = raw_value.strip()
    if not value:
        return None
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = PROJECT_ROOT / candidate
    return candidate.resolve()


def _read_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _read_int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None or not value.strip():
        return default
    return int(value)


def _read_float(name: str, default: float) -> float:
    value = os.getenv(name)
    if value is None or not value.strip():
        return default
    return float(value)


def get_settings() -> Settings:
    generated_dir = PROJECT_ROOT / "generated"
    schemas_dir = PROJECT_ROOT / "schemas"
    llm_backend = os.getenv("LLM_BACKEND", "local_transformers").strip() or "local_transformers"
    normalized_backend = llm_backend.strip().lower().replace("-", "_")
    default_model = "Qwen/Qwen2.5-Coder-7B-Instruct"
    if normalized_backend in {"openai", "openai_compatible", "remote_api"}:
        default_model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    return Settings(
        project_root=PROJECT_ROOT,
        inputs_dir=PROJECT_ROOT / "inputs",
        datasets_dir=PROJECT_ROOT / "datasets",
        datasets_composite_dir=PROJECT_ROOT / "datasets_composite",
        generated_dir=generated_dir,
        generated_router_dir=generated_dir / "router",
        generated_families_dir=generated_dir / "families",
        generated_subskills_dir=generated_dir / "subskills",
        generated_manifests_dir=generated_dir / "manifests",
        templates_dir=PROJECT_ROOT / "templates",
        prompts_dir=PROJECT_ROOT / "prompts",
        prompt_template_path=PROJECT_ROOT / "prompts" / "deepseek_skill_generation_prompt.txt",
        schemas_dir=schemas_dir,
        subtype_skill_schema_path=schemas_dir / "subtype_skill_spec.schema.json",
        family_skill_schema_path=schemas_dir / "family_skill_spec.schema.json",
        algorithm_router_schema_path=schemas_dir / "algorithm_router_spec.schema.json",
        dataset_manifest_schema_path=schemas_dir / "dataset_manifest.schema.json",
        llm_backend=llm_backend,
        llm_provider_name=os.getenv("LLM_PROVIDER_NAME", "LocalTransformers"),
        llm_api_key=os.getenv("LLM_API_KEY", os.getenv("DEEPSEEK_API_KEY", "")),
        llm_base_url=os.getenv("LLM_BASE_URL", "https://api.deepseek.com"),
        llm_model=os.getenv("LLM_MODEL", default_model),
        llm_local_model_dir=_resolve_optional_path(os.getenv("LLM_LOCAL_MODEL_DIR")),
        llm_cache_dir=_resolve_optional_path(os.getenv("LLM_CACHE_DIR")) or (PROJECT_ROOT / ".hf-cache"),
        llm_device_map=os.getenv("LLM_DEVICE_MAP", "auto"),
        llm_dtype=os.getenv("LLM_DTYPE", "auto"),
        llm_temperature=_read_float("LLM_TEMPERATURE", 0.2),
        llm_max_new_tokens=_read_int("LLM_MAX_NEW_TOKENS", 4096),
        llm_trust_remote_code=_read_bool("LLM_TRUST_REMOTE_CODE", False),
        llm_validation_retries=_read_int("LLM_VALIDATION_RETRIES", 2),
    )

