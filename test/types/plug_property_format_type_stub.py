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
    from waylay.services.registry.models.plug_property_format_type import (
        PlugPropertyFormatType,
    )

    PlugPropertyFormatTypeAdapter = TypeAdapter(PlugPropertyFormatType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

plug_property_format_type_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Value domain for a plug input or output property.",
  "enum" : [ "enum", "resource", "vault", "duration", "code", "url", "date", "template", "aiPluginDescriptor", "aiTemplateDescriptor" ]
}
""",
    object_hook=with_example_provider,
)
plug_property_format_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

plug_property_format_type_faker = JSF(
    plug_property_format_type_model_schema, allow_none_optionals=1
)


class PlugPropertyFormatTypeStub:
    """PlugPropertyFormatType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return plug_property_format_type_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "PlugPropertyFormatType":
        """Create PlugPropertyFormatType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                PlugPropertyFormatTypeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PlugPropertyFormatTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
