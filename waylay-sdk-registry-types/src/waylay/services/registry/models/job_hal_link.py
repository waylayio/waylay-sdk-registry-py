"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.ihal_link_href import IHALLinkHref
from ..models.job_type import JobType


class JobHALLink(WaylayBaseModel):
    """JobHALLink."""

    href: IHALLinkHref
    job_type: JobType = Field(alias="jobType")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
