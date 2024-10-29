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
    from waylay.services.registry.models.webscript2 import Webscript2

    Webscript2Adapter = TypeAdapter(Webscript2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

webscript_2_model_schema = json.loads(
    r"""{
  "title" : "Webscript",
  "required" : [ "webscript" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/HALLinks"
    },
    "webscript" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
webscript_2_model_schema.update({"definitions": MODEL_DEFINITIONS})

webscript_2_faker = JSF(webscript_2_model_schema, allow_none_optionals=1)


class Webscript2Stub:
    """Webscript2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return webscript_2_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Webscript2":
        """Create Webscript2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(Webscript2Adapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return Webscript2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
