"""ARIMA Agent interface adapter protocol."""

from typing import Protocol

from arima_agent_platform.adapters.agents.base_agent import BaseAgentProtocol


class ARIMAAgentProtocol(BaseAgentProtocol, Protocol):
    """Protocol for ARIMA Agent executing model parameter tuning and forecasting."""
    ...
