"""API response schemas for {{ cookiecutter.project_name }}."""

from .common import ErrorResponse, HealthResponse
from .kaspa import BlockDagInfoResponse, BlockResponse

__all__ = [
    "BlockDagInfoResponse",
    "BlockResponse",
    "ErrorResponse",
    "HealthResponse",
]

