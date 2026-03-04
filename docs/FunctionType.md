# FunctionType

Type of functions supported by the registry service.

**Source:** `waylay.services.registry.models.function_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**PLUGS** | `'plugs'` |
**WEBSCRIPTS** | `'webscripts'` |
**KFSERVING** | `'kfserving'` |

## Example

```python
from waylay.services.registry.models.function_type import FunctionType

# Use enum by value
my_function_type = FunctionType.PLUGS
print(my_function_type)  # Output: 'plugs'

# Or by string value
my_function_type = FunctionType("plugs")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


