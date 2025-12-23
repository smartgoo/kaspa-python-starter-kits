"""Dependency injection for {{ cookiecutter.project_name }}."""

from .client import get_client

__all__ = [
    "get_client",
]
