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
    from waylay.services.registry.models.supported_events import SupportedEvents

    SupportedEventsAdapter = TypeAdapter(SupportedEvents)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

supported_events_model_schema = json.loads(
    r"""{
  "title" : "SupportedEvents",
  "type" : "string",
  "enum" : [ "completed", "failed", "active", "delayed", "waiting", "waiting-children" ]
}
""",
    object_hook=with_example_provider,
)
supported_events_model_schema.update({"definitions": MODEL_DEFINITIONS})

supported_events_faker = JSF(supported_events_model_schema, allow_none_optionals=1)


class SupportedEventsStub:
    """SupportedEvents unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return supported_events_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "SupportedEvents":
        """Create SupportedEvents stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SupportedEventsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SupportedEventsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
