"""Google Cloud Storage infrastructure wrapper."""

from typing import BinaryIO

from arima_agent_platform.domain.interfaces.storage_repository import StorageRepositoryProtocol


class GCSClientWrapper(StorageRepositoryProtocol):
    """GCS client wrapper implementing StorageRepositoryProtocol."""

    def __init__(self, bucket_name: str, project_id: str) -> None:
        self._bucket_name = bucket_name
        self._project_id = project_id

    async def upload(self, destination_path: str, data: BinaryIO) -> str:
        ...

    async def download(self, source_path: str) -> BinaryIO:
        ...

    async def exists(self, path: str) -> bool:
        ...

    async def delete(self, path: str) -> None:
        ...
