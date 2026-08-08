"""Data Engineer Agent interface adapter protocol."""

from typing import Protocol

from arima_agent_platform.adapters.agents.base_agent import BaseAgentProtocol


class DataEngineerAgentProtocol(BaseAgentProtocol, Protocol):
    """Protocol for Data Engineer Agent handling time series ingestion and preprocessing."""
    ...
