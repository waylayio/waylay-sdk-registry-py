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
    from waylay.services.registry.models.latest_plugs_response_v2 import (
        LatestPlugsResponseV2,
    )

    LatestPlugsResponseV2Adapter = TypeAdapter(LatestPlugsResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

latest_plugs_response_v2_model_schema = json.loads(
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
        "$ref" : "#/components/schemas/EntityWithLinks_IPlugResponseV2_"
      }
    }
  },
  "description" : "Plugs Found"
}
""",
    object_hook=with_example_provider,
)
latest_plugs_response_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

latest_plugs_response_v2_faker = JSF(
    latest_plugs_response_v2_model_schema, allow_none_optionals=1
)


class LatestPlugsResponseV2Stub:
    """LatestPlugsResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return latest_plugs_response_v2_faker.generate()

    @classmethod
    def create_instance(cls) -> "LatestPlugsResponseV2":
        """Create LatestPlugsResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LatestPlugsResponseV2Adapter.validate_python(cls.create_json())
