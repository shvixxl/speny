"""Configuration module."""

from logging import INFO

from aiogram.dispatcher.dispatcher import DEFAULT_BACKOFF_CONFIG
from aiogram.utils.backoff import BackoffConfig
from pydantic import (
    BaseSettings,
)


class Settings(BaseSettings):
    """Application settings."""

    PORT: int = 8080

    BOT_TOKEN: str
    BOT_USERNAME: str = "spenybot"

    CLIENT_SECRETS_PATH: str = "client_secrets.json"

    REDIRECT_URI: str = "http://127.0.0.1:8080/auth"

    SCOPES: tuple[str] = ("https://www.googleapis.com/auth/spreadsheets",)

    LOGGING_LEVEL: int | str = INFO

    POLLING_TIMEOUT: int = 30

    BACKOFF_CONFIG: BackoffConfig = DEFAULT_BACKOFF_CONFIG

    TELEGRAM_URL: str = "https://t.me"

    class Config:
        """Application settings configuration."""

        case_sensitive = True
        env_nested_delimiter = "__"


settings = Settings()
