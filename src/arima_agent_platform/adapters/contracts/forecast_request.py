"""Forecast request contract model."""

from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel, ConfigDict


class ForecastRequestContract(BaseModel):
    model_config = ConfigDict(frozen=True)

    request_id: str
    dataset_uri: str
    target_column: str
    horizon: int
    parameters: Mapping[str, Any] | None = None
