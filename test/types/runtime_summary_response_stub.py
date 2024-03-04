# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.runtime_summary_response import (
    RuntimeSummaryResponse,
)

from .runtime_summary_stub import RuntimeSummaryStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class RuntimeSummaryResponseStub:
    """RuntimeSummaryResponse unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> RuntimeSummaryResponse:
        """Create RuntimeSummaryResponse stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return RuntimeSummaryResponse(
                runtimes=[RuntimeSummaryStub.create_instance()]
            )
        else:
            return RuntimeSummaryResponse(
                runtimes=[RuntimeSummaryStub.create_instance()]
            )
