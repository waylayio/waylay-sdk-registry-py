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
    from waylay.services.registry.models.get_content_params_v2 import GetContentParamsV2

    GetContentParamsV2Adapter = TypeAdapter(GetContentParamsV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

get_content_params_v2_model_schema = json.loads(
    r"""{
  "required" : [ "*", "name", "version" ],
  "type" : "object",
  "properties" : {
    "*" : {
      "type" : "string",
      "description" : "Full path or path prefix of the asset within the archive"
    },
    "name" : {
      "type" : "string",
      "description" : "The name of the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
get_content_params_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_content_params_v2_faker = JSF(
    get_content_params_v2_model_schema, allow_none_optionals=1
)


class GetContentParamsV2Stub:
    """GetContentParamsV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_content_params_v2_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "GetContentParamsV2":
        """Create GetContentParamsV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GetContentParamsV2Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GetContentParamsV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
