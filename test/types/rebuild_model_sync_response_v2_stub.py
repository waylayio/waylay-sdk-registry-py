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
    from waylay.services.registry.models.rebuild_model_sync_response_v2 import (
        RebuildModelSyncResponseV2,
    )

    RebuildModelSyncResponseV2Adapter = TypeAdapter(RebuildModelSyncResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for RebuildModelSyncResponseV2 not available: {exc}")
    MODELS_AVAILABLE = False

rebuild_model_sync_response_v2_model_schema = json.loads(r"""{
  "required" : [ "causes", "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "causes" : {
      "$ref" : "#/components/schemas/JobCauses"
    },
    "entity" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    }
  },
  "description" : "Model Rebuild Ignored"
}
""")
rebuild_model_sync_response_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

rebuild_model_sync_response_v2_faker = JSF(
    rebuild_model_sync_response_v2_model_schema, allow_none_optionals=1
)


class RebuildModelSyncResponseV2Stub:
    """RebuildModelSyncResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return rebuild_model_sync_response_v2_faker.generate()

    @classmethod
    def create_instance(cls) -> "RebuildModelSyncResponseV2":
        """Create RebuildModelSyncResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return RebuildModelSyncResponseV2Adapter.validate_python(cls.create_json())
