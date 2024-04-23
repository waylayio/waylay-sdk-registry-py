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
    from waylay.services.registry.models.openfaas_function_ref import (
        OpenfaasFunctionRef,
    )

    OpenfaasFunctionRefAdapter = TypeAdapter(OpenfaasFunctionRef)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

openfaas_function_ref_model_schema = json.loads(
    r"""{
  "required" : [ "endpoint", "namespace" ],
  "type" : "object",
  "properties" : {
    "namespace" : {
      "type" : "string",
      "description" : "The (openfaas) namespace for the target function."
    },
    "endpoint" : {
      "type" : "string",
      "description" : "The (openfaas) endpoint service name"
    }
  }
}
""",
    object_hook=with_example_provider,
)
openfaas_function_ref_model_schema.update({"definitions": MODEL_DEFINITIONS})

openfaas_function_ref_faker = JSF(
    openfaas_function_ref_model_schema, allow_none_optionals=1
)


class OpenfaasFunctionRefStub:
    """OpenfaasFunctionRef unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return openfaas_function_ref_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "OpenfaasFunctionRef":
        """Create OpenfaasFunctionRef stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                OpenfaasFunctionRefAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return OpenfaasFunctionRefAdapter.validate_python(
            json, context={"skip_validation": True}
        )
