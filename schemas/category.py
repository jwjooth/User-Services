"""Category request/response schemas.

Moved from payloads/CategoryPayload.py to separate schemas module
to remove cyclic dependency: entity → payload → service.
"""

from datetime import datetime

from pydantic import Field

from schemas.base import BaseEntity, BaseEntityOutput


class CategoryCreateInput(BaseEntity):
    """Body of `POST /api/v1/categories`."""

    name: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Unique display name, compared case-insensitively.",
        examples=["Fiction"],
    )


class CategoryUpdateInput(BaseEntity):
    """Body of `PUT /api/v1/categories/{category_id}`."""

    name: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Unique display name, compared case-insensitively.",
        examples=["Fiction"],
    )


class CategoryResponse(BaseEntityOutput):
    """Representation of a category."""

    id: int
    name: str
    created_at: datetime
    updated_at: datetime