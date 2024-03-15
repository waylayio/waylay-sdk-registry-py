# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.plug_property_format_type import (
        PlugPropertyFormatType,
    )

    PlugPropertyFormatTypeAdapter = TypeAdapter(PlugPropertyFormatType)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

plug_property_format_type_model_schema = json.loads(r"""{
  "title" : "PlugPropertyFormatType",
  "type" : "string",
  "description" : "Value domain for a plug input or output property.",
  "enum" : [ "enum", "resource", "vault", "duration", "code", "url", "date", "template" ]
}
""")
plug_property_format_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

plug_property_format_type_faker = JSF(
    plug_property_format_type_model_schema, allow_none_optionals=1
)


class PlugPropertyFormatTypeStub:
    """PlugPropertyFormatType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return plug_property_format_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "PlugPropertyFormatType":
        """Create PlugPropertyFormatType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return PlugPropertyFormatTypeAdapter.validate_python(cls.create_json())
