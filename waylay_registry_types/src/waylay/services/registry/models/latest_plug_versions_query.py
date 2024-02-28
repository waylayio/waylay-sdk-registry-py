# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
from pydantic import ConfigDict


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from ..models.archive_format import ArchiveFormat
from ..models.plug_type import PlugType
from ..models.semantic_version_range import SemanticVersionRange
from ..models.status_filter import StatusFilter
from ..models.tags_filter import TagsFilter
from ..models.timestamp_spec import TimestampSpec


from typing import cast

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


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
    __properties: ClassVar[List[str]] = [
        "tags",
        "type",
        "limit",
        "page",
        "includeDraft",
        "includeDeprecated",
        "deprecated",
        "draft",
        "nameVersion",
        "version",
        "status",
        "runtimeVersion",
        "createdBy",
        "updatedBy",
        "createdBefore",
        "createdAfter",
        "updatedBefore",
        "updatedAfter",
        "name",
        "archiveFormat",
        "runtime",
        "latest",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Get the string representation of the model using alias."""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Get the JSON representation of the model using alias."""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict(), default=str)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LatestPlugVersionsQuery from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        # pylint: disable=not-an-iterable, no-member, unsupported-membership-test
        # pylint has some issues with `field` https://github.com/pylint-dev/pylint/issues/7437, so disable some checks
        """Get the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict["tags"] = self.tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in status (list)
        _items = []
        if self.status:
            for _item in cast(list, self.status):
                if _item:
                    _items.append(_item.to_dict())
            _dict["status"] = _items
        # override the default output from pydantic by calling `to_dict()` of runtime_version
        if self.runtime_version:
            _dict["runtimeVersion"] = self.runtime_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_before
        if self.created_before:
            _dict["createdBefore"] = self.created_before.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_after
        if self.created_after:
            _dict["createdAfter"] = self.created_after.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_before
        if self.updated_before:
            _dict["updatedBefore"] = self.updated_before.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_after
        if self.updated_after:
            _dict["updatedAfter"] = self.updated_after.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LatestPlugVersionsQuery from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "tags": (
                    TagsFilter.from_dict(cast(dict, obj.get("tags")))
                    if obj.get("tags") is not None
                    else None
                ),
                "type": obj.get("type"),
                "limit": obj.get("limit"),
                "page": obj.get("page"),
                "includeDraft": obj.get("includeDraft"),
                "includeDeprecated": obj.get("includeDeprecated"),
                "deprecated": obj.get("deprecated"),
                "draft": obj.get("draft"),
                "nameVersion": obj.get("nameVersion"),
                "version": obj.get("version"),
                "status": [
                    StatusFilter.from_dict(cast(dict, _item))
                    for _item in cast(list, obj.get("status"))
                ]
                if obj.get("status") is not None
                else None,
                "runtimeVersion": (
                    SemanticVersionRange.from_dict(
                        cast(dict, obj.get("runtimeVersion"))
                    )
                    if obj.get("runtimeVersion") is not None
                    else None
                ),
                "createdBy": obj.get("createdBy"),
                "updatedBy": obj.get("updatedBy"),
                "createdBefore": (
                    TimestampSpec.from_dict(cast(dict, obj.get("createdBefore")))
                    if obj.get("createdBefore") is not None
                    else None
                ),
                "createdAfter": (
                    TimestampSpec.from_dict(cast(dict, obj.get("createdAfter")))
                    if obj.get("createdAfter") is not None
                    else None
                ),
                "updatedBefore": (
                    TimestampSpec.from_dict(cast(dict, obj.get("updatedBefore")))
                    if obj.get("updatedBefore") is not None
                    else None
                ),
                "updatedAfter": (
                    TimestampSpec.from_dict(cast(dict, obj.get("updatedAfter")))
                    if obj.get("updatedAfter") is not None
                    else None
                ),
                "name": obj.get("name"),
                "archiveFormat": obj.get("archiveFormat"),
                "runtime": obj.get("runtime"),
                "latest": obj.get("latest"),
            }
        )
        return _obj
