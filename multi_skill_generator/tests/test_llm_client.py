from __future__ import annotations

from src.llm_client import LLMClientPool, _key_label, resolve_api_keys


class _FakeClient:
    def __init__(self, name: str) -> None:
        self.key_label = name

    def generate_json(self, _prompt, **_kwargs):
        return {"client": self.key_label}


def test_resolve_three_api_keys_from_environment(monkeypatch) -> None:
    monkeypatch.setenv("DEEPSEEK_API_KEYS", "key-a, key-b;key-a key-c")
    monkeypatch.setenv("DEEPSEEK_API_KEY", "legacy-single")
    assert resolve_api_keys({"llm": {}}) == ["key-a", "key-b", "key-c"]


def test_round_robin_pool_distributes_requests_across_three_clients() -> None:
    pool = LLMClientPool(
        [_FakeClient("key1"), _FakeClient("key2"), _FakeClient("key3")],
        routing_strategy="round_robin",
    )
    clients = [
        pool.generate_json("prompt", routing_key="same")["client"]
        for _ in range(5)
    ]
    assert clients == ["key1", "key2", "key3", "key1", "key2"]


def test_log_key_label_does_not_contain_key_material() -> None:
    assert _key_label("secret-last-four", 1) == "key2"
