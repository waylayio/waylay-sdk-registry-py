# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.user_plug_meta import UserPlugMeta


from .tag_stub import TagStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class UserPlugMetaStub:
    """UserPlugMeta unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> UserPlugMeta:
        """Create UserPlugMeta stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return UserPlugMeta(
                author="",
                description="",
                icon_url="",
                category="",
                documentation_url="",
                tags=[TagStub.create_instance()],
                friendly_name="",
            )
        else:
            return UserPlugMeta()
