# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.deploy_spec import DeploySpec

from .deploy_spec_openfaas_spec_stub import DeploySpecOpenfaasSpecStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from waylay.services.registry.models.deploy_spec_openfaas_spec import DeploySpecOpenfaasSpec


class DeploySpecStub:
    """DeploySpec unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> DeploySpec:
        """Create DeploySpec stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return DeploySpec(
                openfaas_spec=DeploySpecOpenfaasSpecStub.create_instance()
            )
        else:
            return DeploySpec(
            )
