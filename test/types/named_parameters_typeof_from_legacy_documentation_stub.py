# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import warnings

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.named_parameters_typeof_from_legacy_documentation import (
        NamedParametersTypeofFromLegacyDocumentation,
    )

    NamedParametersTypeofFromLegacyDocumentationAdapter = TypeAdapter(
        NamedParametersTypeofFromLegacyDocumentation
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(
        f"Type adapter for NamedParametersTypeofFromLegacyDocumentation not available: {exc}"
    )
    MODELS_AVAILABLE = False

named_parameters_typeof_from_legacy_documentation__model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "legacyDocumentation" : {
      "$ref" : "#/components/schemas/LegacyPlugRequest_metadata_documentation"
    },
    "currentInterface" : {
      "$ref" : "#/components/schemas/PlugInterface"
    }
  },
  "additionalProperties" : false
}
""")
named_parameters_typeof_from_legacy_documentation__model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

named_parameters_typeof_from_legacy_documentation__faker = JSF(
    named_parameters_typeof_from_legacy_documentation__model_schema,
    allow_none_optionals=1,
)


class NamedParametersTypeofFromLegacyDocumentationStub:
    """NamedParametersTypeofFromLegacyDocumentation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return named_parameters_typeof_from_legacy_documentation__faker.generate()

    @classmethod
    def create_instance(cls) -> "NamedParametersTypeofFromLegacyDocumentation":
        """Create NamedParametersTypeofFromLegacyDocumentation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return NamedParametersTypeofFromLegacyDocumentationAdapter.validate_python(
            cls.create_json()
        )
