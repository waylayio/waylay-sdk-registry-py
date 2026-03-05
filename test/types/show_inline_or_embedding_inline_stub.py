"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.show_inline_or_embedding_inline import (
        ShowInlineOrEmbeddingInline,
    )

    ShowInlineOrEmbeddingInlineAdapter = TypeAdapter(ShowInlineOrEmbeddingInline)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

show_inline_or_embedding_inline_model_schema = json.loads(
    r"""{
  "title" : "ShowInlineOrEmbeddingInline",
  "type" : "string",
  "enum" : [ "inline" ]
}
""",
    object_hook=with_example_provider,
)
show_inline_or_embedding_inline_model_schema.update({"definitions": MODEL_DEFINITIONS})

show_inline_or_embedding_inline_faker = JSF(
    show_inline_or_embedding_inline_model_schema, allow_none_optionals=1
)


class ShowInlineOrEmbeddingInlineStub:
    """ShowInlineOrEmbeddingInline unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return show_inline_or_embedding_inline_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ShowInlineOrEmbeddingInline":
        """Create ShowInlineOrEmbeddingInline stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ShowInlineOrEmbeddingInlineAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ShowInlineOrEmbeddingInlineAdapter.validate_python(
            json, context={"skip_validation": True}
        )
