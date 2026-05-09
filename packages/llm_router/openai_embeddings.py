from openai import OpenAI

from apps.api.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_embedding(text: str):

    if not text:
        return None

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding
