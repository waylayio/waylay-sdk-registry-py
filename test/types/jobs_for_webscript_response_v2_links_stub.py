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
    from waylay.services.registry.models.jobs_for_webscript_response_v2_links import (
        JobsForWebscriptResponseV2Links,
    )

    JobsForWebscriptResponseV2LinksAdapter = TypeAdapter(
        JobsForWebscriptResponseV2Links
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

jobs_for_webscript_response_v2__links_model_schema = json.loads(
    r"""{
  "title" : "JobsForWebscriptResponseV2__links",
  "type" : "object",
  "properties" : {
    "webscript" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  },
  "additionalProperties" : false,
  "description" : "Link to the function entity."
}
""",
    object_hook=with_example_provider,
)
jobs_for_webscript_response_v2__links_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

jobs_for_webscript_response_v2__links_faker = JSF(
    jobs_for_webscript_response_v2__links_model_schema, allow_none_optionals=1
)


class JobsForWebscriptResponseV2LinksStub:
    """JobsForWebscriptResponseV2Links unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return jobs_for_webscript_response_v2__links_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "JobsForWebscriptResponseV2Links":
        """Create JobsForWebscriptResponseV2Links stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                JobsForWebscriptResponseV2LinksAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return JobsForWebscriptResponseV2LinksAdapter.validate_python(
            json, context={"skip_validation": True}
        )
