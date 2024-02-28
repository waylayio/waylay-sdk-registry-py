# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime

from waylay.services.registry.models.webscript_response import WebscriptResponse
from .function_deploy_overrides_type_stub import FunctionDeployOverridesTypeStub


from .semantic_version_range_stub import SemanticVersionRangeStub

from .function_meta_stub import FunctionMetaStub


from .failure_reason_stub import FailureReasonStub


from .job_hal_links_stub import JobHALLinksStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class WebscriptResponseStub:
    """WebscriptResponse unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> WebscriptResponse:
        """Create WebscriptResponse stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return WebscriptResponse(
                deploy=FunctionDeployOverridesTypeStub.create_instance(),
                name="",
                version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
                runtime="",
                runtime_version=SemanticVersionRangeStub.create_instance(),
                metadata=FunctionMetaStub.create_instance(),
                created_by="",
                created_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
                updated_by="",
                updated_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
                status="registered",
                failure_reason=FailureReasonStub.create_instance(),
                links=[JobHALLinksStub.create_instance()],
                secret="",
            )
        else:
            return WebscriptResponse(
                name="",
                version="9072888001528021798096225500850762068629339333975650685139102691291.0.0",
                runtime="",
                metadata=FunctionMetaStub.create_instance(),
                created_by="",
                created_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
                updated_by="",
                updated_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
                status="registered",
                secret="",
            )
