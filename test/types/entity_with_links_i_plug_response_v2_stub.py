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
    from waylay.services.registry.models.entity_with_links_i_plug_response_v2 import (
        EntityWithLinksIPlugResponseV2,
    )

    EntityWithLinksIPlugResponseV2Adapter = TypeAdapter(EntityWithLinksIPlugResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

entity_with_links_i_plug_response_v2__model_schema = json.loads(
    r"""{
  "title" : "EntityWithLinks_IPlugResponseV2_",
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "plug", "runtime", "status", "updatedAt", "updatedBy" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/AltEmbeddedVersion_IPlugResponseV2_"
    },
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
      "description" : "The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations.",
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
entity_with_links_i_plug_response_v2__model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

entity_with_links_i_plug_response_v2__faker = JSF(
    entity_with_links_i_plug_response_v2__model_schema, allow_none_optionals=1
)


class EntityWithLinksIPlugResponseV2Stub:
    """EntityWithLinksIPlugResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return entity_with_links_i_plug_response_v2__faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "EntityWithLinksIPlugResponseV2":
        """Create EntityWithLinksIPlugResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                EntityWithLinksIPlugResponseV2Adapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return EntityWithLinksIPlugResponseV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
