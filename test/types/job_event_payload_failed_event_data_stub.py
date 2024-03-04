# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime

from waylay.services.registry.models.job_event_payload_failed_event_data import (
    JobEventPayloadFailedEventData,
)
from .job_reference_stub import JobReferenceStub

from .failed_event_data_stub import FailedEventDataStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobEventPayloadFailedEventDataStub:
    """JobEventPayloadFailedEventData unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobEventPayloadFailedEventData:
        """Create JobEventPayloadFailedEventData stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return JobEventPayloadFailedEventData(
                job=JobReferenceStub.create_instance(),
                data=FailedEventDataStub.create_instance(),
                timestamp=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
            )
        else:
            return JobEventPayloadFailedEventData(
                job=JobReferenceStub.create_instance(),
                data=FailedEventDataStub.create_instance(),
                timestamp=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
            )
