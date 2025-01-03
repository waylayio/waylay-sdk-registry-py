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
    from waylay.services.registry.models.jobs_for_plug_response_v2 import (
        JobsForPlugResponseV2,
    )

    JobsForPlugResponseV2Adapter = TypeAdapter(JobsForPlugResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

jobs_for_plug_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "function", "jobs" ],
  "type" : "object",
  "properties" : {
    "jobs" : {
      "type" : "array",
      "description" : "Listing of jobs related to the function deployment. This includes active jobs, and the most recently failed job (per type) that was archived on the entity.",
      "items" : {
        "$ref" : "#/components/schemas/AnyJobForFunction"
      }
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobsForPlugResponseV2__links"
    }
  },
  "description" : "Plug Jobs Found"
}
""",
    object_hook=with_example_provider,
)
jobs_for_plug_response_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

jobs_for_plug_response_v2_faker = JSF(
    jobs_for_plug_response_v2_model_schema, allow_none_optionals=1
)


class JobsForPlugResponseV2Stub:
    """JobsForPlugResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return jobs_for_plug_response_v2_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "JobsForPlugResponseV2":
        """Create JobsForPlugResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                JobsForPlugResponseV2Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return JobsForPlugResponseV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
