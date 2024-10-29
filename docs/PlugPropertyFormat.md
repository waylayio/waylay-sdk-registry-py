# PlugPropertyFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PlugPropertyFormatType**](PlugPropertyFormatType.md) |  | 
**values** | **List[object]** | The enumerated value domain when &lt;code&gt;type&#x3D;\&quot;enum\&quot;&lt;/code&gt; | [optional] 

## Example

```python
from waylay.services.registry.models.plug_property_format import PlugPropertyFormat

# TODO update the JSON string below
json = "{}"
# create an instance of PlugPropertyFormat from a JSON string
plug_property_format_instance = PlugPropertyFormat.from_json(json)
# print the JSON string representation of the object
print PlugPropertyFormat.to_json()

# convert the object into a dict
plug_property_format_dict = plug_property_format_instance.to_dict()
# create an instance of PlugPropertyFormat from a dict
plug_property_format_form_dict = plug_property_format.from_dict(plug_property_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


