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
    from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2

    GetPlugResponseV2Adapter = TypeAdapter(GetPlugResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

get_plug_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "entity" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/PlugResponseV2"
    },
    "_links" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__links"
    }
  },
  "description" : "Plug Found"
}
""",
    object_hook=with_example_provider,
)
get_plug_response_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_plug_response_v2_faker = JSF(
    get_plug_response_v2_model_schema, allow_none_optionals=1
)


class GetPlugResponseV2Stub:
    """GetPlugResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_plug_response_v2_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "GetPlugResponseV2":
        """Create GetPlugResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GetPlugResponseV2Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GetPlugResponseV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
