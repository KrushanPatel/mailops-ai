from google import genai

from apps.api.core.config import settings

from packages.llm_router.base_chat import (
    BaseChatProvider
)

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


class GeminiChatProvider(BaseChatProvider):

    def generate(self, prompt: str):

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text
