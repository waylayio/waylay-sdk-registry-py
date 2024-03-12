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
    from waylay.services.registry.models.force_delete_query_v1 import ForceDeleteQueryV1

    ForceDeleteQueryV1Adapter = TypeAdapter(ForceDeleteQueryV1)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for ForceDeleteQueryV1 not available: {exc}")
    MODELS_AVAILABLE = False

force_delete_query_v1_model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "async" : {
      "type" : "boolean",
      "description" : "If this is set to <code>true</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. Otherwise, the request will block until the job actions are completed, or a timeout occurs.",
      "default" : false
    },
    "force" : {
      "type" : "boolean",
      "description" : "If <code>true</code>, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be <code>deprecated</code>, i.e removed from regular listings."
    }
  },
  "additionalProperties" : false
}
""")
force_delete_query_v1_model_schema.update({"definitions": MODEL_DEFINITIONS})

force_delete_query_v1_faker = JSF(
    force_delete_query_v1_model_schema, allow_none_optionals=1
)


class ForceDeleteQueryV1Stub:
    """ForceDeleteQueryV1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return force_delete_query_v1_faker.generate()

    @classmethod
    def create_instance(cls) -> "ForceDeleteQueryV1":
        """Create ForceDeleteQueryV1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ForceDeleteQueryV1Adapter.validate_python(cls.create_json())
