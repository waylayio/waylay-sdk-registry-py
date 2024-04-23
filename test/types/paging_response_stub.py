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
    from waylay.services.registry.models.paging_response import PagingResponse

    PagingResponseAdapter = TypeAdapter(PagingResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

paging_response_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "count" : {
      "type" : "number",
      "description" : "The total count of matching items, from which this result is one page."
    },
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "page" : {
      "type" : "number",
      "description" : "The page number of a paged query result."
    }
  }
}
""",
    object_hook=with_example_provider,
)
paging_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

paging_response_faker = JSF(paging_response_model_schema, allow_none_optionals=1)


class PagingResponseStub:
    """PagingResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return paging_response_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "PagingResponse":
        """Create PagingResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                PagingResponseAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PagingResponseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
