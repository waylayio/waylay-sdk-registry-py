# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.jobs_for_plug_response_v2 import (
    JobsForPlugResponseV2,
)

from .any_job_for_function_stub import AnyJobForFunctionStub
from .function_ref_stub import FunctionRefStub

from .jobs_for_plug_response_v2_links_stub import JobsForPlugResponseV2LinksStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobsForPlugResponseV2Stub:
    """JobsForPlugResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobsForPlugResponseV2:
        """Create JobsForPlugResponseV2 stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return JobsForPlugResponseV2(
                jobs=[AnyJobForFunctionStub.create_instance()],
                function=FunctionRefStub.create_instance(),
                links=JobsForPlugResponseV2LinksStub.create_instance(),
            )
        else:
            return JobsForPlugResponseV2(
                jobs=[AnyJobForFunctionStub.create_instance()],
                function=FunctionRefStub.create_instance(),
            )
