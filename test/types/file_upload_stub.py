# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.file_upload import FileUpload


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBytes, StrictStr


class FileUploadStub:
    """FileUpload unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> FileUpload:
        """Create FileUpload stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return FileUpload(
                file=bytes(b'blah')
            )
        else:
            return FileUpload(
            )
