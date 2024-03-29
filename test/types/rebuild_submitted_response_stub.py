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
    from waylay.services.registry.models.rebuild_submitted_response import (
        RebuildSubmittedResponse,
    )

    RebuildSubmittedResponseAdapter = TypeAdapter(RebuildSubmittedResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

rebuild_submitted_response_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "causes", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "causes" : {
      "$ref" : "#/components/schemas/JobCauses"
    }
  },
  "description" : "Rebuild Initiated"
}
""",
    object_hook=with_example_provider,
)
rebuild_submitted_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

rebuild_submitted_response_faker = JSF(
    rebuild_submitted_response_model_schema, allow_none_optionals=1
)


class RebuildSubmittedResponseStub:
    """RebuildSubmittedResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return rebuild_submitted_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "RebuildSubmittedResponse":
        """Create RebuildSubmittedResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return RebuildSubmittedResponseAdapter.validate_python(cls.create_json())
