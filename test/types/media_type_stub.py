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
    from waylay.services.registry.models.media_type import MediaType

    MediaTypeAdapter = TypeAdapter(MediaType)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

media_type_model_schema = json.loads(r"""{
  "title" : "MediaType",
  "type" : "string",
  "enum" : [ "application/javascript", "application/java-vm", "text/x-python", "text/x-golang" ]
}
""")
media_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

media_type_faker = JSF(media_type_model_schema, allow_none_optionals=1)


class MediaTypeStub:
    """MediaType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return media_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "MediaType":
        """Create MediaType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return MediaTypeAdapter.validate_python(cls.create_json())
