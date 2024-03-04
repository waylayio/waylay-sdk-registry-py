# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.kf_serving_latest_versions_query_v2 import (
    KFServingLatestVersionsQueryV2,
)


from .latest_function_versions_query_stub import LatestFunctionVersionsQueryStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class KFServingLatestVersionsQueryV2Stub:
    """KFServingLatestVersionsQueryV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> KFServingLatestVersionsQueryV2:
        """Create KFServingLatestVersionsQueryV2 stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        # return instance of first type from `anyOf`
        return LatestFunctionVersionsQueryStub.create_instance(
            include_optional=include_optional
        )
