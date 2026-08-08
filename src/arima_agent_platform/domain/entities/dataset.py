"""Dataset domain entity."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from arima_agent_platform.domain.entities.time_series import TimeSeriesEntity


class DatasetEntity(BaseModel):
    model_config = ConfigDict(frozen=True)

    dataset_id: str
    name: str
    source_uri: str
    created_at: datetime
    series_list: list[TimeSeriesEntity]
