# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.deploy_spec_openfaas_spec import DeploySpecOpenfaasSpec


class DeploySpec(WaylayBaseModel):
    """DeploySpec."""

    openfaas_spec: DeploySpecOpenfaasSpec | None = Field(
        default=None, alias="openfaasSpec"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
