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
    from waylay.services.registry.models.invokable_webscript_response_entity_webscript import (
        InvokableWebscriptResponseEntityWebscript,
    )

    InvokableWebscriptResponseEntityWebscriptAdapter = TypeAdapter(
        InvokableWebscriptResponseEntityWebscript
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

invokable_webscript_response_entity_webscript_model_schema = json.loads(
    r"""{
  "title" : "InvokableWebscriptResponse_entity_webscript",
  "required" : [ "allowHmac", "name", "private", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "private" : {
      "title" : "private",
      "type" : "boolean"
    },
    "allowHmac" : {
      "title" : "allowHmac",
      "type" : "boolean"
    }
  }
}
""",
    object_hook=with_example_provider,
)
invokable_webscript_response_entity_webscript_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

invokable_webscript_response_entity_webscript_faker = JSF(
    invokable_webscript_response_entity_webscript_model_schema, allow_none_optionals=1
)


class InvokableWebscriptResponseEntityWebscriptStub:
    """InvokableWebscriptResponseEntityWebscript unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return invokable_webscript_response_entity_webscript_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "InvokableWebscriptResponseEntityWebscript":
        """Create InvokableWebscriptResponseEntityWebscript stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                InvokableWebscriptResponseEntityWebscriptAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return InvokableWebscriptResponseEntityWebscriptAdapter.validate_python(
            json, context={"skip_validation": True}
        )
