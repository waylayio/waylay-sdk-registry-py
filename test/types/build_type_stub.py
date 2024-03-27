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
    from waylay.services.registry.models.build_type import BuildType

    BuildTypeAdapter = TypeAdapter(BuildType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

build_type_model_schema = json.loads(
    r"""{
  "title" : "Build_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "build" ]
}
""",
    object_hook=with_example_provider,
)
build_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

build_type_faker = JSF(build_type_model_schema, allow_none_optionals=1)


class BuildTypeStub:
    """BuildType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return build_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "BuildType":
        """Create BuildType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BuildTypeAdapter.validate_python(cls.create_json())
