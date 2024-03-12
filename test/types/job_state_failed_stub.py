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
    from waylay.services.registry.models.job_state_failed import JobStateFailed

    JobStateFailedAdapter = TypeAdapter(JobStateFailed)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for JobStateFailed not available: {exc}")
    MODELS_AVAILABLE = False

job_state_failed_model_schema = json.loads(r"""{
  "title" : "JobStateFailed",
  "type" : "string",
  "description" : "The job failed in execution.",
  "enum" : [ "failed" ]
}
""")
job_state_failed_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_state_failed_faker = JSF(job_state_failed_model_schema, allow_none_optionals=1)


class JobStateFailedStub:
    """JobStateFailed unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_state_failed_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobStateFailed":
        """Create JobStateFailed stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobStateFailedAdapter.validate_python(cls.create_json())
