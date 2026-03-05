# ArchiveFormat


**Source:** `waylay.services.registry.models.archive_format`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**NODE** | `'node'` |
**PYTHON** | `'python'` |
**GOLANG** | `'golang'` |
**BYOML** | `'byoml'` |
**NATIVE** | `'native'` |

## Example

```python
from waylay.services.registry.models.archive_format import ArchiveFormat

# Use enum by value
my_archive_format = ArchiveFormat.NODE
print(my_archive_format)  # Output: 'node'

# Or by string value
my_archive_format = ArchiveFormat("node")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


