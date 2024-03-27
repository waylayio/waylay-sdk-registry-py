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
    from waylay.services.registry.models.batch_job_status import BatchJobStatus

    BatchJobStatusAdapter = TypeAdapter(BatchJobStatus)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_job_status_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "job", "operation", "request", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/BatchJobStatus_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/BatchArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/BatchResult"
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
""",
    object_hook=with_example_provider,
)
batch_job_status_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_job_status_faker = JSF(batch_job_status_model_schema, allow_none_optionals=1)


class BatchJobStatusStub:
    """BatchJobStatus unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_job_status_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchJobStatus":
        """Create BatchJobStatus stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchJobStatusAdapter.validate_python(cls.create_json())
