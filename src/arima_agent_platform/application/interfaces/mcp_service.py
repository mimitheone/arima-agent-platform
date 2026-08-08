"""MCP Service abstract protocol definition."""

from collections.abc import Mapping, Sequence
from typing import Any, Protocol


class MCPServiceProtocol(Protocol):
    """Abstract application interface for Model Context Protocol interactions."""

    async def list_tools(self) -> Sequence[Mapping[str, Any]]:
        ...

    async def execute_tool(self, tool_name: str, arguments: Mapping[str, Any]) -> Any:
        ...
