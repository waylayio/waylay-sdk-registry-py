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
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated
from ..models.function_type import FunctionType
from ..models.job_state_result import JobStateResult
from ..models.job_type_schema import JobTypeSchema
from ..models.timestamp_spec import TimestampSpec


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class JobQuery(BaseModel):
    """JobQuery."""

    limit: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="The maximum number of items to be return from this query. Has a deployment-defined default and maximum value.")
    type: Optional[List[JobTypeSchema]] = Field(default=None, description="Filter on job type")
    state: Optional[List[JobStateResult]] = Field(default=None, description="Filter on job state")
    function_type: Optional[List[FunctionType]] = Field(default=None, description="Filter on function type", alias="functionType")
    created_before: Optional[TimestampSpec] = Field(default=None, alias="createdBefore")
    created_after: Optional[TimestampSpec] = Field(default=None, alias="createdAfter")
    __properties: ClassVar[List[str]] = ["limit", "type", "state", "functionType", "createdBefore", "createdAfter"]

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
        """Create an instance of JobQuery from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of each item in type (list)
        _items = []
        if self.type:
            for _item in self.type:  # type: ignore
                if _item:
                    _items.append(_item.to_dict())
            _dict['type'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in state (list)
        _items = []
        if self.state:
            for _item in self.state:  # type: ignore
                if _item:
                    _items.append(_item.to_dict())
            _dict['state'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_before
        if self.created_before:
            _dict['createdBefore'] = self.created_before.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_after
        if self.created_after:
            _dict['createdAfter'] = self.created_after.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of JobQuery from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "limit": obj.get("limit"),
            "type": [JobTypeSchema.from_dict(_item) for _item in obj.get("type")] if obj.get("type") is not None else None,  # type: ignore
            "state": [JobStateResult.from_dict(_item) for _item in obj.get("state")] if obj.get("state") is not None else None,  # type: ignore
            "functionType": obj.get("functionType"),
            "createdBefore": TimestampSpec.from_dict(obj.get("createdBefore")) if obj.get("createdBefore") is not None else None,    # type: ignore
            "createdAfter": TimestampSpec.from_dict(obj.get("createdAfter")) if obj.get("createdAfter") is not None else None    # type: ignore
        })
        return _obj
