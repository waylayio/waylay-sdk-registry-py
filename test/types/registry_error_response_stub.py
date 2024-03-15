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
    from waylay.services.registry.models.registry_error_response import (
        RegistryErrorResponse,
    )

    RegistryErrorResponseAdapter = TypeAdapter(RegistryErrorResponse)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

registry_error_response_model_schema = json.loads(r"""{
  "required" : [ "code", "error", "statusCode" ],
  "type" : "object",
  "properties" : {
    "error" : {
      "type" : "string"
    },
    "code" : {
      "type" : "string"
    },
    "statusCode" : {
      "type" : "number"
    },
    "data" : {
      "type" : "object"
    }
  }
}
""")
registry_error_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

registry_error_response_faker = JSF(
    registry_error_response_model_schema, allow_none_optionals=1
)


class RegistryErrorResponseStub:
    """RegistryErrorResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return registry_error_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "RegistryErrorResponse":
        """Create RegistryErrorResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return RegistryErrorResponseAdapter.validate_python(cls.create_json())
