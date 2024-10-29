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
    from waylay.services.registry.models.plug1 import Plug1

    Plug1Adapter = TypeAdapter(Plug1)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

plug_1_model_schema = json.loads(
    r"""{
  "title" : "Plug",
  "required" : [ "plug" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/HALLinks"
    },
    "plug" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
plug_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

plug_1_faker = JSF(plug_1_model_schema, allow_none_optionals=1)


class Plug1Stub:
    """Plug1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return plug_1_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Plug1":
        """Create Plug1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(Plug1Adapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return Plug1Adapter.validate_python(json, context={"skip_validation": True})
