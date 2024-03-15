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
    from waylay.services.registry.models.get_runtime_by_name_and_version_query import (
        GetRuntimeByNameAndVersionQuery,
    )

    GetRuntimeByNameAndVersionQueryAdapter = TypeAdapter(
        GetRuntimeByNameAndVersionQuery
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

get_runtime_by_name_and_version_query_model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "If set to `true`, deprecated runtimes will be included in the query.",
      "default" : true
    }
  },
  "additionalProperties" : false
}
""")
get_runtime_by_name_and_version_query_model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

get_runtime_by_name_and_version_query_faker = JSF(
    get_runtime_by_name_and_version_query_model_schema, allow_none_optionals=1
)


class GetRuntimeByNameAndVersionQueryStub:
    """GetRuntimeByNameAndVersionQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_runtime_by_name_and_version_query_faker.generate()

    @classmethod
    def create_instance(cls) -> "GetRuntimeByNameAndVersionQuery":
        """Create GetRuntimeByNameAndVersionQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return GetRuntimeByNameAndVersionQueryAdapter.validate_python(cls.create_json())
