"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.get_asset_by_role_plugs_asset_role_manifest import (
        GetAssetByRolePlugsAssetRoleManifest,
    )

    GetAssetByRolePlugsAssetRoleManifestAdapter = TypeAdapter(
        GetAssetByRolePlugsAssetRoleManifest
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

get_asset_by_role_plugs_asset_role_manifest_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Metadata specification of the function for the waylay platform.",
  "enum" : [ "manifest" ]
}
""",
    object_hook=with_example_provider,
)
get_asset_by_role_plugs_asset_role_manifest_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

get_asset_by_role_plugs_asset_role_manifest_faker = JSF(
    get_asset_by_role_plugs_asset_role_manifest_model_schema, allow_none_optionals=1
)


class GetAssetByRolePlugsAssetRoleManifestStub:
    """GetAssetByRolePlugsAssetRoleManifest unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_asset_by_role_plugs_asset_role_manifest_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "GetAssetByRolePlugsAssetRoleManifest":
        """Create GetAssetByRolePlugsAssetRoleManifest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GetAssetByRolePlugsAssetRoleManifestAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GetAssetByRolePlugsAssetRoleManifestAdapter.validate_python(
            json, context={"skip_validation": True}
        )
