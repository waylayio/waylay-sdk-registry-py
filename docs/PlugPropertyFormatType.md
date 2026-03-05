# PlugPropertyFormatType

Value domain for a plug input or output property.

**Source:** `waylay.services.registry.models.plug_property_format_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**ENUM** | `'enum'` |
**RESOURCE** | `'resource'` |
**VAULT** | `'vault'` |
**DURATION** | `'duration'` |
**CODE** | `'code'` |
**URL** | `'url'` |
**DATE** | `'date'` |
**TEMPLATE** | `'template'` |
**AIPLUGINDESCRIPTOR** | `'aiPluginDescriptor'` |
**AITEMPLATEDESCRIPTOR** | `'aiTemplateDescriptor'` |

## Example

```python
from waylay.services.registry.models.plug_property_format_type import (
    PlugPropertyFormatType,
)

# Use enum by value
my_plug_property_format_type = PlugPropertyFormatType.ENUM
print(my_plug_property_format_type)  # Output: 'enum'

# Or by string value
my_plug_property_format_type = PlugPropertyFormatType("enum")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


