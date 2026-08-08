"""Prompt template loader infrastructure module."""

from collections.abc import Mapping


class PromptTemplateLoader:
    """Infrastructure utility for loading system prompts and agent instruction templates."""

    def __init__(self, templates_directory: str) -> None:
        self._templates_directory = templates_directory

    async def load_template(self, template_name: str, variables: Mapping[str, str]) -> str:
        ...
