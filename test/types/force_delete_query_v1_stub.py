# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.force_delete_query_v1 import ForceDeleteQueryV1


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class ForceDeleteQueryV1Stub:
    """ForceDeleteQueryV1 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> ForceDeleteQueryV1:
        """Create ForceDeleteQueryV1 stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return ForceDeleteQueryV1(var_async=True, force=True)
        else:
            return ForceDeleteQueryV1()
