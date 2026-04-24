"""Local Qwen2.5-Coder client using Hugging Face Transformers.

Loaded lazily on first `generate()` call. `n` samples are produced in a single
batched call with `num_return_sequences=n` when GPU memory allows, otherwise
the client transparently falls back to serial generation (n x 1).
"""
from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any

from ..settings import QwenConfig
from .base import LLMError

LOG = logging.getLogger(__name__)

# A conservative memory budget (in GiB) to leave on each candidate GPU when
# filtering busy devices. We need ~14 GiB total to host Qwen-7B in bf16/fp16,
# plus headroom for activations + KV cache. Anything with less free than this
# is likely to OOM mid-generation.
_MIN_FREE_GIB_PER_GPU = 6.0
_MIN_FREE_TOTAL_GIB = 16.0


class QwenLocalClient:
    provider = "qwen_local"

    def __init__(self, config: QwenConfig) -> None:
        self.config = config
        self.model = config.model_id
        self._model = None
        self._tokenizer = None
        self._device = None

    def _model_ref(self) -> str:
        if self.config.local_model_dir is not None and self.config.local_model_dir.exists():
            return str(self.config.local_model_dir)
        return self.config.model_id

    @staticmethod
    def _select_gpus(torch_mod: Any) -> str | None:
        """Return a comma-joined list of GPU indices that currently have enough
        free memory to host the model, or None to let accelerate decide.

        Honours CUDA_VISIBLE_DEVICES if set.
        """
        if not torch_mod.cuda.is_available():
            return None
        cvd = os.environ.get("CUDA_VISIBLE_DEVICES")
        if cvd is not None and cvd.strip():
            return None  # user already pinned
        n = torch_mod.cuda.device_count()
        if n == 0:
            return None
        good: list[tuple[int, float]] = []
        total_free_gib = 0.0
        for i in range(n):
            try:
                free_bytes, _total = torch_mod.cuda.mem_get_info(i)
            except Exception:
                continue
            free_gib = free_bytes / (1024 ** 3)
            total_free_gib += free_gib
            if free_gib >= _MIN_FREE_GIB_PER_GPU:
                good.append((i, free_gib))
        if not good:
            return None
        # If total free across all good GPUs is below threshold, bail and let
        # accelerate try anyway (will likely OOM but we raise a clearer error).
        if sum(g for _, g in good) < _MIN_FREE_TOTAL_GIB:
            LOG.warning(
                "All candidate GPUs report <%.1f GiB free in total; generation may OOM.",
                _MIN_FREE_TOTAL_GIB,
            )
        chosen = ",".join(str(i) for i, _ in good)
        LOG.info(
            "Qwen: restricting to GPUs %s (free: %s); total_free=%.1f GiB",
            chosen,
            ", ".join(f"{i}={g:.1f}GiB" for i, g in good),
            total_free_gib,
        )
        return chosen

    def _load(self) -> None:
        if self._model is not None:
            return
        try:
            import torch
            from transformers import AutoModelForCausalLM, AutoTokenizer
        except ImportError as exc:  # pragma: no cover
            raise LLMError(
                "Install torch + transformers before running Qwen generation."
            ) from exc

        # Pin visible GPUs BEFORE transformers sees them, so device_map=auto
        # doesn't spread onto a busy card (the common 2026-04-23 failure mode).
        chosen = self._select_gpus(torch)
        if chosen is not None:
            os.environ["CUDA_VISIBLE_DEVICES"] = chosen

        ref = self._model_ref()
        dtype_raw = (self.config.dtype or "auto").strip().lower()
        dtype: Any
        if dtype_raw in {"", "auto"}:
            dtype = "auto"
        elif dtype_raw in {"fp16", "float16", "half"}:
            dtype = torch.float16
        elif dtype_raw in {"bf16", "bfloat16"}:
            dtype = torch.bfloat16
        elif dtype_raw in {"fp32", "float32"}:
            dtype = torch.float32
        else:
            raise LLMError(f"unsupported QWEN_DTYPE: {self.config.dtype}")

        tokenizer = AutoTokenizer.from_pretrained(ref, trust_remote_code=self.config.trust_remote_code)
        try:
            model = AutoModelForCausalLM.from_pretrained(
                ref,
                torch_dtype=dtype,
                device_map=self.config.device_map,
                trust_remote_code=self.config.trust_remote_code,
            )
        except torch.cuda.OutOfMemoryError as exc:
            torch.cuda.empty_cache()
            raise LLMError(
                f"CUDA OOM while loading Qwen. Free GPU memory and retry, or set "
                f"CUDA_VISIBLE_DEVICES to a subset of idle GPUs. Original: {exc}"
            ) from exc
        model.eval()
        self._model = model
        self._tokenizer = tokenizer
        self._device = next(model.parameters()).device

    def generate(
        self,
        system: str,
        user: str,
        *,
        temperature: float | None = None,
        top_p: float | None = None,
        max_new_tokens: int | None = None,
        n: int = 1,
        stop: list[str] | None = None,
        seed: int | None = None,
    ) -> list[str]:
        self._load()
        assert self._model is not None and self._tokenizer is not None
        import torch

        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]
        prompt = self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self._tokenizer(prompt, return_tensors="pt").to(self._device)

        if seed is not None:
            torch.manual_seed(seed)
            if torch.cuda.is_available():
                torch.cuda.manual_seed_all(seed)

        t = self.config.temperature if temperature is None else temperature
        tp = self.config.top_p if top_p is None else top_p
        mnt = self.config.max_new_tokens if max_new_tokens is None else max_new_tokens

        do_sample = t > 0

        def _base_kwargs(num_seq: int) -> dict[str, Any]:
            k: dict[str, Any] = {
                "max_new_tokens": mnt,
                "do_sample": do_sample,
                "num_return_sequences": num_seq,
                "pad_token_id": self._tokenizer.eos_token_id,
            }
            if do_sample:
                k["temperature"] = t
                k["top_p"] = tp
            return k

        def _decode(output_ids: Any, input_len: int) -> list[str]:
            out: list[str] = []
            for seq in output_ids:
                new_tokens = seq[input_len:]
                text = self._tokenizer.decode(new_tokens, skip_special_tokens=True)
                out.append(self._apply_stop(text, stop))
            return out

        input_len = inputs["input_ids"].shape[1]

        # First try batched generation for speed. On OOM, fall back to serial
        # n×1 calls with cache-clearing between each; this eliminates batched
        # activation peaks that are the typical cause of mid-run CUDA OOMs.
        try:
            with torch.no_grad():
                output_ids = self._model.generate(**inputs, **_base_kwargs(n))
            return _decode(output_ids, input_len)
        except torch.cuda.OutOfMemoryError:
            LOG.warning(
                "CUDA OOM on batched generate (n=%d); falling back to serial n×1.",
                n,
            )
            torch.cuda.empty_cache()

        completions: list[str] = []
        for i in range(n):
            if seed is not None:
                torch.manual_seed(seed + i)
                if torch.cuda.is_available():
                    torch.cuda.manual_seed_all(seed + i)
            try:
                with torch.no_grad():
                    output_ids = self._model.generate(**inputs, **_base_kwargs(1))
                completions.extend(_decode(output_ids, input_len))
            except torch.cuda.OutOfMemoryError as exc:
                torch.cuda.empty_cache()
                raise LLMError(
                    f"CUDA OOM during generation (serial fallback also failed at sample {i+1}/{n}). "
                    f"A co-tenant is likely holding GPU memory. Original: {exc}"
                ) from exc
            finally:
                # Proactively release the transient KV-cache between samples.
                torch.cuda.empty_cache()
        return completions

    @staticmethod
    def _apply_stop(text: str, stop: list[str] | None) -> str:
        if not stop:
            return text
        cut = len(text)
        for token in stop:
            if not token:
                continue
            idx = text.find(token)
            if 0 <= idx < cut:
                cut = idx
        return text[:cut]


def build_qwen_client(config: QwenConfig) -> QwenLocalClient:
    return QwenLocalClient(config)
