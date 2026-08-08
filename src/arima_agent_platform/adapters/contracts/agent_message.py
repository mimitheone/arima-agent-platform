"""Agent message contract data model."""

from collections.abc import Mapping
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class AgentMessageContract(BaseModel):
    model_config = ConfigDict(frozen=True)

    message_id: str
    sender_agent: str
    recipient_agent: str
    payload: Mapping[str, Any]
    timestamp: datetime
