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
    from waylay.services.registry.models.get_runtime_example_query import (
        GetRuntimeExampleQuery,
    )

    GetRuntimeExampleQueryAdapter = TypeAdapter(GetRuntimeExampleQuery)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

get_runtime_example_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "ls" : {
      "type" : "boolean",
      "description" : "If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime.",
      "default" : false
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "If set to `true`, deprecated runtimes will be included in the query.",
      "default" : true
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
get_runtime_example_query_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_runtime_example_query_faker = JSF(
    get_runtime_example_query_model_schema, allow_none_optionals=1
)


class GetRuntimeExampleQueryStub:
    """GetRuntimeExampleQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_runtime_example_query_faker.generate()

    @classmethod
    def create_instance(cls) -> "GetRuntimeExampleQuery":
        """Create GetRuntimeExampleQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return GetRuntimeExampleQueryAdapter.validate_python(cls.create_json())
