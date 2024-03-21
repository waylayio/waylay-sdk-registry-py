# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
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
        return kf_serving_manifest_faker.generate()

    @classmethod
    def create_instance(cls) -> "KFServingManifest":
        """Create KFServingManifest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return KFServingManifestAdapter.validate_python(cls.create_json())
