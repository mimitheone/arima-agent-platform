"""Time series forecasting shared tool interface protocols."""

from typing import Protocol

from arima_agent_platform.interface_adapters.tools.base_tool import BaseToolProtocol


class ARIMATrainingToolProtocol(BaseToolProtocol, Protocol):
    """Protocol for training ARIMA time series models."""
    ...


class MetricsEvaluationToolProtocol(BaseToolProtocol, Protocol):
    """Protocol for calculating forecast evaluation metrics (MAE, RMSE, MAPE)."""
    ...
