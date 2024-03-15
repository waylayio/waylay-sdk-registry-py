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
    from waylay.services.registry.models.alt_embedded_version_i_kfserving_response_v2 import (
        AltEmbeddedVersionIKfservingResponseV2,
    )

    AltEmbeddedVersionIKfservingResponseV2Adapter = TypeAdapter(
        AltEmbeddedVersionIKfservingResponseV2
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

alt_embedded_version_i_kfserving_response_v2__model_schema = json.loads(r"""{
  "title" : "AltEmbeddedVersion_IKfservingResponseV2_",
  "type" : "object",
  "properties" : {
    "draft" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    },
    "published" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    }
  },
  "description" : "Embedded representations of the _latest_ draft/published versions."
}
""")
alt_embedded_version_i_kfserving_response_v2__model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

alt_embedded_version_i_kfserving_response_v2__faker = JSF(
    alt_embedded_version_i_kfserving_response_v2__model_schema, allow_none_optionals=1
)


class AltEmbeddedVersionIKfservingResponseV2Stub:
    """AltEmbeddedVersionIKfservingResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alt_embedded_version_i_kfserving_response_v2__faker.generate()

    @classmethod
    def create_instance(cls) -> "AltEmbeddedVersionIKfservingResponseV2":
        """Create AltEmbeddedVersionIKfservingResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return AltEmbeddedVersionIKfservingResponseV2Adapter.validate_python(
            cls.create_json()
        )
