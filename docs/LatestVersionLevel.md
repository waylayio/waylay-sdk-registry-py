# LatestVersionLevel

Level of latest versions that should be included.

**Source:** `waylay.services.registry.models.latest_version_level`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**MAJOR** | `'major'` |
**MINOR** | `'minor'` |
**PATCH** | `'patch'` |
**TRUE** | `'true'` |
**FALSE** | `'false'` |

## Example

```python
from waylay.services.registry.models.latest_version_level import LatestVersionLevel

# Use enum by value
my_latest_version_level = LatestVersionLevel.MAJOR
print(my_latest_version_level)  # Output: 'major'

# Or by string value
my_latest_version_level = LatestVersionLevel("major")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


