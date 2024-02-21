# LegacyConfigurationResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**PlugPropertyDataType**](PlugPropertyDataType.md) |  | 
**mandatory** | **bool** |  | [optional] 
**format** | [**LegacyConfigurationObjectFormat**](LegacyConfigurationObjectFormat.md) |  | [optional] 
**default_value** | **object** |  | [optional] 
**sensitive** | **bool** |  | [optional] 

## Example

```python
from waylay.services.registry.models.legacy_configuration_response_object import LegacyConfigurationResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyConfigurationResponseObject from a JSON string
legacy_configuration_response_object_instance = LegacyConfigurationResponseObject.from_json(json)
# print the JSON string representation of the object
print LegacyConfigurationResponseObject.to_json()

# convert the object into a dict
legacy_configuration_response_object_dict = legacy_configuration_response_object_instance.to_dict()
# create an instance of LegacyConfigurationResponseObject from a dict
legacy_configuration_response_object_form_dict = legacy_configuration_response_object.from_dict(legacy_configuration_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


