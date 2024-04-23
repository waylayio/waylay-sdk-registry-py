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
from ..models.plug_type import PlugType


class LatestPlugsQuery(WaylayBaseModel):
    """Latest plug versions listing query with latest links. A request that only uses these query parameters will include links to the _latest_ draft/published versions of the plug.."""

    type: PlugType | None = None
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
    name: StrictStr | None = Field(
        default=None,
        description="Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters).",
    )
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
