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


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AsyncVerifyQuery(BaseModel):
    """AsyncVerifyQuery."""

    comment: Optional[StrictStr] = Field(
        default=None,
        description="An optional user-specified comment corresponding to the operation.",
    )
    var_async: Optional[StrictBool] = Field(
        default=True,
        description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
        alias="async",
    )
    scale_to_zero: Optional[StrictBool] = Field(
        default=None,
        description="Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command.",
        alias="scaleToZero",
    )
    __properties: ClassVar[List[str]] = ["comment", "async", "scaleToZero"]

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
        """Create an instance of AsyncVerifyQuery from a JSON string."""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AsyncVerifyQuery from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "comment": obj.get("comment"),
                "async": obj.get("async") if obj.get("async") is not None else True,
                "scaleToZero": obj.get("scaleToZero"),
            }
        )
        return _obj
