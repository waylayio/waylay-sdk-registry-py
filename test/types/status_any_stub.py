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
    from waylay.services.registry.models.status_any import StatusAny

    StatusAnyAdapter = TypeAdapter(StatusAny)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

status_any_model_schema = json.loads(
    r"""{
  "title" : "StatusAny",
  "type" : "string",
  "description" : "Includes *all* statuses (including `undeployed`) as a filter",
  "enum" : [ "any" ]
}
""",
    object_hook=with_example_provider,
)
status_any_model_schema.update({"definitions": MODEL_DEFINITIONS})

status_any_faker = JSF(status_any_model_schema, allow_none_optionals=1)


class StatusAnyStub:
    """StatusAny unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return status_any_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "StatusAny":
        """Create StatusAny stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(StatusAnyAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return StatusAnyAdapter.validate_python(json, context={"skip_validation": True})
