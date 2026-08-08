"""Time series visualization plot tool protocol."""

from typing import Protocol

from arima_agent_platform.adapters.tools.base_tool import BaseToolProtocol


class TimeSeriesPlotToolProtocol(BaseToolProtocol, Protocol):
    """Protocol for rendering time series plots and forecast charts."""
    ...
