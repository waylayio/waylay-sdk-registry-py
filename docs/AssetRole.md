# AssetRole

Classification of assets with regard to their role.

**Source:** `waylay.services.registry.models.asset_role`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**MANIFEST** | `'manifest'` |
**PROJECT** | `'project'` |
**MAIN** | `'main'` |
**LIB** | `'lib'` |
**SCRIPT** | `'script'` |
**OTHER** | `'other'` |

## Example

```python
from waylay.services.registry.models.asset_role import AssetRole

# Use enum by value
my_asset_role = AssetRole.MANIFEST
print(my_asset_role)  # Output: 'manifest'

# Or by string value
my_asset_role = AssetRole("manifest")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


