"""Statistical stationarity testing tool protocol."""

from typing import Protocol

from arima_agent_platform.adapters.tools.base_tool import BaseToolProtocol


class StationarityToolProtocol(BaseToolProtocol, Protocol):
    """Protocol for stationarity testing tools (ADF, KPSS)."""
    ...
