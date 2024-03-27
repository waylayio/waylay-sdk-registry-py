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
    from waylay.services.registry.models.scale_type import ScaleType

    ScaleTypeAdapter = TypeAdapter(ScaleType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

scale_type_model_schema = json.loads(
    r"""{
  "title" : "Scale_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "scale" ]
}
""",
    object_hook=with_example_provider,
)
scale_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

scale_type_faker = JSF(scale_type_model_schema, allow_none_optionals=1)


class ScaleTypeStub:
    """ScaleType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return scale_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "ScaleType":
        """Create ScaleType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ScaleTypeAdapter.validate_python(cls.create_json())
