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
    from waylay.services.registry.models.latest_plugs_response_v2_entities_inner import (
        LatestPlugsResponseV2EntitiesInner,
    )

    LatestPlugsResponseV2EntitiesInnerAdapter = TypeAdapter(
        LatestPlugsResponseV2EntitiesInner
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

latest_plugs_response_v2_entities_inner_model_schema = json.loads(
    r"""{
  "title" : "LatestPlugsResponseV2_entities_inner",
  "required" : [ "_links", "createdAt", "createdBy", "deprecated", "draft", "plug", "runtime", "status", "updatedAt", "updatedBy", "updates" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/AltVersionHALLink"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that created this entity."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp at which this entity was created.",
      "format" : "date-time"
    },
    "updatedBy" : {
      "title" : "updatedBy",
      "type" : "string",
      "description" : "The user that last updated this entity."
    },
    "updatedAt" : {
      "title" : "updatedAt",
      "type" : "string",
      "description" : "The timestamp at which this entity was last updated.",
      "format" : "date-time"
    },
    "updates" : {
      "title" : "updates",
      "type" : "array",
      "description" : "The audit logs corresponding to the latest modifying operations on this entity.",
      "items" : {
        "$ref" : "#/components/schemas/UpdateRecord"
      }
    },
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/RuntimeAttributes"
    },
    "deprecated" : {
      "title" : "deprecated",
      "type" : "boolean",
      "description" : "If <code>true</code> this plug is removed from regular listings, as a result of a <code>DELETE</code> with <code>force=false</code>."
    },
    "draft" : {
      "title" : "draft",
      "type" : "boolean",
      "description" : "If <code>true</code> this function is a draft function and it's assets are still mutable."
    },
    "plug" : {
      "$ref" : "#/components/schemas/PlugManifest"
    }
  }
}
""",
    object_hook=with_example_provider,
)
latest_plugs_response_v2_entities_inner_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

latest_plugs_response_v2_entities_inner_faker = JSF(
    latest_plugs_response_v2_entities_inner_model_schema, allow_none_optionals=1
)


class LatestPlugsResponseV2EntitiesInnerStub:
    """LatestPlugsResponseV2EntitiesInner unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return latest_plugs_response_v2_entities_inner_faker.generate()

    @classmethod
    def create_instance(cls) -> "LatestPlugsResponseV2EntitiesInner":
        """Create LatestPlugsResponseV2EntitiesInner stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LatestPlugsResponseV2EntitiesInnerAdapter.validate_python(
            cls.create_json()
        )
