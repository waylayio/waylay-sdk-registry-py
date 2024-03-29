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
    from waylay.services.registry.models.job_type_batch import JobTypeBatch

    JobTypeBatchAdapter = TypeAdapter(JobTypeBatch)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_type_batch_model_schema = json.loads(
    r"""{
  "title" : "JobTypeBatch",
  "type" : "string",
  "description" : "A job that groups other jobs as a parent.",
  "enum" : [ "batch" ]
}
""",
    object_hook=with_example_provider,
)
job_type_batch_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_type_batch_faker = JSF(job_type_batch_model_schema, allow_none_optionals=1)


class JobTypeBatchStub:
    """JobTypeBatch unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_type_batch_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobTypeBatch":
        """Create JobTypeBatch stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobTypeBatchAdapter.validate_python(cls.create_json())
