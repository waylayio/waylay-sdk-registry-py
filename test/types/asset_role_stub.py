# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.asset_role import AssetRole

    AssetRoleAdapter = TypeAdapter(AssetRole)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

asset_role_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Classification of assets with regard to their role.",
  "enum" : [ "manifest", "project", "main", "lib", "script", "other" ]
}
""",
    object_hook=with_example_provider,
)
asset_role_model_schema.update({"definitions": MODEL_DEFINITIONS})

asset_role_faker = JSF(asset_role_model_schema, allow_none_optionals=1)


class AssetRoleStub:
    """AssetRole unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return asset_role_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AssetRole":
        """Create AssetRole stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(AssetRoleAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AssetRoleAdapter.validate_python(json, context={"skip_validation": True})
