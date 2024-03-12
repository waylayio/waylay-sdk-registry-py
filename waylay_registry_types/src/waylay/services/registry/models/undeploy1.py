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
from typing_extensions import (
    Self,  # >=3.11
)
from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from ..models.function_ref import FunctionRef
from ..models.job_and_function_hal_link import JobAndFunctionHALLink
from ..models.job_state_result import JobStateResult


class Undeploy1(BaseModel):
    """Undeploy1."""

    type: StrictStr = Field(description="The type of the background task.")
    operation: StrictStr = Field(
        description="The operation name for the background task."
    )
    id: StrictStr = Field(
        description="The id of the background job, or the constant `_unknown_`"
    )
    state: JobStateResult
    created_at: datetime = Field(
        description="The creation time of this job", alias="createdAt"
    )
    created_by: StrictStr = Field(
        description="The user that initiated this job", alias="createdBy"
    )
    function: Optional[FunctionRef] = None
    links: JobAndFunctionHALLink = Field(alias="_links")

    @field_validator("type")
    @classmethod
    def type_validate_enum(cls, value):
        """Validate the enum."""
        if value not in ("undeploy"):
            raise ValueError("must be one of enum values ('undeploy')")
        return value

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
        """Create an instance of Undeploy1 from a JSON string."""
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
        """Create an instance of Undeploy1 from a dict."""
        if obj is None:
            return None
        return cls.model_validate(obj)
