# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictFloat,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.any_function_response import AnyFunctionResponse


class VersionsResponseV2(WaylayBaseModel):
    """Version Listing Response."""

    limit: StrictFloat | StrictInt | None = Field(
        default=None, description="The page size used for this query result."
    )
    count: StrictFloat | StrictInt = Field(
        description="The total count of matching items, from which this result is one page."
    )
    page: StrictFloat | StrictInt | None = Field(
        default=None, description="The page number of a paged query result."
    )
    entities: List[AnyFunctionResponse] = Field(
        description="The specification and deployment status of the queried functions"
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
