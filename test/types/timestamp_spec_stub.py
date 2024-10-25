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
    from waylay.services.registry.models.timestamp_spec import TimestampSpec

    TimestampSpecAdapter = TypeAdapter(TimestampSpec)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

timestamp_spec_model_schema = json.loads(
    r"""{
  "description" : "A timestamp specification.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/TimestampAge"
  }, {
    "$ref" : "#/components/schemas/TimestampAbsolute"
  } ]
}
""",
    object_hook=with_example_provider,
)
timestamp_spec_model_schema.update({"definitions": MODEL_DEFINITIONS})

timestamp_spec_faker = JSF(timestamp_spec_model_schema, allow_none_optionals=1)


class TimestampSpecStub:
    """TimestampSpec unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return timestamp_spec_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "TimestampSpec":
        """Create TimestampSpec stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TimestampSpecAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TimestampSpecAdapter.validate_python(
            json, context={"skip_validation": True}
        )
