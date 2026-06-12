from openai import OpenAI

from apps.api.core.config import settings

from packages.llm_router.base_embeddings import (
    BaseEmbeddingProvider
)

client = OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)


class DeepSeekEmbeddingProvider(BaseEmbeddingProvider):

    def generate_embedding(self, text: str):

        if not text:
            return None

        response = client.embeddings.create(
            model="deepseek-embedding",
            input=text
        )

        return response.data[0].embedding
