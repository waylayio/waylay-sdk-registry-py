# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.tag import Tag


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field


class TagStub:
    """Tag unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> Tag:
        """Create Tag stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return Tag(
                name='',
                color=''
            )
        else:
            return Tag(
                name='',
                color=''
            )
