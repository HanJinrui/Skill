"""Local Qwen client and schema-controlled model-call helper."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any, Protocol, TypeVar

from .config import Settings
from .schemas import ContractModel, StructuredOutputError, parse_contract


class LanguageModel(Protocol):
    model_name: str

    def generate(
        self,
        system: str,
        user: str,
        *,
        temperature: float,
        top_p: float = 0.95,
        max_new_tokens: int,
        seed: int | None = None,
    ) -> str: ...


class QwenLocalClient:
    """Lazily load Qwen2.5-Coder for standalone local inference."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.model_name = settings.model_ref()
        self._model: Any = None
        self._tokenizer: Any = None
        self._device: Any = None

    def _load(self) -> None:
        if self._model is not None:
            return
        try:
            import torch
            from transformers import AutoModelForCausalLM, AutoTokenizer
        except ImportError as exc:
            raise RuntimeError("Install torch and transformers to run Qwen inference.") from exc
        cfg = self.settings.data["model"]
        dtype_raw = str(cfg.get("dtype", "auto")).lower()
        dtypes = {
            "float16": torch.float16,
            "fp16": torch.float16,
            "bfloat16": torch.bfloat16,
            "bf16": torch.bfloat16,
            "float32": torch.float32,
            "fp32": torch.float32,
        }
        dtype = dtypes.get(dtype_raw, "auto")
        ref = self.model_name
        is_local = Path(ref).is_dir()
        self._tokenizer = AutoTokenizer.from_pretrained(
            ref,
            local_files_only=is_local,
            trust_remote_code=bool(cfg.get("trust_remote_code", False)),
        )
        self._model = AutoModelForCausalLM.from_pretrained(
            ref,
            dtype=dtype,
            device_map=str(cfg.get("device_map", "auto")),
            local_files_only=is_local,
            trust_remote_code=bool(cfg.get("trust_remote_code", False)),
        )
        self._model.eval()
        self._device = next(self._model.parameters()).device

    def generate(
        self,
        system: str,
        user: str,
        *,
        temperature: float,
        top_p: float = 0.95,
        max_new_tokens: int,
        seed: int | None = None,
    ) -> str:
        self._load()
        assert self._model is not None and self._tokenizer is not None
        import torch

        messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
        rendered = self._tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self._tokenizer(rendered, return_tensors="pt").to(self._device)
        if seed is not None:
            torch.manual_seed(seed)
            if torch.cuda.is_available():
                torch.cuda.manual_seed_all(seed)
        kwargs: dict[str, Any] = {
            "max_new_tokens": int(max_new_tokens),
            "do_sample": float(temperature) > 0,
            "pad_token_id": self._tokenizer.eos_token_id,
        }
        if kwargs["do_sample"]:
            kwargs.update({"temperature": float(temperature), "top_p": float(top_p)})
        else:
            # The bundled generation_config enables sampling by default. Clear
            # its sampling-only defaults for deterministic profiler/gate/plan calls.
            kwargs.update({"temperature": None, "top_p": None, "top_k": None})
        with torch.no_grad():
            output = self._model.generate(**inputs, **kwargs)
        generated = output[0, inputs["input_ids"].shape[1] :]
        return str(self._tokenizer.decode(generated, skip_special_tokens=True))


T = TypeVar("T", bound=ContractModel)


def generate_contract(
    llm: LanguageModel,
    *,
    system: str,
    user: str,
    contract: type[T],
    temperature: float,
    max_new_tokens: int,
    retries: int,
    semantic_validator: Callable[[T], None] | None = None,
) -> T:
    prompt = user
    last_error = ""
    for attempt in range(retries + 1):
        response = llm.generate(
            system,
            prompt,
            temperature=temperature if attempt == 0 else 0.0,
            max_new_tokens=max_new_tokens,
        )
        try:
            parsed = parse_contract(response, contract)
            assert isinstance(parsed, contract)
            if semantic_validator is not None:
                semantic_validator(parsed)
            return parsed
        except (StructuredOutputError, ValueError) as exc:
            last_error = str(exc)
            prompt = (
                user
                + "\n\nYour prior output failed validation. Return a corrected JSON object only.\n"
                + f"Validation error: {last_error}\nPrior output:\n{response[:3000]}"
            )
    raise StructuredOutputError(f"{contract.__name__} remained invalid after repair: {last_error}")
