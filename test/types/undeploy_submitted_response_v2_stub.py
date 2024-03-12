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
    from waylay.services.registry.models.undeploy_submitted_response_v2 import (
        UndeploySubmittedResponseV2,
    )

    UndeploySubmittedResponseV2Adapter = TypeAdapter(UndeploySubmittedResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for UndeploySubmittedResponseV2 not available: {exc}")
    MODELS_AVAILABLE = False

undeploy_submitted_response_v2_model_schema = json.loads(r"""{
  "required" : [ "_links", "message", "versions" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "versions" : {
      "type" : "array",
      "description" : "The versions for which undeployment and/or removal is initiated.",
      "items" : {
        "$ref" : "#/components/schemas/SemanticVersion"
      }
    }
  },
  "description" : "Undeployment Initiated"
}
""")
undeploy_submitted_response_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

undeploy_submitted_response_v2_faker = JSF(
    undeploy_submitted_response_v2_model_schema, allow_none_optionals=1
)


class UndeploySubmittedResponseV2Stub:
    """UndeploySubmittedResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return undeploy_submitted_response_v2_faker.generate()

    @classmethod
    def create_instance(cls) -> "UndeploySubmittedResponseV2":
        """Create UndeploySubmittedResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return UndeploySubmittedResponseV2Adapter.validate_python(cls.create_json())
