# PlugType


**Source:** `waylay.services.registry.models.plug_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**SENSOR** | `'sensor'` |
**ACTUATOR** | `'actuator'` |
**TRANSFORMER** | `'transformer'` |

## Example

```python
from waylay.services.registry.models.plug_type import PlugType

# Use enum by value
my_plug_type = PlugType.SENSOR
print(my_plug_type)  # Output: 'sensor'

# Or by string value
my_plug_type = PlugType("sensor")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


