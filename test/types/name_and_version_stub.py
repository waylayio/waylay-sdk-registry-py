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
    from waylay.services.registry.models.name_and_version import NameAndVersion

    NameAndVersionAdapter = TypeAdapter(NameAndVersion)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

name_and_version_model_schema = json.loads(
    r"""{
  "required" : [ "name", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "The name of the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  }
}
""",
    object_hook=with_example_provider,
)
name_and_version_model_schema.update({"definitions": MODEL_DEFINITIONS})

name_and_version_faker = JSF(name_and_version_model_schema, allow_none_optionals=1)


class NameAndVersionStub:
    """NameAndVersion unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return name_and_version_faker.generate()

    @classmethod
    def create_instance(cls) -> "NameAndVersion":
        """Create NameAndVersion stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return NameAndVersionAdapter.validate_python(cls.create_json())
