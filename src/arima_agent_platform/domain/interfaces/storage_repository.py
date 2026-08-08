"""Storage repository interface definition."""

from typing import BinaryIO, Protocol


class StorageRepositoryProtocol(Protocol):
    """Abstract interface for object storage operations."""

    async def upload(self, destination_path: str, data: BinaryIO) -> str:
        ...

    async def download(self, source_path: str) -> BinaryIO:
        ...

    async def exists(self, path: str) -> bool:
        ...

    async def delete(self, path: str) -> None:
        ...
