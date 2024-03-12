# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import warnings

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.runtime_version_response import (
        RuntimeVersionResponse,
    )

    RuntimeVersionResponseAdapter = TypeAdapter(RuntimeVersionResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for RuntimeVersionResponse not available: {exc}")
    MODELS_AVAILABLE = False

runtime_version_response_model_schema = json.loads(r"""{
  "required" : [ "runtime" ],
  "type" : "object",
  "properties" : {
    "runtime" : {
      "$ref" : "#/components/schemas/CompiledRuntimeVersion"
    }
  },
  "description" : ": Runtime Version Found"
}
""")
runtime_version_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

runtime_version_response_faker = JSF(
    runtime_version_response_model_schema, allow_none_optionals=1
)


class RuntimeVersionResponseStub:
    """RuntimeVersionResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return runtime_version_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "RuntimeVersionResponse":
        """Create RuntimeVersionResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return RuntimeVersionResponseAdapter.validate_python(cls.create_json())
