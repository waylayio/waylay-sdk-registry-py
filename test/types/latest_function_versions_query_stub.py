# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import warnings

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.latest_function_versions_query import (
        LatestFunctionVersionsQuery,
    )

    LatestFunctionVersionsQueryAdapter = TypeAdapter(LatestFunctionVersionsQuery)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for LatestFunctionVersionsQuery not available: {exc}")
    MODELS_AVAILABLE = False

latest_function_versions_query_model_schema = json.loads(r"""{
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
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
    },
    "nameVersion" : {
      "type" : "array",
      "description" : "Filter on exact `{name}@{version}` functions. Using this filter implies a `latest=false` default, returning multiple versions of the same named versions if they are filtered.",
      "items" : {
        "$ref" : "#/components/schemas/NamedVersion"
      }
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
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
    },
    "latest" : {
      "type" : "boolean",
      "description" : "When `true`, only the latest version per function name is returned. If set to `false`, multiple versions per named function can be returned. Defaults to `true`, except when specific versions are selected with the `nameVersion` filter."
    }
  },
  "additionalProperties" : false,
  "description" : "Latest function versions listing query."
}
""")
latest_function_versions_query_model_schema.update({"definitions": MODEL_DEFINITIONS})

latest_function_versions_query_faker = JSF(
    latest_function_versions_query_model_schema, allow_none_optionals=1
)


class LatestFunctionVersionsQueryStub:
    """LatestFunctionVersionsQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return latest_function_versions_query_faker.generate()

    @classmethod
    def create_instance(cls) -> "LatestFunctionVersionsQuery":
        """Create LatestFunctionVersionsQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LatestFunctionVersionsQueryAdapter.validate_python(cls.create_json())
