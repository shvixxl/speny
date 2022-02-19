"""Pytest fixtures."""

import os

from pytest import Config


def pytest_configure(config: Config) -> None:
    """Configures pytest before testing."""

    os.environ['BOT_TOKEN'] = 'token'
