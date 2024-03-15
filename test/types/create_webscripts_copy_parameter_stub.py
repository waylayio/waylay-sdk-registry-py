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
    from waylay.services.registry.models.create_webscripts_copy_parameter import (
        CreateWebscriptsCopyParameter,
    )

    CreateWebscriptsCopyParameterAdapter = TypeAdapter(CreateWebscriptsCopyParameter)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

create_webscripts_copy_parameter_model_schema = json.loads(r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/NamedVersionRange"
  }, {
    "$ref" : "#/components/schemas/ExampleReference"
  } ]
}
""")
create_webscripts_copy_parameter_model_schema.update({"definitions": MODEL_DEFINITIONS})

create_webscripts_copy_parameter_faker = JSF(
    create_webscripts_copy_parameter_model_schema, allow_none_optionals=1
)


class CreateWebscriptsCopyParameterStub:
    """CreateWebscriptsCopyParameter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return create_webscripts_copy_parameter_faker.generate()

    @classmethod
    def create_instance(cls) -> "CreateWebscriptsCopyParameter":
        """Create CreateWebscriptsCopyParameter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return CreateWebscriptsCopyParameterAdapter.validate_python(cls.create_json())