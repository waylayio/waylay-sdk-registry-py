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
    from waylay.services.registry.models.job_events_filter_query import (
        JobEventsFilterQuery,
    )

    JobEventsFilterQueryAdapter = TypeAdapter(JobEventsFilterQuery)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

job_events_filter_query_model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/JobType"
    },
    "id" : {
      "type" : "string",
      "description" : "The id of the job."
    },
    "children" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, the event stream will include events of the job's dependants. E.g., when subscribing to a verify job with `children=true`, you will also receive the events of the underlying build and deploy jobs. Defaults to <code>false</code>."
    }
  },
  "additionalProperties" : false
}
""")
job_events_filter_query_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_events_filter_query_faker = JSF(
    job_events_filter_query_model_schema, allow_none_optionals=1
)


class JobEventsFilterQueryStub:
    """JobEventsFilterQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_events_filter_query_faker.generate()

    @classmethod
    def create_instance(cls) -> "JobEventsFilterQuery":
        """Create JobEventsFilterQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return JobEventsFilterQueryAdapter.validate_python(cls.create_json())
