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
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.event_ack import EventAck


class StreamReady(WaylayBaseModel):
    """A message that acknowledges that the server will sent job state changes.."""

    event: EventAck
    data: StrictStr = Field(
        description="A text message acknowledging what events will be forwarded."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
