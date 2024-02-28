# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.job_type_schema import JobTypeSchema


from .job_type_build_stub import JobTypeBuildStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobTypeSchemaStub:
    """JobTypeSchema unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobTypeSchema:
        """Create JobTypeSchema stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        # return instance of first type from `anyOf`
        return JobTypeSchema(
            JobTypeBuildStub.create_instance(include_optional=include_optional)
        )
