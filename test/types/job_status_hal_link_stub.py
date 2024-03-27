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
    from waylay.services.registry.models.job_status_hal_link import JobStatusHALLink

    JobStatusHALLinkAdapter = TypeAdapter(JobStatusHALLink)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_status_hal_link_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  },
  "description" : "HAL links to related actions."
}
""",
    object_hook=with_example_provider,
)
job_status_hal_link_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_status_hal_link_faker = JSF(
    job_status_hal_link_model_schema, allow_none_optionals=1
)


class JobStatusHALLinkStub:
    """JobStatusHALLink unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_status_hal_link_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobStatusHALLink":
        """Create JobStatusHALLink stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobStatusHALLinkAdapter.validate_python(cls.create_json())
