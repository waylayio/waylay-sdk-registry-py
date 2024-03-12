# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import warnings

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.keep_alive_event_sse import KeepAliveEventSSE

    KeepAliveEventSSEAdapter = TypeAdapter(KeepAliveEventSSE)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for KeepAliveEventSSE not available: {exc}")
    MODELS_AVAILABLE = False

keep_alive_event_sse_model_schema = json.loads(r"""{
  "required" : [ "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/EventKeepAlive"
    },
    "data" : {
      "type" : "string",
      "description" : "A text message acknowledging that events will be forwarded."
    }
  },
  "description" : "A message that acknowledges that the stream is still alive."
}
""")
keep_alive_event_sse_model_schema.update({"definitions": MODEL_DEFINITIONS})

keep_alive_event_sse_faker = JSF(
    keep_alive_event_sse_model_schema, allow_none_optionals=1
)


class KeepAliveEventSSEStub:
    """KeepAliveEventSSE unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return keep_alive_event_sse_faker.generate()

    @classmethod
    def create_instance(cls) -> "KeepAliveEventSSE":
        """Create KeepAliveEventSSE stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return KeepAliveEventSSEAdapter.validate_python(cls.create_json())
