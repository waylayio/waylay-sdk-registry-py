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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from ..models.plug_property_data_type import PlugPropertyDataType
from ..models.plug_property_format import PlugPropertyFormat


from typing import cast

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class PlugProperty(BaseModel):
    """Interface specification of a plug property.."""

    name: StrictStr = Field(description="The name of a plug input or output property.")
    data_type: Optional[PlugPropertyDataType] = Field(default=None, alias="dataType")
    mandatory: Optional[StrictBool] = Field(
        default=None, description="If <code>true</code> this property is required."
    )
    format: Optional[PlugPropertyFormat] = None
    default_value: Optional[Any] = Field(default=None, alias="defaultValue")
    __properties: ClassVar[List[str]] = [
        "name",
        "dataType",
        "mandatory",
        "format",
        "defaultValue",
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
        """Create an instance of PlugProperty from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of format
        if self.format:
            _dict["format"] = self.format.to_dict()
        # set to None if default_value (nullable) is None
        # and model_fields_set contains the field
        if self.default_value is None and "default_value" in self.model_fields_set:
            _dict["defaultValue"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PlugProperty from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "dataType": obj.get("dataType"),
                "mandatory": obj.get("mandatory"),
                "format": (
                    PlugPropertyFormat.from_dict(cast(dict, obj.get("format")))
                    if obj.get("format") is not None
                    else None
                ),
                "defaultValue": obj.get("defaultValue"),
            }
        )
        return _obj
