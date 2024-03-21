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
    from waylay.services.registry.models.rebuild_computed_response import (
        RebuildComputedResponse,
    )

    RebuildComputedResponseAdapter = TypeAdapter(RebuildComputedResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

rebuild_computed_response_model_schema = json.loads(
    r"""{
  "required" : [ "causes", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "causes" : {
      "$ref" : "#/components/schemas/JobCauses"
    }
  },
  "description" : "Rebuild Ignored"
}
""",
    object_hook=with_example_provider,
)
rebuild_computed_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

rebuild_computed_response_faker = JSF(
    rebuild_computed_response_model_schema, allow_none_optionals=1
)


class RebuildComputedResponseStub:
    """RebuildComputedResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return rebuild_computed_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "RebuildComputedResponse":
        """Create RebuildComputedResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return RebuildComputedResponseAdapter.validate_python(cls.create_json())
