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
    from waylay.services.registry.models.legacy_plug_response_metadata import (
        LegacyPlugResponseMetadata,
    )

    LegacyPlugResponseMetadataAdapter = TypeAdapter(LegacyPlugResponseMetadata)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

legacy_plug_response_metadata_model_schema = json.loads(r"""{
  "title" : "LegacyPlugResponse_metadata",
  "type" : "object",
  "properties" : {
    "documentation" : {
      "$ref" : "#/components/schemas/LegacyDocumentation"
    },
    "author" : {
      "title" : "author",
      "type" : "string"
    },
    "description" : {
      "title" : "description",
      "type" : "string"
    },
    "category" : {
      "title" : "category",
      "type" : "string"
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "iconURL" : {
      "title" : "iconURL",
      "type" : "string"
    },
    "friendlyName" : {
      "title" : "friendlyName",
      "type" : "string"
    }
  }
}
""")
legacy_plug_response_metadata_model_schema.update({"definitions": MODEL_DEFINITIONS})

legacy_plug_response_metadata_faker = JSF(
    legacy_plug_response_metadata_model_schema, allow_none_optionals=1
)


class LegacyPlugResponseMetadataStub:
    """LegacyPlugResponseMetadata unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_plug_response_metadata_faker.generate()

    @classmethod
    def create_instance(cls) -> "LegacyPlugResponseMetadata":
        """Create LegacyPlugResponseMetadata stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LegacyPlugResponseMetadataAdapter.validate_python(cls.create_json())
