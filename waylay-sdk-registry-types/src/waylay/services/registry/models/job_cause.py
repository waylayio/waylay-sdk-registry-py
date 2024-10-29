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


class JobCause(WaylayBaseModel):
    """The motivation for including or excluding a job (<em>build</em>, <em>deploy</em>, <em>verify</em>, ...) in response to a <em>rebuild</em> request.."""

    changed: StrictBool = Field(
        description="If <code>true</code>, the argument configuration for this job has changed in comparison to the previous job execution. A <code>false</code> will prevent the job to be run. Use <code>forceVersion</code> or <code>upgrade</code> parameter to force a rebuild."
    )
    reason: StrictStr = Field(
        description="Human readable message describing the cause."
    )
    backoff: StrictBool | None = Field(
        default=None,
        description="If <code>true</code>, recent failures of the job prevented the re-execution. Use <code>forceVersion</code> or <code>upgrade</code> parameter to force a rebuild.",
    )
    new_value: StrictStr | None = Field(
        default=None,
        description="The new configuration value that causes the change.",
        alias="newValue",
    )
    old_value: StrictStr | None = Field(
        default=None,
        description="The old configuration value used by the last succeeded job.",
        alias="oldValue",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
