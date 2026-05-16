from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str

    REDIS_URL: str

    EMBEDDING_PROVIDER: str

    GEMINI_API_KEY: str

    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
