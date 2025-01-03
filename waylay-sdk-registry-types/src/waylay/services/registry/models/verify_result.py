# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class VerifyResult(WaylayBaseModel):
    """The result data for a completed verification job.."""

    healthy: StrictBool = Field(description="If true, the deployment check succeeded.")
    replicas: StrictFloat | StrictInt | None = Field(
        default=None,
        description="The number of replicas this function was running at the time of the check.",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
