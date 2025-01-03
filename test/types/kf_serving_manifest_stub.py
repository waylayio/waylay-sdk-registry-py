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
    from waylay.services.registry.models.kf_serving_manifest import KFServingManifest

    KFServingManifestAdapter = TypeAdapter(KFServingManifest)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

kf_serving_manifest_model_schema = json.loads(
    r"""{
  "title" : "KFServingManifest",
  "required" : [ "metadata", "name", "runtime", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "The logical name for the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/FunctionMeta"
    },
    "protected" : {
      "title" : "protected",
      "type" : "boolean",
      "description" : "Indicates whether the function's script and other assets should be protected."
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "description" : "Tags associated with this entity.",
      "items" : {
        "$ref" : "#/components/schemas/TagOrTagReference"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
kf_serving_manifest_model_schema.update({"definitions": MODEL_DEFINITIONS})

kf_serving_manifest_faker = JSF(
    kf_serving_manifest_model_schema, allow_none_optionals=1
)


class KFServingManifestStub:
    """KFServingManifest unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return kf_serving_manifest_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "KFServingManifest":
        """Create KFServingManifest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                KFServingManifestAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return KFServingManifestAdapter.validate_python(
            json, context={"skip_validation": True}
        )
