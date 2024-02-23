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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from ..models.deploy_args import DeployArgs
from ..models.deploy_result import DeployResult
from ..models.failure_reason import FailureReason
from ..models.function_ref import FunctionRef
from ..models.job_hal_links import JobHALLinks
from ..models.job_state_result import JobStateResult
from ..models.job_status import JobStatus


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Deploy(BaseModel):
    """Deploy."""

    links: Optional[JobHALLinks] = Field(default=None, alias="_links")
    type: StrictStr = Field(description="The type of the background task.")
    state: JobStateResult
    request: Optional[DeployArgs] = None
    result: Optional[DeployResult] = None
    created_at: datetime = Field(description="The timestamp of creation of this job", alias="createdAt")
    created_by: StrictStr = Field(description="The user that created this job", alias="createdBy")
    operation: StrictStr = Field(description="Request operation")
    function: Optional[FunctionRef] = None
    job: Optional[JobStatus] = None
    failure_reason: Optional[FailureReason] = Field(default=None, alias="failureReason")
    __properties: ClassVar[List[str]] = ["_links", "type", "state", "request", "result", "createdAt", "createdBy", "operation", "function", "job", "failureReason"]

    @field_validator('type')
    @classmethod
    def type_validate_enum(cls, value):
        """Validate the enum."""
        if value not in ('deploy'):
            raise ValueError("must be one of enum values ('deploy')")
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
        """Create an instance of Deploy from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of request
        if self.request:
            _dict['request'] = self.request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of function
        if self.function:
            _dict['function'] = self.function.to_dict()
        # override the default output from pydantic by calling `to_dict()` of job
        if self.job:
            _dict['job'] = self.job.to_dict()
        # override the default output from pydantic by calling `to_dict()` of failure_reason
        if self.failure_reason:
            _dict['failureReason'] = self.failure_reason.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Deploy from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": JobHALLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,    # type: ignore
            "type": obj.get("type"),
            "state": JobStateResult.from_dict(obj.get("state")) if obj.get("state") is not None else None,    # type: ignore
            "request": DeployArgs.from_dict(obj.get("request")) if obj.get("request") is not None else None,    # type: ignore
            "result": DeployResult.from_dict(obj.get("result")) if obj.get("result") is not None else None,    # type: ignore
            "createdAt": obj.get("createdAt"),
            "createdBy": obj.get("createdBy"),
            "operation": obj.get("operation"),
            "function": FunctionRef.from_dict(obj.get("function")) if obj.get("function") is not None else None,    # type: ignore
            "job": JobStatus.from_dict(obj.get("job")) if obj.get("job") is not None else None,    # type: ignore
            "failureReason": FailureReason.from_dict(obj.get("failureReason")) if obj.get("failureReason") is not None else None    # type: ignore
        })
        return _obj
