"""Forecasting job entity domain model."""

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class JobStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class ForecastingJobEntity(BaseModel):
    model_config = ConfigDict(frozen=True)

    job_id: str
    dataset_id: str
    status: JobStatus
    created_at: datetime
    updated_at: datetime
    error_message: str | None = None
