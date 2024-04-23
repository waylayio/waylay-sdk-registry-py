# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.job_type import JobType
from ..models.operation_status_error import OperationStatusError


class OperationStatus(WaylayBaseModel):
    """OperationStatus."""

    id: StrictStr
    description: StrictStr
    name: StrictStr
    type: JobType
    done: StrictBool
    error: OperationStatusError | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
