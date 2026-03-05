"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.active_event_sse import ActiveEventSSE
from ..models.completed_event_sse import CompletedEventSSE
from ..models.delayed_event_sse import DelayedEventSSE
from ..models.failed_event_sse import FailedEventSSE
from ..models.waiting_children_event_sse import WaitingChildrenEventSSE
from ..models.waiting_event_sse import WaitingEventSSE

JobEventSSE: TypeAlias = ActiveEventSSE | CompletedEventSSE | FailedEventSSE | DelayedEventSSE | WaitingEventSSE | WaitingChildrenEventSSE
"""JobEventSSE."""
