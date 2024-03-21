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
from pydantic import ConfigDict, SerializationInfo, model_serializer, StrictStr
from pydantic_core import from_json
from typing import Callable, Union
from typing import cast
from typing_extensions import (
    Self,  # >=3.11
)
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from ..models.failure_reason import FailureReason
from ..models.function_deploy_overrides_type import FunctionDeployOverridesType
from ..models.function_meta import FunctionMeta
from ..models.job_hal_links import JobHALLinks
from ..models.semantic_version_range import SemanticVersionRange
from ..models.status import Status


class EntityResponse(BaseModel):
    """EntityResponse."""

    deploy: FunctionDeployOverridesType | None = None
    name: StrictStr = Field(description="The logical name for the function.")
    version: Annotated[str, Field(strict=True)] = Field(
        description="A semantic version with _exactly_ a `major`, `minor` and `patch` specifier. No `pre-release` or `build` identifiers are allowed. See https://semver.org"
    )
    runtime: StrictStr
    runtime_version: SemanticVersionRange | None = Field(
        default=None, alias="runtimeVersion"
    )
    metadata: FunctionMeta
    created_by: StrictStr = Field(
        description="The user that created this entity.", alias="createdBy"
    )
    created_at: datetime = Field(
        description="The timestamp at which this entity was created.", alias="createdAt"
    )
    updated_by: StrictStr = Field(
        description="The user that last updated this entity.", alias="updatedBy"
    )
    updated_at: datetime = Field(
        description="The timestamp at which this entity was last updated.",
        alias="updatedAt",
    )
    status: Status
    failure_reason: FailureReason | None = Field(default=None, alias="failureReason")
    links: List[JobHALLinks] | None = Field(
        default=None, description="Links to related entities.", alias="_links"
    )

    @field_validator("version")
    @classmethod
    def version_validate_regular_expression(cls, value):
        """Validate the regular expression."""
        if not re.match(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$", value):
            raise ValueError(
                r"must validate the regular expression /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/"
            )
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
        """Convert the EntityResponse instance to dict."""
        return self.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)

    def to_json(self) -> str:
        """Convert the EntityResponse instance to a JSON-encoded string."""
        return self.model_dump_json(
            by_alias=True, exclude_unset=True, exclude_none=True
        )

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create a EntityResponse instance from a dict."""
        return cls.model_validate(obj)

    @classmethod
    def from_json(cls, json_data: str | bytes | bytearray) -> Self:
        """Create a EntityResponse instance from a JSON-encoded string."""
        return cls.model_validate_json(json_data)