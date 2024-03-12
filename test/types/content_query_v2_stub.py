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
    from waylay.services.registry.models.content_query_v2 import ContentQueryV2

    ContentQueryV2Adapter = TypeAdapter(ContentQueryV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(f"Type adapter for ContentQueryV2 not available: {exc}")
    MODELS_AVAILABLE = False

content_query_v2_model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "ls" : {
      "type" : "boolean",
      "description" : "If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime.",
      "default" : false
    }
  },
  "additionalProperties" : false
}
""")
content_query_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

content_query_v2_faker = JSF(content_query_v2_model_schema, allow_none_optionals=1)


class ContentQueryV2Stub:
    """ContentQueryV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return content_query_v2_faker.generate()

    @classmethod
    def create_instance(cls) -> "ContentQueryV2":
        """Create ContentQueryV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ContentQueryV2Adapter.validate_python(cls.create_json())
