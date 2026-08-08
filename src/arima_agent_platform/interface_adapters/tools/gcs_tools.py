"""Google Cloud Storage shared tool interface protocols."""

from typing import Protocol

from arima_agent_platform.interface_adapters.tools.base_tool import BaseToolProtocol


class GCSDownloadToolProtocol(BaseToolProtocol, Protocol):
    """Protocol for downloading dataset files from Google Cloud Storage."""
    ...


class GCSUploadToolProtocol(BaseToolProtocol, Protocol):
    """Protocol for uploading forecast results to Google Cloud Storage."""
    ...
