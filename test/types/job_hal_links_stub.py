# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import warnings

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.job_hal_links import JobHALLinks

    JobHALLinksAdapter = TypeAdapter(JobHALLinks)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for JobHALLinks not available: {exc}")
    MODELS_AVAILABLE = False

job_hal_links_model_schema = json.loads(r"""{
  "title" : "JobHALLinks",
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "job" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  },
  "description" : "HAL links to related actions."
}
""")
job_hal_links_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_hal_links_faker = JSF(job_hal_links_model_schema, allow_none_optionals=1)


class JobHALLinksStub:
    """JobHALLinks unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_hal_links_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobHALLinks":
        """Create JobHALLinks stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobHALLinksAdapter.validate_python(cls.create_json())
