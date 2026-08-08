"""Evaluation dataset container model."""

from collections.abc import Sequence

from pydantic import BaseModel, ConfigDict

from arima_agent_platform.domain.entities.time_series import TimeSeriesEntity


class EvaluationDataset(BaseModel):
    model_config = ConfigDict(frozen=True)

    dataset_id: str
    name: str
    series_list: Sequence[TimeSeriesEntity]
