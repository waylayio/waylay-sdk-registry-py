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

from datetime import datetime
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from ..models.completed_event_data import CompletedEventData
from ..models.function_ref import FunctionRef
from ..models.job_reference import JobReference
from ..models.job_status_and_entity_hal_links import JobStatusAndEntityHALLinks


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class JobEventResponseCompletedEventData(BaseModel):
    """Event object describing a state change of a background job.."""

    links: JobStatusAndEntityHALLinks = Field(alias="_links")
    job: JobReference
    data: CompletedEventData
    timestamp: datetime = Field(description="Timestamp of the event")
    function: FunctionRef
    __properties: ClassVar[List[str]] = ["_links", "job", "data", "timestamp", "function"]

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
        """Create an instance of JobEventResponseCompletedEventData from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of job
        if self.job:
            _dict['job'] = self.job.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of function
        if self.function:
            _dict['function'] = self.function.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of JobEventResponseCompletedEventData from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": JobStatusAndEntityHALLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,    # type: ignore
            "job": JobReference.from_dict(obj.get("job")) if obj.get("job") is not None else None,    # type: ignore
            "data": CompletedEventData.from_dict(obj.get("data")) if obj.get("data") is not None else None,    # type: ignore
            "timestamp": obj.get("timestamp"),
            "function": FunctionRef.from_dict(obj.get("function")) if obj.get("function") is not None else None    # type: ignore
        })
        return _obj
