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
    from waylay.services.registry.models.job_cause import JobCause

    JobCauseAdapter = TypeAdapter(JobCause)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

job_cause_model_schema = json.loads(
    r"""{
  "title" : "JobCause",
  "required" : [ "changed", "reason" ],
  "type" : "object",
  "properties" : {
    "changed" : {
      "title" : "changed",
      "type" : "boolean",
      "description" : "If <code>true</code>, the argument configuration for this job has changed in comparison to the previous job execution. A <code>false</code> will prevent the job to be run. Use <code>forceVersion</code> or <code>upgrade</code> parameter to force a rebuild."
    },
    "reason" : {
      "title" : "reason",
      "type" : "string",
      "description" : "Human readable message describing the cause."
    },
    "backoff" : {
      "title" : "backoff",
      "type" : "boolean",
      "description" : "If <code>true</code>, recent failures of the job prevented the re-execution. Use <code>forceVersion</code> or <code>upgrade</code> parameter to force a rebuild."
    },
    "newValue" : {
      "title" : "newValue",
      "type" : "string",
      "description" : "The new configuration value that causes the change."
    },
    "oldValue" : {
      "title" : "oldValue",
      "type" : "string",
      "description" : "The old configuration value used by the last succeeded job."
    }
  },
  "description" : "The motivation for including or excluding a job (<em>build</em>, <em>deploy</em>, <em>verify</em>, ...) in response to a <em>rebuild</em> request."
}
""",
    object_hook=with_example_provider,
)
job_cause_model_schema.update({"definitions": MODEL_DEFINITIONS})

job_cause_faker = JSF(job_cause_model_schema, allow_none_optionals=1)


class JobCauseStub:
    """JobCause unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return job_cause_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "JobCause":
        """Create JobCause stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(JobCauseAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return JobCauseAdapter.validate_python(json, context={"skip_validation": True})
