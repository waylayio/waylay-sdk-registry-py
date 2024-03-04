# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime

from waylay.services.registry.models.undeploy_job_status import UndeployJobStatus


from .job_state_result_stub import JobStateResultStub

from .undeploy_args_stub import UndeployArgsStub

from .undeploy_result_stub import UndeployResultStub


from .function_ref_stub import FunctionRefStub

from .job_status_stub import JobStatusStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class UndeployJobStatusStub:
    """UndeployJobStatus unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> UndeployJobStatus:
        """Create UndeployJobStatus stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return UndeployJobStatus(
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
            )
        else:
            return UndeployJobStatus(
                type="undeploy",
                state=JobStateResultStub.create_instance(),
                request=UndeployArgsStub.create_instance(),
                created_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
                created_by="",
                operation="",
                job=JobStatusStub.create_instance(),
            )
