from __future__ import annotations

from pathlib import Path

from config import Settings
from llm_client import (
    LocalTransformersClient,
    ModelClientError,
    OpenAICompatibleClient as _RemoteOpenAICompatibleClient,
    build_model_client,
    download_local_model,
)


class OpenAICompatibleClient(_RemoteOpenAICompatibleClient):
    def __new__(cls, settings: Settings):
        if cls is OpenAICompatibleClient:
            return build_model_client(settings)
        return super().__new__(cls)


DeepSeekClient = OpenAICompatibleClient
DeepSeekClientError = ModelClientError


__all__ = [
    "DeepSeekClient",
    "DeepSeekClientError",
    "LocalTransformersClient",
    "ModelClientError",
    "OpenAICompatibleClient",
    "build_model_client",
    "download_local_model",
    "Path",
]
