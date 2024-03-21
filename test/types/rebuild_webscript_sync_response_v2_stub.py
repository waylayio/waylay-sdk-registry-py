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
    from waylay.services.registry.models.rebuild_webscript_sync_response_v2 import (
        RebuildWebscriptSyncResponseV2,
    )

    RebuildWebscriptSyncResponseV2Adapter = TypeAdapter(RebuildWebscriptSyncResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

rebuild_webscript_sync_response_v2_model_schema = json.loads(
    r"""{
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
      "$ref" : "#/components/schemas/WebscriptResponseV2"
    }
  },
  "description" : "Webscript Rebuild Ignored"
}
""",
    object_hook=with_example_provider,
)
rebuild_webscript_sync_response_v2_model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

rebuild_webscript_sync_response_v2_faker = JSF(
    rebuild_webscript_sync_response_v2_model_schema, allow_none_optionals=1
)


class RebuildWebscriptSyncResponseV2Stub:
    """RebuildWebscriptSyncResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return rebuild_webscript_sync_response_v2_faker.generate()

    @classmethod
    def create_instance(cls) -> "RebuildWebscriptSyncResponseV2":
        """Create RebuildWebscriptSyncResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return RebuildWebscriptSyncResponseV2Adapter.validate_python(cls.create_json())
