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
    from waylay.services.registry.models.get_runtime_versions_query import (
        GetRuntimeVersionsQuery,
    )

    GetRuntimeVersionsQueryAdapter = TypeAdapter(GetRuntimeVersionsQuery)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

get_runtime_versions_query_model_schema = json.loads(
    r"""{
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
    },
    "functionType" : {
      "type" : "array",
      "description" : "If set, filters on the <code>functionType</code> of a runtime. Uses an exact match.",
      "example" : "plugs",
      "items" : {
        "$ref" : "#/components/schemas/FunctionType"
      }
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "If set, filters on the <code>archiveFormat</code> of a runtime. Uses an exact match.",
      "example" : "node",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
get_runtime_versions_query_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_runtime_versions_query_faker = JSF(
    get_runtime_versions_query_model_schema, allow_none_optionals=1
)


class GetRuntimeVersionsQueryStub:
    """GetRuntimeVersionsQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_runtime_versions_query_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "GetRuntimeVersionsQuery":
        """Create GetRuntimeVersionsQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GetRuntimeVersionsQueryAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GetRuntimeVersionsQueryAdapter.validate_python(
            json, context={"skip_validation": True}
        )
