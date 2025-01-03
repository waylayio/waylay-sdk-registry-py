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
    from waylay.services.registry.models.notify_result import NotifyResult

    NotifyResultAdapter = TypeAdapter(NotifyResult)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

notify_result_model_schema = json.loads(
    r"""{
  "title" : "NotifyResult",
  "required" : [ "operation" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "$ref" : "#/components/schemas/RequestOperation"
    }
  },
  "description" : "The result data for a change notification."
}
""",
    object_hook=with_example_provider,
)
notify_result_model_schema.update({"definitions": MODEL_DEFINITIONS})

notify_result_faker = JSF(notify_result_model_schema, allow_none_optionals=1)


class NotifyResultStub:
    """NotifyResult unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return notify_result_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "NotifyResult":
        """Create NotifyResult stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                NotifyResultAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return NotifyResultAdapter.validate_python(
            json, context={"skip_validation": True}
        )
