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
    from waylay.services.registry.models.legacy_plug_request import LegacyPlugRequest

    LegacyPlugRequestAdapter = TypeAdapter(LegacyPlugRequest)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for LegacyPlugRequest not available: {exc}")
    MODELS_AVAILABLE = False

legacy_plug_request_model_schema = json.loads(r"""{
  "required" : [ "metadata", "name", "script", "type", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "script" : {
      "type" : "string"
    },
    "dependencies" : {
      "$ref" : "#/components/schemas/LegacyPlugDependencies"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/LegacyPlugRequest_metadata"
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    }
  },
  "additionalProperties" : false
}
""")
legacy_plug_request_model_schema.update({"definitions": MODEL_DEFINITIONS})

legacy_plug_request_faker = JSF(
    legacy_plug_request_model_schema, allow_none_optionals=1
)


class LegacyPlugRequestStub:
    """LegacyPlugRequest unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_plug_request_faker.generate()

    @classmethod
    def create_instance(cls) -> "LegacyPlugRequest":
        """Create LegacyPlugRequest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LegacyPlugRequestAdapter.validate_python(cls.create_json())
