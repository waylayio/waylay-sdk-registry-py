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
    from waylay.services.registry.models.deploy_type import DeployType

    DeployTypeAdapter = TypeAdapter(DeployType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

deploy_type_model_schema = json.loads(
    r"""{
  "title" : "Deploy_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "deploy" ]
}
""",
    object_hook=with_example_provider,
)
deploy_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

deploy_type_faker = JSF(deploy_type_model_schema, allow_none_optionals=1)


class DeployTypeStub:
    """DeployType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return deploy_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "DeployType":
        """Create DeployType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return DeployTypeAdapter.validate_python(cls.create_json())