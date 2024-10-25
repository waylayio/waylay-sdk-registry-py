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

from ..models.deploy_args import DeployArgs
from ..models.deploy_result import DeployResult
from ..models.deploy_type import DeployType
from ..models.failure_reason import FailureReason
from ..models.function_ref import FunctionRef
from ..models.job_hal_links import JobHALLinks
from ..models.job_state_result import JobStateResult
from ..models.job_status import JobStatus


class Deploy(WaylayBaseModel):
    """Deploy."""

    links: JobHALLinks | None = Field(default=None, alias="_links")
    type: DeployType
    state: JobStateResult
    request: DeployArgs | None = None
    result: DeployResult | None = None
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
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
