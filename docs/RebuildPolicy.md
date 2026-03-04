# RebuildPolicy

The policy to select a new <em>runtime</em> version when a rebuild is issued.

**Source:** `waylay.services.registry.models.rebuild_policy`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**PATCH** | `'patch'` |
**MINOR** | `'minor'` |
**MAJOR** | `'major'` |
**SAME** | `'same'` |

## Example

```python
from waylay.services.registry.models.rebuild_policy import RebuildPolicy

# Use enum by value
my_rebuild_policy = RebuildPolicy.PATCH
print(my_rebuild_policy)  # Output: 'patch'

# Or by string value
my_rebuild_policy = RebuildPolicy("patch")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


