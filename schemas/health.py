"""Response schema for the service health check.

Moved from payloads/HealthPayload.py to schemas module for consistency.
"""

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Body of `GET /`."""

    status: str = Field(..., examples=["ok"])
    message: str = Field(..., examples=["Welcome to the Products API"])