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
    from waylay.services.registry.models.plug2 import Plug2

    Plug2Adapter = TypeAdapter(Plug2)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

plug_2_model_schema = json.loads(r"""{
  "title" : "Plug",
  "required" : [ "plug" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "plug" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""")
plug_2_model_schema.update({"definitions": MODEL_DEFINITIONS})

plug_2_faker = JSF(plug_2_model_schema, allow_none_optionals=1)


class Plug2Stub:
    """Plug2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return plug_2_faker.generate()

    @classmethod
    def create_instance(cls) -> "Plug2":
        """Create Plug2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return Plug2Adapter.validate_python(cls.create_json())
