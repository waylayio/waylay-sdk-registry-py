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
    from waylay.services.registry.models.legacy_plug_query import LegacyPlugQuery

    LegacyPlugQueryAdapter = TypeAdapter(LegacyPlugQuery)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

legacy_plug_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
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
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "tags" : {
      "$ref" : "#/components/schemas/TagsFilter"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
legacy_plug_query_model_schema.update({"definitions": MODEL_DEFINITIONS})

legacy_plug_query_faker = JSF(legacy_plug_query_model_schema, allow_none_optionals=1)


class LegacyPlugQueryStub:
    """LegacyPlugQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_plug_query_faker.generate()

    @classmethod
    def create_instance(cls) -> "LegacyPlugQuery":
        """Create LegacyPlugQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LegacyPlugQueryAdapter.validate_python(cls.create_json())
