# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.active_event_sse import ActiveEventSSE


from .job_event_response_active_event_data_stub import (
    JobEventResponseActiveEventDataStub,
)


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class ActiveEventSSEStub:
    """ActiveEventSSE unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> ActiveEventSSE:
        """Create ActiveEventSSE stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return ActiveEventSSE(
                event="active",
                data=JobEventResponseActiveEventDataStub.create_instance(),
            )
        else:
            return ActiveEventSSE(
                event="active",
                data=JobEventResponseActiveEventDataStub.create_instance(),
            )
