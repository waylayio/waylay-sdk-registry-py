# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.kf_serving_manifest import KFServingManifest
from .function_deploy_overrides_type_stub import FunctionDeployOverridesTypeStub


from .semantic_version_range_stub import SemanticVersionRangeStub

from .function_meta_stub import FunctionMetaStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class KFServingManifestStub:
    """KFServingManifest unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> KFServingManifest:
        """Create KFServingManifest stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return KFServingManifest(
                deploy=FunctionDeployOverridesTypeStub.create_instance(),
                name="",
                version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
                runtime="",
                runtime_version=SemanticVersionRangeStub.create_instance(),
                metadata=FunctionMetaStub.create_instance(),
            )
        else:
            return KFServingManifest(
                name="",
                version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
                runtime="",
                metadata=FunctionMetaStub.create_instance(),
            )
