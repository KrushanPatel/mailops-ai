from pydantic_settings import BaseSettings


class LLMSettings(BaseSettings):

    CHAT_PROVIDER: str

    CHAT_MODEL: str

    CHAT_API_KEY: str = ""

    CHAT_BASE_URL: str = ""

    EMBEDDING_PROVIDER: str

    EMBEDDING_MODEL: str

    EMBEDDING_API_KEY: str = ""

    EMBEDDING_BASE_URL: str = ""

    class Config:
        env_file = ".env"


llm_settings = LLMSettings()
