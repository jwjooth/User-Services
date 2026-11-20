"""Product request/response schemas.

Moved from payloads/ProductPayload.py to separate schemas module
to remove cyclic dependency: entity → payload → service.
"""

from datetime import datetime
from decimal import Decimal

from pydantic import Field

from schemas.base import BaseEntity, BaseEntityOutput


class ProductCreateInput(BaseEntity):
    """Body of `POST /api/v1/products`."""

    name: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Unique display name, compared case-insensitively.",
        examples=["Mechanical Keyboard"],
    )
    description: str | None = Field(
        default=None,
        max_length=2000,
        description="Optional free-form description.",
        examples=["Mechanical keyboard"],
    )
    price: Decimal = Field(
        ...,
        gt=0,
        max_digits=10,
        decimal_places=2,
        description="Unit price with at most two decimal places.",
        examples=["49.99"],
    )
    stock: int = Field(..., gt=0, description="Units currently in stock.")


class ProductUpdateInput(BaseEntity):
    """Body of `PUT /api/v1/products/{product_id}`."""

    name: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Unique display name, compared case-insensitively.",
        examples=["Mechanical Keyboard"],
    )
    description: str | None = Field(
        default=None,
        max_length=2000,
        description="Optional free-form description.",
        examples=["Mechanical keyboard"],
    )
    price: Decimal = Field(
        ...,
        gt=0,
        max_digits=10,
        decimal_places=2,
        description="Unit price with at most two decimal places.",
        examples=["49.99"],
    )
    stock: int = Field(..., gt=0, description="Units currently in stock.")


class ProductResponse(BaseEntityOutput):
    """Representation of a product."""

    id: int
    name: str
    description: str | None
    price: Decimal
    stock: int
    created_at: datetime
    updated_at: datetime