"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.verify_job_status_type import (
        VerifyJobStatusType,
    )

    VerifyJobStatusTypeAdapter = TypeAdapter(VerifyJobStatusType)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

verify_job_status_type_model_schema = json.loads(
    r"""{
  "title" : "VerifyJobStatus_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "verify" ]
}
""",
    object_hook=with_example_provider,
)
verify_job_status_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

verify_job_status_type_faker = JSF(
    verify_job_status_type_model_schema, allow_none_optionals=1
)


class VerifyJobStatusTypeStub:
    """VerifyJobStatusType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return verify_job_status_type_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "VerifyJobStatusType":
        """Create VerifyJobStatusType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                VerifyJobStatusTypeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return VerifyJobStatusTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
