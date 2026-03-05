# PlugPropertyDataType

Datatype supported in plug input or output properties.

**Source:** `waylay.services.registry.models.plug_property_data_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**STRING** | `'string'` |
**INTEGER** | `'integer'` |
**LONG** | `'long'` |
**FLOAT** | `'float'` |
**DOUBLE** | `'double'` |
**BOOLEAN** | `'boolean'` |
**OBJECT** | `'object'` |
**ARRAY** | `'array'` |

## Example

```python
from waylay.services.registry.models.plug_property_data_type import PlugPropertyDataType

# Use enum by value
my_plug_property_data_type = PlugPropertyDataType.STRING
print(my_plug_property_data_type)  # Output: 'string'

# Or by string value
my_plug_property_data_type = PlugPropertyDataType("string")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


