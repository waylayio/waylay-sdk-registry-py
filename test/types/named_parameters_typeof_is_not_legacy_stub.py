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
    from waylay.services.registry.models.named_parameters_typeof_is_not_legacy import (
        NamedParametersTypeofIsNotLegacy,
    )

    NamedParametersTypeofIsNotLegacyAdapter = TypeAdapter(
        NamedParametersTypeofIsNotLegacy
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

named_parameters_typeof_is_not_legacy__model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "documentation" : {
      "$ref" : "#/components/schemas/LegacyPlugRequest_metadata_documentation"
    }
  },
  "additionalProperties" : false
}
""")
named_parameters_typeof_is_not_legacy__model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

named_parameters_typeof_is_not_legacy__faker = JSF(
    named_parameters_typeof_is_not_legacy__model_schema, allow_none_optionals=1
)


class NamedParametersTypeofIsNotLegacyStub:
    """NamedParametersTypeofIsNotLegacy unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return named_parameters_typeof_is_not_legacy__faker.generate()

    @classmethod
    def create_instance(cls) -> "NamedParametersTypeofIsNotLegacy":
        """Create NamedParametersTypeofIsNotLegacy stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return NamedParametersTypeofIsNotLegacyAdapter.validate_python(
            cls.create_json()
        )
