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

from datetime import datetime
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from ..models.job_reference import JobReference


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class JobEventPayloadWaitingChildrenEventData(BaseModel):
    """JobEventPayloadWaitingChildrenEventData."""

    job: JobReference
    data: Dict[str, Any]
    timestamp: datetime = Field(description="Timestamp of the event")
    __properties: ClassVar[List[str]] = ["job", "data", "timestamp"]

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
        """Create an instance of JobEventPayloadWaitingChildrenEventData from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of job
        if self.job:
            _dict['job'] = self.job.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of JobEventPayloadWaitingChildrenEventData from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "job": JobReference.from_dict(obj.get("job")) if obj.get("job") is not None else None,    # type: ignore
            "data": obj.get("data"),
            "timestamp": obj.get("timestamp")
        })
        return _obj
