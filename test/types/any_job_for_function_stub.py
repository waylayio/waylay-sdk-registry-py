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
    from waylay.services.registry.models.any_job_for_function import AnyJobForFunction

    AnyJobForFunctionAdapter = TypeAdapter(AnyJobForFunction)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

any_job_for_function_model_schema = json.loads(
    r"""{
  "title" : "AnyJobForFunction",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Build"
  }, {
    "$ref" : "#/components/schemas/Deploy"
  }, {
    "$ref" : "#/components/schemas/Verify"
  }, {
    "$ref" : "#/components/schemas/Undeploy"
  }, {
    "$ref" : "#/components/schemas/Scale"
  } ]
}
""",
    object_hook=with_example_provider,
)
any_job_for_function_model_schema.update({"definitions": MODEL_DEFINITIONS})

any_job_for_function_faker = JSF(
    any_job_for_function_model_schema, allow_none_optionals=1
)


class AnyJobForFunctionStub:
    """AnyJobForFunction unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return any_job_for_function_faker.generate()

    @classmethod
    def create_instance(cls) -> "AnyJobForFunction":
        """Create AnyJobForFunction stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return AnyJobForFunctionAdapter.validate_python(cls.create_json())
