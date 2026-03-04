"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.ihal_link_href import IHALLinkHref


class IHALLink(WaylayBaseModel):
    """IHALLink."""

    href: IHALLinkHref

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
