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
    from waylay.services.registry.models.status_include import StatusInclude

    StatusIncludeAdapter = TypeAdapter(StatusInclude)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

status_include_model_schema = json.loads(
    r"""{
  "title" : "StatusInclude",
  "type" : "string",
  "description" : "Inlude a status as a filter.",
  "example" : "running",
  "enum" : [ "registered", "running", "pending", "deployed", "unhealthy", "failed", "undeploying", "undeployed" ]
}
""",
    object_hook=with_example_provider,
)
status_include_model_schema.update({"definitions": MODEL_DEFINITIONS})

status_include_faker = JSF(status_include_model_schema, allow_none_optionals=1)


class StatusIncludeStub:
    """StatusInclude unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return status_include_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "StatusInclude":
        """Create StatusInclude stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                StatusIncludeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return StatusIncludeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
