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
    from waylay.services.registry.models.create_function_query_v2 import (
        CreateFunctionQueryV2,
    )

    CreateFunctionQueryV2Adapter = TypeAdapter(CreateFunctionQueryV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for CreateFunctionQueryV2 not available: {exc}")
    MODELS_AVAILABLE = False

create_function_query_v2_model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "deprecatePrevious" : {
      "$ref" : "#/components/schemas/DeprecatePreviousPolicy"
    },
    "dryRun" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, validates the deployment conditions, but does not change anything."
    },
    "async" : {
      "type" : "boolean",
      "description" : "Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
      "default" : true
    },
    "scaleToZero" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately.",
      "default" : false
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "name" : {
      "type" : "string",
      "description" : "If set, the value will be used as the function name instead of the one specified in the manifest."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "If set, the created function will be a draft function and its assets are still mutable. A build and deploy is initiated only in the case when all necessary assets are present and valid.",
      "default" : false
    }
  },
  "additionalProperties" : false
}
""")
create_function_query_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

create_function_query_v2_faker = JSF(
    create_function_query_v2_model_schema, allow_none_optionals=1
)


class CreateFunctionQueryV2Stub:
    """CreateFunctionQueryV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return create_function_query_v2_faker.generate()

    @classmethod
    def create_instance(cls) -> "CreateFunctionQueryV2":
        """Create CreateFunctionQueryV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return CreateFunctionQueryV2Adapter.validate_python(cls.create_json())
