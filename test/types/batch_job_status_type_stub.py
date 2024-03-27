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
    from waylay.services.registry.models.batch_job_status_type import BatchJobStatusType

    BatchJobStatusTypeAdapter = TypeAdapter(BatchJobStatusType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_job_status_type_model_schema = json.loads(
    r"""{
  "title" : "BatchJobStatus_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "batch" ]
}
""",
    object_hook=with_example_provider,
)
batch_job_status_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_job_status_type_faker = JSF(
    batch_job_status_type_model_schema, allow_none_optionals=1
)


class BatchJobStatusTypeStub:
    """BatchJobStatusType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_job_status_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchJobStatusType":
        """Create BatchJobStatusType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchJobStatusTypeAdapter.validate_python(cls.create_json())
