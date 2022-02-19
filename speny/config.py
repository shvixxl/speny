"""Configuration module."""

from logging import INFO

from aiogram.utils.backoff import BackoffConfig
from aiogram.dispatcher.dispatcher import DEFAULT_BACKOFF_CONFIG

from pydantic import (
    BaseSettings
)


class Settings(BaseSettings):
    """Application settings."""

    BOT_TOKEN: str

    LOGGING_LEVEL: int = INFO

    POLLING_TIMEOUT: int = 30

    BACKOFF_CONFIG: BackoffConfig = DEFAULT_BACKOFF_CONFIG

    class Config:
        """Application settings config."""
        env_nested_delimiter = '__'

settings = Settings()
