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
    from waylay.services.registry.models.unhealthy_invokable_webscript_error import (
        UnhealthyInvokableWebscriptError,
    )

    UnhealthyInvokableWebscriptErrorAdapter = TypeAdapter(
        UnhealthyInvokableWebscriptError
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

unhealthy_invokable_webscript_error_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "code", "entity", "error" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/InvokableWebscriptResponse_entity"
    },
    "_links" : {
      "$ref" : "#/components/schemas/InvokeInternalHALLink"
    },
    "error" : {
      "type" : "string"
    },
    "code" : {
      "type" : "string"
    }
  },
  "description" : "Webscript Not Healthy"
}
""",
    object_hook=with_example_provider,
)
unhealthy_invokable_webscript_error_model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

unhealthy_invokable_webscript_error_faker = JSF(
    unhealthy_invokable_webscript_error_model_schema, allow_none_optionals=1
)


class UnhealthyInvokableWebscriptErrorStub:
    """UnhealthyInvokableWebscriptError unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return unhealthy_invokable_webscript_error_faker.generate()

    @classmethod
    def create_instance(cls) -> "UnhealthyInvokableWebscriptError":
        """Create UnhealthyInvokableWebscriptError stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return UnhealthyInvokableWebscriptErrorAdapter.validate_python(
            cls.create_json()
        )
