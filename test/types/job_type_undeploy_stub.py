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
    from waylay.services.registry.models.job_type_undeploy import JobTypeUndeploy

    JobTypeUndeployAdapter = TypeAdapter(JobTypeUndeploy)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_type_undeploy_model_schema = json.loads(
    r"""{
  "title" : "JobTypeUndeploy",
  "type" : "string",
  "description" : "A job that undeploys a deployed function and removes it from the registry.",
  "enum" : [ "undeploy" ]
}
""",
    object_hook=with_example_provider,
)
job_type_undeploy_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_type_undeploy_faker = JSF(job_type_undeploy_model_schema, allow_none_optionals=1)


class JobTypeUndeployStub:
    """JobTypeUndeploy unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_type_undeploy_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobTypeUndeploy":
        """Create JobTypeUndeploy stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobTypeUndeployAdapter.validate_python(cls.create_json())
