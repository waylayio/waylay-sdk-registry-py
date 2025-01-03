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
    from waylay.services.registry.models.failed_event_sse import FailedEventSSE

    FailedEventSSEAdapter = TypeAdapter(FailedEventSSE)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

failed_event_sse_model_schema = json.loads(
    r"""{
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/FailedEventSSE_event"
    },
    "data" : {
      "$ref" : "#/components/schemas/JobEventResponse_FailedEventData_"
    }
  },
  "description" : "A message that notifies a state change in a background job."
}
""",
    object_hook=with_example_provider,
)
failed_event_sse_model_schema.update({"definitions": MODEL_DEFINITIONS})

failed_event_sse_faker = JSF(failed_event_sse_model_schema, allow_none_optionals=1)


class FailedEventSSEStub:
    """FailedEventSSE unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return failed_event_sse_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "FailedEventSSE":
        """Create FailedEventSSE stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                FailedEventSSEAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return FailedEventSSEAdapter.validate_python(
            json, context={"skip_validation": True}
        )
