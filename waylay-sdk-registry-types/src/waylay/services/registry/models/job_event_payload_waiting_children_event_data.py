# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.job_reference import JobReference


class JobEventPayloadWaitingChildrenEventData(WaylayBaseModel):
    """JobEventPayloadWaitingChildrenEventData."""

    job: JobReference
    data: Dict[str, Any]
    timestamp: datetime = Field(description="Timestamp of the event")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
