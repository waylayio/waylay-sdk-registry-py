# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import re  # noqa: F401
from pydantic import ConfigDict, SerializationInfo, model_serializer, StrictStr
from typing import Callable, Union
from typing_extensions import (
    Self,  # >=3.11
)
from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from ..models.function_ref import FunctionRef
from ..models.job_state_result import JobStateResult
from ..models.job_status import JobStatus
from ..models.scale_args import ScaleArgs


class ScaleJobStatus(BaseModel):
    """ScaleJobStatus."""

    type: StrictStr = Field(description="The type of the background task.")
    state: JobStateResult
    request: ScaleArgs
    result: Optional[Dict[str, Any]] = Field(
        default=None, description="The result data for a completed scale job."
    )
    created_at: datetime = Field(
        description="The timestamp of creation of this job", alias="createdAt"
    )
    created_by: StrictStr = Field(
        description="The user that created this job", alias="createdBy"
    )
    operation: StrictStr = Field(description="Request operation")
    function: Optional[FunctionRef] = None
    job: JobStatus

    @field_validator("type")
    @classmethod
    def type_validate_enum(cls, value):
        """Validate the enum."""
        if value not in ("scale"):
            raise ValueError("must be one of enum values ('scale')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )

    @model_serializer(mode="wrap")
    def serializer(
        self, handler: Callable, info: SerializationInfo
    ) -> Dict[StrictStr, Any]:
        """The default serializer of the model.

        * Excludes `None` fields that were not set at model initialization.
        """
        model_dict = handler(self, info)
        return {
            k: v
            for k, v in model_dict.items()
            if v is not None or k in self.model_fields_set
        }

    def to_dict(self) -> dict[str, Any]:
        """Convert the ScaleJobStatus instance to dict."""
        return self.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)

    def to_json(self) -> str:
        """Convert the ScaleJobStatus instance to a JSON-encoded string."""
        return self.model_dump_json(
            by_alias=True, exclude_unset=True, exclude_none=True
        )

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create a ScaleJobStatus instance from a dict."""
        return cls.model_validate(obj)

    @classmethod
    def from_json(cls, json_data: Union[str, bytes, bytearray]) -> Self:
        """Create a ScaleJobStatus instance from a JSON-encoded string."""
        return cls.model_validate_json(json_data)
