# ARIMA Agent Platform

A production-ready Google Agent Development Kit (ADK) multi-agent platform for time series forecasting, built using Python 3.12 and Clean Architecture.

## Architecture

The codebase strictly follows Clean Architecture principles:

- **`domain/`**: Enterprise business rules (Entities, Value Objects, Domain Interfaces, Exceptions). Framework independent.
- **`use_cases/`**: Application workflows, Orchestrators, DTOs, Application Interfaces.
- **`interface_adapters/`**: Adapters for Agents, Shared Tools, Shared State, and MCP Integrations.
- **`infrastructure/`**: Frameworks & Drivers (Google ADK runner, GCP/GCS adapters, Secret Manager, Config/Settings).

## Requirements

- Python 3.12+
- `uv` package manager

## Development Setup

```bash
# Sync dependencies
uv sync

# Run linter
uv run ruff check .

# Run type checker
uv run pyright

# Run test suite
uv run pytest
```
