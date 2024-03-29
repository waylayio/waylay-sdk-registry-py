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


class UserPlugMeta(WaylayBaseModel):
    """Plug metadata that the user can update as `metadata`."""

    author: StrictStr | None = Field(
        default=None, description="The author of the function."
    )
    description: StrictStr | None = Field(
        default=None, description="A description of the function"
    )
    icon_url: StrictStr | None = Field(
        default=None,
        description="An url to an icon that represents this function.",
        alias="iconURL",
    )
    category: StrictStr | None = Field(
        default=None,
        description="A category for this function (Deprecated: use tags to categorise your functions)",
    )
    documentation_url: StrictStr | None = Field(
        default=None,
        description="External url that document this function.",
        alias="documentationURL",
    )
    tags: List[Tag] | None = Field(
        default=None, description="Tags associated with this function."
    )
    friendly_name: StrictStr | None = Field(
        default=None,
        description="Display title for this function.",
        alias="friendlyName",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
