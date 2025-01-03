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
    from waylay.services.registry.models.status_exclude import StatusExclude

    StatusExcludeAdapter = TypeAdapter(StatusExclude)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

status_exclude_model_schema = json.loads(
    r"""{
  "title" : "StatusExclude",
  "pattern" : "^(registered|pending|deployed|unhealthy|failed|running|undeploying|undeployed)-$",
  "type" : "string",
  "description" : "Any status value with a `-` postfix appended, excludes that status as a filter.",
  "example" : "running-",
  "enum" : [ "registered-", "running-", "pending-", "deployed-", "unhealthy-", "failed-", "undeploying-", "undeployed-" ]
}
""",
    object_hook=with_example_provider,
)
status_exclude_model_schema.update({"definitions": MODEL_DEFINITIONS})

status_exclude_faker = JSF(status_exclude_model_schema, allow_none_optionals=1)


class StatusExcludeStub:
    """StatusExclude unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return status_exclude_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "StatusExclude":
        """Create StatusExclude stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                StatusExcludeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return StatusExcludeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
