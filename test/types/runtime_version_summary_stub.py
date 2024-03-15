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
    from waylay.services.registry.models.runtime_version_summary import (
        RuntimeVersionSummary,
    )

    RuntimeVersionSummaryAdapter = TypeAdapter(RuntimeVersionSummary)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

runtime_version_summary_model_schema = json.loads(r"""{
  "required" : [ "archiveFormat", "deprecated", "functionType", "name", "title", "upgradable", "version" ],
  "type" : "object",
  "properties" : {
    "deprecated" : {
      "type" : "boolean",
      "description" : "If true, the function uses a deprecated runtime."
    },
    "upgradable" : {
      "type" : "boolean",
      "description" : "If true, a newer runtime for this function is available using the `rebuild` API."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "title" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "name" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "functionType" : {
      "$ref" : "#/components/schemas/FunctionType"
    },
    "archiveFormat" : {
      "$ref" : "#/components/schemas/ArchiveFormat"
    }
  }
}
""")
runtime_version_summary_model_schema.update({"definitions": MODEL_DEFINITIONS})

runtime_version_summary_faker = JSF(
    runtime_version_summary_model_schema, allow_none_optionals=1
)


class RuntimeVersionSummaryStub:
    """RuntimeVersionSummary unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return runtime_version_summary_faker.generate()

    @classmethod
    def create_instance(cls) -> "RuntimeVersionSummary":
        """Create RuntimeVersionSummary stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return RuntimeVersionSummaryAdapter.validate_python(cls.create_json())
