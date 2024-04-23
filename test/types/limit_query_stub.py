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
    from waylay.services.registry.models.limit_query import LimitQuery

    LimitQueryAdapter = TypeAdapter(LimitQuery)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

limit_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
limit_query_model_schema.update({"definitions": MODEL_DEFINITIONS})

limit_query_faker = JSF(limit_query_model_schema, allow_none_optionals=1)


class LimitQueryStub:
    """LimitQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return limit_query_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "LimitQuery":
        """Create LimitQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(LimitQueryAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return LimitQueryAdapter.validate_python(
            json, context={"skip_validation": True}
        )
