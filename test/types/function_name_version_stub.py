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
    from waylay.services.registry.models.function_name_version import (
        FunctionNameVersion,
    )

    FunctionNameVersionAdapter = TypeAdapter(FunctionNameVersion)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

function_name_version_model_schema = json.loads(r"""{
  "required" : [ "name", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "The logical name for the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  }
}
""")
function_name_version_model_schema.update({"definitions": MODEL_DEFINITIONS})

function_name_version_faker = JSF(
    function_name_version_model_schema, allow_none_optionals=1
)


class FunctionNameVersionStub:
    """FunctionNameVersion unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return function_name_version_faker.generate()

    @classmethod
    def create_instance(cls) -> "FunctionNameVersion":
        """Create FunctionNameVersion stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return FunctionNameVersionAdapter.validate_python(cls.create_json())
