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
    from waylay.services.registry.models.asset_summary import AssetSummary

    AssetSummaryAdapter = TypeAdapter(AssetSummary)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for AssetSummary not available: {exc}")
    MODELS_AVAILABLE = False

asset_summary_model_schema = json.loads(r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "File name"
    },
    "title" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "role" : {
      "$ref" : "#/components/schemas/AssetRole"
    }
  }
}
""")
asset_summary_model_schema.update({"definitions": MODEL_DEFINITIONS})

asset_summary_faker = JSF(asset_summary_model_schema, allow_none_optionals=1)


class AssetSummaryStub:
    """AssetSummary unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return asset_summary_faker.generate()

    @classmethod
    def create_instance(cls) -> "AssetSummary":
        """Create AssetSummary stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return AssetSummaryAdapter.validate_python(cls.create_json())
