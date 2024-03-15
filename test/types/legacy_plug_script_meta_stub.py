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
    from waylay.services.registry.models.legacy_plug_script_meta import (
        LegacyPlugScriptMeta,
    )

    LegacyPlugScriptMetaAdapter = TypeAdapter(LegacyPlugScriptMeta)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

legacy_plug_script_meta_model_schema = json.loads(r"""{
  "title" : "LegacyPlugScriptMeta",
  "required" : [ "rawData", "supportedStates" ],
  "type" : "object",
  "properties" : {
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
    },
    "supportedStates" : {
      "title" : "supportedStates",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "rawData" : {
      "title" : "rawData",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/LegacyPlugScriptMeta_rawData_inner"
      }
    },
    "requiredProperties" : {
      "$ref" : "#/components/schemas/LegacyRequiredProperties"
    }
  }
}
""")
legacy_plug_script_meta_model_schema.update({"definitions": MODEL_DEFINITIONS})

legacy_plug_script_meta_faker = JSF(
    legacy_plug_script_meta_model_schema, allow_none_optionals=1
)


class LegacyPlugScriptMetaStub:
    """LegacyPlugScriptMeta unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_plug_script_meta_faker.generate()

    @classmethod
    def create_instance(cls) -> "LegacyPlugScriptMeta":
        """Create LegacyPlugScriptMeta stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LegacyPlugScriptMetaAdapter.validate_python(cls.create_json())
