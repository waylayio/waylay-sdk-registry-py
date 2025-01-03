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
    from waylay.services.registry.models.update_plug_metadata_request_v2 import (
        UpdatePlugMetadataRequestV2,
    )

    UpdatePlugMetadataRequestV2Adapter = TypeAdapter(UpdatePlugMetadataRequestV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

update_plug_metadata_request_v2_model_schema = json.loads(
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
    "friendlyName" : {
      "type" : "string",
      "description" : "Display title for this function."
    },
    "tags" : {
      "type" : "array",
      "description" : "During update, a (reference to a) tag\n- that does not yet exist, is created (using default attributes if not specified)\n- that does exist is not updated (even if tag attributes like `color` differ)",
      "example" : [ "awaiting-review", {
        "name" : "demo",
        "color" : "#e639a4"
      } ],
      "deprecated" : false,
      "items" : {
        "$ref" : "#/components/schemas/TagOrTagReference"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
update_plug_metadata_request_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

update_plug_metadata_request_v2_faker = JSF(
    update_plug_metadata_request_v2_model_schema, allow_none_optionals=1
)


class UpdatePlugMetadataRequestV2Stub:
    """UpdatePlugMetadataRequestV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return update_plug_metadata_request_v2_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "UpdatePlugMetadataRequestV2":
        """Create UpdatePlugMetadataRequestV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                UpdatePlugMetadataRequestV2Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return UpdatePlugMetadataRequestV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
