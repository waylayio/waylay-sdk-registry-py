# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.named_parameters_typeof_as_job_reference import (
    NamedParametersTypeofAsJobReference,
)
from .named_parameters_typeof_as_job_reference_job_status_stub import (
    NamedParametersTypeofAsJobReferenceJobStatusStub,
)


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class NamedParametersTypeofAsJobReferenceStub:
    """NamedParametersTypeofAsJobReference unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> NamedParametersTypeofAsJobReference:
        """Create NamedParametersTypeofAsJobReference stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return NamedParametersTypeofAsJobReference(
                job_status=NamedParametersTypeofAsJobReferenceJobStatusStub.create_instance()
            )
        else:
            return NamedParametersTypeofAsJobReference(
                job_status=NamedParametersTypeofAsJobReferenceJobStatusStub.create_instance()
            )
