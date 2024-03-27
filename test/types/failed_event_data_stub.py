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
    from waylay.services.registry.models.failed_event_data import FailedEventData

    FailedEventDataAdapter = TypeAdapter(FailedEventData)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

failed_event_data_model_schema = json.loads(
    r"""{
  "title" : "FailedEventData",
  "required" : [ "failedReason" ],
  "type" : "object",
  "properties" : {
    "prev" : {
      "$ref" : "#/components/schemas/QueueEvents"
    },
    "failedReason" : {
      "title" : "failedReason",
      "type" : "string",
      "description" : "The failure reason of the job"
    }
  }
}
""",
    object_hook=with_example_provider,
)
failed_event_data_model_schema.update({"definitions": MODEL_DEFINITIONS})

failed_event_data_faker = JSF(failed_event_data_model_schema, allow_none_optionals=1)


class FailedEventDataStub:
    """FailedEventData unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return failed_event_data_faker.generate()

    @classmethod
    def create_instance(cls) -> "FailedEventData":
        """Create FailedEventData stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return FailedEventDataAdapter.validate_python(cls.create_json())
