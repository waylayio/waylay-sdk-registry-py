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
    from waylay.services.registry.models.verify_args import VerifyArgs

    VerifyArgsAdapter = TypeAdapter(VerifyArgs)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for VerifyArgs not available: {exc}")
    MODELS_AVAILABLE = False

verify_args_model_schema = json.loads(r"""{
  "title" : "VerifyArgs",
  "required" : [ "endpoint", "namespace", "runtimeName", "runtimeVersion" ],
  "type" : "object",
  "properties" : {
    "namespace" : {
      "title" : "namespace",
      "type" : "string",
      "description" : "The (openfaas) namespace for the target function."
    },
    "endpoint" : {
      "title" : "endpoint",
      "type" : "string",
      "description" : "The (openfaas) endpoint service name"
    },
    "runtimeName" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "revision" : {
      "title" : "revision",
      "type" : "string",
      "description" : "The revision hash of the current (draft) function revision"
    }
  },
  "description" : "Input arguments for an (openfaas) deployment verification job."
}
""")
verify_args_model_schema.update({"definitions": MODEL_DEFINITIONS})

verify_args_faker = JSF(verify_args_model_schema, allow_none_optionals=1)


class VerifyArgsStub:
    """VerifyArgs unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return verify_args_faker.generate()

    @classmethod
    def create_instance(cls) -> "VerifyArgs":
        """Create VerifyArgs stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return VerifyArgsAdapter.validate_python(cls.create_json())
