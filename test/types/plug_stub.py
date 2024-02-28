# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.plug import Plug
from .hal_link_stub import HALLinkStub

from .hal_link_stub import HALLinkStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class PlugStub:
    """Plug unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> Plug:
        """Create Plug stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return Plug(
                event=HALLinkStub.create_instance(), plug=HALLinkStub.create_instance()
            )
        else:
            return Plug(plug=HALLinkStub.create_instance())
