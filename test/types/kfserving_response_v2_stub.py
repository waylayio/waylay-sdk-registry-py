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
    from waylay.services.registry.models.kfserving_response_v2 import (
        KfservingResponseV2,
    )

    KfservingResponseV2Adapter = TypeAdapter(KfservingResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

kfserving_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "model", "runtime", "status", "updatedAt", "updatedBy", "updates" ],
  "type" : "object",
  "properties" : {
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this entity."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was created.",
      "format" : "date-time"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "The user that last updated this entity."
    },
    "updatedAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was last updated.",
      "format" : "date-time"
    },
    "updates" : {
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
      "type" : "boolean",
      "description" : "If <code>true</code> this function is deprecated and removed from regular listings."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this function is a draft function and it's assets are still mutable."
    },
    "model" : {
      "$ref" : "#/components/schemas/KFServingManifest"
    }
  }
}
""",
    object_hook=with_example_provider,
)
kfserving_response_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

kfserving_response_v2_faker = JSF(
    kfserving_response_v2_model_schema, allow_none_optionals=1
)


class KfservingResponseV2Stub:
    """KfservingResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return kfserving_response_v2_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "KfservingResponseV2":
        """Create KfservingResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                KfservingResponseV2Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return KfservingResponseV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
