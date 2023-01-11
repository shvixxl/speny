"""Pytest fixtures."""

import os

import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Configures pytest before testing."""

    os.environ["BOT_TOKEN"] = "token"
