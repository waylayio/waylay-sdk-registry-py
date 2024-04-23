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
    from waylay.services.registry.models.get_webscript_response_v2_links import (
        GetWebscriptResponseV2Links,
    )

    GetWebscriptResponseV2LinksAdapter = TypeAdapter(GetWebscriptResponseV2Links)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

get_webscript_response_v2__links_model_schema = json.loads(
    r"""{
  "title" : "GetWebscriptResponseV2__links",
  "type" : "object",
  "properties" : {
    "invoke" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "jobs" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  },
  "description" : "HAL links to related actions."
}
""",
    object_hook=with_example_provider,
)
get_webscript_response_v2__links_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_webscript_response_v2__links_faker = JSF(
    get_webscript_response_v2__links_model_schema, allow_none_optionals=1
)


class GetWebscriptResponseV2LinksStub:
    """GetWebscriptResponseV2Links unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_webscript_response_v2__links_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "GetWebscriptResponseV2Links":
        """Create GetWebscriptResponseV2Links stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GetWebscriptResponseV2LinksAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GetWebscriptResponseV2LinksAdapter.validate_python(
            json, context={"skip_validation": True}
        )
