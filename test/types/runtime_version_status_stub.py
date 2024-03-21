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
    from waylay.services.registry.models.runtime_version_status import (
        RuntimeVersionStatus,
    )

    RuntimeVersionStatusAdapter = TypeAdapter(RuntimeVersionStatus)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

runtime_version_status_model_schema = json.loads(
    r"""{
  "required" : [ "deprecated", "upgradable" ],
  "type" : "object",
  "properties" : {
    "deprecated" : {
      "type" : "boolean",
      "description" : "If true, the function uses a deprecated runtime."
    },
    "upgradable" : {
      "type" : "boolean",
      "description" : "If true, a newer runtime for this function is available using the `rebuild` API."
    }
  }
}
""",
    object_hook=with_example_provider,
)
runtime_version_status_model_schema.update({"definitions": MODEL_DEFINITIONS})

runtime_version_status_faker = JSF(
    runtime_version_status_model_schema, allow_none_optionals=1
)


class RuntimeVersionStatusStub:
    """RuntimeVersionStatus unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return runtime_version_status_faker.generate()

    @classmethod
    def create_instance(cls) -> "RuntimeVersionStatus":
        """Create RuntimeVersionStatus stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return RuntimeVersionStatusAdapter.validate_python(cls.create_json())
