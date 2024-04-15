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
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class UpdateDraftQuery(WaylayBaseModel):
    """UpdateDraftQuery."""

    scale_to_zero: StrictBool | None = Field(
        default=False,
        description="If set to <code>true</code>, after successful deployment, the deployed function will be scaled to zero. This saves computing resources when the function is not to be used immediately.",
        alias="scaleToZero",
    )
    deploy: StrictBool | None = Field(
        default=True,
        description="Indicates that a function should be _deployed_ when its assets are valid.  * If `true` (default), jobs to build and deploy the function will be initiated after it is checked that the assets are valid. Invalid assets lead to a validation error, and the function and its assets are not created or updated. * If `false`, the uploaded assets are stored and the function is created/updated in `registered` state. Asset validation errors are only returned as warning, and stored as `failureReason` on the function entity. Use an _asset update_ or _rebuild_ to initiate a build and deploy at a later stage.",
    )
    chown: StrictBool | None = Field(
        default=False,
        description="If set, ownership of the draft function is transferred to the current user.",
    )
    comment: StrictStr | None = Field(
        default=None,
        description="An optional user-specified comment corresponding to the operation.",
    )
    author: StrictStr | None = Field(
        default=None,
        description="Optionally changes the author metadata when updating a function.",
    )
    var_async: StrictBool | None = Field(
        default=True,
        description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
        alias="async",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
