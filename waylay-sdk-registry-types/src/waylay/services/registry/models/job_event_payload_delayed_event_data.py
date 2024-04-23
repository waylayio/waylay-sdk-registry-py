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
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.delayed_event_data import DelayedEventData
from ..models.job_reference import JobReference


class JobEventPayloadDelayedEventData(WaylayBaseModel):
    """JobEventPayloadDelayedEventData."""

    job: JobReference
    data: DelayedEventData
    timestamp: datetime = Field(description="Timestamp of the event")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
