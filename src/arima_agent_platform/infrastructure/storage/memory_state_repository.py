"""In-memory state repository implementation."""

from collections.abc import Mapping
from typing import Any

from arima_agent_platform.domain.interfaces.state_repository import StateRepositoryProtocol


class MemoryStateRepository(StateRepositoryProtocol):
    """In-memory implementation of the state repository interface."""

    def __init__(self) -> None:
        self._store: dict[str, dict[str, Any]] = {}

    async def get_state(self, session_id: str, key: str) -> Any | None:
        session = self._store.get(session_id)
        if session is None:
            return None
        return session.get(key)

    async def set_state(self, session_id: str, key: str, value: Any) -> None:
        if session_id not in self._store:
            self._store[session_id] = {}
        self._store[session_id][key] = value

    async def get_all(self, session_id: str) -> Mapping[str, Any]:
        return self._store.get(session_id, {})

    async def clear(self, session_id: str) -> None:
        self._store.pop(session_id, None)
