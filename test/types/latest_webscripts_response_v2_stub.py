# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.latest_webscripts_response_v2 import (
    LatestWebscriptsResponseV2,
)


from .latest_webscripts_response_v2_entities_inner_stub import (
    LatestWebscriptsResponseV2EntitiesInnerStub,
)


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LatestWebscriptsResponseV2Stub:
    """LatestWebscriptsResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LatestWebscriptsResponseV2:
        """Create LatestWebscriptsResponseV2 stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LatestWebscriptsResponseV2(
                limit=1.337,
                count=1.337,
                page=1.337,
                entities=[
                    LatestWebscriptsResponseV2EntitiesInnerStub.create_instance()
                ],
            )
        else:
            return LatestWebscriptsResponseV2(
                count=1.337,
                entities=[
                    LatestWebscriptsResponseV2EntitiesInnerStub.create_instance()
                ],
            )
