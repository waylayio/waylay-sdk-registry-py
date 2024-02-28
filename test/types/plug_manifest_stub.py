# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.plug_manifest import PlugManifest
from .function_deploy_overrides_type_stub import FunctionDeployOverridesTypeStub


from .semantic_version_range_stub import SemanticVersionRangeStub

from .plug_meta_stub import PlugMetaStub


from .plug_interface_stub import PlugInterfaceStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class PlugManifestStub:
    """PlugManifest unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> PlugManifest:
        """Create PlugManifest stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return PlugManifest(
                deploy=FunctionDeployOverridesTypeStub.create_instance(),
                name="",
                version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
                runtime="",
                runtime_version=SemanticVersionRangeStub.create_instance(),
                metadata=PlugMetaStub.create_instance(),
                type="sensor",
                interface=PlugInterfaceStub.create_instance(),
            )
        else:
            return PlugManifest(
                name="",
                version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
                runtime="",
                metadata=PlugMetaStub.create_instance(),
                type="sensor",
                interface=PlugInterfaceStub.create_instance(),
            )
