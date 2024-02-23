# LegacyConfigurationObjectFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PlugPropertyFormatType**](PlugPropertyFormatType.md) |  | [optional] 
**values** | **List[object]** |  | [optional] 

## Example

```python
from waylay.services.registry.models.legacy_configuration_object_format import LegacyConfigurationObjectFormat

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyConfigurationObjectFormat from a JSON string
legacy_configuration_object_format_instance = LegacyConfigurationObjectFormat.from_json(json)
# print the JSON string representation of the object
print LegacyConfigurationObjectFormat.to_json()

# convert the object into a dict
legacy_configuration_object_format_dict = legacy_configuration_object_format_instance.to_dict()
# create an instance of LegacyConfigurationObjectFormat from a dict
legacy_configuration_object_format_form_dict = legacy_configuration_object_format.from_dict(legacy_configuration_object_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


