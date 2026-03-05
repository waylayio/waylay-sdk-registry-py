"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.get_asset_by_role_webscripts_asset_role_main import (
    GetAssetByRoleWebscriptsAssetRoleMain,
)
from ..models.get_asset_by_role_webscripts_asset_role_manifest import (
    GetAssetByRoleWebscriptsAssetRoleManifest,
)
from ..models.get_asset_by_role_webscripts_asset_role_project import (
    GetAssetByRoleWebscriptsAssetRoleProject,
)

GetAssetByRoleWebscriptsAssetRole: TypeAlias = GetAssetByRoleWebscriptsAssetRoleManifest | GetAssetByRoleWebscriptsAssetRoleMain | GetAssetByRoleWebscriptsAssetRoleProject
"""GetAssetByRoleWebscriptsAssetRole."""
