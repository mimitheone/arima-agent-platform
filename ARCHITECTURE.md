# ARIMA Agent Platform - System Architecture

## 1. Overview
ARIMA Agent Platform is an enterprise-ready, multi-agent platform designed to orchestrate, execute, and evaluate time series forecasting workflows using Google ADK and Clean Architecture principles.

---

## 2. High-Level Architecture Diagram

```mermaid
graph TD
    Client[Client / Trigger] --> AppService[Application Layer: Services & Workflows]
    
    subgraph Core
        DomainEntities[Domain Entities: forecast, dataset, model, agent, time_series]
        DomainServices[Domain Services: forecasting_service, validation_service]
    end

    subgraph Workflows & Orchestration
        AppService --> ARIMAWorkflow[ARIMA Workflow (Deterministic Python Coordinator)]
    end

    subgraph Adapters
        ARIMAWorkflow --> Agents[ADK Agents: Data Engineer, Statistician, ARIMA, QA, Reporting]
        ARIMAWorkflow --> Tools[Categorized Tools: Storage, Statistics, Forecasting, Validation, Visualization]
        ARIMAWorkflow --> Contracts[Contracts: Messages, Events, Requests, Results]
    end

    subgraph Infrastructure & Cloud
        Agents --> ADK[Google ADK Runner]
        Tools --> GCP[GCP Services: GCS, BigQuery, PubSub, Secret Manager, Vertex, Logging]
        Agents --> State[State Storage / Memory]
        Agents --> Observability[Observability: Tracing, Logging, Metrics]
    end

    subgraph Evaluation
        Eval[Evaluation Framework: Datasets, Benchmarks, Metrics, Goldens]
    end
```

---

## 3. Layer Architecture Breakdown

| Layer | Path | Description |
| :--- | :--- | :--- |
| **Domain** | `src/arima_agent_platform/domain/` | Entities (`forecast`, `dataset`, `model`, `agent`, `time_series`), Domain Services (`forecasting_service`, `validation_service`), Interfaces, and Exceptions. |
| **Application** | `src/arima_agent_platform/application/` | DTOs, Application Services (`forecasting_application_service`, `agent_execution_service`), Application Agent Contracts, and Workflows (`arima_workflow.py`). |
| **Adapters** | `src/arima_agent_platform/adapters/` | Deterministic Coordinator Protocol, Specialized Agent Protocols, Categorized Tools, and Contracts. |
| **Infrastructure** | `src/arima_agent_platform/infrastructure/` | GCP wrappers, ADK Runner, State Repositories, Observability (`tracing`, `logging`, `metrics`). |
| **Evaluation** | `src/arima_agent_platform/evaluation/` | Datasets, Benchmarks, Metrics, and Golden Datasets. |
| **Prompts** | `src/arima_agent_platform/prompts/` | Agent System Prompt Markdown Templates. |
