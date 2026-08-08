"""Application service orchestrating end-to-end forecasting use cases."""

from arima_agent_platform.application.dto.forecasting_request import ForecastingRequestDTO
from arima_agent_platform.application.dto.forecasting_response import ForecastingResponseDTO


class ForecastingApplicationService:
    """High-level service coordinating forecasting workflows, agents, and storage repositories."""

    async def run_forecasting_pipeline(
        self, request: ForecastingRequestDTO
    ) -> ForecastingResponseDTO:
        ...
