"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.archive_format import ArchiveFormat
from ..models.archive_format_exclude import ArchiveFormatExclude

ArchiveFormatFilter: TypeAlias = ArchiveFormat | ArchiveFormatExclude
"""ArchiveFormatFilter."""
