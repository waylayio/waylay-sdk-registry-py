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
    from waylay.services.registry.models.request_operation import RequestOperation

    RequestOperationAdapter = TypeAdapter(RequestOperation)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

request_operation_model_schema = json.loads(
    r"""{
  "title" : "RequestOperation",
  "type" : "string",
  "description" : "A modifying operation on the function.",
  "enum" : [ "create", "metadata-update", "assets-update", "rebuild", "verify", "publish", "deprecate", "undeploy" ]
}
""",
    object_hook=with_example_provider,
)
request_operation_model_schema.update({"definitions": MODEL_DEFINITIONS})

request_operation_faker = JSF(request_operation_model_schema, allow_none_optionals=1)


class RequestOperationStub:
    """RequestOperation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return request_operation_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "RequestOperation":
        """Create RequestOperation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                RequestOperationAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return RequestOperationAdapter.validate_python(
            json, context={"skip_validation": True}
        )
