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
    from waylay.services.registry.models.webscript_versions_response_v2 import (
        WebscriptVersionsResponseV2,
    )

    WebscriptVersionsResponseV2Adapter = TypeAdapter(WebscriptVersionsResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

webscript_versions_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "count", "entities" ],
  "type" : "object",
  "properties" : {
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "count" : {
      "type" : "number",
      "description" : "The total count of matching items, from which this result is one page."
    },
    "page" : {
      "type" : "number",
      "description" : "The page number of a paged query result."
    },
    "entities" : {
      "type" : "array",
      "description" : "The specification and deployment status of the queried functions",
      "items" : {
        "$ref" : "#/components/schemas/WebscriptResponseWithInvokeLinkV2"
      }
    }
  },
  "description" : "Webscript Versions Found"
}
""",
    object_hook=with_example_provider,
)
webscript_versions_response_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

webscript_versions_response_v2_faker = JSF(
    webscript_versions_response_v2_model_schema, allow_none_optionals=1
)


class WebscriptVersionsResponseV2Stub:
    """WebscriptVersionsResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return webscript_versions_response_v2_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "WebscriptVersionsResponseV2":
        """Create WebscriptVersionsResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                WebscriptVersionsResponseV2Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return WebscriptVersionsResponseV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
