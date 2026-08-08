"""Unit tests for BaseAgent."""

from collections.abc import Mapping
from typing import Any

import pytest

from arima_agent_platform.adapters.agents.base_agent import BaseAgent
from arima_agent_platform.domain.entities.agent import AgentRole


class DummyAgent(BaseAgent):
    async def run(self, input_data: Mapping[str, Any]) -> Mapping[str, Any]:
        return {"status": "completed", "output": input_data.get("input")}


@pytest.mark.asyncio
async def test_base_agent_initialization_and_utilities() -> None:
    agent = DummyAgent(
        name="test_agent",
        role=AgentRole.ARIMA,
        description="Test agent instance",
        prompt_filename="arima.md",
    )

    assert agent.name == "test_agent"
    assert agent.role == AgentRole.ARIMA
    assert agent.description == "Test agent instance"
    assert "ARIMA Agent System Prompt" in agent.prompt

    transfer = agent.transfer_to("coordinator", {"key": "val"})
    assert transfer["action"] == "transfer"
    assert transfer["target_agent"] == "coordinator"

    result = await agent.run({"input": "test_payload"})
    assert result["status"] == "completed"
    assert result["output"] == "test_payload"
