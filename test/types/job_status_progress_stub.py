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
    from waylay.services.registry.models.job_status_progress import JobStatusProgress

    JobStatusProgressAdapter = TypeAdapter(JobStatusProgress)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

job_status_progress_model_schema = json.loads(r"""{
  "title" : "JobStatus_progress",
  "anyOf" : [ {
    "type" : "number"
  }, {
    "type" : "object"
  } ]
}
""")
job_status_progress_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_status_progress_faker = JSF(
    job_status_progress_model_schema, allow_none_optionals=1
)


class JobStatusProgressStub:
    """JobStatusProgress unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_status_progress_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobStatusProgress":
        """Create JobStatusProgress stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobStatusProgressAdapter.validate_python(cls.create_json())
