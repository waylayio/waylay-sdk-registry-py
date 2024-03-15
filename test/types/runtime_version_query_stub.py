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
    from waylay.services.registry.models.runtime_version_query import (
        RuntimeVersionQuery,
    )

    RuntimeVersionQueryAdapter = TypeAdapter(RuntimeVersionQuery)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

runtime_version_query_model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "latest" : {
      "$ref" : "#/components/schemas/LatestVersionLevel"
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "If set to `true`, deprecated runtimes will be included in the query.",
      "default" : false
    }
  },
  "additionalProperties" : false
}
""")
runtime_version_query_model_schema.update({"definitions": MODEL_DEFINITIONS})

runtime_version_query_faker = JSF(
    runtime_version_query_model_schema, allow_none_optionals=1
)


class RuntimeVersionQueryStub:
    """RuntimeVersionQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return runtime_version_query_faker.generate()

    @classmethod
    def create_instance(cls) -> "RuntimeVersionQuery":
        """Create RuntimeVersionQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return RuntimeVersionQueryAdapter.validate_python(cls.create_json())
