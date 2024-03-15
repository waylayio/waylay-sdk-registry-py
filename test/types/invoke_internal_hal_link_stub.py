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
    from waylay.services.registry.models.invoke_internal_hal_link import (
        InvokeInternalHALLink,
    )

    InvokeInternalHALLinkAdapter = TypeAdapter(InvokeInternalHALLink)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

invoke_internal_hal_link_model_schema = json.loads(r"""{
  "title" : "InvokeInternalHALLink",
  "type" : "object",
  "properties" : {
    "invoke-internal" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""")
invoke_internal_hal_link_model_schema.update({"definitions": MODEL_DEFINITIONS})

invoke_internal_hal_link_faker = JSF(
    invoke_internal_hal_link_model_schema, allow_none_optionals=1
)


class InvokeInternalHALLinkStub:
    """InvokeInternalHALLink unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return invoke_internal_hal_link_faker.generate()

    @classmethod
    def create_instance(cls) -> "InvokeInternalHALLink":
        """Create InvokeInternalHALLink stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return InvokeInternalHALLinkAdapter.validate_python(cls.create_json())
