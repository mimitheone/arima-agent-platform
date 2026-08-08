"""State repository interface definition."""

from collections.abc import Mapping
from typing import Any, Protocol


class StateRepositoryProtocol(Protocol):
    """Abstract interface for session and shared state storage."""

    async def get_state(self, session_id: str, key: str) -> Any | None:
        ...

    async def set_state(self, session_id: str, key: str, value: Any) -> None:
        ...

    async def get_all(self, session_id: str) -> Mapping[str, Any]:
        ...

    async def clear(self, session_id: str) -> None:
        ...
