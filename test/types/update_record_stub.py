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
    from waylay.services.registry.models.update_record import UpdateRecord

    UpdateRecordAdapter = TypeAdapter(UpdateRecord)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

update_record_model_schema = json.loads(
    r"""{
  "title" : "UpdateRecord",
  "required" : [ "at", "by", "operation" ],
  "type" : "object",
  "properties" : {
    "comment" : {
      "title" : "comment",
      "type" : "string",
      "description" : "An optional user-specified comment corresponding to the operation."
    },
    "operation" : {
      "$ref" : "#/components/schemas/RequestOperation"
    },
    "jobs" : {
      "title" : "jobs",
      "type" : "array",
      "description" : "The job id's of the corresponding jobs, if applicable.",
      "items" : {
        "type" : "string"
      }
    },
    "at" : {
      "title" : "at",
      "type" : "string",
      "format" : "date-time"
    },
    "by" : {
      "title" : "by",
      "type" : "string",
      "description" : "The user that initiated this operation."
    }
  },
  "description" : "An update report corresponding to a modifying operation initiated by a user/administrator on the entity."
}
""",
    object_hook=with_example_provider,
)
update_record_model_schema.update({"definitions": MODEL_DEFINITIONS})

update_record_faker = JSF(update_record_model_schema, allow_none_optionals=1)


class UpdateRecordStub:
    """UpdateRecord unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return update_record_faker.generate()

    @classmethod
    def create_instance(cls) -> "UpdateRecord":
        """Create UpdateRecord stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return UpdateRecordAdapter.validate_python(cls.create_json())
