"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.job_event_sse import JobEventSSE
from ..models.keep_alive_event_sse import KeepAliveEventSSE
from ..models.stream_closing import StreamClosing
from ..models.stream_ready import StreamReady

EventWithCloseSSE: TypeAlias = StreamReady | JobEventSSE | KeepAliveEventSSE | StreamClosing
"""SSE stream events with closing protocol."""
