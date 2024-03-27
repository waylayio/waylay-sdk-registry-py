# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import List

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.any_job_for_function import AnyJobForFunction
from ..models.function_ref import FunctionRef
from ..models.jobs_for_plug_response_v2_links import JobsForPlugResponseV2Links


class JobsForPlugResponseV2(WaylayBaseModel):
    """Plug Jobs Found."""

    jobs: List[AnyJobForFunction] = Field(
        description="Listing of jobs related to the function deployment. This includes active jobs, and the most recently failed job (per type) that was archived on the entity."
    )
    function: FunctionRef
    links: JobsForPlugResponseV2Links | None = Field(default=None, alias="_links")

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
