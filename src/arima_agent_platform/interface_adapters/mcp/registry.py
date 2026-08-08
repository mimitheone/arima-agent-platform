"""MCP Tool and Resource Registry adapter protocol definition."""

from collections.abc import Sequence
from typing import Protocol

from arima_agent_platform.interface_adapters.mcp.client import MCPClientAdapterProtocol


class MCPRegistryAdapterProtocol(Protocol):
    """Protocol for registering and querying MCP servers and tools."""

    async def register_server(self, name: str, client: MCPClientAdapterProtocol) -> None:
        ...

    async def get_client(self, name: str) -> MCPClientAdapterProtocol:
        ...

    async def list_registered_servers(self) -> Sequence[str]:
        ...
