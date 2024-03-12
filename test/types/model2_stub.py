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
    from waylay.services.registry.models.model2 import Model2

    Model2Adapter = TypeAdapter(Model2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for Model2 not available: {exc}")
    MODELS_AVAILABLE = False

model_2_model_schema = json.loads(r"""{
  "title" : "Model",
  "required" : [ "model" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "model" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""")
model_2_model_schema.update({"definitions": MODEL_DEFINITIONS})

model_2_faker = JSF(model_2_model_schema, allow_none_optionals=1)


class Model2Stub:
    """Model2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return model_2_faker.generate()

    @classmethod
    def create_instance(cls) -> "Model2":
        """Create Model2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return Model2Adapter.validate_python(cls.create_json())
