"""Base tool interface protocol definition."""

from collections.abc import Mapping
from typing import Any, Protocol


class BaseToolProtocol(Protocol):
    """Abstract protocol for tools shared across agents."""

    @property
    def name(self) -> str:
        ...

    @property
    def description(self) -> str:
        ...

    async def execute(self, **kwargs: Any) -> Mapping[str, Any]:
        ...
