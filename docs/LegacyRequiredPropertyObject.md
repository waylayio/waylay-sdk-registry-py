# LegacyRequiredPropertyObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**PlugPropertyDataType**](PlugPropertyDataType.md) |  | 
**mandatory** | **bool** |  | 
**sensitive** | **bool** |  | 

## Example

```python
from waylay.services.registry.models.legacy_required_property_object import LegacyRequiredPropertyObject

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyRequiredPropertyObject from a JSON string
legacy_required_property_object_instance = LegacyRequiredPropertyObject.from_json(json)
# print the JSON string representation of the object
print LegacyRequiredPropertyObject.to_json()

# convert the object into a dict
legacy_required_property_object_dict = legacy_required_property_object_instance.to_dict()
# create an instance of LegacyRequiredPropertyObject from a dict
legacy_required_property_object_form_dict = legacy_required_property_object.from_dict(legacy_required_property_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


