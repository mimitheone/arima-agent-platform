"""Coordinator Agent interface adapter protocol."""

from typing import Protocol

from arima_agent_platform.adapters.agents.base_agent import BaseAgentProtocol


class CoordinatorAgentProtocol(BaseAgentProtocol, Protocol):
    """Protocol for Coordinator Agent orchestrating multi-agent tasks."""
    ...
