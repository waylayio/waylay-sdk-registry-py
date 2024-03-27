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
    StrictBool,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class DeprecatedDraftFilter(WaylayBaseModel):
    """DeprecatedDraftFilter."""

    deprecated: StrictBool | None = Field(
        default=None, description="Filter on the deprecation status of the function."
    )
    draft: StrictBool | None = Field(
        default=None, description="Filter on the draft status of the function."
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
