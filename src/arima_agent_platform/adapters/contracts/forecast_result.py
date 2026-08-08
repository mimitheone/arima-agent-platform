"""Forecast result contract model."""

from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel, ConfigDict


class ForecastResultContract(BaseModel):
    model_config = ConfigDict(frozen=True)

    job_id: str
    status: str
    output_uri: str
    metrics: Mapping[str, Any]
