"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.deprecate_previous_policy_patch import (
        DeprecatePreviousPolicyPatch,
    )

    DeprecatePreviousPolicyPatchAdapter = TypeAdapter(DeprecatePreviousPolicyPatch)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

deprecate_previous_policy_patch_model_schema = json.loads(
    r"""{
  "title" : "DeprecatePreviousPolicyPatch",
  "type" : "string",
  "enum" : [ "patch" ]
}
""",
    object_hook=with_example_provider,
)
deprecate_previous_policy_patch_model_schema.update({"definitions": MODEL_DEFINITIONS})

deprecate_previous_policy_patch_faker = JSF(
    deprecate_previous_policy_patch_model_schema, allow_none_optionals=1
)


class DeprecatePreviousPolicyPatchStub:
    """DeprecatePreviousPolicyPatch unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return deprecate_previous_policy_patch_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "DeprecatePreviousPolicyPatch":
        """Create DeprecatePreviousPolicyPatch stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                DeprecatePreviousPolicyPatchAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return DeprecatePreviousPolicyPatchAdapter.validate_python(
            json, context={"skip_validation": True}
        )
