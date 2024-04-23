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
    from waylay.services.registry.models.build_args import BuildArgs

    BuildArgsAdapter = TypeAdapter(BuildArgs)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

build_args_model_schema = json.loads(
    r"""{
  "title" : "BuildArgs",
  "required" : [ "args", "imageName", "runtimeName", "runtimeVersion", "storageLocation" ],
  "type" : "object",
  "properties" : {
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
    "storageLocation" : {
      "title" : "storageLocation",
      "type" : "string",
      "description" : "Location of the function assets."
    },
    "imageName" : {
      "title" : "imageName",
      "type" : "string",
      "description" : "Provided (or defaulted) image name to publish the function image."
    },
    "args" : {
      "title" : "args",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      },
      "description" : "Parameters to the runtime configuration."
    }
  },
  "description" : "Input arguments to a job that builds a function."
}
""",
    object_hook=with_example_provider,
)
build_args_model_schema.update({"definitions": MODEL_DEFINITIONS})

build_args_faker = JSF(build_args_model_schema, allow_none_optionals=1)


class BuildArgsStub:
    """BuildArgs unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return build_args_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "BuildArgs":
        """Create BuildArgs stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(BuildArgsAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BuildArgsAdapter.validate_python(json, context={"skip_validation": True})
