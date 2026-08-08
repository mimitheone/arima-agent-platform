"""Forecasting Agent interface adapter protocol."""

from typing import Protocol

from arima_agent_platform.interface_adapters.agents.base_agent import BaseAgentProtocol


class ForecastingAgentProtocol(BaseAgentProtocol, Protocol):
    """Protocol for agent handling model training and forecasting execution."""
    ...
