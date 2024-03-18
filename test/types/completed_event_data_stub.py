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
    from waylay.services.registry.models.completed_event_data import CompletedEventData

    CompletedEventDataAdapter = TypeAdapter(CompletedEventData)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

completed_event_data_model_schema = json.loads(r"""{
  "title" : "CompletedEventData",
  "required" : [ "returnvalue" ],
  "type" : "object",
  "properties" : {
    "prev" : {
      "$ref" : "#/components/schemas/QueueEvents"
    },
    "returnvalue" : {
      "$ref" : "#/components/schemas/AnyJobResult"
    }
  }
}
""")
completed_event_data_model_schema.update({"definitions": MODEL_DEFINITIONS})

completed_event_data_faker = JSF(
    completed_event_data_model_schema, allow_none_optionals=1
)


class CompletedEventDataStub:
    """CompletedEventData unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return completed_event_data_faker.generate()

    @classmethod
    def create_instance(cls) -> "CompletedEventData":
        """Create CompletedEventData stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return CompletedEventDataAdapter.validate_python(cls.create_json())
