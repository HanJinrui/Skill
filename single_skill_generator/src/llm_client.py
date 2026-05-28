from __future__ import annotations

import hashlib
import json
import os
import re
import threading
import time
from pathlib import Path
from typing import Any

from openai import OpenAI


class LLMClientError(RuntimeError):
    pass


class DiskCache:
    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()

    @staticmethod
    def make_key(parts: dict[str, Any]) -> str:
        canonical = json.dumps(parts, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def _path(self, namespace: str, key: str) -> Path:
        folder = self.root / namespace / key[:2]
        folder.mkdir(parents=True, exist_ok=True)
        return folder / f"{key}.json"

    def get(self, namespace: str, key: str) -> dict[str, Any] | None:
        path = self._path(namespace, key)
        if not path.exists():
            return None
        with self._lock:
            try:
                return json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                return None

    def set(self, namespace: str, key: str, value: dict[str, Any]) -> None:
        path = self._path(namespace, key)
        payload = json.dumps(value, ensure_ascii=False, indent=2)
        with self._lock:
            path.write_text(payload, encoding="utf-8")


_LOG_LOCK = threading.Lock()


def resolve_api_keys(config: dict[str, Any]) -> list[str]:
    """Load API keys from config list or env (never log full keys)."""
    lc = config.get("llm", {})
    keys: list[str] = []

    raw_list = lc.get("api_keys")
    if isinstance(raw_list, list):
        keys.extend(str(k).strip() for k in raw_list if str(k).strip())

    env_multi = os.getenv("DEEPSEEK_API_KEYS", "").strip()
    if env_multi:
        for part in re.split(r"[\s,;]+", env_multi):
            part = part.strip()
            if part:
                keys.append(part)

    single = (
        os.getenv("DEEPSEEK_API_KEY")
        or os.getenv("OPENAI_API_KEY")
        or os.getenv("LLM_API_KEY")
        or ""
    ).strip()
    if single and single not in keys:
        keys.append(single)

    # dedupe preserve order
    seen: set[str] = set()
    unique: list[str] = []
    for k in keys:
        if k not in seen:
            seen.add(k)
            unique.append(k)
    return unique


def _key_label(api_key: str, index: int) -> str:
    suffix = api_key[-4:] if len(api_key) >= 4 else "????"
    return f"key{index + 1}:{suffix}"


def _extract_json_object(text: str) -> dict[str, Any]:
    normalized = text.strip()
    if not normalized:
        raise LLMClientError("Empty LLM response")
    try:
        payload = json.loads(normalized)
    except json.JSONDecodeError:
        decoder = json.JSONDecoder()
        for idx, ch in enumerate(normalized):
            if ch != "{":
                continue
            try:
                payload, _ = decoder.raw_decode(normalized[idx:])
            except json.JSONDecodeError:
                continue
            if isinstance(payload, dict):
                return payload
        fenced = re.search(r"```(?:json)?\s*(\{.*\})\s*```", normalized, re.DOTALL)
        if fenced:
            payload = json.loads(fenced.group(1))
            if isinstance(payload, dict):
                return payload
        raise LLMClientError("Could not parse JSON from LLM response")
    if not isinstance(payload, dict):
        raise LLMClientError("LLM response must be a JSON object")
    return payload


class LLMClient:
    def __init__(
        self,
        config: dict[str, Any],
        *,
        project_root: Path,
        api_key: str | None = None,
        cache: DiskCache | None = None,
        log_path: Path | None = None,
        key_label: str = "default",
    ) -> None:
        lc = config.get("llm", {})
        self.provider = str(lc.get("provider", "deepseek")).lower()
        self.model = lc.get("model") or os.getenv("DEEPSEEK_MODEL", "deepseek-v4-pro")
        self.temperature = float(lc.get("temperature", 0.2))
        self.max_tokens = int(lc.get("max_tokens", 8192))
        self.retry_times = int(lc.get("retry_times", 3))
        self.timeout = float(lc.get("timeout", 180.0))
        self.enabled = bool(lc.get("enabled", True))
        self.key_label = key_label

        resolved_key = (api_key or "").strip()
        if not resolved_key:
            keys = resolve_api_keys(config)
            resolved_key = keys[0] if keys else ""

        base_url = (
            lc.get("base_url")
            or os.getenv("DEEPSEEK_BASE_URL")
            or os.getenv("OPENAI_BASE_URL")
            or "https://api.deepseek.com/v1"
        )
        if self.enabled and not resolved_key:
            raise LLMClientError(
                "API key missing. Set DEEPSEEK_API_KEYS, DEEPSEEK_API_KEY, or llm.api_keys in config."
            )

        self._client = OpenAI(api_key=resolved_key, base_url=base_url, timeout=self.timeout)
        cache_dir = project_root / str(lc.get("cache_dir", "outputs/cache"))
        self.cache = cache or DiskCache(cache_dir)
        output_dir = Path(config.get("output", {}).get("output_dir") or (project_root / "outputs"))
        self._log_path = log_path or (output_dir / "logs/llm_generation_log.jsonl")

    def _append_log(self, entry: dict[str, Any]) -> None:
        entry = {**entry, "key_label": self.key_label}
        self._log_path.parent.mkdir(parents=True, exist_ok=True)
        line = json.dumps(entry, ensure_ascii=False) + "\n"
        with _LOG_LOCK:
            with open(self._log_path, "a", encoding="utf-8") as fh:
                fh.write(line)

    def generate(self, prompt: str, *, system: str = "", cache_key: dict[str, Any] | None = None) -> str:
        if not self.enabled:
            raise LLMClientError("LLM is disabled in config")

        namespace = "single_skill"
        key = DiskCache.make_key(cache_key or {"prompt": prompt[:5000]})
        cached = self.cache.get(namespace, key)
        if cached and "text" in cached:
            return str(cached["text"])

        sys_msg = system or (
            "You are an algorithm skill distillation expert. "
            "Respond with strict JSON only, no markdown fences."
        )
        last_err: Exception | None = None
        for attempt in range(1, self.retry_times + 1):
            t0 = time.time()
            try:
                resp = self._client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": sys_msg},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    response_format={"type": "json_object"},
                )
                content = resp.choices[0].message.content or ""
                text = str(content).strip()
                self.cache.set(namespace, key, {"text": text})
                self._append_log(
                    {
                        "cache_key": key,
                        "model": self.model,
                        "attempt": attempt,
                        "latency_s": round(time.time() - t0, 2),
                        "prompt_chars": len(prompt),
                        "response_chars": len(text),
                    }
                )
                return text
            except Exception as exc:
                last_err = exc
                self._append_log(
                    {
                        "cache_key": key,
                        "model": self.model,
                        "attempt": attempt,
                        "error": str(exc),
                    }
                )
                if attempt < self.retry_times:
                    time.sleep(min(2 ** attempt, 8))
        raise LLMClientError(f"LLM call failed after {self.retry_times} retries: {last_err}")

    def generate_json(
        self,
        prompt: str,
        *,
        system: str = "",
        cache_key: dict[str, Any] | None = None,
        routing_key: str | None = None,  # ignored on single client; used by pool
    ) -> dict[str, Any]:
        del routing_key
        return _extract_json_object(self.generate(prompt, system=system, cache_key=cache_key))


class LLMClientPool:
    """Round-robin / sticky routing across multiple API keys with a shared cache."""

    def __init__(self, clients: list[LLMClient], *, max_parallel: int | None = None) -> None:
        if not clients:
            raise LLMClientError("LLMClientPool requires at least one client")
        self._clients = clients
        self.max_parallel = max_parallel or len(clients)
        self.key_labels = [c.key_label for c in clients]

    def client_for(self, routing_key: str) -> LLMClient:
        digest = hashlib.sha256(routing_key.encode("utf-8")).hexdigest()
        idx = int(digest[:8], 16) % len(self._clients)
        return self._clients[idx]

    def generate(
        self,
        prompt: str,
        *,
        system: str = "",
        cache_key: dict[str, Any] | None = None,
        routing_key: str = "default",
    ) -> str:
        return self.client_for(routing_key).generate(
            prompt, system=system, cache_key=cache_key
        )

    def generate_json(
        self,
        prompt: str,
        *,
        system: str = "",
        cache_key: dict[str, Any] | None = None,
        routing_key: str = "default",
    ) -> dict[str, Any]:
        return self.client_for(routing_key).generate_json(
            prompt, system=system, cache_key=cache_key
        )


def build_llm_client(config: dict[str, Any], *, project_root: Path) -> LLMClient | LLMClientPool:
    lc = config.get("llm", {})
    keys = resolve_api_keys(config)
    max_workers = int(lc.get("max_workers", 1))

    if not lc.get("enabled", True):
        return LLMClient(config, project_root=project_root, api_key=keys[0] if keys else "")

    if not keys:
        return LLMClient(config, project_root=project_root)

    cache_dir = project_root / str(lc.get("cache_dir", "outputs/cache"))
    shared_cache = DiskCache(cache_dir)
    output_dir = Path(config.get("output", {}).get("output_dir") or (project_root / "outputs"))
    log_path = output_dir / "logs/llm_generation_log.jsonl"

    if len(keys) == 1 and max_workers <= 1:
        return LLMClient(
            config,
            project_root=project_root,
            api_key=keys[0],
            cache=shared_cache,
            log_path=log_path,
            key_label=_key_label(keys[0], 0),
        )

    clients = [
        LLMClient(
            config,
            project_root=project_root,
            api_key=k,
            cache=shared_cache,
            log_path=log_path,
            key_label=_key_label(k, i),
        )
        for i, k in enumerate(keys)
    ]
    parallel = min(max_workers, len(clients))
    return LLMClientPool(clients, max_parallel=parallel)
