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
    from waylay.services.registry.models.show_inline_or_embedding_any_of import (
        ShowInlineOrEmbeddingAnyOf,
    )

    ShowInlineOrEmbeddingAnyOfAdapter = TypeAdapter(ShowInlineOrEmbeddingAnyOf)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

show_inline_or_embedding_any_of_model_schema = json.loads(
    r"""{
  "title" : "ShowInlineOrEmbedding_anyOf",
  "type" : "string",
  "enum" : [ "inline" ]
}
""",
    object_hook=with_example_provider,
)
show_inline_or_embedding_any_of_model_schema.update({"definitions": MODEL_DEFINITIONS})

show_inline_or_embedding_any_of_faker = JSF(
    show_inline_or_embedding_any_of_model_schema, allow_none_optionals=1
)


class ShowInlineOrEmbeddingAnyOfStub:
    """ShowInlineOrEmbeddingAnyOf unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return show_inline_or_embedding_any_of_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ShowInlineOrEmbeddingAnyOf":
        """Create ShowInlineOrEmbeddingAnyOf stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ShowInlineOrEmbeddingAnyOfAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ShowInlineOrEmbeddingAnyOfAdapter.validate_python(
            json, context={"skip_validation": True}
        )
