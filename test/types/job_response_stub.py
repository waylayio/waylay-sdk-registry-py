# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.job_response import JobResponse
from .any_job_status_stub import AnyJobStatusStub

from .job_events_and_function_hal_link_stub import JobEventsAndFunctionHALLinkStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobResponseStub:
    """JobResponse unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobResponse:
        """Create JobResponse stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return JobResponse(
                job=AnyJobStatusStub.create_instance(),
                links=JobEventsAndFunctionHALLinkStub.create_instance(),
            )
        else:
            return JobResponse(
                job=AnyJobStatusStub.create_instance(),
                links=JobEventsAndFunctionHALLinkStub.create_instance(),
            )
