# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.any_job_status_summary import AnyJobStatusSummary


from .job_state_result_stub import JobStateResultStub


from .function_ref_stub import FunctionRefStub

from .job_hal_links_stub import JobHALLinksStub

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from waylay.services.registry.models.batch import Batch
from waylay.services.registry.models.build1 import Build1
from waylay.services.registry.models.deploy1 import Deploy1
from waylay.services.registry.models.scale1 import Scale1
from waylay.services.registry.models.undeploy1 import Undeploy1
from waylay.services.registry.models.verify1 import Verify1


from .build1_stub import Build1Stub

from .deploy1_stub import Deploy1Stub

from .verify1_stub import Verify1Stub

from .undeploy1_stub import Undeploy1Stub

from .scale1_stub import Scale1Stub

from .batch_stub import BatchStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class AnyJobStatusSummaryStub:
    """AnyJobStatusSummary unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> AnyJobStatusSummary:
        """Create AnyJobStatusSummary stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        # return instance of first type from `anyOf`
        return AnyJobStatusSummary(Build1Stub.create_instance(include_optional=include_optional))
