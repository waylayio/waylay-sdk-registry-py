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
    from waylay.services.registry.models.async_query_default_false import (
        AsyncQueryDefaultFalse,
    )

    AsyncQueryDefaultFalseAdapter = TypeAdapter(AsyncQueryDefaultFalse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

async_query_default_false_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "async" : {
      "type" : "boolean",
      "description" : "If this is set to <code>true</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. Otherwise, the request will block until the job actions are completed, or a timeout occurs.",
      "default" : false
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
async_query_default_false_model_schema.update({"definitions": MODEL_DEFINITIONS})

async_query_default_false_faker = JSF(
    async_query_default_false_model_schema, allow_none_optionals=1
)


class AsyncQueryDefaultFalseStub:
    """AsyncQueryDefaultFalse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return async_query_default_false_faker.generate()

    @classmethod
    def create_instance(cls) -> "AsyncQueryDefaultFalse":
        """Create AsyncQueryDefaultFalse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return AsyncQueryDefaultFalseAdapter.validate_python(cls.create_json())
