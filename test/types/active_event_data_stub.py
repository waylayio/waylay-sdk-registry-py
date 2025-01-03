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
    from waylay.services.registry.models.active_event_data import ActiveEventData

    ActiveEventDataAdapter = TypeAdapter(ActiveEventData)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

active_event_data_model_schema = json.loads(
    r"""{
  "title" : "ActiveEventData",
  "type" : "object",
  "properties" : {
    "prev" : {
      "$ref" : "#/components/schemas/QueueEvents"
    }
  }
}
""",
    object_hook=with_example_provider,
)
active_event_data_model_schema.update({"definitions": MODEL_DEFINITIONS})

active_event_data_faker = JSF(active_event_data_model_schema, allow_none_optionals=1)


class ActiveEventDataStub:
    """ActiveEventData unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return active_event_data_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ActiveEventData":
        """Create ActiveEventData stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ActiveEventDataAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ActiveEventDataAdapter.validate_python(
            json, context={"skip_validation": True}
        )
