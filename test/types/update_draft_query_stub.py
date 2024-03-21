# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.update_draft_query import UpdateDraftQuery

    UpdateDraftQueryAdapter = TypeAdapter(UpdateDraftQuery)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

update_draft_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "chown" : {
      "type" : "boolean",
      "description" : "If set, ownership of the draft function is transferred to the current user.",
      "default" : false
    },
    "comment" : {
      "type" : "string",
      "description" : "An optional user-specified comment corresponding to the operation."
    },
    "author" : {
      "type" : "string",
      "description" : "Optionally changes the author metadata when updating a function."
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
update_draft_query_model_schema.update({"definitions": MODEL_DEFINITIONS})

update_draft_query_faker = JSF(update_draft_query_model_schema, allow_none_optionals=1)


class UpdateDraftQueryStub:
    """UpdateDraftQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return update_draft_query_faker.generate()

    @classmethod
    def create_instance(cls) -> "UpdateDraftQuery":
        """Create UpdateDraftQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return UpdateDraftQueryAdapter.validate_python(cls.create_json())
