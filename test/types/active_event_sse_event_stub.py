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
    from waylay.services.registry.models.active_event_sse_event import (
        ActiveEventSSEEvent,
    )

    ActiveEventSSEEventAdapter = TypeAdapter(ActiveEventSSEEvent)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

active_event_sse_event_model_schema = json.loads(
    r"""{
  "title" : "ActiveEventSSE_event",
  "type" : "string",
  "description" : "The job queue event that trigged this message",
  "enum" : [ "active" ]
}
""",
    object_hook=with_example_provider,
)
active_event_sse_event_model_schema.update({"definitions": MODEL_DEFINITIONS})

active_event_sse_event_faker = JSF(
    active_event_sse_event_model_schema, allow_none_optionals=1
)


class ActiveEventSSEEventStub:
    """ActiveEventSSEEvent unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return active_event_sse_event_faker.generate()

    @classmethod
    def create_instance(cls) -> "ActiveEventSSEEvent":
        """Create ActiveEventSSEEvent stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ActiveEventSSEEventAdapter.validate_python(cls.create_json())
