from apps.api.core.config import settings

from packages.llm_router.gemini_embeddings import (
    GeminiEmbeddingProvider
)

from packages.llm_router.gemini_chat import (
    GeminiChatProvider
)

from packages.llm_router.deepseek_chat import (
    DeepSeekChatProvider
)

from packages.llm_router.deepseek_embeddings import (
    DeepSeekEmbeddingProvider
)


def get_embedding_provider():

    provider = settings.EMBEDDING_PROVIDER

    if provider == "gemini":
        return GeminiEmbeddingProvider()

    if provider == "deepseek":
        return DeepSeekEmbeddingProvider()

    raise Exception("Invalid embedding provider")


def get_chat_provider():

    provider = settings.CHAT_PROVIDER or settings.EMBEDDING_PROVIDER

    if provider == "gemini":
        return GeminiChatProvider()

    if provider == "deepseek":
        return DeepSeekChatProvider()

    raise Exception("Invalid chat provider")
