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
    from waylay.services.registry.models.named_webscript_versions_query_v2 import (
        NamedWebscriptVersionsQueryV2,
    )

    NamedWebscriptVersionsQueryV2Adapter = TypeAdapter(NamedWebscriptVersionsQueryV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

named_webscript_versions_query_v2_model_schema = json.loads(
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
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
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
  "description" : "Webscript named versions listing query."
}
""",
    object_hook=with_example_provider,
)
named_webscript_versions_query_v2_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

named_webscript_versions_query_v2_faker = JSF(
    named_webscript_versions_query_v2_model_schema, allow_none_optionals=1
)


class NamedWebscriptVersionsQueryV2Stub:
    """NamedWebscriptVersionsQueryV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return named_webscript_versions_query_v2_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "NamedWebscriptVersionsQueryV2":
        """Create NamedWebscriptVersionsQueryV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                NamedWebscriptVersionsQueryV2Adapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return NamedWebscriptVersionsQueryV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
