"""Time series data entity domain model."""

from collections.abc import Sequence
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DataPoint(BaseModel):
    model_config = ConfigDict(frozen=True)

    timestamp: datetime
    value: float


class TimeSeriesEntity(BaseModel):
    model_config = ConfigDict(frozen=True)

    series_id: str
    target_column: str
    data_points: Sequence[DataPoint]
