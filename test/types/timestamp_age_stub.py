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
    from waylay.services.registry.models.timestamp_age import TimestampAge

    TimestampAgeAdapter = TypeAdapter(TimestampAge)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

timestamp_age_model_schema = json.loads(
    r"""{
  "title" : "TimestampAge",
  "description" : "A timestamp expressed as a age relative to now",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/SO8601Period"
  }, {
    "$ref" : "#/components/schemas/DurationSpec"
  } ]
}
""",
    object_hook=with_example_provider,
)
timestamp_age_model_schema.update({"definitions": MODEL_DEFINITIONS})

timestamp_age_faker = JSF(timestamp_age_model_schema, allow_none_optionals=1)


class TimestampAgeStub:
    """TimestampAge unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return timestamp_age_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "TimestampAge":
        """Create TimestampAge stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TimestampAgeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TimestampAgeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
