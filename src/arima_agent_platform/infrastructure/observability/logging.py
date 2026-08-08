"""Structured logging configuration module."""

import logging
import sys
from collections.abc import Mapping
from typing import Any


def configure_logging(level: str = "INFO") -> None:
    """Configure system-wide structured logging."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


class StructuredLogger:
    """Structured JSON logger utility."""

    def __init__(self, logger_name: str) -> None:
        self._logger = logging.getLogger(logger_name)

    def info(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        self._logger.info("%s - context: %s", message, context or {})

    def error(
        self,
        message: str,
        exc: Exception | None = None,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        self._logger.error("%s - context: %s", message, context or {}, exc_info=exc)
