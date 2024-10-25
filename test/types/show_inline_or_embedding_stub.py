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
    from waylay.services.registry.models.show_inline_or_embedding import (
        ShowInlineOrEmbedding,
    )

    ShowInlineOrEmbeddingAdapter = TypeAdapter(ShowInlineOrEmbedding)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

show_inline_or_embedding_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/ShowEmbedding"
  }, {
    "$ref" : "#/components/schemas/ShowInlineOrEmbedding_anyOf"
  } ]
}
""",
    object_hook=with_example_provider,
)
show_inline_or_embedding_model_schema.update({"definitions": MODEL_DEFINITIONS})

show_inline_or_embedding_faker = JSF(
    show_inline_or_embedding_model_schema, allow_none_optionals=1
)


class ShowInlineOrEmbeddingStub:
    """ShowInlineOrEmbedding unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return show_inline_or_embedding_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ShowInlineOrEmbedding":
        """Create ShowInlineOrEmbedding stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ShowInlineOrEmbeddingAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ShowInlineOrEmbeddingAdapter.validate_python(
            json, context={"skip_validation": True}
        )
