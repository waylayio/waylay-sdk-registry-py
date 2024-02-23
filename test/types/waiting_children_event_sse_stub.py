# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.waiting_children_event_sse import WaitingChildrenEventSSE


from .job_event_response_waiting_children_event_data_stub import JobEventResponseWaitingChildrenEventDataStub


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from waylay.services.registry.models.job_event_response_waiting_children_event_data import JobEventResponseWaitingChildrenEventData


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class WaitingChildrenEventSSEStub:
    """WaitingChildrenEventSSE unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> WaitingChildrenEventSSE:
        """Create WaitingChildrenEventSSE stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return WaitingChildrenEventSSE(
                event='waiting-children',
                data=JobEventResponseWaitingChildrenEventDataStub.create_instance()
            )
        else:
            return WaitingChildrenEventSSE(
                event='waiting-children',
                data=JobEventResponseWaitingChildrenEventDataStub.create_instance()
            )
