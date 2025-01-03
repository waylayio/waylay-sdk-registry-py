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
    from waylay.services.registry.models.latest_version_level import LatestVersionLevel

    LatestVersionLevelAdapter = TypeAdapter(LatestVersionLevel)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

latest_version_level_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Level of latest versions that should be included.",
  "enum" : [ "major", "minor", "patch", "true", "false" ]
}
""",
    object_hook=with_example_provider,
)
latest_version_level_model_schema.update({"definitions": MODEL_DEFINITIONS})

latest_version_level_faker = JSF(
    latest_version_level_model_schema, allow_none_optionals=1
)


class LatestVersionLevelStub:
    """LatestVersionLevel unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return latest_version_level_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "LatestVersionLevel":
        """Create LatestVersionLevel stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                LatestVersionLevelAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return LatestVersionLevelAdapter.validate_python(
            json, context={"skip_validation": True}
        )
