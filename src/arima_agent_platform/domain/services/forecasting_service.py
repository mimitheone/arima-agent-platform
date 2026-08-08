"""Domain forecasting service protocol for pure forecasting business rules."""

from typing import Protocol

from arima_agent_platform.domain.entities.forecast import ForecastEntity
from arima_agent_platform.domain.entities.time_series import TimeSeriesEntity
from arima_agent_platform.domain.value_objects.model_config import ModelConfigValueObject


class DomainForecastingServiceProtocol(Protocol):
    """Domain service interface for computing forecasts from time series and configurations."""

    def compute_forecast(
        self, series: TimeSeriesEntity, config: ModelConfigValueObject
    ) -> ForecastEntity:
        ...
