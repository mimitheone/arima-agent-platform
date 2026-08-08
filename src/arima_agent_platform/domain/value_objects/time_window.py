"""Time window value object."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TimeWindowValueObject(BaseModel):
    model_config = ConfigDict(frozen=True)

    start_time: datetime
    end_time: datetime
    frequency: str
