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
    from waylay.services.registry.models.jobs_response import JobsResponse

    JobsResponseAdapter = TypeAdapter(JobsResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

jobs_response_model_schema = json.loads(
    r"""{
  "required" : [ "jobs" ],
  "type" : "object",
  "properties" : {
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "jobs" : {
      "type" : "array",
      "description" : "Listing of jobs that satisfy the query.",
      "items" : {
        "$ref" : "#/components/schemas/AnyJobStatusSummary"
      }
    }
  },
  "description" : "Jobs Found"
}
""",
    object_hook=with_example_provider,
)
jobs_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

jobs_response_faker = JSF(jobs_response_model_schema, allow_none_optionals=1)


class JobsResponseStub:
    """JobsResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return jobs_response_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "JobsResponse":
        """Create JobsResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                JobsResponseAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return JobsResponseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
