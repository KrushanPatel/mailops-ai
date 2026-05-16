from apps.api.core.config import settings

from packages.llm_router.gemini_embeddings import (
    GeminiEmbeddingProvider
)


def get_embedding_provider():

    provider = settings.EMBEDDING_PROVIDER

    if provider == "gemini":
        return GeminiEmbeddingProvider()

    raise Exception("Invalid embedding provider")
