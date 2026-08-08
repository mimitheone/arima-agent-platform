"""Google Cloud Logging infrastructure wrapper."""

from collections.abc import Mapping
from typing import Any


class CloudLoggingWrapper:
    """Google Cloud Logging wrapper for structured log shipping."""

    def __init__(self, project_id: str, log_name: str) -> None:
        self._project_id = project_id
        self._log_name = log_name

    def write_entry(
        self,
        message: str,
        severity: str = "INFO",
        payload: Mapping[str, Any] | None = None,
    ) -> None:
        ...
