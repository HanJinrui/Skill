from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Protocol

from openai import OpenAI

from config import Settings


SYSTEM_PROMPT = (
    "You are a careful algorithm skill generator. "
    "You must obey the requested JSON schema and never wrap the response in markdown."
)

LOCAL_BACKENDS = {"local", "local_hf", "local_transformers", "transformers", "huggingface", "hf_local"}
REMOTE_BACKENDS = {"openai", "openai_compatible", "remote", "remote_api", "iflow", "deepseek", "siliconflow"}


class ModelClientError(RuntimeError):
    pass


class ModelClient(Protocol):
    def generate_skill_payload(self, prompt: str) -> dict[str, Any]:
        ...


class JsonParsingMixin:
    @staticmethod
    def _parse_json(content: str) -> dict[str, Any]:
        normalized = str(content).strip()
        if not normalized:
            raise ModelClientError("Model provider returned empty content.")
        try:
            payload = json.loads(normalized)
        except json.JSONDecodeError:
            payload = JsonParsingMixin._extract_first_json_object(normalized)
        if not isinstance(payload, dict):
            raise ModelClientError("Model provider output must be a JSON object.")
        return payload

    @staticmethod
    def _extract_first_json_object(content: str) -> dict[str, Any]:
        decoder = json.JSONDecoder()
        for index, char in enumerate(content):
            if char != "{":
                continue
            try:
                payload, _ = decoder.raw_decode(content[index:])
            except json.JSONDecodeError:
                continue
            if isinstance(payload, dict):
                return payload
        raise ModelClientError("Model provider returned invalid JSON content.")


class OpenAICompatibleClient(JsonParsingMixin):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        if not settings.llm_api_key:
            raise ModelClientError(
                "LLM_API_KEY is missing. Create a .env file or export the environment variable first."
            )
        self.client = OpenAI(
            api_key=settings.llm_api_key,
            base_url=settings.llm_base_url,
        )

    def generate_skill_payload(self, prompt: str) -> dict[str, Any]:
        response = self.client.chat.completions.create(
            model=self.settings.llm_model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=self.settings.llm_temperature,
            response_format={"type": "json_object"},
        )

        content = self._extract_content(response)
        return self._parse_json(content)

    @staticmethod
    def _extract_content(response: Any) -> str:
        choices = getattr(response, "choices", None)
        if not choices:
            raise ModelClientError("Model provider returned no choices.")
        message = getattr(choices[0], "message", None)
        content = getattr(message, "content", None) if message else None
        if isinstance(content, list):
            fragments = []
            for item in content:
                text = getattr(item, "text", None)
                if text:
                    fragments.append(text)
            content = "".join(fragments)
        if not content or not str(content).strip():
            raise ModelClientError("Model provider returned empty content.")
        return str(content).strip()


class LocalTransformersClient(JsonParsingMixin):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._pipeline: Any | None = None

    def generate_skill_payload(self, prompt: str) -> dict[str, Any]:
        generator = self._ensure_pipeline()
        response = generator(
            [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ]
        )
        content = self._extract_generated_text(response)
        return self._parse_json(content)

    def download_model(self, destination: Path | None = None) -> Path:
        try:
            from huggingface_hub import snapshot_download
        except ImportError as exc:
            raise ModelClientError(
                "Install huggingface_hub before downloading a local model: pip install huggingface_hub"
            ) from exc

        model_id = self._remote_model_id()
        if model_id is None:
            local_model_path = self._local_model_path()
            if local_model_path is None:
                raise ModelClientError("LLM_MODEL must be a Hugging Face repo id or an existing local model path.")
            return local_model_path

        target_dir = destination or self._default_download_dir()
        target_dir.mkdir(parents=True, exist_ok=True)
        snapshot_download(
            repo_id=model_id,
            local_dir=str(target_dir),
            cache_dir=str(self.settings.llm_cache_dir),
        )
        return target_dir.resolve()

    def _ensure_pipeline(self) -> Any:
        if self._pipeline is not None:
            return self._pipeline
        try:
            import torch
            from transformers import pipeline
        except ImportError as exc:
            raise ModelClientError(
                "Install the local inference stack first: pip install transformers accelerate huggingface_hub, "
                "then install a matching torch build for your machine."
            ) from exc

        model_ref = self._model_reference()
        pipeline_kwargs: dict[str, Any] = {
            "task": "text-generation",
            "model": model_ref,
            "tokenizer": model_ref,
            "trust_remote_code": self.settings.llm_trust_remote_code,
        }
        dtype = self._resolve_dtype(torch)
        if dtype is not None:
            pipeline_kwargs["dtype"] = dtype
        device_map = self.settings.llm_device_map.strip() or "auto"
        if device_map.lower() == "cpu":
            pipeline_kwargs["device"] = "cpu"
        else:
            pipeline_kwargs["device_map"] = device_map
        model_kwargs: dict[str, Any] = {}
        if not self._looks_like_local_path(model_ref):
            model_kwargs["cache_dir"] = str(self.settings.llm_cache_dir)
        if model_kwargs:
            pipeline_kwargs["model_kwargs"] = model_kwargs
        try:
            self._pipeline = pipeline(**pipeline_kwargs)
        except Exception as exc:
            raise ModelClientError(
                "Failed to load the local Transformers pipeline. "
                "Check that the model is downloaded, torch matches your hardware, and the dtype/device settings are valid."
            ) from exc

        generation_config = getattr(self._pipeline.model, "generation_config", None)
        if generation_config is not None:
            generation_config.max_new_tokens = self.settings.llm_max_new_tokens
            generation_config.do_sample = self.settings.llm_temperature > 0
            if self.settings.llm_temperature > 0:
                generation_config.temperature = self.settings.llm_temperature
            elif hasattr(generation_config, "temperature"):
                generation_config.temperature = None
            if hasattr(generation_config, "max_length"):
                generation_config.max_length = None
        return self._pipeline

    @staticmethod
    def _extract_generated_text(response: Any) -> str:
        if not isinstance(response, list) or not response:
            raise ModelClientError("Local model returned an unexpected response shape.")
        first = response[0]
        if not isinstance(first, dict) or "generated_text" not in first:
            raise ModelClientError("Local model response does not contain generated_text.")
        generated = first["generated_text"]
        if isinstance(generated, str) and generated.strip():
            return generated.strip()
        if isinstance(generated, list):
            for item in reversed(generated):
                if not isinstance(item, dict):
                    continue
                content = item.get("content")
                if isinstance(content, str) and content.strip():
                    return content.strip()
        raise ModelClientError("Local model returned empty content.")

    def _model_reference(self) -> str:
        local_model_path = self._local_model_path()
        if local_model_path is not None and local_model_path.exists():
            return str(local_model_path)
        model_value = self.settings.llm_model.strip()
        if not model_value:
            raise ModelClientError("LLM_MODEL is missing.")
        if self._looks_like_local_path(model_value):
            return str(Path(model_value).resolve())
        return model_value

    def _local_model_path(self) -> Path | None:
        if self.settings.llm_local_model_dir is not None:
            return self.settings.llm_local_model_dir
        model_value = self.settings.llm_model.strip()
        if not model_value:
            return None
        candidate = Path(model_value)
        if candidate.exists():
            return candidate.resolve()
        return None

    def _remote_model_id(self) -> str | None:
        model_value = self.settings.llm_model.strip()
        if not model_value:
            return None
        if self._looks_like_local_path(model_value):
            return None
        return model_value

    def _default_download_dir(self) -> Path:
        if self.settings.llm_local_model_dir is not None:
            return self.settings.llm_local_model_dir
        return (self.settings.llm_cache_dir / "models" / _sanitize_repo_id(self.settings.llm_model)).resolve()

    @staticmethod
    def _looks_like_local_path(value: str) -> bool:
        if not value:
            return False
        return value.startswith(".") or value.startswith("/") or value.startswith("\\") or (len(value) > 1 and value[1] == ":")

    def _resolve_dtype(self, torch_module: Any) -> Any:
        raw_dtype = self.settings.llm_dtype.strip().lower()
        if not raw_dtype or raw_dtype == "auto":
            if bool(getattr(torch_module.cuda, "is_available", lambda: False)()):
                return "auto"
            return None
        if raw_dtype in {"float16", "fp16", "half"}:
            return torch_module.float16
        if raw_dtype in {"bfloat16", "bf16"}:
            return torch_module.bfloat16
        if raw_dtype in {"float32", "fp32"}:
            return torch_module.float32
        raise ModelClientError(f"Unsupported LLM_DTYPE value: {self.settings.llm_dtype}")


def _sanitize_repo_id(repo_id: str) -> str:
    sanitized = repo_id.replace("/", "__").replace("\\", "__")
    sanitized = sanitized.replace(":", "_").replace("@", "_")
    return sanitized


def normalize_backend_name(raw_backend: str) -> str:
    backend = raw_backend.strip().lower().replace("-", "_")
    if backend in LOCAL_BACKENDS:
        return "local_transformers"
    if backend in REMOTE_BACKENDS:
        return "openai_compatible"
    raise ModelClientError(
        "Unsupported LLM_BACKEND value. Use one of: local_transformers, openai_compatible."
    )


def build_model_client(settings: Settings) -> ModelClient:
    normalized_backend = normalize_backend_name(settings.llm_backend)
    if normalized_backend == "local_transformers":
        return LocalTransformersClient(settings)
    return OpenAICompatibleClient(settings)


def download_local_model(settings: Settings, destination: Path | None = None) -> Path:
    normalized_backend = normalize_backend_name(settings.llm_backend)
    if normalized_backend != "local_transformers":
        raise ModelClientError("download-model is only available when LLM_BACKEND=local_transformers.")
    client = LocalTransformersClient(settings)
    return client.download_model(destination)

