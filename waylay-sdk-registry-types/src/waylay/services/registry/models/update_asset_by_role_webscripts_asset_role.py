"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.update_asset_by_role_webscripts_asset_role_main import (
    UpdateAssetByRoleWebscriptsAssetRoleMain,
)
from ..models.update_asset_by_role_webscripts_asset_role_manifest import (
    UpdateAssetByRoleWebscriptsAssetRoleManifest,
)
from ..models.update_asset_by_role_webscripts_asset_role_project import (
    UpdateAssetByRoleWebscriptsAssetRoleProject,
)

UpdateAssetByRoleWebscriptsAssetRole: TypeAlias = UpdateAssetByRoleWebscriptsAssetRoleManifest | UpdateAssetByRoleWebscriptsAssetRoleMain | UpdateAssetByRoleWebscriptsAssetRoleProject
"""UpdateAssetByRoleWebscriptsAssetRole."""
