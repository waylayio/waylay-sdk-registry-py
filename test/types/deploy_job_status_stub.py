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
    from waylay.services.registry.models.deploy_job_status import DeployJobStatus

    DeployJobStatusAdapter = TypeAdapter(DeployJobStatus)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

deploy_job_status_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "job", "operation", "request", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "title" : "Deploy",
      "type" : "string",
      "description" : "The type of the background task.",
      "enum" : [ "deploy" ]
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/DeployArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/DeployResult"
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "type" : "string",
      "description" : "Request operation"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    }
  }
}
""",
    object_hook=with_example_provider,
)
deploy_job_status_model_schema.update({"definitions": MODEL_DEFINITIONS})

deploy_job_status_faker = JSF(deploy_job_status_model_schema, allow_none_optionals=1)


class DeployJobStatusStub:
    """DeployJobStatus unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return deploy_job_status_faker.generate()

    @classmethod
    def create_instance(cls) -> "DeployJobStatus":
        """Create DeployJobStatus stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return DeployJobStatusAdapter.validate_python(cls.create_json())
