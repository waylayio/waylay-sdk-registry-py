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
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.archive_format import ArchiveFormat
from ..models.semantic_version_range import SemanticVersionRange
from ..models.status_filter import StatusFilter
from ..models.timestamp_spec import TimestampSpec


class NamedKFServingVersionsQueryV2(WaylayBaseModel):
    """Named Model versions query.."""

    limit: (
        Annotated[float, Field(strict=True, ge=0)]
        | Annotated[int, Field(strict=True, ge=0)]
        | None
    ) = Field(
        default=None,
        description="The maximum number of items to be return from this query. Has a deployment-defined default and maximum value.",
    )
    page: (
        Annotated[float, Field(strict=True, ge=0)]
        | Annotated[int, Field(strict=True, ge=0)]
        | None
    ) = Field(
        default=None,
        description="The number of pages to skip when returning result to this query.",
    )
    deprecated: StrictBool | None = Field(
        default=None, description="Filter on the deprecation status of the function."
    )
    draft: StrictBool | None = Field(
        default=None, description="Filter on the draft status of the function."
    )
    version: StrictStr | None = Field(
        default=None,
        description="Filter on the version of the function (case-sensitive, supports wildcards).",
    )
    status: List[StatusFilter] | None = Field(
        default=None,
        description="Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
    )
    runtime_version: SemanticVersionRange | None = Field(
        default=None, alias="runtimeVersion"
    )
    created_by: StrictStr | None = Field(
        default=None,
        description="Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
        alias="createdBy",
    )
    updated_by: StrictStr | None = Field(
        default=None,
        description="Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
        alias="updatedBy",
    )
    created_before: TimestampSpec | None = Field(default=None, alias="createdBefore")
    created_after: TimestampSpec | None = Field(default=None, alias="createdAfter")
    updated_before: TimestampSpec | None = Field(default=None, alias="updatedBefore")
    updated_after: TimestampSpec | None = Field(default=None, alias="updatedAfter")
    archive_format: List[ArchiveFormat] | None = Field(
        default=None,
        description="Filter on the archive format of the function.",
        alias="archiveFormat",
    )
    runtime: List[StrictStr] | None = Field(
        default=None, description="Filter on the runtime of the function."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
