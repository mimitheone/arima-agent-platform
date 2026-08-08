"""Application contract for executing individual agents."""

from collections.abc import Mapping
from typing import Any, Protocol


class AgentRunnerContractProtocol(Protocol):
    """Protocol for triggering agent execution within application workflows."""

    async def execute_agent(
        self, agent_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        ...
