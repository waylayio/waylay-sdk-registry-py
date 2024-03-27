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

from ..models.failure_reason import FailureReason
from ..models.function_ref import FunctionRef
from ..models.job_hal_links import JobHALLinks
from ..models.job_state_result import JobStateResult
from ..models.job_status import JobStatus
from ..models.undeploy_args import UndeployArgs
from ..models.undeploy_result import UndeployResult
from ..models.undeploy_type import UndeployType


class Undeploy(WaylayBaseModel):
    """Undeploy."""

    links: JobHALLinks | None = Field(default=None, alias="_links")
    type: UndeployType
    state: JobStateResult
    request: UndeployArgs | None = None
    result: UndeployResult | None = None
    created_at: datetime = Field(
        description="The timestamp of creation of this job", alias="createdAt"
    )
    created_by: StrictStr = Field(
        description="The user that created this job", alias="createdBy"
    )
    operation: StrictStr = Field(description="Request operation")
    function: FunctionRef | None = None
    job: JobStatus | None = None
    failure_reason: FailureReason | None = Field(default=None, alias="failureReason")

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
