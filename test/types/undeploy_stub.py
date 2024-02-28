# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime

from waylay.services.registry.models.undeploy import Undeploy
from .job_hal_links_stub import JobHALLinksStub


from .job_state_result_stub import JobStateResultStub

from .undeploy_args_stub import UndeployArgsStub

from .undeploy_result_stub import UndeployResultStub


from .function_ref_stub import FunctionRefStub

from .job_status_stub import JobStatusStub

from .failure_reason_stub import FailureReasonStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class UndeployStub:
    """Undeploy unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> Undeploy:
        """Create Undeploy stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return Undeploy(
                links=JobHALLinksStub.create_instance(),
                type="undeploy",
                state=JobStateResultStub.create_instance(),
                request=UndeployArgsStub.create_instance(),
                result=UndeployResultStub.create_instance(),
                created_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
                created_by="",
                operation="",
                function=FunctionRefStub.create_instance(),
                job=JobStatusStub.create_instance(),
                failure_reason=FailureReasonStub.create_instance(),
            )
        else:
            return Undeploy(
                type="undeploy",
                state=JobStateResultStub.create_instance(),
                created_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
                created_by="",
                operation="",
            )
