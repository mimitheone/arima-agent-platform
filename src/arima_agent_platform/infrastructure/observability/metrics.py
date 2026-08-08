"""Application metrics collector module."""

from collections.abc import Mapping


class MetricsCollector:
    """Collector for monitoring agent execution duration, token usage, and errors."""

    def increment_counter(
        self, name: str, value: int = 1, labels: Mapping[str, str] | None = None
    ) -> None:
        ...

    def record_histogram(
        self, name: str, value: float, labels: Mapping[str, str] | None = None
    ) -> None:
        ...
