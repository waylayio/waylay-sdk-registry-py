# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.jobs_for_model_response_v2 import JobsForModelResponseV2


from .any_job_for_function_stub import AnyJobForFunctionStub
from .function_ref_stub import FunctionRefStub

from .jobs_for_model_response_v2_links_stub import JobsForModelResponseV2LinksStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from waylay.services.registry.models.any_job_for_function import AnyJobForFunction
from waylay.services.registry.models.function_ref import FunctionRef
from waylay.services.registry.models.jobs_for_model_response_v2_links import JobsForModelResponseV2Links


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobsForModelResponseV2Stub:
    """JobsForModelResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobsForModelResponseV2:
        """Create JobsForModelResponseV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return JobsForModelResponseV2(
                jobs=[AnyJobForFunctionStub.create_instance()],
                function=FunctionRefStub.create_instance(),
                links=JobsForModelResponseV2LinksStub.create_instance()
            )
        else:
            return JobsForModelResponseV2(
                jobs=[AnyJobForFunctionStub.create_instance()],
                function=FunctionRefStub.create_instance(),
            )
