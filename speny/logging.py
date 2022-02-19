"""Logging module."""

import logging

from speny.config import settings


logging.basicConfig(level=settings.LOGGING_LEVEL)


def create_logger(name: str) -> logging.Logger:
    """Returns configured logger with specified name."""

    logger = logging.getLogger(name)

    return logger
