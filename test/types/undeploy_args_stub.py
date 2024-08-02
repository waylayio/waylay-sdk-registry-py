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
    from waylay.services.registry.models.undeploy_args import UndeployArgs

    UndeployArgsAdapter = TypeAdapter(UndeployArgs)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

undeploy_args_model_schema = json.loads(
    r"""{
  "title" : "UndeployArgs",
  "required" : [ "deleteEntity", "endpoint", "isNativePlug", "namespace", "resetEntity", "revision", "runtimeName", "runtimeVersion" ],
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
    },
    "isNativePlug" : {
      "title" : "isNativePlug",
      "type" : "boolean",
      "description" : "If true, the function is not expected to be deployed on openfaas."
    },
    "deleteEntity" : {
      "title" : "deleteEntity",
      "type" : "boolean"
    },
    "resetEntity" : {
      "title" : "resetEntity",
      "type" : "boolean"
    }
  },
  "description" : "Input argument to an (openfaas) undeployment job for a function."
}
""",
    object_hook=with_example_provider,
)
undeploy_args_model_schema.update({"definitions": MODEL_DEFINITIONS})

undeploy_args_faker = JSF(undeploy_args_model_schema, allow_none_optionals=1)


class UndeployArgsStub:
    """UndeployArgs unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return undeploy_args_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "UndeployArgs":
        """Create UndeployArgs stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                UndeployArgsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return UndeployArgsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
