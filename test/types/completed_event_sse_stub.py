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
    from waylay.services.registry.models.completed_event_sse import CompletedEventSSE

    CompletedEventSSEAdapter = TypeAdapter(CompletedEventSSE)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

completed_event_sse_model_schema = json.loads(
    r"""{
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/CompletedEventSSE_event"
    },
    "data" : {
      "$ref" : "#/components/schemas/JobEventResponse_CompletedEventData_"
    }
  },
  "description" : "A message that notifies a state change in a background job."
}
""",
    object_hook=with_example_provider,
)
completed_event_sse_model_schema.update({"definitions": MODEL_DEFINITIONS})

completed_event_sse_faker = JSF(
    completed_event_sse_model_schema, allow_none_optionals=1
)


class CompletedEventSSEStub:
    """CompletedEventSSE unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return completed_event_sse_faker.generate()

    @classmethod
    def create_instance(cls) -> "CompletedEventSSE":
        """Create CompletedEventSSE stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return CompletedEventSSEAdapter.validate_python(cls.create_json())
