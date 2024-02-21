# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.any_job_result import AnyJobResult


from .exposed_openfaas_deploy_spec_stub import ExposedOpenfaasDeploySpecStub


from .job_reference_stub import JobReferenceStub


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from pydantic import Field
from waylay.services.registry.models.batch_result import BatchResult
from waylay.services.registry.models.build_result import BuildResult
from waylay.services.registry.models.cleanup_result import CleanupResult
from waylay.services.registry.models.deploy_result import DeployResult
from waylay.services.registry.models.undeploy_result import UndeployResult
from waylay.services.registry.models.verify_result import VerifyResult


from .build_result_stub import BuildResultStub

from .deploy_result_stub import DeployResultStub

from .verify_result_stub import VerifyResultStub

from .undeploy_result_stub import UndeployResultStub

from .batch_result_stub import BatchResultStub

from .cleanup_result_stub import CleanupResultStub


class AnyJobResultStub:
    """AnyJobResult unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> AnyJobResult:
        """Create AnyJobResult stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        # return instance of first type from `anyOf`
        return AnyJobResult(BuildResultStub.create_instance(include_optional=include_optional))
