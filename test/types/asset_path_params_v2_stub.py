# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.asset_path_params_v2 import AssetPathParamsV2


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class AssetPathParamsV2Stub:
    """AssetPathParamsV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> AssetPathParamsV2:
        """Create AssetPathParamsV2 stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return AssetPathParamsV2(wildcard="")
        else:
            return AssetPathParamsV2(wildcard="")
