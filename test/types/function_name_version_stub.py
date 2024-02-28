# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.function_name_version import FunctionNameVersion


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class FunctionNameVersionStub:
    """FunctionNameVersion unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> FunctionNameVersion:
        """Create FunctionNameVersion stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return FunctionNameVersion(
                name="",
                version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
            )
        else:
            return FunctionNameVersion(
                name="",
                version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
            )
