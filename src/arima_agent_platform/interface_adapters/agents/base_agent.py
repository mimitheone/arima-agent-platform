"""Base agent abstract protocol definition."""

from collections.abc import Mapping
from typing import Any, Protocol

from arima_agent_platform.domain.entities.agent import AgentRole


class BaseAgentProtocol(Protocol):
    """Abstract protocol for agent interface adapters."""

    @property
    def name(self) -> str:
        ...

    @property
    def role(self) -> AgentRole:
        ...

    async def run(self, input_data: Mapping[str, Any]) -> Mapping[str, Any]:
        ...
