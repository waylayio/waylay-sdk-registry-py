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
    from waylay.services.registry.models.event_sse import EventSSE

    EventSSEAdapter = TypeAdapter(EventSSE)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

event_sse_model_schema = json.loads(
    r"""{
  "description" : "SSE stream events without closing protocol",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Stream_Ready"
  }, {
    "$ref" : "#/components/schemas/JobEventSSE"
  }, {
    "$ref" : "#/components/schemas/KeepAliveEventSSE"
  } ]
}
""",
    object_hook=with_example_provider,
)
event_sse_model_schema.update({"definitions": MODEL_DEFINITIONS})

event_sse_faker = JSF(event_sse_model_schema, allow_none_optionals=1)


class EventSSEStub:
    """EventSSE unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return event_sse_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "EventSSE":
        """Create EventSSE stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(EventSSEAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return EventSSEAdapter.validate_python(json, context={"skip_validation": True})
