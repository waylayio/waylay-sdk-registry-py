# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.tags_filter import TagsFilter

    TagsFilterAdapter = TypeAdapter(TagsFilter)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

tags_filter_model_schema = json.loads(r"""{
  "title" : "TagsFilter",
  "anyOf" : [ {
    "type" : "array",
    "items" : {
      "type" : "string"
    }
  }, {
    "type" : "string"
  } ]
}
""")
tags_filter_model_schema.update({"definitions": MODEL_DEFINITIONS})

tags_filter_faker = JSF(tags_filter_model_schema, allow_none_optionals=1)


class TagsFilterStub:
    """TagsFilter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return tags_filter_faker.generate()

    @classmethod
    def create_instance(cls) -> "TagsFilter":
        """Create TagsFilter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return TagsFilterAdapter.validate_python(cls.create_json())
