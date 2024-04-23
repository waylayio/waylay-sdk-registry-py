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
    from waylay.services.registry.models.event_ack import EventAck

    EventAckAdapter = TypeAdapter(EventAck)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

event_ack_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "ack" ]
}
""",
    object_hook=with_example_provider,
)
event_ack_model_schema.update({"definitions": MODEL_DEFINITIONS})

event_ack_faker = JSF(event_ack_model_schema, allow_none_optionals=1)


class EventAckStub:
    """EventAck unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return event_ack_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "EventAck":
        """Create EventAck stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(EventAckAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return EventAckAdapter.validate_python(json, context={"skip_validation": True})
