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
    from waylay.services.registry.models.legacy_plug_request_metadata_raw_data_inner import (
        LegacyPlugRequestMetadataRawDataInner,
    )

    LegacyPlugRequestMetadataRawDataInnerAdapter = TypeAdapter(
        LegacyPlugRequestMetadataRawDataInner
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

legacy_plug_request_metadata_raw_data_inner_model_schema = json.loads(r"""{
  "title" : "LegacyPlugRequest_metadata_rawData_inner",
  "required" : [ "parameter" ],
  "type" : "object",
  "properties" : {
    "parameter" : {
      "title" : "parameter",
      "type" : "string"
    },
    "dataType" : {
      "$ref" : "#/components/schemas/PlugPropertyDataType"
    }
  },
  "additionalProperties" : false
}
""")
legacy_plug_request_metadata_raw_data_inner_model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

legacy_plug_request_metadata_raw_data_inner_faker = JSF(
    legacy_plug_request_metadata_raw_data_inner_model_schema, allow_none_optionals=1
)


class LegacyPlugRequestMetadataRawDataInnerStub:
    """LegacyPlugRequestMetadataRawDataInner unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_plug_request_metadata_raw_data_inner_faker.generate()

    @classmethod
    def create_instance(cls) -> "LegacyPlugRequestMetadataRawDataInner":
        """Create LegacyPlugRequestMetadataRawDataInner stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LegacyPlugRequestMetadataRawDataInnerAdapter.validate_python(
            cls.create_json()
        )
