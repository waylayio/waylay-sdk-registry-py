"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.show_embedding import ShowEmbedding
from ..models.show_inline_or_embedding_inline import ShowInlineOrEmbeddingInline

ShowInlineOrEmbedding: TypeAlias = ShowEmbedding | ShowInlineOrEmbeddingInline
"""ShowInlineOrEmbedding."""
