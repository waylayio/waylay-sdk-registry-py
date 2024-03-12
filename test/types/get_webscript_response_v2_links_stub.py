# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import warnings

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.get_webscript_response_v2_links import (
        GetWebscriptResponseV2Links,
    )

    GetWebscriptResponseV2LinksAdapter = TypeAdapter(GetWebscriptResponseV2Links)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for GetWebscriptResponseV2Links not available: {exc}")
    MODELS_AVAILABLE = False

get_webscript_response_v2__links_model_schema = json.loads(r"""{
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
""")
get_webscript_response_v2__links_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_webscript_response_v2__links_faker = JSF(
    get_webscript_response_v2__links_model_schema, allow_none_optionals=1
)


class GetWebscriptResponseV2LinksStub:
    """GetWebscriptResponseV2Links unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_webscript_response_v2__links_faker.generate()

    @classmethod
    def create_instance(cls) -> "GetWebscriptResponseV2Links":
        """Create GetWebscriptResponseV2Links stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return GetWebscriptResponseV2LinksAdapter.validate_python(cls.create_json())
