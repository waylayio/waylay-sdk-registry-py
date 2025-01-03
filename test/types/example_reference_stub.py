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
    from waylay.services.registry.models.example_reference import ExampleReference

    ExampleReferenceAdapter = TypeAdapter(ExampleReference)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

example_reference_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Example reference.\n\nReferences the example assets from the selected runtime.",
  "enum" : [ "!example" ]
}
""",
    object_hook=with_example_provider,
)
example_reference_model_schema.update({"definitions": MODEL_DEFINITIONS})

example_reference_faker = JSF(example_reference_model_schema, allow_none_optionals=1)


class ExampleReferenceStub:
    """ExampleReference unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return example_reference_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ExampleReference":
        """Create ExampleReference stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExampleReferenceAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExampleReferenceAdapter.validate_python(
            json, context={"skip_validation": True}
        )
