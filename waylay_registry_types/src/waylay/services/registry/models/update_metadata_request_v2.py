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
from ..models.tag import Tag


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class UpdateMetadataRequestV2(BaseModel):
    """UpdateMetadataRequestV2."""

    author: Optional[StrictStr] = Field(default=None, description="The author of the function.")
    description: Optional[StrictStr] = Field(default=None, description="A description of the function")
    icon_url: Optional[StrictStr] = Field(default=None, description="An url to an icon that represents this function.", alias="iconURL")
    category: Optional[StrictStr] = Field(default=None, description="A category for this function (Deprecated: use tags to categorise your functions)")
    documentation_url: Optional[StrictStr] = Field(default=None, description="External url that document this function.", alias="documentationURL")
    tags: Optional[List[Tag]] = Field(default=None, description="Tags associated with this function.")
    friendly_name: Optional[StrictStr] = Field(default=None, description="Display title for this function.", alias="friendlyName")
    __properties: ClassVar[List[str]] = ["author", "description", "iconURL", "category", "documentationURL", "tags", "friendlyName"]

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
        """Create an instance of UpdateMetadataRequestV2 from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:  # type: ignore
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdateMetadataRequestV2 from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "author": obj.get("author"),
            "description": obj.get("description"),
            "iconURL": obj.get("iconURL"),
            "category": obj.get("category"),
            "documentationURL": obj.get("documentationURL"),
            "tags": [Tag.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,  # type: ignore
            "friendlyName": obj.get("friendlyName")
        })
        return _obj
