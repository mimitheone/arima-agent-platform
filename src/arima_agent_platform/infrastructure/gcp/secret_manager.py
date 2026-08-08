"""Google Cloud Secret Manager client wrapper."""


class SecretManagerWrapper:
    """Secret Manager client wrapper for retrieving system secrets."""

    def __init__(self, project_id: str) -> None:
        self._project_id = project_id

    async def get_secret(self, secret_id: str, version_id: str = "latest") -> str:
        ...
