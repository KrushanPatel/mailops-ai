from apps.api.core.config import settings

from packages.llm_router.gemini_embeddings import (
    GeminiEmbeddingProvider
)

from packages.llm_router.gemini_chat import (
    GeminiChatProvider
)


def get_embedding_provider():

    provider = settings.EMBEDDING_PROVIDER

    if provider == "gemini":
        return GeminiEmbeddingProvider()

    raise Exception("Invalid embedding provider")


def get_chat_provider():

    provider = settings.EMBEDDING_PROVIDER

    if provider == "gemini":
        return GeminiChatProvider()

    raise Exception("Invalid chat provider")
