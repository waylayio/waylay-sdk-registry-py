"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.ikf_serving_manifest_patch import (
        IKFServingManifestPatch,
    )

    IKFServingManifestPatchAdapter = TypeAdapter(IKFServingManifestPatch)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

ikf_serving_manifest_patch_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/FunctionMeta"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    }
  },
  "additionalProperties" : false,
  "description" : "Patch attributes to merge into an existing model manifest."
}
""",
    object_hook=with_example_provider,
)
ikf_serving_manifest_patch_model_schema.update({"definitions": MODEL_DEFINITIONS})

ikf_serving_manifest_patch_faker = JSF(
    ikf_serving_manifest_patch_model_schema, allow_none_optionals=1
)


class IKFServingManifestPatchStub:
    """IKFServingManifestPatch unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return ikf_serving_manifest_patch_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "IKFServingManifestPatch":
        """Create IKFServingManifestPatch stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                IKFServingManifestPatchAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return IKFServingManifestPatchAdapter.validate_python(
            json, context={"skip_validation": True}
        )
