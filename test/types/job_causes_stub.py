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
    from waylay.services.registry.models.job_causes import JobCauses

    JobCausesAdapter = TypeAdapter(JobCauses)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_causes_model_schema = json.loads(
    r"""{
  "title" : "JobCauses",
  "type" : "object",
  "properties" : {
    "build" : {
      "$ref" : "#/components/schemas/JobCause"
    },
    "deploy" : {
      "$ref" : "#/components/schemas/JobCause"
    },
    "verify" : {
      "$ref" : "#/components/schemas/JobCause"
    },
    "undeploy" : {
      "$ref" : "#/components/schemas/JobCause"
    },
    "scale" : {
      "$ref" : "#/components/schemas/JobCause"
    }
  },
  "description" : "The motivations for including or excluding a job in response to a <em>rebuild</em> request."
}
""",
    object_hook=with_example_provider,
)
job_causes_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_causes_faker = JSF(job_causes_model_schema, allow_none_optionals=1)


class JobCausesStub:
    """JobCauses unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_causes_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobCauses":
        """Create JobCauses stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobCausesAdapter.validate_python(cls.create_json())
