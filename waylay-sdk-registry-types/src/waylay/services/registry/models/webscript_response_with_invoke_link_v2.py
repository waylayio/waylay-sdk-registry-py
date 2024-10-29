# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime
from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.failure_reason import FailureReason
from ..models.invoke_hal_link import InvokeHALLink
from ..models.runtime_attributes import RuntimeAttributes
from ..models.status import Status
from ..models.update_record import UpdateRecord
from ..models.webscript_manifest import WebscriptManifest


class WebscriptResponseWithInvokeLinkV2(WaylayBaseModel):
    """WebscriptResponseWithInvokeLinkV2."""

    created_by: StrictStr = Field(
        description="The user that created this entity.", alias="createdBy"
    )
    created_at: datetime = Field(
        description="The timestamp at which this entity was created.", alias="createdAt"
    )
    updated_by: StrictStr = Field(
        description="The user that last updated this entity.", alias="updatedBy"
    )
    updated_at: datetime = Field(
        description="The timestamp at which this entity was last updated.",
        alias="updatedAt",
    )
    updates: List[UpdateRecord] | None = Field(
        default=None,
        description="The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations.",
    )
    status: Status
    failure_reason: FailureReason | None = Field(default=None, alias="failureReason")
    runtime: RuntimeAttributes
    deprecated: StrictBool = Field(
        description="If <code>true</code> this function is deprecated and removed from regular listings."
    )
    draft: StrictBool = Field(
        description="If <code>true</code> this function is a draft function and it's assets are still mutable."
    )
    webscript: WebscriptManifest
    secret: StrictStr | None = Field(
        default=None,
        description="The secret for this webscript deployment. This is <code>null</code> when <code>allowHmac=false</code> in the webscript specificaton.",
    )
    links: InvokeHALLink | None = Field(default=None, alias="_links")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
