from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "MailOps AI"

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/mailops"

    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"


settings = Settings()
