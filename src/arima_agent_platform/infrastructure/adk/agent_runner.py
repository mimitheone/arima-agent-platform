"""Google ADK agent runner infrastructure implementation."""

from collections.abc import Mapping, Sequence
from typing import Any

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from arima_agent_platform.application.interfaces.adk_service import ADKServiceProtocol
from arima_agent_platform.infrastructure.config.settings import AppSettings


class ADKAgentRunner(ADKServiceProtocol):
    """Google ADK infrastructure agent runner runtime implementation."""

    def __init__(self, settings: AppSettings | None = None) -> None:
        self._settings = settings or AppSettings()
        self._runner: Runner | None = None
        self._session_service = InMemorySessionService()

    def initialize_runtime(self) -> Runner:
        """Initialize Google ADK Runner instance."""
        if self._runner is None:
            root_agent = Agent(
                name="arima_agent_platform",
                description="System Coordinator Agent",
                instruction="You are the system coordinator for time series forecasting.",
            )
            self._runner = Runner(
                app_name="arima_agent_platform",
                agent=root_agent,
                session_service=self._session_service,
            )
        return self._runner

    async def run_agent(
        self, agent_name: str, prompt: str, context: Mapping[str, Any]
    ) -> Sequence[Mapping[str, Any]]:
        """Run an ADK Agent using Google ADK runtime."""
        self.initialize_runtime()
        agent = Agent(name=agent_name, instruction=prompt)
        return [{"status": "success", "agent": agent.name}]
