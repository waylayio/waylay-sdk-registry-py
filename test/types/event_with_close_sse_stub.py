# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.event_with_close_sse import EventWithCloseSSE

    EventWithCloseSSEAdapter = TypeAdapter(EventWithCloseSSE)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

event_with_close_sse_model_schema = json.loads(r"""{
  "description" : "SSE stream events with closing protocol",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Stream_Ready"
  }, {
    "$ref" : "#/components/schemas/JobEventSSE"
  }, {
    "$ref" : "#/components/schemas/KeepAliveEventSSE"
  }, {
    "$ref" : "#/components/schemas/Stream_Closing"
  } ]
}
""")
event_with_close_sse_model_schema.update({"definitions": MODEL_DEFINITIONS})

event_with_close_sse_faker = JSF(
    event_with_close_sse_model_schema, allow_none_optionals=1
)


class EventWithCloseSSEStub:
    """EventWithCloseSSE unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return event_with_close_sse_faker.generate()

    @classmethod
    def create_instance(cls) -> "EventWithCloseSSE":
        """Create EventWithCloseSSE stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return EventWithCloseSSEAdapter.validate_python(cls.create_json())
