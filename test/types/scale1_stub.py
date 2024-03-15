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
    from waylay.services.registry.models.scale1 import Scale1

    Scale1Adapter = TypeAdapter(Scale1)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

scale_1_model_schema = json.loads(r"""{
  "title" : "Scale",
  "required" : [ "_links", "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "title" : "type",
      "type" : "string",
      "description" : "The type of the background task.",
      "enum" : [ "scale" ]
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
""")
scale_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

scale_1_faker = JSF(scale_1_model_schema, allow_none_optionals=1)


class Scale1Stub:
    """Scale1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return scale_1_faker.generate()

    @classmethod
    def create_instance(cls) -> "Scale1":
        """Create Scale1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return Scale1Adapter.validate_python(cls.create_json())
