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
    from waylay.services.registry.models.job_type import JobType

    JobTypeAdapter = TypeAdapter(JobType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_type_model_schema = json.loads(
    r"""{
  "title" : "JobType",
  "type" : "string",
  "enum" : [ "build", "deploy", "verify", "undeploy", "batch", "scale", "cleanup", "other" ]
}
""",
    object_hook=with_example_provider,
)
job_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_type_faker = JSF(job_type_model_schema, allow_none_optionals=1)


class JobTypeStub:
    """JobType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_type_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "JobType":
        """Create JobType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(JobTypeAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return JobTypeAdapter.validate_python(json, context={"skip_validation": True})
