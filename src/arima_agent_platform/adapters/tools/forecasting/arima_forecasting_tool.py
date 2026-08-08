"""ARIMA model training tool protocol."""

from typing import Protocol

from arima_agent_platform.adapters.tools.base_tool import BaseToolProtocol


class ARIMAExecutionToolProtocol(BaseToolProtocol, Protocol):
    """Protocol for training ARIMA / AutoARIMA time series models."""
    ...
