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
    from waylay.services.registry.models.job_event_response_failed_event_data import (
        JobEventResponseFailedEventData,
    )

    JobEventResponseFailedEventDataAdapter = TypeAdapter(
        JobEventResponseFailedEventData
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(
        f"Type adapter for JobEventResponseFailedEventData not available: {exc}"
    )
    MODELS_AVAILABLE = False

job_event_response_failed_event_data__model_schema = json.loads(r"""{
  "title" : "JobEventResponse_FailedEventData_",
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
      "$ref" : "#/components/schemas/FailedEventData"
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
""")
job_event_response_failed_event_data__model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

job_event_response_failed_event_data__faker = JSF(
    job_event_response_failed_event_data__model_schema, allow_none_optionals=1
)


class JobEventResponseFailedEventDataStub:
    """JobEventResponseFailedEventData unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_event_response_failed_event_data__faker.generate()

    @classmethod
    def create_instance(cls) -> "JobEventResponseFailedEventData":
        """Create JobEventResponseFailedEventData stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobEventResponseFailedEventDataAdapter.validate_python(cls.create_json())
