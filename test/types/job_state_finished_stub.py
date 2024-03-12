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
    from waylay.services.registry.models.job_state_finished import JobStateFinished

    JobStateFinishedAdapter = TypeAdapter(JobStateFinished)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for JobStateFinished not available: {exc}")
    MODELS_AVAILABLE = False

job_state_finished_model_schema = json.loads(r"""{
  "title" : "JobStateFinished",
  "description" : "The job completed successfully or with failure.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/JobStateCompleted"
  }, {
    "$ref" : "#/components/schemas/JobStateFailed"
  } ]
}
""")
job_state_finished_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_state_finished_faker = JSF(job_state_finished_model_schema, allow_none_optionals=1)


class JobStateFinishedStub:
    """JobStateFinished unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_state_finished_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobStateFinished":
        """Create JobStateFinished stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobStateFinishedAdapter.validate_python(cls.create_json())
