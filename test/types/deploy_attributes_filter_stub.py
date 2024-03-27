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
    from waylay.services.registry.models.deploy_attributes_filter import (
        DeployAttributesFilter,
    )

    DeployAttributesFilterAdapter = TypeAdapter(DeployAttributesFilter)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

deploy_attributes_filter_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "endpoint" : {
      "type" : "string",
      "description" : "Filter on the openfaas endpoint. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "imageName" : {
      "type" : "string",
      "description" : "Filter on the container image name. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "storageLocation" : {
      "type" : "string",
      "description" : "Filter on the storageLocation. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
deploy_attributes_filter_model_schema.update({"definitions": MODEL_DEFINITIONS})

deploy_attributes_filter_faker = JSF(
    deploy_attributes_filter_model_schema, allow_none_optionals=1
)


class DeployAttributesFilterStub:
    """DeployAttributesFilter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return deploy_attributes_filter_faker.generate()

    @classmethod
    def create_instance(cls) -> "DeployAttributesFilter":
        """Create DeployAttributesFilter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return DeployAttributesFilterAdapter.validate_python(cls.create_json())