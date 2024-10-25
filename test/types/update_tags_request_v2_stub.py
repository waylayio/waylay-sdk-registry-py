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
    from waylay.services.registry.models.update_tags_request_v2 import (
        UpdateTagsRequestV2,
    )

    UpdateTagsRequestV2Adapter = TypeAdapter(UpdateTagsRequestV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

update_tags_request_v2_model_schema = json.loads(
    r"""{
  "required" : [ "tags" ],
  "type" : "object",
  "properties" : {
    "tags" : {
      "type" : "array",
      "description" : "During update, a (reference to a) tag\n- that does not yet exist, is created (using default attributes if not specified)\n- that does exist is **not** updated (even if tag attributes like `color` differ)",
      "example" : [ "awaiting-review", {
        "name" : "demo",
        "color" : "#e639a4"
      } ],
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
update_tags_request_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

update_tags_request_v2_faker = JSF(
    update_tags_request_v2_model_schema, allow_none_optionals=1
)


class UpdateTagsRequestV2Stub:
    """UpdateTagsRequestV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return update_tags_request_v2_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "UpdateTagsRequestV2":
        """Create UpdateTagsRequestV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                UpdateTagsRequestV2Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return UpdateTagsRequestV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
