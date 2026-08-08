"""Domain exceptions definition module."""


class DomainError(Exception):
    """Base exception for all domain errors."""


class AgentError(DomainError):
    """Raised when an agent operation fails."""


class ForecastingJobError(DomainError):
    """Raised when a forecasting job operation fails."""


class StorageError(DomainError):
    """Raised when a storage operation fails."""


class StateError(DomainError):
    """Raised when a state management operation fails."""
