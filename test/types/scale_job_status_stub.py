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
    from waylay.services.registry.models.scale_job_status import ScaleJobStatus

    ScaleJobStatusAdapter = TypeAdapter(ScaleJobStatus)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

scale_job_status_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "job", "operation", "request", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/Scale_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/ScaleArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/ScaleResult"
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
scale_job_status_model_schema.update({"definitions": MODEL_DEFINITIONS})

scale_job_status_faker = JSF(scale_job_status_model_schema, allow_none_optionals=1)


class ScaleJobStatusStub:
    """ScaleJobStatus unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return scale_job_status_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ScaleJobStatus":
        """Create ScaleJobStatus stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ScaleJobStatusAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ScaleJobStatusAdapter.validate_python(
            json, context={"skip_validation": True}
        )
