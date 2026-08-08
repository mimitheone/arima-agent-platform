"""Data Ingestion Agent interface adapter protocol."""

from typing import Protocol

from arima_agent_platform.interface_adapters.agents.base_agent import BaseAgentProtocol


class DataIngestionAgentProtocol(BaseAgentProtocol, Protocol):
    """Protocol for agent handling time series data ingestion and validation."""
    ...
