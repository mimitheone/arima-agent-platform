"""Golden baseline dataset reference model."""

from collections.abc import Sequence

from pydantic import BaseModel, ConfigDict

from arima_agent_platform.domain.entities.time_series import DataPoint


class GoldenDataset(BaseModel):
    model_config = ConfigDict(frozen=True)

    golden_id: str
    description: str
    expected_values: Sequence[DataPoint]
