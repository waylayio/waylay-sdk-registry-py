"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.get_asset_by_role_plugs_asset_role_main import (
    GetAssetByRolePlugsAssetRoleMain,
)
from ..models.get_asset_by_role_plugs_asset_role_manifest import (
    GetAssetByRolePlugsAssetRoleManifest,
)
from ..models.get_asset_by_role_plugs_asset_role_project import (
    GetAssetByRolePlugsAssetRoleProject,
)

GetAssetByRolePlugsAssetRole: TypeAlias = GetAssetByRolePlugsAssetRoleManifest | GetAssetByRolePlugsAssetRoleMain | GetAssetByRolePlugsAssetRoleProject
"""GetAssetByRolePlugsAssetRole."""
