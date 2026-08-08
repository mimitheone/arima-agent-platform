"""Forecasting response DTO."""

from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel, ConfigDict


class ForecastingResponseDTO(BaseModel):
    model_config = ConfigDict(frozen=True)

    job_id: str
    status: str
    output_uri: str
    metrics: Mapping[str, Any]
