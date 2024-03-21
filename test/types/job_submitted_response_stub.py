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
    from waylay.services.registry.models.job_submitted_response import (
        JobSubmittedResponse,
    )

    JobSubmittedResponseAdapter = TypeAdapter(JobSubmittedResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_submitted_response_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
job_submitted_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_submitted_response_faker = JSF(
    job_submitted_response_model_schema, allow_none_optionals=1
)


class JobSubmittedResponseStub:
    """JobSubmittedResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_submitted_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobSubmittedResponse":
        """Create JobSubmittedResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobSubmittedResponseAdapter.validate_python(cls.create_json())
