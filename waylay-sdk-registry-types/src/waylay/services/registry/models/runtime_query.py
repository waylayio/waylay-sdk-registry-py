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
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.archive_format import ArchiveFormat
from ..models.function_type import FunctionType
from ..models.latest_version_level import LatestVersionLevel
from ..models.semantic_version_range import SemanticVersionRange


class RuntimeQuery(WaylayBaseModel):
    """RuntimeQuery."""

    version: SemanticVersionRange | None = None
    latest: LatestVersionLevel | None = None
    include_deprecated: StrictBool | None = Field(
        default=False,
        description="If set to `true`, deprecated runtimes will be included in the query.",
        alias="includeDeprecated",
    )
    name: StrictStr | None = Field(
        default=None,
        description="If set, filters on the <code>name</code> of a runtime. Supports <code>*</code> and <code>?</code> wildcards and is case-insensitive.",
    )
    function_type: List[FunctionType] | None = Field(
        default=None,
        description="If set, filters on the <code>functionType</code> of a runtime. Uses an exact match.",
        alias="functionType",
    )
    archive_format: List[ArchiveFormat] | None = Field(
        default=None,
        description="If set, filters on the <code>archiveFormat</code> of a runtime. Uses an exact match.",
        alias="archiveFormat",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
