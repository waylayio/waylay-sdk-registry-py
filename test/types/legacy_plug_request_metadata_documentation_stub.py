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
    from waylay.services.registry.models.legacy_plug_request_metadata_documentation import (
        LegacyPlugRequestMetadataDocumentation,
    )

    LegacyPlugRequestMetadataDocumentationAdapter = TypeAdapter(
        LegacyPlugRequestMetadataDocumentation
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(
        f"Type adapter for LegacyPlugRequestMetadataDocumentation not available: {exc}"
    )
    MODELS_AVAILABLE = False

legacy_plug_request_metadata_documentation_model_schema = json.loads(r"""{
  "title" : "LegacyPlugRequest_metadata_documentation",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/LegacyPlugRequest_metadata_documentation_anyOf"
  }, {
    "$ref" : "#/components/schemas/Documentation"
  } ]
}
""")
legacy_plug_request_metadata_documentation_model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

legacy_plug_request_metadata_documentation_faker = JSF(
    legacy_plug_request_metadata_documentation_model_schema, allow_none_optionals=1
)


class LegacyPlugRequestMetadataDocumentationStub:
    """LegacyPlugRequestMetadataDocumentation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_plug_request_metadata_documentation_faker.generate()

    @classmethod
    def create_instance(cls) -> "LegacyPlugRequestMetadataDocumentation":
        """Create LegacyPlugRequestMetadataDocumentation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LegacyPlugRequestMetadataDocumentationAdapter.validate_python(
            cls.create_json()
        )
