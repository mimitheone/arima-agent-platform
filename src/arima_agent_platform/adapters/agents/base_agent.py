"""Base agent abstract class and protocol definition."""

from abc import ABC, abstractmethod
from collections.abc import Mapping
from pathlib import Path
from typing import Any, Protocol

from arima_agent_platform.adapters.tools.base_tool import BaseToolProtocol
from arima_agent_platform.domain.entities.agent import AgentRole


class BaseAgentProtocol(Protocol):
    """Abstract protocol for agent interface adapters."""

    @property
    def name(self) -> str:
        ...

    @property
    def role(self) -> AgentRole:
        ...

    @property
    def description(self) -> str:
        ...

    @property
    def instruction(self) -> str:
        ...

    async def run(self, input_data: Mapping[str, Any]) -> Mapping[str, Any]:
        ...


class BaseAgent(ABC):
    """Abstract base class used by every agent in the platform."""

    def __init__(
        self,
        name: str,
        role: AgentRole,
        description: str,
        prompt_filename: str | None = None,
        instruction: str | None = None,
    ) -> None:
        self._name = name
        self._role = role
        self._description = description
        self._registered_tools: dict[str, BaseToolProtocol] = {}
        self._instruction: str = instruction or ""

        if prompt_filename:
            loaded_prompt = self.load_prompt(prompt_filename)
            if loaded_prompt:
                self._instruction = loaded_prompt

    @property
    def name(self) -> str:
        """Return the agent name."""
        return self._name

    @property
    def role(self) -> AgentRole:
        """Return the agent role."""
        return self._role

    @property
    def description(self) -> str:
        """Return the agent description."""
        return self._description

    @property
    def instruction(self) -> str:
        """Return the agent system prompt instructions."""
        return self._instruction

    @property
    def prompt(self) -> str:
        """Alias for instruction system prompt."""
        return self._instruction

    @property
    def registered_tools(self) -> Mapping[str, BaseToolProtocol]:
        """Return all registered tools."""
        return self._registered_tools

    def load_prompt(self, prompt_filename: str) -> str:
        """Load prompt template from the prompts directory."""
        prompts_dir = Path(__file__).parents[2] / "prompts"
        prompt_file = prompts_dir / prompt_filename
        if prompt_file.exists():
            return prompt_file.read_text(encoding="utf-8").strip()
        return ""

    def register_tool(self, tool: BaseToolProtocol) -> None:
        """Register a tool for use by this agent."""
        self._registered_tools[tool.name] = tool

    def transfer_to(self, target_agent_name: str, payload: Mapping[str, Any]) -> dict[str, Any]:
        """Prepare hand-off payload for transferring control to target agent."""
        return {
            "action": "transfer",
            "from_agent": self.name,
            "target_agent": target_agent_name,
            "payload": dict(payload),
        }

    def format_context(self, context: Mapping[str, Any]) -> str:
        """Common utility method to format execution context as text."""
        items = [f"{key}: {value}" for key, value in context.items()]
        return "\n".join(items)

    @abstractmethod
    async def run(self, input_data: Mapping[str, Any]) -> Mapping[str, Any]:
        """Execute agent task asynchronously."""
        ...
