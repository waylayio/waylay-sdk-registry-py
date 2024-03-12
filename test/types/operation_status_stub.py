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
    from waylay.services.registry.models.operation_status import OperationStatus

    OperationStatusAdapter = TypeAdapter(OperationStatus)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for OperationStatus not available: {exc}")
    MODELS_AVAILABLE = False

operation_status_model_schema = json.loads(r"""{
  "required" : [ "description", "done", "id", "name", "type" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "name" : {
      "type" : "string",
      "deprecated" : true
    },
    "type" : {
      "$ref" : "#/components/schemas/JobType"
    },
    "done" : {
      "type" : "boolean"
    },
    "error" : {
      "$ref" : "#/components/schemas/OperationStatus_error"
    }
  }
}
""")
operation_status_model_schema.update({"definitions": MODEL_DEFINITIONS})

operation_status_faker = JSF(operation_status_model_schema, allow_none_optionals=1)


class OperationStatusStub:
    """OperationStatus unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return operation_status_faker.generate()

    @classmethod
    def create_instance(cls) -> "OperationStatus":
        """Create OperationStatus stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return OperationStatusAdapter.validate_python(cls.create_json())
