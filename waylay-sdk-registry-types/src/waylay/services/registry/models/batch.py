# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_job_status_type import BatchJobStatusType
from ..models.function_ref import FunctionRef
from ..models.job_hal_links import JobHALLinks
from ..models.job_state_result import JobStateResult


class Batch(WaylayBaseModel):
    """Batch."""

    type: BatchJobStatusType
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
    function: FunctionRef | None = None
    links: JobHALLinks = Field(alias="_links")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
