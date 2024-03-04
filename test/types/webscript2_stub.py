# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.webscript2 import Webscript2
from .hal_link_stub import HALLinkStub

from .hal_link_stub import HALLinkStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class Webscript2Stub:
    """Webscript2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> Webscript2:
        """Create Webscript2 stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return Webscript2(
                job=HALLinkStub.create_instance(),
                webscript=HALLinkStub.create_instance(),
            )
        else:
            return Webscript2(webscript=HALLinkStub.create_instance())
