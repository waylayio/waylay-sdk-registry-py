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
    from waylay.services.registry.models.runtime_specification import (
        RuntimeSpecification,
    )

    RuntimeSpecificationAdapter = TypeAdapter(RuntimeSpecification)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for RuntimeSpecification not available: {exc}")
    MODELS_AVAILABLE = False

runtime_specification_model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "build" : {
      "$ref" : "#/components/schemas/BuildSpec"
    },
    "deploy" : {
      "$ref" : "#/components/schemas/DeploySpec"
    },
    "language" : {
      "$ref" : "#/components/schemas/LanguageRelease"
    },
    "providedDependencies" : {
      "type" : "array",
      "description" : "Description of dependencies provided by this runtime version.",
      "items" : {
        "$ref" : "#/components/schemas/ProvidedDependency"
      }
    },
    "assets" : {
      "$ref" : "#/components/schemas/AssetsConditions"
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "If true, this runtime should no longer be used for new functions."
    }
  },
  "description" : "Runtime (version) specification that says\n* what assets are required/allowed to build the function\n* what build parameters are used\n* what deployment parameters are used\n* which dependencies are provided by the runtime"
}
""")
runtime_specification_model_schema.update({"definitions": MODEL_DEFINITIONS})

runtime_specification_faker = JSF(
    runtime_specification_model_schema, allow_none_optionals=1
)


class RuntimeSpecificationStub:
    """RuntimeSpecification unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return runtime_specification_faker.generate()

    @classmethod
    def create_instance(cls) -> "RuntimeSpecification":
        """Create RuntimeSpecification stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return RuntimeSpecificationAdapter.validate_python(cls.create_json())
