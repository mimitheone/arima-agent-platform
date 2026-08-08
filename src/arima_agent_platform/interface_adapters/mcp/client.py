"""MCP Client adapter protocol definition."""

from collections.abc import Mapping, Sequence
from typing import Any, Protocol


class MCPClientAdapterProtocol(Protocol):
    """Protocol for communicating with remote Model Context Protocol servers."""

    async def connect(self, server_uri: str) -> None:
        ...

    async def disconnect(self) -> None:
        ...

    async def call_tool(self, name: str, arguments: Mapping[str, Any]) -> Any:
        ...

    async def list_resources(self) -> Sequence[Mapping[str, Any]]:
        ...
