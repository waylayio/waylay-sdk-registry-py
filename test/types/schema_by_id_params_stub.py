# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import warnings

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.schema_by_id_params import SchemaByIdParams

    SchemaByIdParamsAdapter = TypeAdapter(SchemaByIdParams)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for SchemaByIdParams not available: {exc}")
    MODELS_AVAILABLE = False

schema_by_id_params_model_schema = json.loads(r"""{
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
""")
schema_by_id_params_model_schema.update({"definitions": MODEL_DEFINITIONS})

schema_by_id_params_faker = JSF(
    schema_by_id_params_model_schema, allow_none_optionals=1
)


class SchemaByIdParamsStub:
    """SchemaByIdParams unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return schema_by_id_params_faker.generate()

    @classmethod
    def create_instance(cls) -> "SchemaByIdParams":
        """Create SchemaByIdParams stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return SchemaByIdParamsAdapter.validate_python(cls.create_json())
