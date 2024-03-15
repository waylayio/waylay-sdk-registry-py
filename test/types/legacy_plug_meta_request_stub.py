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
    from waylay.services.registry.models.legacy_plug_meta_request import (
        LegacyPlugMetaRequest,
    )

    LegacyPlugMetaRequestAdapter = TypeAdapter(LegacyPlugMetaRequest)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

legacy_plug_meta_request_model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "author" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "category" : {
      "type" : "string"
    },
    "tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "iconURL" : {
      "type" : "string"
    },
    "friendlyName" : {
      "type" : "string"
    },
    "documentation" : {
      "$ref" : "#/components/schemas/LegacyPlugRequest_metadata_documentation"
    },
    "documentationURL" : {
      "type" : "string"
    }
  },
  "additionalProperties" : false
}
""")
legacy_plug_meta_request_model_schema.update({"definitions": MODEL_DEFINITIONS})

legacy_plug_meta_request_faker = JSF(
    legacy_plug_meta_request_model_schema, allow_none_optionals=1
)


class LegacyPlugMetaRequestStub:
    """LegacyPlugMetaRequest unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_plug_meta_request_faker.generate()

    @classmethod
    def create_instance(cls) -> "LegacyPlugMetaRequest":
        """Create LegacyPlugMetaRequest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LegacyPlugMetaRequestAdapter.validate_python(cls.create_json())
