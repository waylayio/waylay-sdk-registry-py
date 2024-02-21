# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.delayed_event_sse import DelayedEventSSE


from .job_event_response_delayed_event_data_stub import JobEventResponseDelayedEventDataStub


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from waylay.services.registry.models.job_event_response_delayed_event_data import JobEventResponseDelayedEventData


class DelayedEventSSEStub:
    """DelayedEventSSE unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> DelayedEventSSE:
        """Create DelayedEventSSE stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return DelayedEventSSE(
                event='delayed',
                data=JobEventResponseDelayedEventDataStub.create_instance()
            )
        else:
            return DelayedEventSSE(
                event='delayed',
                data=JobEventResponseDelayedEventDataStub.create_instance()
            )
