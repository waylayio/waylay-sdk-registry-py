# PlugInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**states** | **List[str]** | The states of a plug as implemented in the plug code. Required and supported for &#x60;type&#x3D;sensor&#x60; plugs _only_. | [optional] 
**input** | [**List[PlugProperty]**](PlugProperty.md) | The named input parameters of a plug. Supported for &#x60;type&#x3D;sensor&#x60; plugs; fixed with input attributes &#x60;data&#x60; and &#x60;resource&#x60; for &#x60;type&#x3D;transformer&#x60;plugs. | [optional] 
**output** | [**List[PlugProperty]**](PlugProperty.md) | The named output parameters of a plug. Supported for all plug types. | [optional] 

## Example

```python
from waylay.services.registry.models.plug_interface import PlugInterface

# TODO update the JSON string below
json = "{}"
# create an instance of PlugInterface from a JSON string
plug_interface_instance = PlugInterface.from_json(json)
# print the JSON string representation of the object
print PlugInterface.to_json()

# convert the object into a dict
plug_interface_dict = plug_interface_instance.to_dict()
# create an instance of PlugInterface from a dict
plug_interface_form_dict = plug_interface.from_dict(plug_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


