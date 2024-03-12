# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import re  # noqa: F401

from ..models.event_ack import EventAck
from ..models.event_close import EventClose
from ..models.event_keep_alive import EventKeepAlive
from ..models.supported_events import SupportedEvents

from typing import (
    Union,  # >=3.8
)
from typing_extensions import (
    Annotated,  # >=3.9
)


EventTypeSSE = Union[
    Annotated[SupportedEvents, ""],
    Annotated[EventAck, ""],
    Annotated[EventClose, ""],
    Annotated[EventKeepAlive, ""],
]
"""EventTypeSSE."""
