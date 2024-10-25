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
    StrictFloat,
    StrictInt,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.function_ref import FunctionRef
from ..models.job_and_function_hal_link import JobAndFunctionHALLink
from ..models.job_state_result import JobStateResult
from ..models.verify_type import VerifyType


class Verify1(WaylayBaseModel):
    """Verify1."""

    type: VerifyType
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
    processed_at: datetime | None = Field(
        default=None,
        description="The timestamp of when the job has begun processing.",
        alias="processedAt",
    )
    finished_at: datetime | None = Field(
        default=None,
        description="The timestamp of when the job has finished processing.",
        alias="finishedAt",
    )
    attempts_made: StrictFloat | StrictInt | None = Field(
        default=None,
        description="The number of retries that were attempted.",
        alias="attemptsMade",
    )
    created_by: StrictStr = Field(
        description="The user that initiated this job", alias="createdBy"
    )
    function: FunctionRef | None = None
    links: JobAndFunctionHALLink = Field(alias="_links")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
