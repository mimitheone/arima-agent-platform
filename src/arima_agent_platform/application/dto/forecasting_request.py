"""Forecasting request DTO."""

from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel, ConfigDict


class ForecastingRequestDTO(BaseModel):
    model_config = ConfigDict(frozen=True)

    dataset_uri: str
    target_column: str
    forecast_horizon: int
    parameters: Mapping[str, Any] | None = None
