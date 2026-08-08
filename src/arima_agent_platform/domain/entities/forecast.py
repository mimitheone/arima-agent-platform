"""Forecast output domain entity."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from arima_agent_platform.domain.entities.time_series import DataPoint


class ForecastEntity(BaseModel):
    model_config = ConfigDict(frozen=True)

    forecast_id: str
    series_id: str
    generated_at: datetime
    predictions: list[DataPoint]
    confidence_lower: list[DataPoint] | None = None
    confidence_upper: list[DataPoint] | None = None
