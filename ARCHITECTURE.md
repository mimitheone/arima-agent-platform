# ARIMA Agent Platform - System Architecture

## 1. Overview
ARIMA Agent Platform is an enterprise-ready, multi-agent platform designed to orchestrate, execute, and evaluate time series forecasting workflows using Google ADK and Clean Architecture principles.

---

## 2. High-Level Architecture Diagram

```mermaid
graph TD
    Client[Client / Trigger] --> App[Application Layer: Workflows & DTOs]
    
    subgraph Core
        Domain[Domain Layer: Entities & Interfaces]
    end

    subgraph Adapters
        App --> Agents[Agents: Coordinator, Data Engineer, Statistician, ARIMA, QA, Reporting]
        App --> Tools[Categorized Tools: Storage, Statistics, Forecasting, Validation, Visualization]
        App --> Contracts[Contracts: Messages, Events, Requests, Results]
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
| **Domain** | `src/arima_agent_platform/domain/` | Enterprise Entities, Value Objects, Domain Interfaces, Exceptions. |
| **Application** | `src/arima_agent_platform/application/` | DTOs, Service Interfaces, and Workflow Orchestrators. |
| **Adapters** | `src/arima_agent_platform/adapters/` | Agent protocols, Categorized Tools, and Data Contracts. |
| **Infrastructure** | `src/arima_agent_platform/infrastructure/` | GCP wrappers, ADK Runner, State Repositories, Observability. |
| **Evaluation** | `src/arima_agent_platform/evaluation/` | Datasets, Benchmarks, Metrics, and Golden Datasets. |
| **Prompts** | `src/arima_agent_platform/prompts/` | Agent System Prompt Markdown Templates. |
