"""Google Cloud Vertex AI infrastructure wrapper."""

from collections.abc import Mapping, Sequence
from typing import Any


class VertexAIWrapper:
    """Vertex AI client wrapper for AI Model Endpoints and Pipelines."""

    def __init__(self, project_id: str, location: str) -> None:
        self._project_id = project_id
        self._location = location

    async def predict(
        self, endpoint_id: str, instances: Sequence[Mapping[str, Any]]
    ) -> Mapping[str, Any]:
        ...
