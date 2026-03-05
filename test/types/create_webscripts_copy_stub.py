"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.create_webscripts_copy import (
        CreateWebscriptsCopy,
    )

    CreateWebscriptsCopyAdapter = TypeAdapter(CreateWebscriptsCopy)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

create_webscripts_copy_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/NamedVersionRange"
  }, {
    "$ref" : "#/components/schemas/ExampleReference"
  } ]
}
""",
    object_hook=with_example_provider,
)
create_webscripts_copy_model_schema.update({"definitions": MODEL_DEFINITIONS})

create_webscripts_copy_faker = JSF(
    create_webscripts_copy_model_schema, allow_none_optionals=1
)


class CreateWebscriptsCopyStub:
    """CreateWebscriptsCopy unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return create_webscripts_copy_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "CreateWebscriptsCopy":
        """Create CreateWebscriptsCopy stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                CreateWebscriptsCopyAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return CreateWebscriptsCopyAdapter.validate_python(
            json, context={"skip_validation": True}
        )
