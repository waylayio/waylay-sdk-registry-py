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
    from waylay.services.registry.models.kf_serving_models_response import (
        KFServingModelsResponse,
    )

    KFServingModelsResponseAdapter = TypeAdapter(KFServingModelsResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for KFServingModelsResponse not available: {exc}")
    MODELS_AVAILABLE = False

kf_serving_models_response_model_schema = json.loads(r"""{
  "required" : [ "models" ],
  "type" : "object",
  "properties" : {
    "models" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/KFServingResponse"
      }
    },
    "paging" : {
      "$ref" : "#/components/schemas/PagingResponse"
    }
  },
  "description" : "Successful Response"
}
""")
kf_serving_models_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

kf_serving_models_response_faker = JSF(
    kf_serving_models_response_model_schema, allow_none_optionals=1
)


class KFServingModelsResponseStub:
    """KFServingModelsResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return kf_serving_models_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "KFServingModelsResponse":
        """Create KFServingModelsResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return KFServingModelsResponseAdapter.validate_python(cls.create_json())
