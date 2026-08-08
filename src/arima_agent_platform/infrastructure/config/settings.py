"""Application settings and environment configurations using Pydantic Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    environment: str = "development"
    debug: bool = False

    # GCP Configurations
    gcp_project_id: str = ""
    gcs_bucket_name: str = ""

    # Google ADK / Gemini Configurations
    gemini_api_key: str = ""
    adk_model_name: str = "gemini-2.5-flash"

    # MCP Server Configurations
    mcp_server_url: str = ""
