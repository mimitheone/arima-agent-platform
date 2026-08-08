"""Shared state contract data model."""

from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel, ConfigDict


class SharedStateContract(BaseModel):
    model_config = ConfigDict(frozen=True)

    session_id: str
    context: Mapping[str, Any]
