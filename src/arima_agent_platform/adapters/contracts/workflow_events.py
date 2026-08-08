"""Workflow event contract data model."""

from collections.abc import Mapping
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class WorkflowEventContract(BaseModel):
    model_config = ConfigDict(frozen=True)

    event_id: str
    workflow_id: str
    event_type: str
    data: Mapping[str, Any]
    timestamp: datetime
