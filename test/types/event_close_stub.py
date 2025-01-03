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
    from waylay.services.registry.models.event_close import EventClose

    EventCloseAdapter = TypeAdapter(EventClose)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

event_close_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "close" ]
}
""",
    object_hook=with_example_provider,
)
event_close_model_schema.update({"definitions": MODEL_DEFINITIONS})

event_close_faker = JSF(event_close_model_schema, allow_none_optionals=1)


class EventCloseStub:
    """EventClose unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return event_close_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "EventClose":
        """Create EventClose stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(EventCloseAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return EventCloseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
