"""Shared state adapter protocol for multi-agent workflows."""

from collections.abc import Mapping
from typing import Any, Protocol


class SharedStateAdapterProtocol(Protocol):
    """Protocol for managing state shared across multiple active agents in a workflow session."""

    async def update_context(self, session_id: str, updates: Mapping[str, Any]) -> None:
        ...

    async def get_context(self, session_id: str) -> Mapping[str, Any]:
        ...

    async def get_value(self, session_id: str, key: str) -> Any | None:
        ...
