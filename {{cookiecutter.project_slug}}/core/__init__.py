"""Core modules for {{ cookiecutter.project_name }}."""

from .config import Settings, get_settings

__version__ = "0.1.0"

__all__ = [
    "Settings",
    "__version__",
    "get_settings",
]

