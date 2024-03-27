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
    from waylay.services.registry.models.asset_condition import AssetCondition

    AssetConditionAdapter = TypeAdapter(AssetCondition)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

asset_condition_model_schema = json.loads(
    r"""{
  "title" : "AssetCondition",
  "required" : [ "pattern", "role" ],
  "type" : "object",
  "properties" : {
    "title" : {
      "title" : "title",
      "type" : "string"
    },
    "description" : {
      "title" : "description",
      "type" : "string"
    },
    "role" : {
      "$ref" : "#/components/schemas/AssetRole"
    },
    "pattern" : {
      "$ref" : "#/components/schemas/AssetCondition_pattern"
    },
    "contentType" : {
      "$ref" : "#/components/schemas/AssetCondition_contentType"
    },
    "min" : {
      "title" : "min",
      "type" : "number",
      "description" : "The minimal number of files that must match this pattern. Use `0` for an optional file.",
      "example" : 0
    },
    "max" : {
      "title" : "max",
      "type" : "number",
      "description" : "The maximal number of files that can match this pattern. Use `0` for a disallowed file. This condition only raises an error if there are no other conditions that",
      "example" : 1
    },
    "maxSize" : {
      "title" : "maxSize",
      "type" : "string",
      "description" : "The maximum size for each file matching this pattern (in bytes, unless unit is provided)"
    },
    "schema" : {
      "title" : "schema",
      "description" : "The json schema validator that applies (in case of `application/json` entries)."
    }
  },
  "description" : "Describes conditions on the set of files that match a file pattern."
}
""",
    object_hook=with_example_provider,
)
asset_condition_model_schema.update({"definitions": MODEL_DEFINITIONS})

asset_condition_faker = JSF(asset_condition_model_schema, allow_none_optionals=1)


class AssetConditionStub:
    """AssetCondition unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return asset_condition_faker.generate()

    @classmethod
    def create_instance(cls) -> "AssetCondition":
        """Create AssetCondition stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return AssetConditionAdapter.validate_python(cls.create_json())
