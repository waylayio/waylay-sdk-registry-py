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
    from waylay.services.registry.models.content_validation_listing import (
        ContentValidationListing,
    )

    ContentValidationListingAdapter = TypeAdapter(ContentValidationListing)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

content_validation_listing_model_schema = json.loads(
    r"""{
  "required" : [ "assets" ],
  "type" : "object",
  "properties" : {
    "assets" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/AssetSummaryWithHALLink"
      }
    }
  },
  "description" : "Content listing"
}
""",
    object_hook=with_example_provider,
)
content_validation_listing_model_schema.update({"definitions": MODEL_DEFINITIONS})

content_validation_listing_faker = JSF(
    content_validation_listing_model_schema, allow_none_optionals=1
)


class ContentValidationListingStub:
    """ContentValidationListing unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return content_validation_listing_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ContentValidationListing":
        """Create ContentValidationListing stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ContentValidationListingAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ContentValidationListingAdapter.validate_python(
            json, context={"skip_validation": True}
        )
