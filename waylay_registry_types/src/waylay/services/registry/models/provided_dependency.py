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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field


from typing_extensions import (
    Self,  # >=3.11
)


class ProvidedDependency(BaseModel):
    """Library dependency that is provided by this runtime.."""

    name: StrictStr = Field(description="Name of a provided dependency.")
    title: Optional[StrictStr] = Field(
        default=None, description="Optional display title."
    )
    description: Optional[StrictStr] = Field(
        default=None, description="Optional description."
    )
    version: Optional[StrictStr] = Field(
        default=None, description="Versions specification of a provided dependency"
    )
    deprecated: Optional[StrictBool] = Field(
        default=False,
        description="If true, this provided dependency is scheduled for removal (or incompatible upgrade) in a next runtime version.",
    )
    removed: Optional[StrictBool] = Field(
        default=False,
        description="If true, this dependency has been removed from the runtime (version)",
    )
    globals: Optional[List[StrictStr]] = Field(
        default=None,
        description="Global variables that expose this library to the user code. As the usage of these globals is deprecated, any usage of such global will pose issues in an next runtime version.",
    )
    native: Optional[StrictBool] = Field(
        default=None,
        description="If true, the library is provided natively by the runtime: e.g. node for javascript.",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
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
        """Create an instance of ProvidedDependency from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProvidedDependency from a dict."""
        if obj is None:
            return None
        return cls.model_validate(obj)
