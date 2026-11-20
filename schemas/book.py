"""Book request/response schemas.

Moved from payloads/BookPayload.py to separate schemas module
to remove cyclic dependency: entity → payload → service.
"""

from datetime import datetime

from pydantic import Field

from schemas.base import BaseEntity, BaseEntityOutput


class BookCreateInput(BaseEntity):
    """Body of `POST /api/v1/books`."""

    category_id: int = Field(..., gt=0, description="Existing category id.")
    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Unique title, compared case-insensitively.",
        examples=["Dune"],
    )
    author: str = Field(..., min_length=1, max_length=255, examples=["Frank Herbert"])
    stock: int = Field(..., ge=0, description="Copies currently in stock.")


class BookUpdateInput(BaseEntity):
    """Body of `PUT /api/v1/books/{book_id}`."""

    category_id: int = Field(..., gt=0, description="Existing category id.")
    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Unique title, compared case-insensitively.",
        examples=["Dune"],
    )
    author: str = Field(..., min_length=1, max_length=255, examples=["Frank Herbert"])
    stock: int = Field(..., ge=0, description="Copies currently in stock.")


class BookResponse(BaseEntityOutput):
    """Representation of a book."""

    id: int
    category_id: int
    title: str
    author: str
    stock: int
    created_at: datetime
    updated_at: datetime