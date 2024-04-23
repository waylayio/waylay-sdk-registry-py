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
    from waylay.services.registry.models.legacy_required_properties_inner import (
        LegacyRequiredPropertiesInner,
    )

    LegacyRequiredPropertiesInnerAdapter = TypeAdapter(LegacyRequiredPropertiesInner)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

legacy_required_properties_inner_model_schema = json.loads(
    r"""{
  "title" : "LegacyRequiredProperties_inner",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "$ref" : "#/components/schemas/LegacyRequiredPropertyObject"
  } ]
}
""",
    object_hook=with_example_provider,
)
legacy_required_properties_inner_model_schema.update({"definitions": MODEL_DEFINITIONS})

legacy_required_properties_inner_faker = JSF(
    legacy_required_properties_inner_model_schema, allow_none_optionals=1
)


class LegacyRequiredPropertiesInnerStub:
    """LegacyRequiredPropertiesInner unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_required_properties_inner_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "LegacyRequiredPropertiesInner":
        """Create LegacyRequiredPropertiesInner stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                LegacyRequiredPropertiesInnerAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return LegacyRequiredPropertiesInnerAdapter.validate_python(
            json, context={"skip_validation": True}
        )
