"""Google ADK agent runner infrastructure implementation stub."""

from collections.abc import Mapping, Sequence
from typing import Any

from arima_agent_platform.use_cases.interfaces.adk_service import ADKServiceProtocol


class ADKAgentRunner(ADKServiceProtocol):
    """Google ADK infrastructure agent runner implementation."""

    def __init__(self, api_key: str, model_name: str) -> None:
        self._api_key = api_key
        self._model_name = model_name

    async def run_agent(
        self, agent_name: str, prompt: str, context: Mapping[str, Any]
    ) -> Sequence[Mapping[str, Any]]:
        ...
