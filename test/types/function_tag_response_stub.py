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
    from waylay.services.registry.models.function_tag_response import (
        FunctionTagResponse,
    )

    FunctionTagResponseAdapter = TypeAdapter(FunctionTagResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

function_tag_response_model_schema = json.loads(
    r"""{
  "required" : [ "tag" ],
  "type" : "object",
  "properties" : {
    "tag" : {
      "$ref" : "#/components/schemas/Tag"
    }
  },
  "description" : "Function Tag Found"
}
""",
    object_hook=with_example_provider,
)
function_tag_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

function_tag_response_faker = JSF(
    function_tag_response_model_schema, allow_none_optionals=1
)


class FunctionTagResponseStub:
    """FunctionTagResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return function_tag_response_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "FunctionTagResponse":
        """Create FunctionTagResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                FunctionTagResponseAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return FunctionTagResponseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
