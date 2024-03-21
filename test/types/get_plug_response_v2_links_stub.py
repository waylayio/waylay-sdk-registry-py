# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.get_plug_response_v2_links import (
        GetPlugResponseV2Links,
    )

    GetPlugResponseV2LinksAdapter = TypeAdapter(GetPlugResponseV2Links)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

get_plug_response_v2__links_model_schema = json.loads(
    r"""{
  "title" : "GetPlugResponseV2__links",
  "type" : "object",
  "properties" : {
    "draft" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__links_draft"
    },
    "published" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__links_published"
    },
    "jobs" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  },
  "description" : "HAL links to related jobs and plugs"
}
""",
    object_hook=with_example_provider,
)
get_plug_response_v2__links_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_plug_response_v2__links_faker = JSF(
    get_plug_response_v2__links_model_schema, allow_none_optionals=1
)


class GetPlugResponseV2LinksStub:
    """GetPlugResponseV2Links unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_plug_response_v2__links_faker.generate()

    @classmethod
    def create_instance(cls) -> "GetPlugResponseV2Links":
        """Create GetPlugResponseV2Links stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return GetPlugResponseV2LinksAdapter.validate_python(cls.create_json())
