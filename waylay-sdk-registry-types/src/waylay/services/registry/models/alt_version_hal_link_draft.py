"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.ihal_link_href import IHALLinkHref


class AltVersionHALLinkDraft(WaylayBaseModel):
    """Link to the lastest draft version.."""

    draft: StrictBool
    href: IHALLinkHref
    version: StrictStr
    deprecated: StrictBool

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
