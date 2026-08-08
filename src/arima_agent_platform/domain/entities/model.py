"""Forecasting model domain entity."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from arima_agent_platform.domain.value_objects.model_config import ModelConfigValueObject


class ModelEntity(BaseModel):
    model_config = ConfigDict(frozen=True)

    model_id: str
    name: str
    config: ModelConfigValueObject
    trained_at: datetime
