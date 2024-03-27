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
    from waylay.services.registry.models.stream_closing import StreamClosing

    StreamClosingAdapter = TypeAdapter(StreamClosing)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

stream_closing_model_schema = json.loads(
    r"""{
  "title" : "Stream Closing",
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/EventClose"
    },
    "data" : {
      "title" : "data",
      "type" : "string",
      "description" : "A text message describing the cause for closing the stream."
    }
  },
  "description" : "A message that notifies that the server will not send more events, and that the client should close."
}
""",
    object_hook=with_example_provider,
)
stream_closing_model_schema.update({"definitions": MODEL_DEFINITIONS})

stream_closing_faker = JSF(stream_closing_model_schema, allow_none_optionals=1)


class StreamClosingStub:
    """StreamClosing unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return stream_closing_faker.generate()

    @classmethod
    def create_instance(cls) -> "StreamClosing":
        """Create StreamClosing stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return StreamClosingAdapter.validate_python(cls.create_json())
