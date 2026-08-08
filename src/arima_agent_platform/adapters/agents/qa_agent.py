"""QA Agent interface adapter protocol."""

from typing import Protocol

from arima_agent_platform.adapters.agents.base_agent import BaseAgentProtocol


class QAAgentProtocol(BaseAgentProtocol, Protocol):
    """Protocol for Quality Assurance (QA) Agent validating model output and forecast bounds."""
    ...
