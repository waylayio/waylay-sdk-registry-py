# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.function_type import FunctionType

    FunctionTypeAdapter = TypeAdapter(FunctionType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

function_type_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Type of functions supported by the registry service.",
  "enum" : [ "plugs", "webscripts", "kfserving" ]
}
""",
    object_hook=with_example_provider,
)
function_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

function_type_faker = JSF(function_type_model_schema, allow_none_optionals=1)


class FunctionTypeStub:
    """FunctionType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return function_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "FunctionType":
        """Create FunctionType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return FunctionTypeAdapter.validate_python(cls.create_json())
