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
    from waylay.services.registry.models.deprecated_draft_filter import (
        DeprecatedDraftFilter,
    )

    DeprecatedDraftFilterAdapter = TypeAdapter(DeprecatedDraftFilter)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for DeprecatedDraftFilter not available: {exc}")
    MODELS_AVAILABLE = False

deprecated_draft_filter_model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
    }
  },
  "additionalProperties" : false
}
""")
deprecated_draft_filter_model_schema.update({"definitions": MODEL_DEFINITIONS})

deprecated_draft_filter_faker = JSF(
    deprecated_draft_filter_model_schema, allow_none_optionals=1
)


class DeprecatedDraftFilterStub:
    """DeprecatedDraftFilter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return deprecated_draft_filter_faker.generate()

    @classmethod
    def create_instance(cls) -> "DeprecatedDraftFilter":
        """Create DeprecatedDraftFilter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return DeprecatedDraftFilterAdapter.validate_python(cls.create_json())
