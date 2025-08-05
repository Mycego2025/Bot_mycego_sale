from pathlib import Path

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    telegram_bot_token: str
    django_api_url: str
    django_api_token: str

    class Config:
        env_file = ".env"

settings = Settings()
