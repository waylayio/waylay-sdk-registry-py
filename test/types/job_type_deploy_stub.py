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
    from waylay.services.registry.models.job_type_deploy import JobTypeDeploy

    JobTypeDeployAdapter = TypeAdapter(JobTypeDeploy)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

job_type_deploy_model_schema = json.loads(r"""{
  "title" : "JobTypeDeploy",
  "type" : "string",
  "description" : "A job that deploys a function image to the openfaas runtime.",
  "enum" : [ "deploy" ]
}
""")
job_type_deploy_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_type_deploy_faker = JSF(job_type_deploy_model_schema, allow_none_optionals=1)


class JobTypeDeployStub:
    """JobTypeDeploy unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_type_deploy_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobTypeDeploy":
        """Create JobTypeDeploy stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobTypeDeployAdapter.validate_python(cls.create_json())
