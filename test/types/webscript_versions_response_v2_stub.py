# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.webscript_versions_response_v2 import (
    WebscriptVersionsResponseV2,
)


from .webscript_response_with_invoke_link_v2_stub import (
    WebscriptResponseWithInvokeLinkV2Stub,
)


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class WebscriptVersionsResponseV2Stub:
    """WebscriptVersionsResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> WebscriptVersionsResponseV2:
        """Create WebscriptVersionsResponseV2 stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return WebscriptVersionsResponseV2(
                limit=1.337,
                count=1.337,
                page=1.337,
                entities=[WebscriptResponseWithInvokeLinkV2Stub.create_instance()],
            )
        else:
            return WebscriptVersionsResponseV2(
                count=1.337,
                entities=[WebscriptResponseWithInvokeLinkV2Stub.create_instance()],
            )
