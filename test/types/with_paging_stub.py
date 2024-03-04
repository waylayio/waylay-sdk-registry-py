# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.with_paging import WithPaging


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class WithPagingStub:
    """WithPaging unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> WithPaging:
        """Create WithPaging stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return WithPaging(limit=1.337, count=1.337, page=1.337)
        else:
            return WithPaging(
                count=1.337,
            )
