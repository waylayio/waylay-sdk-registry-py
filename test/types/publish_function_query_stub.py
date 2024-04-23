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
    from waylay.services.registry.models.publish_function_query import (
        PublishFunctionQuery,
    )

    PublishFunctionQueryAdapter = TypeAdapter(PublishFunctionQuery)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

publish_function_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "comment" : {
      "type" : "string",
      "description" : "An optional user-specified comment corresponding to the operation."
    },
    "deprecatePrevious" : {
      "$ref" : "#/components/schemas/DeprecatePreviousPolicy"
    },
    "async" : {
      "type" : "boolean",
      "description" : "Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
      "default" : true
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
publish_function_query_model_schema.update({"definitions": MODEL_DEFINITIONS})

publish_function_query_faker = JSF(
    publish_function_query_model_schema, allow_none_optionals=1
)


class PublishFunctionQueryStub:
    """PublishFunctionQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return publish_function_query_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "PublishFunctionQuery":
        """Create PublishFunctionQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                PublishFunctionQueryAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PublishFunctionQueryAdapter.validate_python(
            json, context={"skip_validation": True}
        )
