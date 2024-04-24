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
    from waylay.services.registry.models.language_release import LanguageRelease

    LanguageReleaseAdapter = TypeAdapter(LanguageRelease)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

language_release_model_schema = json.loads(
    r"""{
  "title" : "LanguageRelease",
  "required" : [ "name", "title", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "Short technical name of the language or framework used."
    },
    "version" : {
      "title" : "version",
      "type" : "string",
      "description" : "Release version of the language or framework."
    },
    "title" : {
      "title" : "title",
      "type" : "string",
      "description" : "Display title."
    },
    "description" : {
      "title" : "description",
      "type" : "string"
    }
  },
  "description" : "Description of the language or framework release used by a runtime (version)."
}
""",
    object_hook=with_example_provider,
)
language_release_model_schema.update({"definitions": MODEL_DEFINITIONS})

language_release_faker = JSF(language_release_model_schema, allow_none_optionals=1)


class LanguageReleaseStub:
    """LanguageRelease unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return language_release_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "LanguageRelease":
        """Create LanguageRelease stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                LanguageReleaseAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return LanguageReleaseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
