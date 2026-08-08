"""Application service for managing agent invocations and state passing."""

from collections.abc import Mapping
from typing import Any


class AgentExecutionService:
    """Service managing state dispatching and step execution across specialized platform agents."""

    async def execute_step(
        self, agent_name: str, session_id: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        ...
