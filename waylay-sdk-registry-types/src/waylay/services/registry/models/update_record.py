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
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.request_operation import RequestOperation


class UpdateRecord(WaylayBaseModel):
    """An update report corresponding to a modifying operation initiated by a user/administrator on the entity.."""

    comment: StrictStr | None = Field(
        default=None,
        description="An optional user-specified comment corresponding to the operation.",
    )
    operation: RequestOperation
    jobs: List[StrictStr] | None = Field(
        default=None,
        description="The job id's of the corresponding jobs, if applicable.",
    )
    at: datetime
    by: StrictStr = Field(description="The user that initiated this operation.")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
