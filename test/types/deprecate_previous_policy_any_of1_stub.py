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
    from waylay.services.registry.models.deprecate_previous_policy_any_of1 import (
        DeprecatePreviousPolicyAnyOf1,
    )

    DeprecatePreviousPolicyAnyOf1Adapter = TypeAdapter(DeprecatePreviousPolicyAnyOf1)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

deprecate_previous_policy_any_of_1_model_schema = json.loads(
    r"""{
  "title" : "DeprecatePreviousPolicy_anyOf_1",
  "type" : "string",
  "enum" : [ "all" ]
}
""",
    object_hook=with_example_provider,
)
deprecate_previous_policy_any_of_1_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

deprecate_previous_policy_any_of_1_faker = JSF(
    deprecate_previous_policy_any_of_1_model_schema, allow_none_optionals=1
)


class DeprecatePreviousPolicyAnyOf1Stub:
    """DeprecatePreviousPolicyAnyOf1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return deprecate_previous_policy_any_of_1_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "DeprecatePreviousPolicyAnyOf1":
        """Create DeprecatePreviousPolicyAnyOf1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                DeprecatePreviousPolicyAnyOf1Adapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return DeprecatePreviousPolicyAnyOf1Adapter.validate_python(
            json, context={"skip_validation": True}
        )
