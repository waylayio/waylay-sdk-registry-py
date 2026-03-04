# ArchiveFormatExclude


**Source:** `waylay.services.registry.models.archive_format_exclude`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**NODE_MINUS** | `'node-'` |
**PYTHON_MINUS** | `'python-'` |
**GOLANG_MINUS** | `'golang-'` |
**BYOML_MINUS** | `'byoml-'` |
**NATIVE_MINUS** | `'native-'` |

## Example

```python
from waylay.services.registry.models.archive_format_exclude import ArchiveFormatExclude

# Use enum by value
my_archive_format_exclude = ArchiveFormatExclude.NODE_MINUS
print(my_archive_format_exclude)  # Output: 'node-'

# Or by string value
my_archive_format_exclude = ArchiveFormatExclude("node-")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


