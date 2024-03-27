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
    from waylay.services.registry.models.legacy_debug_plug_manifest import (
        LegacyDebugPlugManifest,
    )

    LegacyDebugPlugManifestAdapter = TypeAdapter(LegacyDebugPlugManifest)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

legacy_debug_plug_manifest_model_schema = json.loads(
    r"""{
  "required" : [ "metadata", "name", "runtime", "script", "tenant", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
      "type" : "string",
      "description" : "The logical name for the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/FunctionMeta"
    },
    "tenant" : {
      "$ref" : "#/components/schemas/TenantId"
    },
    "dependencies" : {
      "$ref" : "#/components/schemas/LegacyPlugDependencies"
    },
    "script" : {
      "type" : "string"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
legacy_debug_plug_manifest_model_schema.update({"definitions": MODEL_DEFINITIONS})

legacy_debug_plug_manifest_faker = JSF(
    legacy_debug_plug_manifest_model_schema, allow_none_optionals=1
)


class LegacyDebugPlugManifestStub:
    """LegacyDebugPlugManifest unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_debug_plug_manifest_faker.generate()

    @classmethod
    def create_instance(cls) -> "LegacyDebugPlugManifest":
        """Create LegacyDebugPlugManifest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LegacyDebugPlugManifestAdapter.validate_python(cls.create_json())
