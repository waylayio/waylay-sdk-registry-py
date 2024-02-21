# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.job_event_payload_active_event_data import JobEventPayloadActiveEventData

from .job_reference_stub import JobReferenceStub

from .active_event_data_stub import ActiveEventDataStub


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from waylay.services.registry.models.active_event_data import ActiveEventData
from waylay.services.registry.models.job_reference import JobReference


class JobEventPayloadActiveEventDataStub:
    """JobEventPayloadActiveEventData unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobEventPayloadActiveEventData:
        """Create JobEventPayloadActiveEventData stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return JobEventPayloadActiveEventData(
                job=JobReferenceStub.create_instance(),
                data=ActiveEventDataStub.create_instance(),
                timestamp=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return JobEventPayloadActiveEventData(
                job=JobReferenceStub.create_instance(),
                data=ActiveEventDataStub.create_instance(),
                timestamp=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
