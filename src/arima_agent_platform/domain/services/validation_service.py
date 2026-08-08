"""Domain validation service protocol for checking data and model business rules."""

from typing import Protocol

from arima_agent_platform.domain.entities.dataset import DatasetEntity
from arima_agent_platform.domain.entities.time_series import TimeSeriesEntity


class DomainValidationServiceProtocol(Protocol):
    """Domain service interface for validating time series data integrity."""

    def validate_series(self, series: TimeSeriesEntity) -> bool:
        ...

    def validate_dataset(self, dataset: DatasetEntity) -> bool:
        ...
