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
    from waylay.services.registry.models.model1 import Model1

    Model1Adapter = TypeAdapter(Model1)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

model_1_model_schema = json.loads(
    r"""{
  "title" : "Model",
  "required" : [ "model" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "job" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "model" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
model_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

model_1_faker = JSF(model_1_model_schema, allow_none_optionals=1)


class Model1Stub:
    """Model1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return model_1_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Model1":
        """Create Model1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(Model1Adapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return Model1Adapter.validate_python(json, context={"skip_validation": True})
