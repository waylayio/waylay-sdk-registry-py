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
    from waylay.services.registry.models.active_event_sse import ActiveEventSSE

    ActiveEventSSEAdapter = TypeAdapter(ActiveEventSSE)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

active_event_sse_model_schema = json.loads(
    r"""{
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/ActiveEventSSE_event"
    },
    "data" : {
      "$ref" : "#/components/schemas/JobEventResponse_ActiveEventData_"
    }
  },
  "description" : "A message that notifies a state change in a background job."
}
""",
    object_hook=with_example_provider,
)
active_event_sse_model_schema.update({"definitions": MODEL_DEFINITIONS})

active_event_sse_faker = JSF(active_event_sse_model_schema, allow_none_optionals=1)


class ActiveEventSSEStub:
    """ActiveEventSSE unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return active_event_sse_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ActiveEventSSE":
        """Create ActiveEventSSE stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ActiveEventSSEAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ActiveEventSSEAdapter.validate_python(
            json, context={"skip_validation": True}
        )
