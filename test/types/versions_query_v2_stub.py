# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.versions_query_v2 import VersionsQueryV2

    VersionsQueryV2Adapter = TypeAdapter(VersionsQueryV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

versions_query_v2_model_schema = json.loads(
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
    "endpoint" : {
      "type" : "string",
      "description" : "Filter on the openfaas endpoint. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "imageName" : {
      "type" : "string",
      "description" : "Filter on the container image name. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "storageLocation" : {
      "type" : "string",
      "description" : "Filter on the storageLocation. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
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
    }
  },
  "additionalProperties" : false,
  "description" : "Function versions paged query"
}
""",
    object_hook=with_example_provider,
)
versions_query_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

versions_query_v2_faker = JSF(versions_query_v2_model_schema, allow_none_optionals=1)


class VersionsQueryV2Stub:
    """VersionsQueryV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return versions_query_v2_faker.generate()

    @classmethod
    def create_instance(cls) -> "VersionsQueryV2":
        """Create VersionsQueryV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return VersionsQueryV2Adapter.validate_python(cls.create_json())
