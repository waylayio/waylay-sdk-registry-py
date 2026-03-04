"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.any_job_for_function_verify import (
        AnyJobForFunctionVerify,
    )

    AnyJobForFunctionVerifyAdapter = TypeAdapter(AnyJobForFunctionVerify)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

any_job_for_function_verify_model_schema = json.loads(
    r"""{
  "title" : "AnyJobForFunctionVerify",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "verify" ]
}
""",
    object_hook=with_example_provider,
)
any_job_for_function_verify_model_schema.update({"definitions": MODEL_DEFINITIONS})

any_job_for_function_verify_faker = JSF(
    any_job_for_function_verify_model_schema, allow_none_optionals=1
)


class AnyJobForFunctionVerifyStub:
    """AnyJobForFunctionVerify unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return any_job_for_function_verify_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AnyJobForFunctionVerify":
        """Create AnyJobForFunctionVerify stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AnyJobForFunctionVerifyAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AnyJobForFunctionVerifyAdapter.validate_python(
            json, context={"skip_validation": True}
        )
