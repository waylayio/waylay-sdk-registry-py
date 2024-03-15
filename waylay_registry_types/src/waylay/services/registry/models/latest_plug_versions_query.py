# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import re  # noqa: F401
from pydantic import ConfigDict, SerializationInfo, model_serializer, StrictStr
from typing import Callable, Union
from typing_extensions import (
    Self,  # >=3.11
)

from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from ..models.archive_format import ArchiveFormat
from ..models.plug_type import PlugType
from ..models.semantic_version_range import SemanticVersionRange
from ..models.status_filter import StatusFilter
from ..models.tags_filter import TagsFilter
from ..models.timestamp_spec import TimestampSpec


class LatestPlugVersionsQuery(BaseModel):
    """Plug versions listing query.."""

    tags: Optional[TagsFilter] = None
    type: Optional[PlugType] = None
    limit: Optional[
        Union[
            Annotated[float, Field(strict=True, ge=0)],
            Annotated[int, Field(strict=True, ge=0)],
        ]
    ] = Field(
        default=None,
        description="The maximum number of items to be return from this query. Has a deployment-defined default and maximum value.",
    )
    page: Optional[
        Union[
            Annotated[float, Field(strict=True, ge=0)],
            Annotated[int, Field(strict=True, ge=0)],
        ]
    ] = Field(
        default=None,
        description="The number of pages to skip when returning result to this query.",
    )
    include_draft: Optional[StrictBool] = Field(
        default=None,
        description="Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**.",
        alias="includeDraft",
    )
    include_deprecated: Optional[StrictBool] = Field(
        default=None,
        description="Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**.",
        alias="includeDeprecated",
    )
    deprecated: Optional[StrictBool] = Field(
        default=None, description="Filter on the deprecation status of the function."
    )
    draft: Optional[StrictBool] = Field(
        default=None, description="Filter on the draft status of the function."
    )
    name_version: Optional[List[Annotated[str, Field(strict=True)]]] = Field(
        default=None,
        description="Filter on exact `{name}@{version}` functions. Using this filter implies a `latest=false` default, returning multiple versions of the same named versions if they are filtered.",
        alias="nameVersion",
    )
    version: Optional[StrictStr] = Field(
        default=None,
        description="Filter on the version of the function (case-sensitive, supports wildcards).",
    )
    status: Optional[List[StatusFilter]] = Field(
        default=None,
        description="Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
    )
    runtime_version: Optional[SemanticVersionRange] = Field(
        default=None, alias="runtimeVersion"
    )
    created_by: Optional[StrictStr] = Field(
        default=None,
        description="Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
        alias="createdBy",
    )
    updated_by: Optional[StrictStr] = Field(
        default=None,
        description="Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
        alias="updatedBy",
    )
    created_before: Optional[TimestampSpec] = Field(default=None, alias="createdBefore")
    created_after: Optional[TimestampSpec] = Field(default=None, alias="createdAfter")
    updated_before: Optional[TimestampSpec] = Field(default=None, alias="updatedBefore")
    updated_after: Optional[TimestampSpec] = Field(default=None, alias="updatedAfter")
    name: Optional[StrictStr] = Field(
        default=None,
        description="Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters).",
    )
    archive_format: Optional[List[ArchiveFormat]] = Field(
        default=None,
        description="Filter on the archive format of the function.",
        alias="archiveFormat",
    )
    runtime: Optional[List[StrictStr]] = Field(
        default=None, description="Filter on the runtime of the function."
    )
    latest: Optional[StrictBool] = Field(
        default=None,
        description="When `true`, only the latest version per function name is returned. If set to `false`, multiple versions per named function can be returned. Defaults to `true`, except when specific versions are selected with the `nameVersion` filter.",
    )
    show_related: Optional[StrictStr] = Field(default=None, alias="showRelated")

    @field_validator("show_related")
    @classmethod
    def show_related_validate_enum(cls, value):
        """Validate the enum."""
        if value is None:
            return value
        if value not in ("none"):
            raise ValueError("must be one of enum values ('none')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )

    @model_serializer(mode="wrap")
    def serializer(
        self, handler: Callable, info: SerializationInfo
    ) -> Dict[StrictStr, Any]:
        """The default serializer of the model.

        * Excludes `None` fields that were not set at model initialization.
        """
        model_dict = handler(self, info)
        return {
            k: v
            for k, v in model_dict.items()
            if v is not None or k in self.model_fields_set
        }

    def to_dict(self) -> dict[str, Any]:
        """Convert the LatestPlugVersionsQuery instance to dict."""
        return self.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)

    def to_json(self) -> str:
        """Convert the LatestPlugVersionsQuery instance to a JSON-encoded string."""
        return self.model_dump_json(
            by_alias=True, exclude_unset=True, exclude_none=True
        )

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create a LatestPlugVersionsQuery instance from a dict."""
        return cls.model_validate(obj)

    @classmethod
    def from_json(cls, json_data: Union[str, bytes, bytearray]) -> Self:
        """Create a LatestPlugVersionsQuery instance from a JSON-encoded string."""
        return cls.model_validate_json(json_data)
