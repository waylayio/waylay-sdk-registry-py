# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime

from waylay.services.registry.models.job_event_response_waiting_event_data import (
    JobEventResponseWaitingEventData,
)
from .job_status_and_entity_hal_links_stub import JobStatusAndEntityHALLinksStub

from .job_reference_stub import JobReferenceStub

from .waiting_event_data_stub import WaitingEventDataStub


from .function_ref_stub import FunctionRefStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobEventResponseWaitingEventDataStub:
    """JobEventResponseWaitingEventData unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobEventResponseWaitingEventData:
        """Create JobEventResponseWaitingEventData stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return JobEventResponseWaitingEventData(
                links=JobStatusAndEntityHALLinksStub.create_instance(),
                job=JobReferenceStub.create_instance(),
                data=WaitingEventDataStub.create_instance(),
                timestamp=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
                function=FunctionRefStub.create_instance(),
            )
        else:
            return JobEventResponseWaitingEventData(
                links=JobStatusAndEntityHALLinksStub.create_instance(),
                job=JobReferenceStub.create_instance(),
                data=WaitingEventDataStub.create_instance(),
                timestamp=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
                function=FunctionRefStub.create_instance(),
            )
