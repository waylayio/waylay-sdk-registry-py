# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.job_event_sse import JobEventSSE


from .active_event_sse_stub import ActiveEventSSEStub


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
        return ActiveEventSSEStub.create_instance(include_optional=include_optional)
