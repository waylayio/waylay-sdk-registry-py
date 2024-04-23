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
    from waylay.services.registry.models.semantic_version_range import (
        SemanticVersionRange,
    )

    SemanticVersionRangeAdapter = TypeAdapter(SemanticVersionRange)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

semantic_version_range_model_schema = json.loads(
    r"""{
  "description" : "A range of semantic versions. See https://devhints.io/semver",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "$ref" : "#/components/schemas/SemanticVersion"
  } ]
}
""",
    object_hook=with_example_provider,
)
semantic_version_range_model_schema.update({"definitions": MODEL_DEFINITIONS})

semantic_version_range_faker = JSF(
    semantic_version_range_model_schema, allow_none_optionals=1
)


class SemanticVersionRangeStub:
    """SemanticVersionRange unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return semantic_version_range_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "SemanticVersionRange":
        """Create SemanticVersionRange stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SemanticVersionRangeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SemanticVersionRangeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
