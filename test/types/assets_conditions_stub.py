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
    from waylay.services.registry.models.assets_conditions import AssetsConditions

    AssetsConditionsAdapter = TypeAdapter(AssetsConditions)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

assets_conditions_model_schema = json.loads(
    r"""{
  "title" : "AssetsConditions",
  "type" : "object",
  "properties" : {
    "conditions" : {
      "title" : "conditions",
      "type" : "array",
      "description" : "All files in a function archive are checked against these conditions. A file that is not matched is ignored.",
      "items" : {
        "$ref" : "#/components/schemas/AssetCondition"
      }
    },
    "maxSize" : {
      "title" : "maxSize",
      "type" : "string",
      "description" : "The maximum size of the archive (in bytes, unless unit is provided)"
    }
  },
  "description" : "Describes the assets that are required/allowed/supported for a function."
}
""",
    object_hook=with_example_provider,
)
assets_conditions_model_schema.update({"definitions": MODEL_DEFINITIONS})

assets_conditions_faker = JSF(assets_conditions_model_schema, allow_none_optionals=1)


class AssetsConditionsStub:
    """AssetsConditions unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return assets_conditions_faker.generate()

    @classmethod
    def create_instance(cls) -> "AssetsConditions":
        """Create AssetsConditions stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return AssetsConditionsAdapter.validate_python(cls.create_json())
