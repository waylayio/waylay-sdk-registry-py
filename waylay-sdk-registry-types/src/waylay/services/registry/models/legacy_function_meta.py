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
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.tag import Tag


class LegacyFunctionMeta(WaylayBaseModel):
    """LegacyFunctionMeta."""

    author: StrictStr | None = None
    description: StrictStr | None = None
    category: StrictStr | None = None
    tags: List[Tag] | None = None
    icon_url: StrictStr | None = Field(default=None, alias="iconURL")
    friendly_name: StrictStr | None = Field(default=None, alias="friendlyName")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
