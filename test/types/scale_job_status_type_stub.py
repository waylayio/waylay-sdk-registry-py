"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.scale_job_status_type import ScaleJobStatusType

    ScaleJobStatusTypeAdapter = TypeAdapter(ScaleJobStatusType)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

scale_job_status_type_model_schema = json.loads(
    r"""{
  "title" : "ScaleJobStatus_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "scale" ]
}
""",
    object_hook=with_example_provider,
)
scale_job_status_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

scale_job_status_type_faker = JSF(
    scale_job_status_type_model_schema, allow_none_optionals=1
)


class ScaleJobStatusTypeStub:
    """ScaleJobStatusType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return scale_job_status_type_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ScaleJobStatusType":
        """Create ScaleJobStatusType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ScaleJobStatusTypeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ScaleJobStatusTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
