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
    from waylay.services.registry.models.legacy_plug_script_meta_raw_data_inner import (
        LegacyPlugScriptMetaRawDataInner,
    )

    LegacyPlugScriptMetaRawDataInnerAdapter = TypeAdapter(
        LegacyPlugScriptMetaRawDataInner
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

legacy_plug_script_meta_raw_data_inner_model_schema = json.loads(
    r"""{
  "title" : "LegacyPlugScriptMeta_rawData_inner",
  "required" : [ "parameter" ],
  "type" : "object",
  "properties" : {
    "parameter" : {
      "title" : "parameter",
      "type" : "string"
    },
    "dataType" : {
      "title" : "dataType",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
legacy_plug_script_meta_raw_data_inner_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

legacy_plug_script_meta_raw_data_inner_faker = JSF(
    legacy_plug_script_meta_raw_data_inner_model_schema, allow_none_optionals=1
)


class LegacyPlugScriptMetaRawDataInnerStub:
    """LegacyPlugScriptMetaRawDataInner unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return legacy_plug_script_meta_raw_data_inner_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "LegacyPlugScriptMetaRawDataInner":
        """Create LegacyPlugScriptMetaRawDataInner stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                LegacyPlugScriptMetaRawDataInnerAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return LegacyPlugScriptMetaRawDataInnerAdapter.validate_python(
            json, context={"skip_validation": True}
        )
