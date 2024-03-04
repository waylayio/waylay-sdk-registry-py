# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.legacy_plug_create_query import (
    LegacyPlugCreateQuery,
)


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LegacyPlugCreateQueryStub:
    """LegacyPlugCreateQuery unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyPlugCreateQuery:
        """Create LegacyPlugCreateQuery stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyPlugCreateQuery(
                var_async=True, dry_run=True, scale_to_zero=True
            )
        else:
            return LegacyPlugCreateQuery()
