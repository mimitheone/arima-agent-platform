"""Forecasting orchestrator workflow protocol."""

from typing import Protocol

from arima_agent_platform.application.dto.forecasting_request import ForecastingRequestDTO
from arima_agent_platform.application.dto.forecasting_response import ForecastingResponseDTO


class ForecastingOrchestratorProtocol(Protocol):
    """Abstract protocol for executing forecasting workflows."""

    async def execute(self, request: ForecastingRequestDTO) -> ForecastingResponseDTO:
        ...
