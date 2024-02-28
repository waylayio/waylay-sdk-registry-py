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
from pydantic import BaseModel
from pydantic import Field
from ..models.legacy_plug_request_metadata_documentation import (
    LegacyPlugRequestMetadataDocumentation,
)
from ..models.plug_interface import PlugInterface


from typing import cast

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class NamedParametersTypeofFromLegacyDocumentation(BaseModel):
    """NamedParametersTypeofFromLegacyDocumentation."""

    legacy_documentation: Optional[LegacyPlugRequestMetadataDocumentation] = Field(
        default=None, alias="legacyDocumentation"
    )
    current_interface: Optional[PlugInterface] = Field(
        default=None, alias="currentInterface"
    )
    __properties: ClassVar[List[str]] = ["legacyDocumentation", "currentInterface"]

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
        """Create an instance of NamedParametersTypeofFromLegacyDocumentation from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of legacy_documentation
        if self.legacy_documentation:
            _dict["legacyDocumentation"] = self.legacy_documentation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_interface
        if self.current_interface:
            _dict["currentInterface"] = self.current_interface.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NamedParametersTypeofFromLegacyDocumentation from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "legacyDocumentation": (
                    LegacyPlugRequestMetadataDocumentation.from_dict(
                        cast(dict, obj.get("legacyDocumentation"))
                    )
                    if obj.get("legacyDocumentation") is not None
                    else None
                ),
                "currentInterface": (
                    PlugInterface.from_dict(cast(dict, obj.get("currentInterface")))
                    if obj.get("currentInterface") is not None
                    else None
                ),
            }
        )
        return _obj
