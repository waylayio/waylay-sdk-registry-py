"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.update_asset_by_role_plugs_asset_role import (
        UpdateAssetByRolePlugsAssetRole,
    )

    UpdateAssetByRolePlugsAssetRoleAdapter = TypeAdapter(
        UpdateAssetByRolePlugsAssetRole
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

update_asset_by_role_plugs_asset_role_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/UpdateAssetByRolePlugsAssetRoleManifest"
  }, {
    "$ref" : "#/components/schemas/UpdateAssetByRolePlugsAssetRoleMain"
  }, {
    "$ref" : "#/components/schemas/UpdateAssetByRolePlugsAssetRoleProject"
  } ]
}
""",
    object_hook=with_example_provider,
)
update_asset_by_role_plugs_asset_role_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

update_asset_by_role_plugs_asset_role_faker = JSF(
    update_asset_by_role_plugs_asset_role_model_schema, allow_none_optionals=1
)


class UpdateAssetByRolePlugsAssetRoleStub:
    """UpdateAssetByRolePlugsAssetRole unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return update_asset_by_role_plugs_asset_role_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "UpdateAssetByRolePlugsAssetRole":
        """Create UpdateAssetByRolePlugsAssetRole stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                UpdateAssetByRolePlugsAssetRoleAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return UpdateAssetByRolePlugsAssetRoleAdapter.validate_python(
            json, context={"skip_validation": True}
        )
