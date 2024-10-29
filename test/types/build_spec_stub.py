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
    from waylay.services.registry.models.build_spec import BuildSpec

    BuildSpecAdapter = TypeAdapter(BuildSpec)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

build_spec_model_schema = json.loads(
    r"""{
  "title" : "BuildSpec",
  "required" : [ "args", "context" ],
  "type" : "object",
  "properties" : {
    "context" : {
      "title" : "context",
      "type" : "string"
    },
    "file" : {
      "title" : "file",
      "type" : "string"
    },
    "args" : {
      "title" : "args",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
build_spec_model_schema.update({"definitions": MODEL_DEFINITIONS})

build_spec_faker = JSF(build_spec_model_schema, allow_none_optionals=1)


class BuildSpecStub:
    """BuildSpec unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return build_spec_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "BuildSpec":
        """Create BuildSpec stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(BuildSpecAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BuildSpecAdapter.validate_python(json, context={"skip_validation": True})
