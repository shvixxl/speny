"""Tests configuration module."""

from aiogram.utils.backoff import BackoffConfig

from speny.config import Settings, settings


def test_settings():
    """Tests if settings object."""

    assert isinstance(settings, Settings)

    assert isinstance(settings.BOT_TOKEN, str)
    assert isinstance(settings.LOGGING_LEVEL, int)
    assert isinstance(settings.POLLING_TIMEOUT, int)
    assert isinstance(settings.BACKOFF_CONFIG, BackoffConfig)
