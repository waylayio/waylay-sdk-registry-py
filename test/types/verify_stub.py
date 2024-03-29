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
    from waylay.services.registry.models.verify import Verify

    VerifyAdapter = TypeAdapter(Verify)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

verify_model_schema = json.loads(
    r"""{
  "title" : "Verify",
  "required" : [ "createdAt", "createdBy", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "type" : {
      "$ref" : "#/components/schemas/Verify_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/VerifyArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/VerifyResult"
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
""",
    object_hook=with_example_provider,
)
verify_model_schema.update({"definitions": MODEL_DEFINITIONS})

verify_faker = JSF(verify_model_schema, allow_none_optionals=1)


class VerifyStub:
    """Verify unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return verify_faker.generate()

    @classmethod
    def create_instance(cls) -> "Verify":
        """Create Verify stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return VerifyAdapter.validate_python(cls.create_json())
