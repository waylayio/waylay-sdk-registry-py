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
    from waylay.services.registry.models.job_response import JobResponse

    JobResponseAdapter = TypeAdapter(JobResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for JobResponse not available: {exc}")
    MODELS_AVAILABLE = False

job_response_model_schema = json.loads(r"""{
  "required" : [ "_links", "job" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/AnyJobStatus"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobEventsAndFunctionHALLink"
    }
  },
  "description" : "Job Found"
}
""")
job_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_response_faker = JSF(job_response_model_schema, allow_none_optionals=1)


class JobResponseStub:
    """JobResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobResponse":
        """Create JobResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobResponseAdapter.validate_python(cls.create_json())
