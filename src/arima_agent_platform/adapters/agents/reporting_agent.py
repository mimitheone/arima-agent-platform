"""Reporting Agent interface adapter protocol."""

from typing import Protocol

from arima_agent_platform.adapters.agents.base_agent import BaseAgentProtocol


class ReportingAgentProtocol(BaseAgentProtocol, Protocol):
    """Protocol for Reporting Agent generating summary reports and visualizations."""
    ...
