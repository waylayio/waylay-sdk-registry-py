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
    from waylay.services.registry.models.webscript1 import Webscript1

    Webscript1Adapter = TypeAdapter(Webscript1)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for Webscript1 not available: {exc}")
    MODELS_AVAILABLE = False

webscript_1_model_schema = json.loads(r"""{
  "title" : "Webscript",
  "required" : [ "webscript" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "job" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "webscript" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""")
webscript_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

webscript_1_faker = JSF(webscript_1_model_schema, allow_none_optionals=1)


class Webscript1Stub:
    """Webscript1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return webscript_1_faker.generate()

    @classmethod
    def create_instance(cls) -> "Webscript1":
        """Create Webscript1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return Webscript1Adapter.validate_python(cls.create_json())
