# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.deploy_result import DeployResult
from .exposed_openfaas_deploy_spec_stub import ExposedOpenfaasDeploySpecStub

from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from waylay.services.registry.models.exposed_openfaas_deploy_spec import ExposedOpenfaasDeploySpec


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class DeployResultStub:
    """DeployResult unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> DeployResult:
        """Create DeployResult stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return DeployResult(
                deploy_spec=ExposedOpenfaasDeploySpecStub.create_instance()
            )
        else:
            return DeployResult(
                deploy_spec=ExposedOpenfaasDeploySpecStub.create_instance()
            )
