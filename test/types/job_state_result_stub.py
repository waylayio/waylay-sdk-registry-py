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
    from waylay.services.registry.models.job_state_result import JobStateResult

    JobStateResultAdapter = TypeAdapter(JobStateResult)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_state_result_model_schema = json.loads(
    r"""{
  "title" : "JobStateResult",
  "description" : "All reported job states",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/JobState"
  }, {
    "$ref" : "#/components/schemas/JobStateUnknown"
  } ]
}
""",
    object_hook=with_example_provider,
)
job_state_result_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_state_result_faker = JSF(job_state_result_model_schema, allow_none_optionals=1)


class JobStateResultStub:
    """JobStateResult unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_state_result_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobStateResult":
        """Create JobStateResult stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobStateResultAdapter.validate_python(cls.create_json())
