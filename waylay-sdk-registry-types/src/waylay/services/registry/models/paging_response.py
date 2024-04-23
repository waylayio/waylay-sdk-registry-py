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
    StrictFloat,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class PagingResponse(WaylayBaseModel):
    """PagingResponse."""

    count: StrictFloat | StrictInt | None = Field(
        default=None,
        description="The total count of matching items, from which this result is one page.",
    )
    limit: StrictFloat | StrictInt | None = Field(
        default=None, description="The page size used for this query result."
    )
    page: StrictFloat | StrictInt | None = Field(
        default=None, description="The page number of a paged query result."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
