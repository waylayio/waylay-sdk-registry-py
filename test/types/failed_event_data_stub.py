# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.failed_event_data import FailedEventData


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class FailedEventDataStub:
    """FailedEventData unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> FailedEventData:
        """Create FailedEventData stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return FailedEventData(prev="completed", failed_reason="")
        else:
            return FailedEventData(failed_reason="")
