"""Agent entity domain model."""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class AgentRole(StrEnum):
    COORDINATOR = "coordinator"
    DATA_ENGINEER = "data_engineer"
    STATISTICIAN = "statistician"
    ARIMA = "arima"
    QA = "qa"
    REPORTING = "reporting"


class AgentEntity(BaseModel):
    model_config = ConfigDict(frozen=True)

    agent_id: str
    name: str
    role: AgentRole
    description: str
