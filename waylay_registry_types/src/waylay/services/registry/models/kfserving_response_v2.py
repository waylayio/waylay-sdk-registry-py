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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from ..models.failure_reason import FailureReason
from ..models.kf_serving_manifest import KFServingManifest
from ..models.runtime_attributes import RuntimeAttributes
from ..models.status import Status
from ..models.update_record import UpdateRecord


from typing_extensions import (
    Self,  # >=3.11
)


class KfservingResponseV2(BaseModel):
    """KfservingResponseV2."""

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
    updates: List[UpdateRecord] = Field(
        description="The audit logs corresponding to the latest modifying operations on this entity."
    )
    status: Status
    failure_reason: Optional[FailureReason] = Field(default=None, alias="failureReason")
    runtime: RuntimeAttributes
    deprecated: StrictBool = Field(
        description="If <code>true</code> this function is deprecated and removed from regular listings."
    )
    draft: StrictBool = Field(
        description="If <code>true</code> this function is a draft function and it's assets are still mutable."
    )
    model: KFServingManifest

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
        """Create an instance of KfservingResponseV2 from a JSON string."""
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
        """Create an instance of KfservingResponseV2 from a dict."""
        if obj is None:
            return None
        return cls.model_validate(obj)
