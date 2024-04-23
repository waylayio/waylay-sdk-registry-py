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


class VersionIncludes(WaylayBaseModel):
    """VersionIncludes."""

    include_draft: StrictBool | None = Field(
        default=None,
        description="Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**.",
        alias="includeDraft",
    )
    include_deprecated: StrictBool | None = Field(
        default=None,
        description="Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**.",
        alias="includeDeprecated",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
