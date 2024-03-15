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
    from waylay.services.registry.models.batch_args import BatchArgs

    BatchArgsAdapter = TypeAdapter(BatchArgs)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

batch_args_model_schema = json.loads(r"""{
  "title" : "BatchArgs",
  "required" : [ "functionType", "plugName" ],
  "type" : "object",
  "properties" : {
    "plugName" : {
      "title" : "plugName",
      "type" : "string"
    },
    "functionType" : {
      "$ref" : "#/components/schemas/FunctionType"
    },
    "childType" : {
      "title" : "childType",
      "type" : "string"
    }
  }
}
""")
batch_args_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_args_faker = JSF(batch_args_model_schema, allow_none_optionals=1)


class BatchArgsStub:
    """BatchArgs unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_args_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchArgs":
        """Create BatchArgs stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchArgsAdapter.validate_python(cls.create_json())
