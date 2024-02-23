# PlugProperty

Interface specification of a plug property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of a plug input or output property. | 
**data_type** | [**PlugPropertyDataType**](PlugPropertyDataType.md) |  | [optional] 
**mandatory** | **bool** | If &lt;code&gt;true&lt;/code&gt; this property is required. | [optional] 
**format** | [**PlugPropertyFormat**](PlugPropertyFormat.md) |  | [optional] 
**default_value** | **object** |  | [optional] 

## Example

```python
from waylay.services.registry.models.plug_property import PlugProperty

# TODO update the JSON string below
json = "{}"
# create an instance of PlugProperty from a JSON string
plug_property_instance = PlugProperty.from_json(json)
# print the JSON string representation of the object
print PlugProperty.to_json()

# convert the object into a dict
plug_property_dict = plug_property_instance.to_dict()
# create an instance of PlugProperty from a dict
plug_property_form_dict = plug_property.from_dict(plug_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


