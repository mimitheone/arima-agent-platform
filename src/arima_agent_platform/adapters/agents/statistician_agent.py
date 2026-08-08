"""Statistician Agent interface adapter protocol."""

from typing import Protocol

from arima_agent_platform.adapters.agents.base_agent import BaseAgentProtocol


class StatisticianAgentProtocol(BaseAgentProtocol, Protocol):
    """Protocol for Statistician Agent evaluating stationarity, trend, and seasonality."""
    ...
