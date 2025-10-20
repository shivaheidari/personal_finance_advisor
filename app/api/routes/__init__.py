"""Routes package.

This package exposes route modules. Do not re-export `app` here. The
FastAPI application instance lives in `app.main`.
"""
from . import portfolio  # noqa: F401

__all__ = ["portfolio"]
