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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from ..models.legacy_plug_script_meta_raw_data_inner import (
    LegacyPlugScriptMetaRawDataInner,
)
from ..models.legacy_required_properties_inner import LegacyRequiredPropertiesInner
from ..models.tag import Tag


from typing import cast

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class LegacyPlugScriptMeta(BaseModel):
    """LegacyPlugScriptMeta."""

    author: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    category: Optional[StrictStr] = None
    tags: Optional[List[Tag]] = None
    icon_url: Optional[StrictStr] = Field(default=None, alias="iconURL")
    friendly_name: Optional[StrictStr] = Field(default=None, alias="friendlyName")
    supported_states: List[StrictStr] = Field(alias="supportedStates")
    raw_data: List[LegacyPlugScriptMetaRawDataInner] = Field(alias="rawData")
    required_properties: Optional[List[LegacyRequiredPropertiesInner]] = Field(
        default=None, alias="requiredProperties"
    )
    __properties: ClassVar[List[str]] = [
        "author",
        "description",
        "category",
        "tags",
        "iconURL",
        "friendlyName",
        "supportedStates",
        "rawData",
        "requiredProperties",
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
        """Create an instance of LegacyPlugScriptMeta from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in cast(list, self.tags):
                if _item:
                    _items.append(_item.to_dict())
            _dict["tags"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in raw_data (list)
        _items = []
        if self.raw_data:
            for _item in cast(list, self.raw_data):
                if _item:
                    _items.append(_item.to_dict())
            _dict["rawData"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in required_properties (list)
        _items = []
        if self.required_properties:
            for _item in cast(list, self.required_properties):
                if _item:
                    _items.append(_item.to_dict())
            _dict["requiredProperties"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LegacyPlugScriptMeta from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "author": obj.get("author"),
                "description": obj.get("description"),
                "category": obj.get("category"),
                "tags": [
                    Tag.from_dict(cast(dict, _item))
                    for _item in cast(list, obj.get("tags"))
                ]
                if obj.get("tags") is not None
                else None,
                "iconURL": obj.get("iconURL"),
                "friendlyName": obj.get("friendlyName"),
                "supportedStates": obj.get("supportedStates"),
                "rawData": [
                    LegacyPlugScriptMetaRawDataInner.from_dict(cast(dict, _item))
                    for _item in cast(list, obj.get("rawData"))
                ]
                if obj.get("rawData") is not None
                else None,
                "requiredProperties": [
                    LegacyRequiredPropertiesInner.from_dict(cast(dict, _item))
                    for _item in cast(list, obj.get("requiredProperties"))
                ]
                if obj.get("requiredProperties") is not None
                else None,
            }
        )
        return _obj
