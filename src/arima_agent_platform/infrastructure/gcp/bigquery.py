"""Google Cloud BigQuery infrastructure wrapper."""

from collections.abc import Mapping, Sequence
from typing import Any


class BigQueryClientWrapper:
    """BigQuery client wrapper for querying time series tables."""

    def __init__(self, project_id: str, dataset_id: str) -> None:
        self._project_id = project_id
        self._dataset_id = dataset_id

    async def query(self, sql_query: str) -> Sequence[Mapping[str, Any]]:
        ...
