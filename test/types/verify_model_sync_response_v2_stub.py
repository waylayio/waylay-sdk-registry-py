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
    from waylay.services.registry.models.verify_model_sync_response_v2 import (
        VerifyModelSyncResponseV2,
    )

    VerifyModelSyncResponseV2Adapter = TypeAdapter(VerifyModelSyncResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

verify_model_sync_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "message", "result" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "entity" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    },
    "result" : {
      "$ref" : "#/components/schemas/VerifyResult"
    }
  },
  "description" : "Model Health Verified"
}
""",
    object_hook=with_example_provider,
)
verify_model_sync_response_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

verify_model_sync_response_v2_faker = JSF(
    verify_model_sync_response_v2_model_schema, allow_none_optionals=1
)


class VerifyModelSyncResponseV2Stub:
    """VerifyModelSyncResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return verify_model_sync_response_v2_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "VerifyModelSyncResponseV2":
        """Create VerifyModelSyncResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                VerifyModelSyncResponseV2Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return VerifyModelSyncResponseV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
