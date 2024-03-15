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
    from waylay.services.registry.models.plug_property import PlugProperty

    PlugPropertyAdapter = TypeAdapter(PlugProperty)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

plug_property_model_schema = json.loads(r"""{
  "title" : "PlugProperty",
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "The name of a plug input or output property."
    },
    "dataType" : {
      "$ref" : "#/components/schemas/PlugPropertyDataType"
    },
    "mandatory" : {
      "title" : "mandatory",
      "type" : "boolean",
      "description" : "If <code>true</code> this property is required.",
      "example" : true
    },
    "format" : {
      "$ref" : "#/components/schemas/PlugPropertyFormat"
    },
    "defaultValue" : {
      "$ref" : "#/components/schemas/DefaultValue"
    }
  },
  "description" : "Interface specification of a plug property."
}
""")
plug_property_model_schema.update({"definitions": MODEL_DEFINITIONS})

plug_property_faker = JSF(plug_property_model_schema, allow_none_optionals=1)


class PlugPropertyStub:
    """PlugProperty unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return plug_property_faker.generate()

    @classmethod
    def create_instance(cls) -> "PlugProperty":
        """Create PlugProperty stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return PlugPropertyAdapter.validate_python(cls.create_json())
