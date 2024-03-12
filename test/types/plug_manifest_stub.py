# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import warnings

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.plug_manifest import PlugManifest

    PlugManifestAdapter = TypeAdapter(PlugManifest)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for PlugManifest not available: {exc}")
    MODELS_AVAILABLE = False

plug_manifest_model_schema = json.loads(r"""{
  "title" : "PlugManifest",
  "required" : [ "interface", "metadata", "name", "runtime", "type", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
      "title" : "name",
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
      "$ref" : "#/components/schemas/PlugMeta"
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    },
    "interface" : {
      "$ref" : "#/components/schemas/PlugInterface"
    }
  }
}
""")
plug_manifest_model_schema.update({"definitions": MODEL_DEFINITIONS})

plug_manifest_faker = JSF(plug_manifest_model_schema, allow_none_optionals=1)


class PlugManifestStub:
    """PlugManifest unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return plug_manifest_faker.generate()

    @classmethod
    def create_instance(cls) -> "PlugManifest":
        """Create PlugManifest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return PlugManifestAdapter.validate_python(cls.create_json())
