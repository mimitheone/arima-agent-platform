"""Unit tests for domain entities."""

from arima_agent_platform.domain.entities.agent import AgentEntity, AgentRole


def test_agent_entity_instantiation() -> None:
    agent = AgentEntity(
        agent_id="agent-001",
        name="ARIMA Agent",
        role=AgentRole.ARIMA,
        description="Handles time series model training.",
    )
    assert agent.agent_id == "agent-001"
    assert agent.role == AgentRole.ARIMA
