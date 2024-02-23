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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from ..models.function_type import FunctionType


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class FunctionRef(BaseModel):
    """FunctionRef."""

    function_type: FunctionType = Field(alias="functionType")
    name: StrictStr = Field(description="The logical name for the function.")
    version: Optional[StrictStr] = Field(default=None, description="The semantic version of the function (all versions if undefined)")
    runtime: Optional[StrictStr] = None
    runtime_version: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A semantic version with _exactly_ a `major`, `minor` and `patch` specifier. No `pre-release` or `build` identifiers are allowed. See https://semver.org", alias="runtimeVersion")
    __properties: ClassVar[List[str]] = ["functionType", "name", "version", "runtime", "runtimeVersion"]

    @field_validator('runtime_version')
    @classmethod
    def runtime_version_validate_regular_expression(cls, value):
        """Validate the regular expression."""
        if value is None:
            return value

        if not re.match(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/")
        return value

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
        """Create an instance of FunctionRef from a JSON string."""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FunctionRef from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "functionType": obj.get("functionType"),
            "name": obj.get("name"),
            "version": obj.get("version"),
            "runtime": obj.get("runtime"),
            "runtimeVersion": obj.get("runtimeVersion")
        })
        return _obj
