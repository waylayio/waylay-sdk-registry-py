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
    from waylay.services.registry.models.schema_by_id_params import SchemaByIdParams

    SchemaByIdParamsAdapter = TypeAdapter(SchemaByIdParams)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

schema_by_id_params_model_schema = json.loads(
    r"""{
  "required" : [ "schemaId" ],
  "type" : "object",
  "properties" : {
    "schemaId" : {
      "type" : "string",
      "description" : "Schema id"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
schema_by_id_params_model_schema.update({"definitions": MODEL_DEFINITIONS})

schema_by_id_params_faker = JSF(
    schema_by_id_params_model_schema, allow_none_optionals=1
)


class SchemaByIdParamsStub:
    """SchemaByIdParams unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return schema_by_id_params_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "SchemaByIdParams":
        """Create SchemaByIdParams stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SchemaByIdParamsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SchemaByIdParamsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
