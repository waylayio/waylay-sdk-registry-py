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
    from waylay.services.registry.models.delayed_event_data import DelayedEventData

    DelayedEventDataAdapter = TypeAdapter(DelayedEventData)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

delayed_event_data_model_schema = json.loads(
    r"""{
  "title" : "DelayedEventData",
  "required" : [ "delay" ],
  "type" : "object",
  "properties" : {
    "delay" : {
      "title" : "delay",
      "type" : "number"
    }
  }
}
""",
    object_hook=with_example_provider,
)
delayed_event_data_model_schema.update({"definitions": MODEL_DEFINITIONS})

delayed_event_data_faker = JSF(delayed_event_data_model_schema, allow_none_optionals=1)


class DelayedEventDataStub:
    """DelayedEventData unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return delayed_event_data_faker.generate()

    @classmethod
    def create_instance(cls) -> "DelayedEventData":
        """Create DelayedEventData stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return DelayedEventDataAdapter.validate_python(cls.create_json())
