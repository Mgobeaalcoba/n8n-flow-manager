"""
n8n-flow-manager: A robust SDK and CLI for n8n workflow automation.

This package provides a modern, async-first Python client for the n8n Public API
with strong typing, validation, and DevOps capabilities.
"""

from .client import N8NClient
from .exceptions import (
    N8NAPIError,
    N8NAuthError,
    N8NError,
    N8NNotFoundError,
    N8NValidationError,
)
from .models.execution import Execution, ExecutionStatus
from .models.workflow import Connection, Node, Workflow

__version__ = "0.1.3"
__all__ = [
    "N8NClient",
    "N8NError",
    "N8NAuthError",
    "N8NNotFoundError",
    "N8NValidationError",
    "N8NAPIError",
    "Workflow",
    "Node",
    "Connection",
    "Execution",
    "ExecutionStatus",
]
