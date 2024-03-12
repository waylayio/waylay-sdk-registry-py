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
    from waylay.services.registry.models.undeploy import Undeploy

    UndeployAdapter = TypeAdapter(Undeploy)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for Undeploy not available: {exc}")
    MODELS_AVAILABLE = False

undeploy_model_schema = json.loads(r"""{
  "title" : "Undeploy",
  "required" : [ "createdAt", "createdBy", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "type" : {
      "title" : "Undeploy",
      "type" : "string",
      "description" : "The type of the background task.",
      "enum" : [ "undeploy" ]
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/UndeployArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/UndeployResult"
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "Request operation"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    }
  }
}
""")
undeploy_model_schema.update({"definitions": MODEL_DEFINITIONS})

undeploy_faker = JSF(undeploy_model_schema, allow_none_optionals=1)


class UndeployStub:
    """Undeploy unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return undeploy_faker.generate()

    @classmethod
    def create_instance(cls) -> "Undeploy":
        """Create Undeploy stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return UndeployAdapter.validate_python(cls.create_json())
