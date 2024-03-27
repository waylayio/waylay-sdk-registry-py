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
    from waylay.services.registry.models.job_event_sse import JobEventSSE

    JobEventSSEAdapter = TypeAdapter(JobEventSSE)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_event_sse_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/ActiveEventSSE"
  }, {
    "$ref" : "#/components/schemas/CompletedEventSSE"
  }, {
    "$ref" : "#/components/schemas/FailedEventSSE"
  }, {
    "$ref" : "#/components/schemas/DelayedEventSSE"
  }, {
    "$ref" : "#/components/schemas/WaitingEventSSE"
  }, {
    "$ref" : "#/components/schemas/WaitingChildrenEventSSE"
  } ]
}
""",
    object_hook=with_example_provider,
)
job_event_sse_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_event_sse_faker = JSF(job_event_sse_model_schema, allow_none_optionals=1)


class JobEventSSEStub:
    """JobEventSSE unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_event_sse_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobEventSSE":
        """Create JobEventSSE stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobEventSSEAdapter.validate_python(cls.create_json())
