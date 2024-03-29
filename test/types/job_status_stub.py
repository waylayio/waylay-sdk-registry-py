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
    from waylay.services.registry.models.job_status import JobStatus

    JobStatusAdapter = TypeAdapter(JobStatus)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_status_model_schema = json.loads(
    r"""{
  "title" : "JobStatus",
  "required" : [ "attemptsMade", "id", "name", "progress" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "title" : "id",
      "type" : "string"
    },
    "name" : {
      "title" : "name",
      "type" : "string"
    },
    "progress" : {
      "$ref" : "#/components/schemas/JobStatus_progress"
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number"
    },
    "finishedOn" : {
      "title" : "finishedOn",
      "type" : "string",
      "format" : "date-time"
    },
    "processedOn" : {
      "title" : "processedOn",
      "type" : "string",
      "format" : "date-time"
    },
    "failedReason" : {
      "title" : "failedReason",
      "type" : "string"
    },
    "parent" : {
      "$ref" : "#/components/schemas/ParentKeys"
    },
    "delay" : {
      "title" : "delay",
      "type" : "number"
    }
  }
}
""",
    object_hook=with_example_provider,
)
job_status_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_status_faker = JSF(job_status_model_schema, allow_none_optionals=1)


class JobStatusStub:
    """JobStatus unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_status_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobStatus":
        """Create JobStatus stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobStatusAdapter.validate_python(cls.create_json())
