# ARIMA Agent Platform Roadmap

> Goal: Build a production-ready multi-agent forecasting platform using Google ADK, Google Cloud and Clean Architecture.
>
> Development strategy:
> - Small iterations
> - One feature per commit
> - Working software after every sprint
> - Infrastructure first, business logic later

---

# Sprint 1 — Foundation

## Goal
Create the technical foundation of the platform. No forecasting, no statistics, no ARIMA yet. Only infrastructure.

---

## Task 1 — Project Bootstrap
### Deliverables
- Configure Python project
- Configure uv
- Configure Ruff
- Configure Pyright
- Configure pytest
- Configure pre-commit
- Configure logging

### Commit
`feat(project): bootstrap project`

---

## Task 2 — Google ADK Integration
### Deliverables
- Install Google ADK
- Configure runtime
- Create run.py
- Verify ADK starts successfully

### Commit
`feat(adk): integrate Google ADK runtime`

---

## Task 3 — Base Agent
Create the abstract base class used by every agent.

### Responsibilities
- Name
- Description
- Prompt loading
- Tool registration
- Transfer support
- Common utilities

### Deliverables
- `BaseAgent`

### Commit
`feat(core): add BaseAgent`

---

## Task 4 — Shared Contracts
Create all shared message contracts using Pydantic v2.

### Models
- ForecastRequest
- ForecastResponse
- Dataset
- ForecastResult
- WorkflowState
- AgentContext

### Commit
`feat(core): add workflow contracts`

---

## Task 5 — Shared Workflow State
Implement the shared workflow state with keys:
- `dataset`
- `clean_dataset`
- `statistics`
- `forecast`
- `qa`
- `report`

### Commit
`feat(core): add workflow state`

---

## Task 6 — Coordinator Agent
The Coordinator orchestrates workflows, transfers between agents, and maintains workflow state.

### Commit
`feat(agent): implement CoordinatorAgent`

---

# Sprint 2 — Core Agents
- Task 1: `DatasetResolver` -> `feat(agent): implement DatasetResolver`
- Task 2: `DataEngineer` -> `feat(agent): implement DataEngineer`
- Task 3: `Statistician` -> `feat(agent): implement Statistician`
- Task 4: `ARIMAExpert` -> `feat(agent): implement ARIMAExpert`
- Task 5: `QualityAssurance` -> `feat(agent): implement QualityAssurance`
- Task 6: `ReportingAgent` -> `feat(agent): implement ReportingAgent`

---

# Sprint 3 — Tools
- Storage tools (GCS, Local Files, CSV Reader) -> `feat(tool): storage tools`
- Statistics tools (ADF, KPSS, Ljung-Box, ACF, PACF) -> `feat(tool): statistics tools`
- Forecasting tools (ARIMA, SARIMA, AutoARIMA) -> `feat(tool): forecasting tools`
- Validation tools (RMSE, MAE, MAPE, SMAPE) -> `feat(tool): validation tools`
- Visualisation tools (Trend, Residuals, Forecast, Seasonality) -> `feat(tool): visualisation tools`

---

# Sprint 4 — Google Cloud
- Google Cloud Storage -> `feat(gcp): integrate Cloud Storage`
- BigQuery -> `feat(gcp): integrate BigQuery`
- Secret Manager -> `feat(gcp): integrate Secret Manager`
- Vertex AI -> `feat(gcp): integrate Vertex AI`
- MCP -> `feat(gcp): integrate MCP servers`

---

# Sprint 5 — Deployment
- Cloud Run -> `feat(deployment): deploy Cloud Run`
- Vertex Agent Engine -> `feat(deployment): deploy Agent Engine`
- CI/CD -> `feat(ci): GitHub Actions pipeline`
- Docker -> `feat(devops): containerize platform`

---

# Sprint 6 — Enterprise Features
- Evaluation -> `feat(evaluation): add evaluation framework`
- Observability -> `feat(observability): add monitoring`
- Security -> `feat(security): add security layer`
- Memory -> `feat(memory): add memory subsystem`
