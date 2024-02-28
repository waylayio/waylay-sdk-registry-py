# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.jobs_for_plug_response_v2_links import (
    JobsForPlugResponseV2Links,
)
from .hal_link_stub import HALLinkStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobsForPlugResponseV2LinksStub:
    """JobsForPlugResponseV2Links unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobsForPlugResponseV2Links:
        """Create JobsForPlugResponseV2Links stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return JobsForPlugResponseV2Links(plug=HALLinkStub.create_instance())
        else:
            return JobsForPlugResponseV2Links()
