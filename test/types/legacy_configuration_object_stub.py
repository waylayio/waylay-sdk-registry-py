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
    from waylay.services.registry.models.legacy_configuration_object import (
        LegacyConfigurationObject,
    )

    LegacyConfigurationObjectAdapter = TypeAdapter(LegacyConfigurationObject)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

legacy_configuration_object_model_schema = json.loads(
    r"""{
  "title" : "LegacyConfigurationObject",
  "required" : [ "name", "type" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string"
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugPropertyDataType"
    },
    "mandatory" : {
      "title" : "mandatory",
      "type" : "boolean"
    },
    "format" : {
      "$ref" : "#/components/schemas/LegacyConfigurationObject_format"
    },
    "defaultValue" : {
      "$ref" : "#/components/schemas/DefaultValue"
    }
  }
}
""",
    object_hook=with_example_provider,
)
legacy_configuration_object_model_schema.update({"definitions": MODEL_DEFINITIONS})

legacy_configuration_object_faker = JSF(
    legacy_configuration_object_model_schema, allow_none_optionals=1
)


class LegacyConfigurationObjectStub:
    """LegacyConfigurationObject unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_configuration_object_faker.generate()

    @classmethod
    def create_instance(cls) -> "LegacyConfigurationObject":
        """Create LegacyConfigurationObject stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LegacyConfigurationObjectAdapter.validate_python(cls.create_json())
