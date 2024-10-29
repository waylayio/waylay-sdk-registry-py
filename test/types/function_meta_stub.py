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
    from waylay.services.registry.models.function_meta import FunctionMeta

    FunctionMetaAdapter = TypeAdapter(FunctionMeta)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

function_meta_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "author" : {
      "type" : "string",
      "description" : "The author of the function."
    },
    "description" : {
      "type" : "string",
      "description" : "A description of the function"
    },
    "iconURL" : {
      "type" : "string",
      "description" : "An url to an icon that represents this function."
    },
    "category" : {
      "type" : "string",
      "description" : "A category for this function (Deprecated: use tags to categorise your functions)",
      "deprecated" : true
    }
  }
}
""",
    object_hook=with_example_provider,
)
function_meta_model_schema.update({"definitions": MODEL_DEFINITIONS})

function_meta_faker = JSF(function_meta_model_schema, allow_none_optionals=1)


class FunctionMetaStub:
    """FunctionMeta unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return function_meta_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "FunctionMeta":
        """Create FunctionMeta stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                FunctionMetaAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return FunctionMetaAdapter.validate_python(
            json, context={"skip_validation": True}
        )
