"""Agent entity domain model."""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class AgentRole(StrEnum):
    COORDINATOR = "coordinator"
    DATA_INGESTION = "data_ingestion"
    FORECASTING = "forecasting"
    EVALUATION = "evaluation"


class AgentEntity(BaseModel):
    model_config = ConfigDict(frozen=True)

    agent_id: str
    name: str
    role: AgentRole
    description: str
