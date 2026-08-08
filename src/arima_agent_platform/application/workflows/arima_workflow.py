"""Deterministic ARIMA Workflow Orchestrator (Python Coordinator)."""

from typing import Protocol

from arima_agent_platform.application.dto.forecasting_request import ForecastingRequestDTO
from arima_agent_platform.application.dto.forecasting_response import ForecastingResponseDTO


class ARIMAWorkflowProtocol(Protocol):
    """Deterministic Python workflow orchestrator.

    Coordinates Data Engineer, Statistician, ARIMA, QA, and Reporting agents.
    """

    async def run_workflow(self, request: ForecastingRequestDTO) -> ForecastingResponseDTO:
        ...
