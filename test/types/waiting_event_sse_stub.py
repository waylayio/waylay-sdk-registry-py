# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.waiting_event_sse import WaitingEventSSE


from .job_event_response_waiting_event_data_stub import (
    JobEventResponseWaitingEventDataStub,
)


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class WaitingEventSSEStub:
    """WaitingEventSSE unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> WaitingEventSSE:
        """Create WaitingEventSSE stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return WaitingEventSSE(
                event="waiting",
                data=JobEventResponseWaitingEventDataStub.create_instance(),
            )
        else:
            return WaitingEventSSE(
                event="waiting",
                data=JobEventResponseWaitingEventDataStub.create_instance(),
            )
