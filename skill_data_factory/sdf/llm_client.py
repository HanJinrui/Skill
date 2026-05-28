"""Bridge factory settings to rag_experiment DeepSeek client."""
from __future__ import annotations

import threading
from typing import Any

from sdf.factory_settings import Settings
from sdf.shared import bootstrap  # noqa: F401

from src.llm import build_deepseek_client
from src.settings import DeepSeekConfig as RagDeepSeekConfig


class FactoryDeepSeekPool:
    """Distribute independent labeling requests across configured API keys."""

    def __init__(self, clients: list[Any]) -> None:
        if not clients:
            raise ValueError("FactoryDeepSeekPool requires at least one client")
        self._clients = clients
        self._lock = threading.Lock()
        self._next_index = 0
        self.model = clients[0].model
        self.num_clients = len(clients)

    def chat_json(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        with self._lock:
            client = self._clients[self._next_index % len(self._clients)]
            self._next_index += 1
        return client.chat_json(*args, **kwargs)


def build_factory_deepseek(settings: Settings):
    d = settings.deepseek
    keys = list(d.api_keys) or [d.api_key]
    clients = [
        build_deepseek_client(
            RagDeepSeekConfig(
                api_key=api_key,
                base_url=d.base_url,
                model=d.model,
                temperature=d.temperature,
                max_tokens=d.max_tokens,
                timeout=d.timeout,
                response_format_json=True,
                max_retries=2,
            )
        )
        for api_key in keys
    ]
    if len(clients) == 1:
        client = clients[0]
        client.num_clients = 1
        return client
    return FactoryDeepSeekPool(clients)
