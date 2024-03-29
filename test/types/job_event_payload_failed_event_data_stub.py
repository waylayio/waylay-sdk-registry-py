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
    from waylay.services.registry.models.job_event_payload_failed_event_data import (
        JobEventPayloadFailedEventData,
    )

    JobEventPayloadFailedEventDataAdapter = TypeAdapter(JobEventPayloadFailedEventData)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_event_payload_failed_event_data__model_schema = json.loads(
    r"""{
  "required" : [ "data", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/FailedEventData"
    },
    "timestamp" : {
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    }
  }
}
""",
    object_hook=with_example_provider,
)
job_event_payload_failed_event_data__model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

job_event_payload_failed_event_data__faker = JSF(
    job_event_payload_failed_event_data__model_schema, allow_none_optionals=1
)


class JobEventPayloadFailedEventDataStub:
    """JobEventPayloadFailedEventData unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_event_payload_failed_event_data__faker.generate()

    @classmethod
    def create_instance(cls) -> "JobEventPayloadFailedEventData":
        """Create JobEventPayloadFailedEventData stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobEventPayloadFailedEventDataAdapter.validate_python(cls.create_json())
