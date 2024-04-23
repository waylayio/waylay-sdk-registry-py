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
    from waylay.services.registry.models.job_event_response_waiting_event_data import (
        JobEventResponseWaitingEventData,
    )

    JobEventResponseWaitingEventDataAdapter = TypeAdapter(
        JobEventResponseWaitingEventData
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_event_response_waiting_event_data__model_schema = json.loads(
    r"""{
  "title" : "JobEventResponse_WaitingEventData_",
  "required" : [ "_links", "data", "function", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobStatusAndEntityHALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/WaitingEventData"
    },
    "timestamp" : {
      "title" : "timestamp",
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    }
  },
  "description" : "Event object describing a state change of a background job."
}
""",
    object_hook=with_example_provider,
)
job_event_response_waiting_event_data__model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

job_event_response_waiting_event_data__faker = JSF(
    job_event_response_waiting_event_data__model_schema, allow_none_optionals=1
)


class JobEventResponseWaitingEventDataStub:
    """JobEventResponseWaitingEventData unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_event_response_waiting_event_data__faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "JobEventResponseWaitingEventData":
        """Create JobEventResponseWaitingEventData stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                JobEventResponseWaitingEventDataAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return JobEventResponseWaitingEventDataAdapter.validate_python(
            json, context={"skip_validation": True}
        )
