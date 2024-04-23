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
    from waylay.services.registry.models.update_metadata_request_v1 import (
        UpdateMetadataRequestV1,
    )

    UpdateMetadataRequestV1Adapter = TypeAdapter(UpdateMetadataRequestV1)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

update_metadata_request_v1_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "author" : {
      "type" : "string",
      "description" : "The author of the function."
    },
    "description" : {
      "type" : "string",
      "description" : "A description of the function"
    },
    "iconURL" : {
      "type" : "string",
      "description" : "An url to an icon that represents this function."
    },
    "category" : {
      "type" : "string",
      "description" : "A category for this function (Deprecated: use tags to categorise your functions)",
      "deprecated" : true
    },
    "documentationURL" : {
      "type" : "string",
      "description" : "External url that document this function."
    },
    "tags" : {
      "type" : "array",
      "description" : "Tags associated with this function.",
      "example" : [ {
        "name" : "awaiting-review",
        "color" : "#4153ea"
      }, {
        "name" : "demo",
        "color" : "#e639a4"
      } ],
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "friendlyName" : {
      "type" : "string",
      "description" : "Display title for this function."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
update_metadata_request_v1_model_schema.update({"definitions": MODEL_DEFINITIONS})

update_metadata_request_v1_faker = JSF(
    update_metadata_request_v1_model_schema, allow_none_optionals=1
)


class UpdateMetadataRequestV1Stub:
    """UpdateMetadataRequestV1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return update_metadata_request_v1_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "UpdateMetadataRequestV1":
        """Create UpdateMetadataRequestV1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                UpdateMetadataRequestV1Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return UpdateMetadataRequestV1Adapter.validate_python(
            json, context={"skip_validation": True}
        )
