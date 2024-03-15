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
    from waylay.services.registry.models.verify_job_status import VerifyJobStatus

    VerifyJobStatusAdapter = TypeAdapter(VerifyJobStatus)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

verify_job_status_model_schema = json.loads(r"""{
  "required" : [ "createdAt", "createdBy", "job", "operation", "request", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "title" : "Verify",
      "type" : "string",
      "description" : "The type of the background task.",
      "enum" : [ "verify" ]
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
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "type" : "string",
      "description" : "Request operation"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    }
  }
}
""")
verify_job_status_model_schema.update({"definitions": MODEL_DEFINITIONS})

verify_job_status_faker = JSF(verify_job_status_model_schema, allow_none_optionals=1)


class VerifyJobStatusStub:
    """VerifyJobStatus unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return verify_job_status_faker.generate()

    @classmethod
    def create_instance(cls) -> "VerifyJobStatus":
        """Create VerifyJobStatus stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return VerifyJobStatusAdapter.validate_python(cls.create_json())
