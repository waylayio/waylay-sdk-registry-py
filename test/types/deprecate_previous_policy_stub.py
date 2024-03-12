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
    from waylay.services.registry.models.deprecate_previous_policy import (
        DeprecatePreviousPolicy,
    )

    DeprecatePreviousPolicyAdapter = TypeAdapter(DeprecatePreviousPolicy)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for DeprecatePreviousPolicy not available: {exc}")
    MODELS_AVAILABLE = False

deprecate_previous_policy_model_schema = json.loads(r"""{
  "title" : "DeprecatePreviousPolicy",
  "type" : "string",
  "enum" : [ "none", "all", "patch", "minor" ]
}
""")
deprecate_previous_policy_model_schema.update({"definitions": MODEL_DEFINITIONS})

deprecate_previous_policy_faker = JSF(
    deprecate_previous_policy_model_schema, allow_none_optionals=1
)


class DeprecatePreviousPolicyStub:
    """DeprecatePreviousPolicy unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return deprecate_previous_policy_faker.generate()

    @classmethod
    def create_instance(cls) -> "DeprecatePreviousPolicy":
        """Create DeprecatePreviousPolicy stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return DeprecatePreviousPolicyAdapter.validate_python(cls.create_json())
