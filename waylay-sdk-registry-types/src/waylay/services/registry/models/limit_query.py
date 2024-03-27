# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class LimitQuery(WaylayBaseModel):
    """LimitQuery."""

    limit: (
        Annotated[float, Field(strict=True, ge=0)]
        | Annotated[int, Field(strict=True, ge=0)]
        | None
    ) = Field(
        default=None,
        description="The maximum number of items to be return from this query. Has a deployment-defined default and maximum value.",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
