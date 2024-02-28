# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.undeploy_args import UndeployArgs


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class UndeployArgsStub:
    """UndeployArgs unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> UndeployArgs:
        """Create UndeployArgs stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return UndeployArgs(
                namespace="",
                endpoint="",
                runtime_name="",
                runtime_version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
                revision="",
                is_native_plug=True,
                delete_entity=True,
            )
        else:
            return UndeployArgs(
                namespace="",
                endpoint="",
                runtime_name="",
                runtime_version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
                is_native_plug=True,
                delete_entity=True,
            )
