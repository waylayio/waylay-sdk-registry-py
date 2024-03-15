# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.legacy_plug_response import LegacyPlugResponse

    LegacyPlugResponseAdapter = TypeAdapter(LegacyPlugResponse)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

legacy_plug_response_model_schema = json.loads(r"""{
  "required" : [ "commands", "isDeprecated", "mediaType", "metadata", "name", "status", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "author" : {
      "type" : "string"
    },
    "category" : {
      "type" : "string"
    },
    "iconURL" : {
      "type" : "string"
    },
    "documentationURL" : {
      "type" : "string"
    },
    "isDeprecated" : {
      "type" : "boolean"
    },
    "description" : {
      "type" : "string"
    },
    "states" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "rawData" : {
      "type" : "array",
      "items" : {
        "type" : "object"
      }
    },
    "mediaType" : {
      "$ref" : "#/components/schemas/MediaType"
    },
    "configuration" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/LegacyConfigurationResponseObject"
      }
    },
    "commands" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/LegacyPlugResponse_metadata"
    }
  }
}
""")
legacy_plug_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

legacy_plug_response_faker = JSF(
    legacy_plug_response_model_schema, allow_none_optionals=1
)


class LegacyPlugResponseStub:
    """LegacyPlugResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_plug_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "LegacyPlugResponse":
        """Create LegacyPlugResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LegacyPlugResponseAdapter.validate_python(cls.create_json())
