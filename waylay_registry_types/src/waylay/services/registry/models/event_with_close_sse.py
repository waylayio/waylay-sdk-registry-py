# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import re  # noqa: F401

from ..models.job_event_sse import JobEventSSE
from ..models.keep_alive_event_sse import KeepAliveEventSSE
from ..models.stream_closing import StreamClosing
from ..models.stream_ready import StreamReady

from typing import (
    Union,  # >=3.8
)
from typing_extensions import (
    Annotated,  # >=3.9
)


EventWithCloseSSE = Union[
    Annotated[StreamReady, ""],
    Annotated[JobEventSSE, ""],
    Annotated[KeepAliveEventSSE, ""],
    Annotated[StreamClosing, ""],
]
"""SSE stream events with closing protocol."""
