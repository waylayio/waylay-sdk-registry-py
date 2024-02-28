# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.invokable_webscript_response_entity import (
    InvokableWebscriptResponseEntity,
)


from .invokable_webscript_response_entity_webscript_stub import (
    InvokableWebscriptResponseEntityWebscriptStub,
)


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class InvokableWebscriptResponseEntityStub:
    """InvokableWebscriptResponseEntity unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> InvokableWebscriptResponseEntity:
        """Create InvokableWebscriptResponseEntity stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return InvokableWebscriptResponseEntity(
                status="registered",
                draft=True,
                webscript=InvokableWebscriptResponseEntityWebscriptStub.create_instance(),
                secret="",
            )
        else:
            return InvokableWebscriptResponseEntity(
                status="registered",
                draft=True,
                webscript=InvokableWebscriptResponseEntityWebscriptStub.create_instance(),
            )
