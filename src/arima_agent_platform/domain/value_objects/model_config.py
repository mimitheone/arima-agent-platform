"""Model configuration value object."""

from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel, ConfigDict


class ModelConfigValueObject(BaseModel):
    model_config = ConfigDict(frozen=True)

    model_name: str
    hyperparameters: Mapping[str, Any]
    forecast_horizon: int
