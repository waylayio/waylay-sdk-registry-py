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
    from waylay.services.registry.models.latest_plug_versions_query_v2 import (
        LatestPlugVersionsQueryV2,
    )

    LatestPlugVersionsQueryV2Adapter = TypeAdapter(LatestPlugVersionsQueryV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

latest_plug_versions_query_v2_model_schema = json.loads(
    r"""{
  "description" : "Latest plug versions listing query.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/LatestPlugVersionsQuery"
  }, {
    "$ref" : "#/components/schemas/LatestPlugsQuery"
  } ]
}
""",
    object_hook=with_example_provider,
)
latest_plug_versions_query_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

latest_plug_versions_query_v2_faker = JSF(
    latest_plug_versions_query_v2_model_schema, allow_none_optionals=1
)


class LatestPlugVersionsQueryV2Stub:
    """LatestPlugVersionsQueryV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return latest_plug_versions_query_v2_faker.generate()

    @classmethod
    def create_instance(cls) -> "LatestPlugVersionsQueryV2":
        """Create LatestPlugVersionsQueryV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LatestPlugVersionsQueryV2Adapter.validate_python(cls.create_json())
