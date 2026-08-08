"""OpenTelemetry tracing setup and utilities."""

from collections.abc import Mapping
from typing import Any


class TracerProvider:
    """Infrastructure tracer provider for OpenTelemetry distributed tracing."""

    def __init__(self, service_name: str) -> None:
        self._service_name = service_name

    def start_span(self, name: str, attributes: Mapping[str, Any] | None = None) -> Any:
        ...
