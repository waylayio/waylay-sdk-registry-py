# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.cleanup_result import CleanupResult
from .job_reference_stub import JobReferenceStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class CleanupResultStub:
    """CleanupResult unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> CleanupResult:
        """Create CleanupResult stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return CleanupResult(scheduled_job=JobReferenceStub.create_instance())
        else:
            return CleanupResult()
