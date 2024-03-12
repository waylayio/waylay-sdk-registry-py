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
    from waylay.services.registry.models.deploy_args import DeployArgs

    DeployArgsAdapter = TypeAdapter(DeployArgs)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for DeployArgs not available: {exc}")
    MODELS_AVAILABLE = False

deploy_args_model_schema = json.loads(r"""{
  "title" : "DeployArgs",
  "required" : [ "deploySpecOverrides", "endpoint", "imageName", "namespace", "runtimeName", "runtimeVersion" ],
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
    "imageName" : {
      "title" : "imageName",
      "type" : "string",
      "description" : "The image name to use for deploying this function"
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
    },
    "deploySpecOverrides" : {
      "$ref" : "#/components/schemas/DeployArgs_deploySpecOverrides"
    }
  },
  "description" : "Input argument to an (openfaas) deployment job for a function."
}
""")
deploy_args_model_schema.update({"definitions": MODEL_DEFINITIONS})

deploy_args_faker = JSF(deploy_args_model_schema, allow_none_optionals=1)


class DeployArgsStub:
    """DeployArgs unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return deploy_args_faker.generate()

    @classmethod
    def create_instance(cls) -> "DeployArgs":
        """Create DeployArgs stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return DeployArgsAdapter.validate_python(cls.create_json())
