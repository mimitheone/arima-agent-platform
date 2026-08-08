"""ADK Service abstract protocol definition."""

from collections.abc import Mapping, Sequence
from typing import Any, Protocol


class ADKServiceProtocol(Protocol):
    """Abstract application interface for Google ADK execution engine."""

    async def run_agent(
        self, agent_name: str, prompt: str, context: Mapping[str, Any]
    ) -> Sequence[Mapping[str, Any]]:
        ...
