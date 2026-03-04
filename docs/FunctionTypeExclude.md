# FunctionTypeExclude


**Source:** `waylay.services.registry.models.function_type_exclude`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**PLUGS_MINUS** | `'plugs-'` |
**WEBSCRIPTS_MINUS** | `'webscripts-'` |
**KFSERVING_MINUS** | `'kfserving-'` |

## Example

```python
from waylay.services.registry.models.function_type_exclude import FunctionTypeExclude

# Use enum by value
my_function_type_exclude = FunctionTypeExclude.PLUGS_MINUS
print(my_function_type_exclude)  # Output: 'plugs-'

# Or by string value
my_function_type_exclude = FunctionTypeExclude("plugs-")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


