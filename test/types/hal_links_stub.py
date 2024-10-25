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
    from waylay.services.registry.models.hal_links import HALLinks

    HALLinksAdapter = TypeAdapter(HALLinks)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

hal_links_model_schema = json.loads(
    r"""{
  "description" : "One or more links of the same HAL collection.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
hal_links_model_schema.update({"definitions": MODEL_DEFINITIONS})

hal_links_faker = JSF(hal_links_model_schema, allow_none_optionals=1)


class HALLinksStub:
    """HALLinks unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return hal_links_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "HALLinks":
        """Create HALLinks stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(HALLinksAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return HALLinksAdapter.validate_python(json, context={"skip_validation": True})
