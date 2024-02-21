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
from ..models.documentation_property import DocumentationProperty


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Documentation(BaseModel):
    """Documentation."""

    description: Optional[StrictStr] = None
    states: Optional[List[DocumentationProperty]] = Field(default=None, description="Documentation of the plug states.")
    input: Optional[List[DocumentationProperty]] = Field(default=None, description="Documentation of the plug input parameters.")
    output: Optional[List[DocumentationProperty]] = Field(default=None, description="Documentation of the plug response parameters.")
    __properties: ClassVar[List[str]] = ["description", "states", "input", "output"]

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
        """Create an instance of Documentation from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of each item in states (list)
        _items = []
        if self.states:
            for _item in self.states:  # type: ignore
                if _item:
                    _items.append(_item.to_dict())
            _dict['states'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in input (list)
        _items = []
        if self.input:
            for _item in self.input:  # type: ignore
                if _item:
                    _items.append(_item.to_dict())
            _dict['input'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in output (list)
        _items = []
        if self.output:
            for _item in self.output:  # type: ignore
                if _item:
                    _items.append(_item.to_dict())
            _dict['output'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Documentation from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "states": [DocumentationProperty.from_dict(_item) for _item in obj.get("states")] if obj.get("states") is not None else None,  # type: ignore
            "input": [DocumentationProperty.from_dict(_item) for _item in obj.get("input")] if obj.get("input") is not None else None,  # type: ignore
            "output": [DocumentationProperty.from_dict(_item) for _item in obj.get("output")] if obj.get("output") is not None else None  # type: ignore
        })
        return _obj
