"""Data quality validation tool protocol."""

from typing import Protocol

from arima_agent_platform.adapters.tools.base_tool import BaseToolProtocol


class DataValidationToolProtocol(BaseToolProtocol, Protocol):
    """Protocol for checking dataset integrity, missing values, and frequency consistency."""
    ...
