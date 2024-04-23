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
    from waylay.services.registry.models.deploy1 import Deploy1

    Deploy1Adapter = TypeAdapter(Deploy1)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

deploy_1_model_schema = json.loads(
    r"""{
  "title" : "Deploy",
  "required" : [ "_links", "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/Deploy_type"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The operation name for the background task."
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The creation time of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that initiated this job"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobAndFunctionHALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
deploy_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

deploy_1_faker = JSF(deploy_1_model_schema, allow_none_optionals=1)


class Deploy1Stub:
    """Deploy1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return deploy_1_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Deploy1":
        """Create Deploy1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(Deploy1Adapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return Deploy1Adapter.validate_python(json, context={"skip_validation": True})
