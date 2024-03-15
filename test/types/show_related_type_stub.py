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
    from waylay.services.registry.models.show_related_type import ShowRelatedType

    ShowRelatedTypeAdapter = TypeAdapter(ShowRelatedType)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

show_related_type_model_schema = json.loads(r"""{
  "type" : "string",
  "enum" : [ "embed", "link", "none" ]
}
""")
show_related_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

show_related_type_faker = JSF(show_related_type_model_schema, allow_none_optionals=1)


class ShowRelatedTypeStub:
    """ShowRelatedType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return show_related_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "ShowRelatedType":
        """Create ShowRelatedType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ShowRelatedTypeAdapter.validate_python(cls.create_json())
