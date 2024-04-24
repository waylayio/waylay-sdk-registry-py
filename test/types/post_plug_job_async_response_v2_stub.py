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
    from waylay.services.registry.models.post_plug_job_async_response_v2 import (
        PostPlugJobAsyncResponseV2,
    )

    PostPlugJobAsyncResponseV2Adapter = TypeAdapter(PostPlugJobAsyncResponseV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

post_plug_job_async_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "entity" : {
      "$ref" : "#/components/schemas/PlugResponseV2"
    }
  },
  "description" : "Plug Deployment Initiated"
}
""",
    object_hook=with_example_provider,
)
post_plug_job_async_response_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

post_plug_job_async_response_v2_faker = JSF(
    post_plug_job_async_response_v2_model_schema, allow_none_optionals=1
)


class PostPlugJobAsyncResponseV2Stub:
    """PostPlugJobAsyncResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return post_plug_job_async_response_v2_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "PostPlugJobAsyncResponseV2":
        """Create PostPlugJobAsyncResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                PostPlugJobAsyncResponseV2Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PostPlugJobAsyncResponseV2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
