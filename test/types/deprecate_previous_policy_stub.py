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
    from waylay.services.registry.models.deprecate_previous_policy import (
        DeprecatePreviousPolicy,
    )

    DeprecatePreviousPolicyAdapter = TypeAdapter(DeprecatePreviousPolicy)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

deprecate_previous_policy_model_schema = json.loads(
    r"""{
  "title" : "DeprecatePreviousPolicy",
  "type" : "string",
  "enum" : [ "none", "all", "patch", "minor" ]
}
""",
    object_hook=with_example_provider,
)
deprecate_previous_policy_model_schema.update({"definitions": MODEL_DEFINITIONS})

deprecate_previous_policy_faker = JSF(
    deprecate_previous_policy_model_schema, allow_none_optionals=1
)


class DeprecatePreviousPolicyStub:
    """DeprecatePreviousPolicy unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return deprecate_previous_policy_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "DeprecatePreviousPolicy":
        """Create DeprecatePreviousPolicy stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                DeprecatePreviousPolicyAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return DeprecatePreviousPolicyAdapter.validate_python(
            json, context={"skip_validation": True}
        )
