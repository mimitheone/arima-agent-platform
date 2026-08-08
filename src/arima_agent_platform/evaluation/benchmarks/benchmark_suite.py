"""Benchmark suite runner protocol for evaluation."""

from collections.abc import Mapping
from typing import Any, Protocol


class BenchmarkSuiteProtocol(Protocol):
    """Protocol for running benchmark datasets against forecasting workflows."""

    async def run_benchmark(self, dataset_id: str) -> Mapping[str, Any]:
        ...
