# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.job_event_payload_delayed_event_data import JobEventPayloadDelayedEventData

from .job_reference_stub import JobReferenceStub

from .delayed_event_data_stub import DelayedEventDataStub


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from waylay.services.registry.models.delayed_event_data import DelayedEventData
from waylay.services.registry.models.job_reference import JobReference


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobEventPayloadDelayedEventDataStub:
    """JobEventPayloadDelayedEventData unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobEventPayloadDelayedEventData:
        """Create JobEventPayloadDelayedEventData stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return JobEventPayloadDelayedEventData(
                job=JobReferenceStub.create_instance(),
                data=DelayedEventDataStub.create_instance(),
                timestamp=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return JobEventPayloadDelayedEventData(
                job=JobReferenceStub.create_instance(),
                data=DelayedEventDataStub.create_instance(),
                timestamp=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
