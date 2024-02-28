# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.job_event_sse import JobEventSSE


from .job_event_response_waiting_children_event_data_stub import JobEventResponseWaitingChildrenEventDataStub

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from waylay.services.registry.models.active_event_sse import ActiveEventSSE
from waylay.services.registry.models.completed_event_sse import CompletedEventSSE
from waylay.services.registry.models.delayed_event_sse import DelayedEventSSE
from waylay.services.registry.models.failed_event_sse import FailedEventSSE
from waylay.services.registry.models.waiting_children_event_sse import WaitingChildrenEventSSE
from waylay.services.registry.models.waiting_event_sse import WaitingEventSSE


from .active_event_sse_stub import ActiveEventSSEStub

from .completed_event_sse_stub import CompletedEventSSEStub

from .failed_event_sse_stub import FailedEventSSEStub

from .delayed_event_sse_stub import DelayedEventSSEStub

from .waiting_event_sse_stub import WaitingEventSSEStub

from .waiting_children_event_sse_stub import WaitingChildrenEventSSEStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobEventSSEStub:
    """JobEventSSE unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobEventSSE:
        """Create JobEventSSE stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        # return instance of first type from `anyOf`
        return JobEventSSE(ActiveEventSSEStub.create_instance(include_optional=include_optional))
