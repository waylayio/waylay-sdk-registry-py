"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.any_job_status_summary_deploy import (
        AnyJobStatusSummaryDeploy,
    )

    AnyJobStatusSummaryDeployAdapter = TypeAdapter(AnyJobStatusSummaryDeploy)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

any_job_status_summary_deploy_model_schema = json.loads(
    r"""{
  "title" : "AnyJobStatusSummaryDeploy",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "deploy" ]
}
""",
    object_hook=with_example_provider,
)
any_job_status_summary_deploy_model_schema.update({"definitions": MODEL_DEFINITIONS})

any_job_status_summary_deploy_faker = JSF(
    any_job_status_summary_deploy_model_schema, allow_none_optionals=1
)


class AnyJobStatusSummaryDeployStub:
    """AnyJobStatusSummaryDeploy unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return any_job_status_summary_deploy_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AnyJobStatusSummaryDeploy":
        """Create AnyJobStatusSummaryDeploy stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AnyJobStatusSummaryDeployAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AnyJobStatusSummaryDeployAdapter.validate_python(
            json, context={"skip_validation": True}
        )
