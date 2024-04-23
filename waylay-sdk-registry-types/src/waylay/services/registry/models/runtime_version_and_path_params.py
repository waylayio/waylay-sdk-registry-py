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
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.semantic_version_range import SemanticVersionRange


class RuntimeVersionAndPathParams(WaylayBaseModel):
    """RuntimeVersionAndPathParams."""

    wildcard: StrictStr = Field(
        description="Full path or path prefix of the asset within the archive",
        alias="*",
    )
    name: StrictStr
    version: SemanticVersionRange

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
