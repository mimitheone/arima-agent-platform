"""Forecast accuracy metrics container model."""

from pydantic import BaseModel, ConfigDict


class ForecastMetrics(BaseModel):
    model_config = ConfigDict(frozen=True)

    mae: float
    rmse: float
    mape: float
    smape: float
