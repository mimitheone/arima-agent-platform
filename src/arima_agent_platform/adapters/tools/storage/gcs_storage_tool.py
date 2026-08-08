"""Google Cloud Storage tool interface protocols."""

from typing import Protocol

from arima_agent_platform.adapters.tools.base_tool import BaseToolProtocol


class GCSStorageToolProtocol(BaseToolProtocol, Protocol):
    """Protocol for Google Cloud Storage file upload/download operations."""
    ...
