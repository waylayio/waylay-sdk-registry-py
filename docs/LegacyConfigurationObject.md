# LegacyConfigurationObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**PlugPropertyDataType**](PlugPropertyDataType.md) |  | 
**mandatory** | **bool** |  | [optional] 
**format** | [**LegacyConfigurationObjectFormat**](LegacyConfigurationObjectFormat.md) |  | [optional] 
**default_value** | **object** |  | [optional] 

## Example

```python
from waylay.services.registry.models.legacy_configuration_object import LegacyConfigurationObject

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyConfigurationObject from a JSON string
legacy_configuration_object_instance = LegacyConfigurationObject.from_json(json)
# print the JSON string representation of the object
print LegacyConfigurationObject.to_json()

# convert the object into a dict
legacy_configuration_object_dict = legacy_configuration_object_instance.to_dict()
# create an instance of LegacyConfigurationObject from a dict
legacy_configuration_object_form_dict = legacy_configuration_object.from_dict(legacy_configuration_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


