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
    from waylay.services.registry.models.runtime_summary_attrs import (
        RuntimeSummaryAttrs,
    )

    RuntimeSummaryAttrsAdapter = TypeAdapter(RuntimeSummaryAttrs)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

runtime_summary_attrs_model_schema = json.loads(
    r"""{
  "required" : [ "archiveFormat", "functionType", "name", "title" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "title" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "functionType" : {
      "$ref" : "#/components/schemas/FunctionType"
    },
    "archiveFormat" : {
      "$ref" : "#/components/schemas/ArchiveFormat"
    }
  }
}
""",
    object_hook=with_example_provider,
)
runtime_summary_attrs_model_schema.update({"definitions": MODEL_DEFINITIONS})

runtime_summary_attrs_faker = JSF(
    runtime_summary_attrs_model_schema, allow_none_optionals=1
)


class RuntimeSummaryAttrsStub:
    """RuntimeSummaryAttrs unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return runtime_summary_attrs_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "RuntimeSummaryAttrs":
        """Create RuntimeSummaryAttrs stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                RuntimeSummaryAttrsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return RuntimeSummaryAttrsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
