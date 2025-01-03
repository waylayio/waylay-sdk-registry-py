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
    from waylay.services.registry.models.model2 import Model2

    Model2Adapter = TypeAdapter(Model2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

model_2_model_schema = json.loads(
    r"""{
  "title" : "Model",
  "required" : [ "model" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/HALLinks"
    },
    "model" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
model_2_model_schema.update({"definitions": MODEL_DEFINITIONS})

model_2_faker = JSF(model_2_model_schema, allow_none_optionals=1)


class Model2Stub:
    """Model2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return model_2_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Model2":
        """Create Model2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(Model2Adapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return Model2Adapter.validate_python(json, context={"skip_validation": True})
