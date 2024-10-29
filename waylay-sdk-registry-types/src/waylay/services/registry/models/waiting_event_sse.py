# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.job_event_response_waiting_event_data import (
    JobEventResponseWaitingEventData,
)
from ..models.waiting_event_sse_event import WaitingEventSSEEvent


class WaitingEventSSE(WaylayBaseModel):
    """A message that notifies a state change in a background job.."""

    event: WaitingEventSSEEvent
    data: JobEventResponseWaitingEventData

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
