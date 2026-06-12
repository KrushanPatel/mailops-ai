from openai import OpenAI

from apps.api.core.config import settings

from packages.llm_router.base_chat import (
    BaseChatProvider
)

client = OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)


class DeepSeekChatProvider(BaseChatProvider):

    def generate(self, prompt: str):

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
