"""Pytest configuration fixtures."""

import pytest

from arima_agent_platform.infrastructure.storage.memory_state_repository import (
    MemoryStateRepository,
)


@pytest.fixture
def memory_state_repo() -> MemoryStateRepository:
    return MemoryStateRepository()
