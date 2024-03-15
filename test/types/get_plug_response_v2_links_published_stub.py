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
    from waylay.services.registry.models.get_plug_response_v2_links_published import (
        GetPlugResponseV2LinksPublished,
    )

    GetPlugResponseV2LinksPublishedAdapter = TypeAdapter(
        GetPlugResponseV2LinksPublished
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

get_plug_response_v2__links_published_model_schema = json.loads(r"""{
  "title" : "GetPlugResponseV2__links_published",
  "required" : [ "deprecated", "draft", "href", "version" ],
  "type" : "object",
  "properties" : {
    "draft" : {
      "type" : "boolean"
    },
    "href" : {
      "type" : "string"
    },
    "version" : {
      "type" : "string"
    },
    "deprecated" : {
      "type" : "boolean"
    }
  },
  "description" : "Link to the lastest published version.",
  "example" : {
    "href" : "https://api.waylay.io/registry/v2/models/modelName/versions/1.0.1",
    "version" : "1.2.0",
    "draft" : false,
    "deprecated" : false
  }
}
""")
get_plug_response_v2__links_published_model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

get_plug_response_v2__links_published_faker = JSF(
    get_plug_response_v2__links_published_model_schema, allow_none_optionals=1
)


class GetPlugResponseV2LinksPublishedStub:
    """GetPlugResponseV2LinksPublished unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_plug_response_v2__links_published_faker.generate()

    @classmethod
    def create_instance(cls) -> "GetPlugResponseV2LinksPublished":
        """Create GetPlugResponseV2LinksPublished stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return GetPlugResponseV2LinksPublishedAdapter.validate_python(cls.create_json())
