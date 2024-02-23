# LegacyRequiredPropertiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**PlugPropertyDataType**](PlugPropertyDataType.md) |  | 
**mandatory** | **bool** |  | 
**sensitive** | **bool** |  | 

## Example

```python
from waylay.services.registry.models.legacy_required_properties_inner import LegacyRequiredPropertiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyRequiredPropertiesInner from a JSON string
legacy_required_properties_inner_instance = LegacyRequiredPropertiesInner.from_json(json)
# print the JSON string representation of the object
print LegacyRequiredPropertiesInner.to_json()

# convert the object into a dict
legacy_required_properties_inner_dict = legacy_required_properties_inner_instance.to_dict()
# create an instance of LegacyRequiredPropertiesInner from a dict
legacy_required_properties_inner_form_dict = legacy_required_properties_inner.from_dict(legacy_required_properties_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


