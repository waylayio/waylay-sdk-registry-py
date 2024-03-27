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
    from waylay.services.registry.models.asset_summary_with_hal_link_links import (
        AssetSummaryWithHALLinkLinks,
    )

    AssetSummaryWithHALLinkLinksAdapter = TypeAdapter(AssetSummaryWithHALLinkLinks)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

asset_summary_with_hal_link__links_model_schema = json.loads(
    r"""{
  "title" : "AssetSummaryWithHALLink__links",
  "required" : [ "asset" ],
  "type" : "object",
  "properties" : {
    "asset" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  },
  "description" : "HAL links to the asset"
}
""",
    object_hook=with_example_provider,
)
asset_summary_with_hal_link__links_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

asset_summary_with_hal_link__links_faker = JSF(
    asset_summary_with_hal_link__links_model_schema, allow_none_optionals=1
)


class AssetSummaryWithHALLinkLinksStub:
    """AssetSummaryWithHALLinkLinks unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return asset_summary_with_hal_link__links_faker.generate()

    @classmethod
    def create_instance(cls) -> "AssetSummaryWithHALLinkLinks":
        """Create AssetSummaryWithHALLinkLinks stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return AssetSummaryWithHALLinkLinksAdapter.validate_python(cls.create_json())
