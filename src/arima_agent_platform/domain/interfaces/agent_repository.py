"""Agent repository interface definition."""

from collections.abc import Sequence
from typing import Protocol

from arima_agent_platform.domain.entities.agent import AgentEntity


class AgentRepositoryProtocol(Protocol):
    """Abstract interface for agent metadata repository."""

    async def get_by_id(self, agent_id: str) -> AgentEntity:
        ...

    async def list_all(self) -> Sequence[AgentEntity]:
        ...

    async def save(self, agent: AgentEntity) -> None:
        ...
