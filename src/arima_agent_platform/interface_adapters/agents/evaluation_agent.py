"""Evaluation Agent interface adapter protocol."""

from typing import Protocol

from arima_agent_platform.interface_adapters.agents.base_agent import BaseAgentProtocol


class EvaluationAgentProtocol(BaseAgentProtocol, Protocol):
    """Protocol for agent evaluating forecast accuracy metrics and performance."""
    ...
