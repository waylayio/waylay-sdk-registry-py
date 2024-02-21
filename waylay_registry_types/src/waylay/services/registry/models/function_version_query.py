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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from ..models.semantic_version_range import SemanticVersionRange
from ..models.status_filter import StatusFilter
from ..models.timestamp_spec import TimestampSpec


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class FunctionVersionQuery(BaseModel):
    """Filter on function attributes that can change across function versions. When these query parameters are used, the query is considered a _function version_ listing and no HAL links to latest (_draft_, _published_) versions are included.."""

    version: Optional[StrictStr] = Field(default=None, description="Filter on the version of the function (case-sensitive, supports wildcards).")
    status: Optional[List[StatusFilter]] = Field(default=None, description="Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.")
    runtime_version: Optional[SemanticVersionRange] = Field(default=None, alias="runtimeVersion")
    created_by: Optional[StrictStr] = Field(default=None, description="Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.", alias="createdBy")
    updated_by: Optional[StrictStr] = Field(default=None, description="Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.", alias="updatedBy")
    created_before: Optional[TimestampSpec] = Field(default=None, alias="createdBefore")
    created_after: Optional[TimestampSpec] = Field(default=None, alias="createdAfter")
    updated_before: Optional[TimestampSpec] = Field(default=None, alias="updatedBefore")
    updated_after: Optional[TimestampSpec] = Field(default=None, alias="updatedAfter")
    __properties: ClassVar[List[str]] = ["version", "status", "runtimeVersion", "createdBy", "updatedBy", "createdBefore", "createdAfter", "updatedBefore", "updatedAfter"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def to_str(self) -> str:
        """Get the string representation of the model using alias."""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Get the JSON representation of the model using alias."""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict(), default=str)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FunctionVersionQuery from a JSON string."""
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
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in status (list)
        _items = []
        if self.status:
            for _item in self.status:  # type: ignore
                if _item:
                    _items.append(_item.to_dict())
            _dict['status'] = _items
        # override the default output from pydantic by calling `to_dict()` of runtime_version
        if self.runtime_version:
            _dict['runtimeVersion'] = self.runtime_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_before
        if self.created_before:
            _dict['createdBefore'] = self.created_before.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_after
        if self.created_after:
            _dict['createdAfter'] = self.created_after.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_before
        if self.updated_before:
            _dict['updatedBefore'] = self.updated_before.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_after
        if self.updated_after:
            _dict['updatedAfter'] = self.updated_after.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FunctionVersionQuery from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "version": obj.get("version"),
            "status": [StatusFilter.from_dict(_item) for _item in obj.get("status")] if obj.get("status") is not None else None,  # type: ignore
            "runtimeVersion": SemanticVersionRange.from_dict(obj.get("runtimeVersion")) if obj.get("runtimeVersion") is not None else None,    # type: ignore
            "createdBy": obj.get("createdBy"),
            "updatedBy": obj.get("updatedBy"),
            "createdBefore": TimestampSpec.from_dict(obj.get("createdBefore")) if obj.get("createdBefore") is not None else None,    # type: ignore
            "createdAfter": TimestampSpec.from_dict(obj.get("createdAfter")) if obj.get("createdAfter") is not None else None,    # type: ignore
            "updatedBefore": TimestampSpec.from_dict(obj.get("updatedBefore")) if obj.get("updatedBefore") is not None else None,    # type: ignore
            "updatedAfter": TimestampSpec.from_dict(obj.get("updatedAfter")) if obj.get("updatedAfter") is not None else None    # type: ignore
        })
        return _obj
