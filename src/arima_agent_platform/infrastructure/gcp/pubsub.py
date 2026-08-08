"""Google Cloud Pub/Sub infrastructure wrapper."""

from collections.abc import Mapping
from typing import Any


class PubSubClientWrapper:
    """Pub/Sub client wrapper for event messaging."""

    def __init__(self, project_id: str, topic_id: str) -> None:
        self._project_id = project_id
        self._topic_id = topic_id

    async def publish_event(self, event_type: str, data: Mapping[str, Any]) -> str:
        ...
