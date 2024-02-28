# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.invokable_webscript_response_entity_webscript import (
    InvokableWebscriptResponseEntityWebscript,
)


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class InvokableWebscriptResponseEntityWebscriptStub:
    """InvokableWebscriptResponseEntityWebscript unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> InvokableWebscriptResponseEntityWebscript:
        """Create InvokableWebscriptResponseEntityWebscript stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return InvokableWebscriptResponseEntityWebscript(
                name="",
                version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
                private=True,
                allow_hmac=True,
            )
        else:
            return InvokableWebscriptResponseEntityWebscript(
                name="",
                version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
                private=True,
                allow_hmac=True,
            )
