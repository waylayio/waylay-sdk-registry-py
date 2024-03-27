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
    from waylay.services.registry.models.delayed_event_sse_event import (
        DelayedEventSSEEvent,
    )

    DelayedEventSSEEventAdapter = TypeAdapter(DelayedEventSSEEvent)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

delayed_event_sse_event_model_schema = json.loads(
    r"""{
  "title" : "DelayedEventSSE_event",
  "type" : "string",
  "description" : "The job queue event that trigged this message",
  "enum" : [ "delayed" ]
}
""",
    object_hook=with_example_provider,
)
delayed_event_sse_event_model_schema.update({"definitions": MODEL_DEFINITIONS})

delayed_event_sse_event_faker = JSF(
    delayed_event_sse_event_model_schema, allow_none_optionals=1
)


class DelayedEventSSEEventStub:
    """DelayedEventSSEEvent unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return delayed_event_sse_event_faker.generate()

    @classmethod
    def create_instance(cls) -> "DelayedEventSSEEvent":
        """Create DelayedEventSSEEvent stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return DelayedEventSSEEventAdapter.validate_python(cls.create_json())