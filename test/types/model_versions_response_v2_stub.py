# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.model_versions_response_v2 import (
    ModelVersionsResponseV2,
)


from .kfserving_response_v2_stub import KfservingResponseV2Stub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class ModelVersionsResponseV2Stub:
    """ModelVersionsResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> ModelVersionsResponseV2:
        """Create ModelVersionsResponseV2 stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return ModelVersionsResponseV2(
                limit=1.337,
                count=1.337,
                page=1.337,
                entities=[KfservingResponseV2Stub.create_instance()],
            )
        else:
            return ModelVersionsResponseV2(
                count=1.337, entities=[KfservingResponseV2Stub.create_instance()]
            )
