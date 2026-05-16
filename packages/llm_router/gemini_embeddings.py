from google import genai

from apps.api.core.config import settings

from packages.llm_router.base_embeddings import (
    BaseEmbeddingProvider
)

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


class GeminiEmbeddingProvider(BaseEmbeddingProvider):

    def generate_embedding(self, text: str):

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )

        return response.embeddings[0].values
