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
    from waylay.services.registry.models.undeployed_response_v2 import (
        UndeployedResponseV2,
    )

    UndeployedResponseV2Adapter = TypeAdapter(UndeployedResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

undeployed_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "message", "versions" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "versions" : {
      "type" : "array",
      "description" : "The versions that were deprecated, undeployed and/or removed.",
      "items" : {
        "$ref" : "#/components/schemas/SemanticVersion"
      }
    }
  },
  "description" : "Undeployed"
}
""",
    object_hook=with_example_provider,
)
undeployed_response_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

undeployed_response_v2_faker = JSF(
    undeployed_response_v2_model_schema, allow_none_optionals=1
)


class UndeployedResponseV2Stub:
    """UndeployedResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return undeployed_response_v2_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "UndeployedResponseV2":
        """Create UndeployedResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                UndeployedResponseV2Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return UndeployedResponseV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
