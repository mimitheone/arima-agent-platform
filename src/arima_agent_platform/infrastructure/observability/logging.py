"""Structured logging configuration module."""

from collections.abc import Mapping
from typing import Any


class StructuredLogger:
    """Structured JSON logger utility."""

    def __init__(self, logger_name: str) -> None:
        self._logger_name = logger_name

    def info(self, message: str, context: Mapping[str, Any] | None = None) -> None:
        ...

    def error(
        self,
        message: str,
        exc: Exception | None = None,
        context: Mapping[str, Any] | None = None,
    ) -> None:
        ...
