# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.openfaas_function_ref import OpenfaasFunctionRef


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class OpenfaasFunctionRefStub:
    """OpenfaasFunctionRef unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> OpenfaasFunctionRef:
        """Create OpenfaasFunctionRef stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return OpenfaasFunctionRef(namespace="", endpoint="")
        else:
            return OpenfaasFunctionRef(namespace="", endpoint="")
