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
    from waylay.services.registry.models.invoke_hal_link import InvokeHALLink

    InvokeHALLinkAdapter = TypeAdapter(InvokeHALLink)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for InvokeHALLink not available: {exc}")
    MODELS_AVAILABLE = False

invoke_hal_link_model_schema = json.loads(r"""{
  "title" : "InvokeHALLink",
  "type" : "object",
  "properties" : {
    "invoke" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""")
invoke_hal_link_model_schema.update({"definitions": MODEL_DEFINITIONS})

invoke_hal_link_faker = JSF(invoke_hal_link_model_schema, allow_none_optionals=1)


class InvokeHALLinkStub:
    """InvokeHALLink unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return invoke_hal_link_faker.generate()

    @classmethod
    def create_instance(cls) -> "InvokeHALLink":
        """Create InvokeHALLink stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return InvokeHALLinkAdapter.validate_python(cls.create_json())
