"""Routes package.

This module re-exports the FastAPI `app` object so that a command
like `uvicorn app.api.routes:app --reload` works.
"""
from .portfolio import app  # noqa: F401
