# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.function_ref import FunctionRef
from ..models.job_state_result import JobStateResult
from ..models.job_status import JobStatus
from ..models.scale_args import ScaleArgs
from ..models.scale_type import ScaleType


class ScaleJobStatus(WaylayBaseModel):
    """ScaleJobStatus."""

    type: ScaleType
    state: JobStateResult
    request: ScaleArgs
    result: Dict[str, Any] | None = Field(
        default=None, description="The result data for a completed scale job."
    )
    created_at: datetime = Field(
        description="The timestamp of creation of this job", alias="createdAt"
    )
    created_by: StrictStr = Field(
        description="The user that created this job", alias="createdBy"
    )
    operation: StrictStr = Field(description="Request operation")
    function: FunctionRef | None = None
    job: JobStatus

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
