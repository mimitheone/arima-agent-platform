"""Multi-agent coordinator workflow protocol."""

from collections.abc import Mapping, Sequence
from typing import Any, Protocol


class MultiAgentCoordinatorProtocol(Protocol):
    """Abstract protocol for orchestrating communication among multiple agents."""

    async def coordinate_step(
        self, session_id: str, current_agent: str, message: Mapping[str, Any]
    ) -> Sequence[Mapping[str, Any]]:
        ...
