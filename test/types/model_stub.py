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
    from waylay.services.registry.models.model import Model

    ModelAdapter = TypeAdapter(Model)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

model_model_schema = json.loads(
    r"""{
  "title" : "Model",
  "required" : [ "model" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "model" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
model_model_schema.update({"definitions": MODEL_DEFINITIONS})

model_faker = JSF(model_model_schema, allow_none_optionals=1)


class ModelStub:
    """Model unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return model_faker.generate()

    @classmethod
    def create_instance(cls) -> "Model":
        """Create Model stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ModelAdapter.validate_python(cls.create_json())
