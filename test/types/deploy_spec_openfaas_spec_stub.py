# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.deploy_spec_openfaas_spec import DeploySpecOpenfaasSpec


from .resource_limits_stub import ResourceLimitsStub

from .resource_limits_stub import ResourceLimitsStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from waylay.services.registry.models.resource_limits import ResourceLimits


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class DeploySpecOpenfaasSpecStub:
    """DeploySpecOpenfaasSpec unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> DeploySpecOpenfaasSpec:
        """Create DeploySpecOpenfaasSpec stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return DeploySpecOpenfaasSpec(
                service='',
                image='',
                namespace='',
                env_process='',
                network='',
                env_vars={
                    'key': ''
                },
                constraints=[''],
                labels={
                    'key': ''
                },
                annotations={
                    'key': ''
                },
                secrets=[''],
                registry_auth='',
                limits=ResourceLimitsStub.create_instance(),
                requests=ResourceLimitsStub.create_instance(),
                read_only_root_filesystem=True
            )
        else:
            return DeploySpecOpenfaasSpec(
            )
