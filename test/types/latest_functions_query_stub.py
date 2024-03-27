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
    from waylay.services.registry.models.latest_functions_query import (
        LatestFunctionsQuery,
    )

    LatestFunctionsQueryAdapter = TypeAdapter(LatestFunctionsQuery)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

latest_functions_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Request to list latest function versions per named function. A request that only uses these query parameters will include links to the _latest_ draft/published versions."
}
""",
    object_hook=with_example_provider,
)
latest_functions_query_model_schema.update({"definitions": MODEL_DEFINITIONS})

latest_functions_query_faker = JSF(
    latest_functions_query_model_schema, allow_none_optionals=1
)


class LatestFunctionsQueryStub:
    """LatestFunctionsQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return latest_functions_query_faker.generate()

    @classmethod
    def create_instance(cls) -> "LatestFunctionsQuery":
        """Create LatestFunctionsQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LatestFunctionsQueryAdapter.validate_python(cls.create_json())
