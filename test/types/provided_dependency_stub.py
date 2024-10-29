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
    from waylay.services.registry.models.provided_dependency import ProvidedDependency

    ProvidedDependencyAdapter = TypeAdapter(ProvidedDependency)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

provided_dependency_model_schema = json.loads(
    r"""{
  "title" : "ProvidedDependency",
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "Name of a provided dependency."
    },
    "title" : {
      "title" : "title",
      "type" : "string",
      "description" : "Optional display title."
    },
    "description" : {
      "title" : "description",
      "type" : "string",
      "description" : "Optional description."
    },
    "version" : {
      "title" : "version",
      "type" : "string",
      "description" : "Versions specification of a provided dependency"
    },
    "deprecated" : {
      "title" : "deprecated",
      "type" : "boolean",
      "description" : "If true, this provided dependency is scheduled for removal (or incompatible upgrade) in a next runtime version.",
      "default" : false
    },
    "removed" : {
      "title" : "removed",
      "type" : "boolean",
      "description" : "If true, this dependency has been removed from the runtime (version)",
      "default" : false
    },
    "globals" : {
      "title" : "globals",
      "type" : "array",
      "description" : "Global variables that expose this library to the user code. As the usage of these globals is deprecated, any usage of such global will pose issues in an next runtime version.",
      "items" : {
        "type" : "string"
      }
    },
    "native" : {
      "title" : "native",
      "type" : "boolean",
      "description" : "If true, the library is provided natively by the runtime: e.g. node for javascript."
    }
  },
  "description" : "Library dependency that is provided by this runtime."
}
""",
    object_hook=with_example_provider,
)
provided_dependency_model_schema.update({"definitions": MODEL_DEFINITIONS})

provided_dependency_faker = JSF(
    provided_dependency_model_schema, allow_none_optionals=1
)


class ProvidedDependencyStub:
    """ProvidedDependency unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return provided_dependency_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ProvidedDependency":
        """Create ProvidedDependency stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ProvidedDependencyAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ProvidedDependencyAdapter.validate_python(
            json, context={"skip_validation": True}
        )
