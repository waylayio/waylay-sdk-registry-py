# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.get_webscript_response_v2_links import (
    GetWebscriptResponseV2Links,
)
from .hal_link_stub import HALLinkStub

from .hal_link_stub import HALLinkStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class GetWebscriptResponseV2LinksStub:
    """GetWebscriptResponseV2Links unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> GetWebscriptResponseV2Links:
        """Create GetWebscriptResponseV2Links stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return GetWebscriptResponseV2Links(
                invoke=HALLinkStub.create_instance(), jobs=HALLinkStub.create_instance()
            )
        else:
            return GetWebscriptResponseV2Links()
