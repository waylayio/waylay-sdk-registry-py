# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.verify_webscript_sync_response_v2 import (
        VerifyWebscriptSyncResponseV2,
    )

    VerifyWebscriptSyncResponseV2Adapter = TypeAdapter(VerifyWebscriptSyncResponseV2)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

verify_webscript_sync_response_v2_model_schema = json.loads(r"""{
  "required" : [ "entity", "message", "result" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "entity" : {
      "$ref" : "#/components/schemas/WebscriptResponseV2"
    },
    "result" : {
      "$ref" : "#/components/schemas/VerifyResult"
    }
  },
  "description" : "Webscript Health Verified"
}
""")
verify_webscript_sync_response_v2_model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

verify_webscript_sync_response_v2_faker = JSF(
    verify_webscript_sync_response_v2_model_schema, allow_none_optionals=1
)


class VerifyWebscriptSyncResponseV2Stub:
    """VerifyWebscriptSyncResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return verify_webscript_sync_response_v2_faker.generate()

    @classmethod
    def create_instance(cls) -> "VerifyWebscriptSyncResponseV2":
        """Create VerifyWebscriptSyncResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return VerifyWebscriptSyncResponseV2Adapter.validate_python(cls.create_json())
