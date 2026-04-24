"""Simple on-disk key/value cache used by LLM clients.

Keys are derived from (namespace, prompt_version, payload_hash) so that changing
the prompt template automatically invalidates the cache for that task.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


class DiskCache:
    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _key_path(self, namespace: str, key: str) -> Path:
        folder = self.root / namespace / key[:2]
        folder.mkdir(parents=True, exist_ok=True)
        return folder / f"{key}.json"

    @staticmethod
    def make_key(parts: dict[str, Any]) -> str:
        canonical = json.dumps(parts, sort_keys=True, ensure_ascii=False)
        return hashlib.sha1(canonical.encode("utf-8")).hexdigest()

    def get(self, namespace: str, key: str) -> dict[str, Any] | None:
        path = self._key_path(namespace, key)
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return None

    def set(self, namespace: str, key: str, value: dict[str, Any]) -> None:
        path = self._key_path(namespace, key)
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
