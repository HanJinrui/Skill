from __future__ import annotations

import sys
from dataclasses import replace
from pathlib import Path

FACTORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FACTORY_ROOT))
sys.path.insert(0, str(FACTORY_ROOT.parent / "rag_experiment" / "src"))

from sdf.factory_settings import DeepSeekConfig, get_settings  # noqa: E402
from sdf.llm_client import build_factory_deepseek  # noqa: E402


class _FakeClient:
    model = "model"

    def __init__(self, key: str) -> None:
        self.key = key

    def chat_json(self, *_args, **_kwargs):
        return {"key": self.key}


def test_factory_settings_reads_three_api_keys_without_duplicates(monkeypatch) -> None:
    monkeypatch.setenv("DEEPSEEK_API_KEYS", "key-a,key-b;key-a")
    monkeypatch.setenv("DEEPSEEK_API_KEY_1", "key-c")
    monkeypatch.delenv("DEEPSEEK_API_KEY_2", raising=False)
    monkeypatch.delenv("DEEPSEEK_API_KEY_3", raising=False)
    monkeypatch.setenv("DEEPSEEK_API_KEY", "legacy-single")

    settings = get_settings("configs/codecontests_multi.yaml")

    assert settings.deepseek.api_keys == ("key-a", "key-b", "key-c")
    assert settings.deepseek.api_key == "key-a"


def test_factory_pool_round_robins_across_api_keys(monkeypatch) -> None:
    deepseek = DeepSeekConfig(
        api_key="key-a",
        api_keys=("key-a", "key-b", "key-c"),
        base_url="https://example.invalid/v1",
        model="model",
        temperature=0.0,
        max_tokens=100,
        timeout=1.0,
    )
    settings = replace(get_settings("configs/codecontests_multi.yaml"), deepseek=deepseek)
    monkeypatch.setattr(
        "sdf.llm_client.build_deepseek_client",
        lambda cfg: _FakeClient(cfg.api_key),
    )

    pool = build_factory_deepseek(settings)
    routed = [pool.chat_json(system="", user={})["key"] for _ in range(5)]

    assert pool.num_clients == 3
    assert routed == ["key-a", "key-b", "key-c", "key-a", "key-b"]
