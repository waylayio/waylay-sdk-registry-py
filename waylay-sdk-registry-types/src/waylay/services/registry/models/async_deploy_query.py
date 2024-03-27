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
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.deprecate_previous_policy import DeprecatePreviousPolicy


class AsyncDeployQuery(WaylayBaseModel):
    """AsyncDeployQuery."""

    deprecate_previous: DeprecatePreviousPolicy | None = Field(
        default=None, alias="deprecatePrevious"
    )
    dry_run: StrictBool | None = Field(
        default=None,
        description="If set to <code>true</code>, validates the deployment conditions, but does not change anything.",
        alias="dryRun",
    )
    var_async: StrictBool | None = Field(
        default=True,
        description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
        alias="async",
    )
    scale_to_zero: StrictBool | None = Field(
        default=False,
        description="If set to <code>true</code>, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately.",
        alias="scaleToZero",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )