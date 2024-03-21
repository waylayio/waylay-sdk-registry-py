# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.status_filter import StatusFilter

    StatusFilterAdapter = TypeAdapter(StatusFilter)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

status_filter_model_schema = json.loads(
    r"""{
  "description" : "Inclusion or exclusion filter on the `status` property.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/StatusInclude"
  }, {
    "$ref" : "#/components/schemas/StatusExclude"
  }, {
    "$ref" : "#/components/schemas/StatusAny"
  } ]
}
""",
    object_hook=with_example_provider,
)
status_filter_model_schema.update({"definitions": MODEL_DEFINITIONS})

status_filter_faker = JSF(status_filter_model_schema, allow_none_optionals=1)


class StatusFilterStub:
    """StatusFilter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return status_filter_faker.generate()

    @classmethod
    def create_instance(cls) -> "StatusFilter":
        """Create StatusFilter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return StatusFilterAdapter.validate_python(cls.create_json())
