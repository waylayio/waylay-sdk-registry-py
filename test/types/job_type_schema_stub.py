# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.job_type_schema import JobTypeSchema

    JobTypeSchemaAdapter = TypeAdapter(JobTypeSchema)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_type_schema_model_schema = json.loads(
    r"""{
  "title" : "JobTypeSchema",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/JobTypeBuild"
  }, {
    "$ref" : "#/components/schemas/JobTypeDeploy"
  }, {
    "$ref" : "#/components/schemas/JobTypeVerify"
  }, {
    "$ref" : "#/components/schemas/JobTypeUndeploy"
  }, {
    "$ref" : "#/components/schemas/JobTypeScale"
  }, {
    "$ref" : "#/components/schemas/JobTypeBatch"
  }, {
    "$ref" : "#/components/schemas/JobTypeNotify"
  } ]
}
""",
    object_hook=with_example_provider,
)
job_type_schema_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_type_schema_faker = JSF(job_type_schema_model_schema, allow_none_optionals=1)


class JobTypeSchemaStub:
    """JobTypeSchema unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_type_schema_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobTypeSchema":
        """Create JobTypeSchema stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobTypeSchemaAdapter.validate_python(cls.create_json())
